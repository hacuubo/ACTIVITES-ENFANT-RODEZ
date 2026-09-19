#!/usr/bin/env python3
"""Fusionne des fichiers JSON de recherche (listes d'événements) dans data/events.json.
Usage : python3 scripts/merge.py --from 2026-09-19 --to 2027-01-10 fichier1.json fichier2.json ...
- dédoublonne par id, puis par (titre normalisé, date, ville)
- supprime les événements terminés avant hier
- trie par date puis heure et écrit data/events.json avec updated_at"""
import argparse, datetime, json, pathlib, re, unicodedata, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'data' / 'events.json'

def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def slug_id(e):
    return f"{norm(e['title'])[:60]}_{e['date']}_{norm(e['city'])}"

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
merged, by_id, by_key = [], {}, {}
for e in events:
    if not e.get('title') or not e.get('date') or not e.get('city'): continue
    e.setdefault('id', slug_id(e))
    e['id'] = norm(e['id'].replace('_', '|')).replace('|', '_') if '_' in e['id'] else slug_id(e)
    end = e.get('end_date') or e['date']
    if end < yesterday: continue
    if args.dto and e['date'] > args.dto: continue
    key = (norm(e['title']), e['date'], norm(e['city']))
    dup = by_id.get(e['id']) or by_key.get(key)
    if dup:
        # garde la version la plus complète (le plus de champs renseignés)
        if sum(1 for v in e.values() if v not in (None, '', [])) > sum(1 for v in dup.values() if v not in (None, '', [])):
            merged[merged.index(dup)] = e; by_id[e['id']] = e; by_key[key] = e
        continue
    merged.append(e); by_id[e['id']] = e; by_key[key] = e

merged.sort(key=lambda e: (e['date'], e.get('time') or '00:00', e['title']))
now = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps({'updated_at': now, 'period': {'from': args.dfrom, 'to': args.dto or ''}, 'events': merged}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(merged)} événements écrits dans {OUT}')
