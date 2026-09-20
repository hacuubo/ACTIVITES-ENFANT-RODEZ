#!/usr/bin/env python3
"""Fusionne des fichiers JSON de recherche (listes d'événements) dans data/events.json.
Usage : python3 scripts/merge.py --from 2026-09-19 --to 2027-01-10 fichier1.json fichier2.json ...
- dédoublonne par id, puis par (titre normalisé, date, ville)
- supprime les événements terminés avant hier
- trie par date puis heure et écrit data/events.json avec updated_at"""
import argparse, datetime, difflib, json, pathlib, re, unicodedata, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'data' / 'events.json'

def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def slug_id(e):
    return f"{norm(e['title'])[:60]}_{e['date']}_{norm(e['city'])}"

def fix_id(e):
    parts = str(e.get('id') or '').split('_')
    if len(parts) == 3 and re.fullmatch(r'\d{4}-\d{2}-\d{2}', parts[1]):
        return f"{norm(parts[0])[:60]}_{parts[1]}_{norm(parts[2])}"
    return slug_id(e)

def same_event(a, b):
    """Même jour, même lieu (ou même ville) et titres proches, ou même titre normalisé."""
    if a['date'] != b['date']: return False
    ta, tb = norm(a['title']), norm(b['title'])
    if ta == tb: return True
    same_time = (a.get('time') or '') == (b.get('time') or '')
    if same_time and min(len(ta), len(tb)) >= 6 and (ta in tb or tb in ta): return True
    try:
        near = abs(float(a['lat']) - float(b['lat'])) < 0.0012 and abs(float(a['lng']) - float(b['lng'])) < 0.0016  # ≈ 130 m
    except (KeyError, TypeError, ValueError):
        near = False
    same_place = near or norm(a.get('venue'))[:12] == norm(b.get('venue'))[:12] or (
        norm(a['city']) == norm(b['city']) and same_time and a.get('time'))
    if not same_place: return False
    ratio = difflib.SequenceMatcher(None, ta, tb).ratio()
    if ratio >= 0.6: return True
    # même créneau horaire, même lieu, même tranche d'âge : très probablement identique
    return (same_time and a.get('time') and (near or norm(a.get('venue'))[:12] == norm(b.get('venue'))[:12])
            and a.get('age_min') == b.get('age_min') and a.get('age_max') == b.get('age_max') and ratio >= 0.25)

def completeness(e):
    return sum(1 for v in e.values() if v not in (None, '', []))

def fuse(keep, other):
    """Complète les champs vides de `keep` avec ceux de `other` ; garde l'id le plus ancien (favoris)."""
    for k, v in other.items():
        if keep.get(k) in (None, '', []) and v not in (None, '', []): keep[k] = v
    if len(other.get('description') or '') > len(keep.get('description') or ''): keep['description'] = other['description']
    tags = list(dict.fromkeys((keep.get('tags') or []) + (other.get('tags') or [])))
    if tags: keep['tags'] = tags
    return keep

ap = argparse.ArgumentParser()
ap.add_argument('files', nargs='*')
ap.add_argument('--from', dest='dfrom', default=str(datetime.date.today()))
ap.add_argument('--to', dest='dto')
ap.add_argument('--keep-existing', action='store_true', help='conserver les événements déjà présents dans data/events.json')
args = ap.parse_args()

events = []
if args.keep_existing and OUT.exists():
    events += json.loads(OUT.read_text(encoding='utf-8')).get('events', [])
for f in args.files:
    try:
        payload = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    except Exception as ex:
        print(f'IGNORÉ {f}: {ex}', file=sys.stderr); continue
    if isinstance(payload, dict): payload = payload.get('events', [])
    events += [e for e in payload if isinstance(e, dict)]

yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
merged, by_id = [], {}
for e in events:
    if not e.get('title') or not e.get('date') or not e.get('city'): continue
    e['id'] = fix_id(e)
    end = e.get('end_date') or e['date']
    if end < yesterday: continue
    if args.dto and e['date'] > args.dto: continue
    dup = by_id.get(e['id']) or next((m for m in merged if same_event(m, e)), None)
    if dup:
        # garde la version la plus complète, complétée par l'autre ; conserve l'id déjà connu (favoris)
        if completeness(e) > completeness(dup):
            e['id'] = dup['id']
            merged[merged.index(dup)] = fuse(e, dup); by_id[e['id']] = merged[merged.index(e)]
        else:
            fuse(dup, e)
        continue
    merged.append(e); by_id[e['id']] = e

merged.sort(key=lambda e: (e['date'], e.get('time') or '00:00', e['title']))
now = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps({'updated_at': now, 'period': {'from': args.dfrom, 'to': args.dto or ''}, 'events': merged}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(merged)} événements écrits dans {OUT}')
