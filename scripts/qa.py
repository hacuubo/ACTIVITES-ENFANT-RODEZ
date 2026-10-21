#!/usr/bin/env python3
"""Contrôles d'après-fusion : pertes, doublons de fond, tags, days_of_week.

merge.py dédoublonne de façon agressive et avale parfois des événements distincts
(deux séances d'âges différents le même jour au même lieu, deux rencontres dans la
même salle). Il peut aussi écraser une fiche en gardant son `id`, ce qui rend la
perte invisible. Ce script attrape ces cas, que ni merge.py ni validate.py ne voient.

Usage :
  python3 scripts/qa.py                                  # contrôle data/events.json
  python3 scripts/qa.py --before <events.json d'avant>    # titres disparus depuis
  python3 scripts/qa.py --inputs f1.json f2.json ...      # contrôle de pertes sur la fusion
"""
import argparse, collections, datetime, difflib, json, pathlib, re, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'data' / 'events.json'

def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def load(p):
    data = json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
    return data.get('events', data) if isinstance(data, dict) else data

def slot(e):
    return (e.get('date'), e.get('time') or '')

ap = argparse.ArgumentParser()
ap.add_argument('events', nargs='?', default=str(OUT))
ap.add_argument('--before', help="version précédente de data/events.json (git show HEAD~1:data/events.json)")
ap.add_argument('--inputs', nargs='*', default=[], help='fichiers passés à merge.py')
args = ap.parse_args()

events = load(args.events)
print(f'{len(events)} événements dans {args.events}')
problems = 0

if args.inputs:
    survivors = collections.Counter(slot(e) for e in events)
    wanted = collections.Counter()
    sample = {}
    for f in args.inputs:
        for e in load(f):
            if not e.get('date'): continue
            wanted[slot(e)] += 1
            sample.setdefault(slot(e), []).append((pathlib.Path(f).name, e.get('city'), e.get('title')))
    squeezed = [k for k in wanted if survivors.get(k, 0) < wanted[k]]
    print(f'\n== CRÉNEAUX RÉDUITS PAR LA FUSION : {len(squeezed)} ==')
    print('   (entrées > survivants sur date+heure : vérifier si merge.py a avalé des séances distinctes)')
    for k in sorted(squeezed):
        print(f'  {k[0]} {k[1] or "--:--"} : {wanted[k]} en entrée -> {survivors.get(k, 0)} survivant(s)')
        for s in sample[k]: print(f'      {s[0]} | {s[1]} | {s[2]}')
    problems += len(squeezed)

if args.before:
    before = load(args.before)
    current = [norm(e['title']) for e in events]
    today = str(datetime.date.today())
    gone = [p for p in before
            if (p.get('end_date') or p.get('date', '')) >= today
            and not any(difflib.SequenceMatcher(None, norm(p['title']), c).ratio() >= 0.85 for c in current)]
    print(f'\n== TITRES DISPARUS DEPUIS {args.before} : {len(gone)} ==')
    print('   (une suppression voulue est normale ; sinon la fiche a été écrasée en gardant son id)')
    for p in gone:
        print(f'  {p["date"]} {p.get("time") or "--:--"} {p["city"]} | {p["title"]} | {p["id"]}')
    problems += len(gone)

print('\n== DOUBLONS : même date + même heure + lieu proche ==')
groups = collections.defaultdict(list)
for e in events: groups[(e.get('date'), e.get('time') or '', norm(e.get('venue'))[:12])].append(e)
n = 0
for k, v in sorted(groups.items()):
    if len(v) < 2: continue
    n += 1
    print(f'  {k[0]} {k[1] or "--:--"} {k[2]} :')
    for e in v: print(f'      {e["id"]} | {e["title"]} | {e["city"]} | {e.get("age_min")}-{e.get("age_max")} ans')
print(f'  ({n} créneaux — des séances d\'âges différents au même endroit sont légitimes)')

print('\n== DOUBLONS DE RÉCURRENTS : même lieu + même heure + mêmes days_of_week ==')
groups = collections.defaultdict(list)
for e in events:
    if e.get('days_of_week'):
        groups[(norm(e.get('venue'))[:12], e.get('time') or '', tuple(e['days_of_week']))].append(e)
n = 0
for k, v in sorted(groups.items()):
    if len(v) < 2: continue
    n += 1
    print(f'  {k[0]} {k[1] or "--:--"} dow={list(k[2])} :')
    for e in v: print(f'      {e["id"]} | {e["date"]}..{e.get("end_date")} | {e["title"]}')
print(f'  ({n} groupes)')
problems += n

print('\n== TAGS NON NORMALISÉS (minuscules, sans accents, tirets) ==')
bad = collections.Counter(t for e in events for t in (e.get('tags') or []) if t != norm(t))
for t, c in bad.most_common(): print(f'  {t!r} ({c}×)')
print(f'  ({len(bad)} tags à corriger)')
problems += len(bad)

print('\n== days_of_week SUSPECTS (beaucoup de séances affichées) ==')
print('   (ne jamais utiliser days_of_week pour des dates isolées : une entrée par date)')
for e in events:
    dow, end = e.get('days_of_week'), e.get('end_date')
    if not dow or not end: continue
    try:
        d0, d1 = datetime.date.fromisoformat(e['date']), datetime.date.fromisoformat(end)
    except ValueError:
        continue
    occ = sum(1 for i in range((d1 - d0).days + 1) if (d0 + datetime.timedelta(days=i)).isoweekday() in dow)
    if occ >= 10: print(f'  {occ:2d} séances | {e["date"]}..{end} dow={dow} | {e["title"]}')

print('\n== FORMATS ==')
for e in events:
    if e.get('phone') and not re.fullmatch(r'0\d( \d\d){4}', e['phone']):
        print(f'  téléphone {e["phone"]!r} : {e["id"]}'); problems += 1
    if norm(e.get('city')).startswith('laissac') and e['city'] != "Laissac-Séverac-l'Église":
        print(f'  commune {e["city"]!r} (attendu Laissac-Séverac-l\'Église) : {e["id"]}'); problems += 1

print(f'\n{len(events)} événements, {problems} point(s) à inspecter')
