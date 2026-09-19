#!/usr/bin/env python3
"""Valide data/events.json contre docs/SCHEMA.md (champs, enums, dates, zone géographique).
Usage : python3 scripts/validate.py [data/events.json]
Sortie non nulle si une erreur bloquante est trouvée."""
import json, math, re, sys, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'data' / 'events.json'
CATS = {'spectacle', 'atelier', 'musee', 'lecture', 'cinema', 'sport', 'nature', 'fete', 'stage', 'jeux', 'autre'}
AUD = {'enfant', 'famille', 'ados', 'amis'}
REQ = ['id', 'title', 'summary', 'category', 'date', 'age_min', 'age_max', 'audience', 'city', 'venue',
       'address', 'lat', 'lng', 'price', 'booking_required', 'url', 'source', 'source_checked']
RODEZ = (44.3506, 2.5750)
RADIUS_KM = 22  # 20 km + marge

def dist_km(lat, lng):
    r = 6371.0
    p1, p2 = math.radians(RODEZ[0]), math.radians(lat)
    dphi, dl = math.radians(lat - RODEZ[0]), math.radians(lng - RODEZ[1])
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))

def is_date(s): 
    try: datetime.date.fromisoformat(s); return True
    except Exception: return False

data = json.loads(path.read_text(encoding='utf-8'))
errors, warnings = [], []
events = data.get('events')
if not isinstance(events, list): sys.exit('events doit être une liste')
if not data.get('updated_at'): errors.append('updated_at manquant')
seen = set()
for i, e in enumerate(events):
    tag = f'#{i} {e.get("id", "?")}'
    for k in REQ:
        if k not in e or e[k] in (None, ''): errors.append(f'{tag}: champ obligatoire manquant « {k} »')
    if e.get('id') in seen: errors.append(f'{tag}: id en double')
    seen.add(e.get('id'))
    if e.get('id') and not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*_\d{4}-\d{2}-\d{2}_[a-z0-9-]+', e['id']):
        warnings.append(f'{tag}: id non conforme au format slug_date_ville')
    if e.get('category') not in CATS: errors.append(f'{tag}: category invalide « {e.get("category")} »')
    if e.get('audience') not in AUD: errors.append(f'{tag}: audience invalide « {e.get("audience")} »')
    if not is_date(str(e.get('date'))): errors.append(f'{tag}: date invalide')
    if e.get('end_date') and not is_date(str(e['end_date'])): errors.append(f'{tag}: end_date invalide')
    if e.get('end_date') and e.get('date') and e['end_date'] < e['date']: errors.append(f'{tag}: end_date avant date')
    for k in ('time', 'end_time'):
        if e.get(k) and not re.fullmatch(r'\d{2}:\d{2}', e[k]): errors.append(f'{tag}: {k} doit être HH:MM')
    if e.get('days_of_week') is not None and (not isinstance(e['days_of_week'], list) or any(d not in range(1, 8) for d in e['days_of_week'])):
        errors.append(f'{tag}: days_of_week doit être une liste de 1..7')
    try:
        amin, amax = int(e['age_min']), int(e['age_max'])
        if not (0 <= amin <= amax <= 18): errors.append(f'{tag}: tranche d’âge incohérente {amin}-{amax}')
        if amin > 15: errors.append(f'{tag}: hors cible (age_min > 15)')
    except Exception: errors.append(f'{tag}: age_min/age_max invalides')
    try:
        d = dist_km(float(e['lat']), float(e['lng']))
        if d > RADIUS_KM: errors.append(f'{tag}: lieu à {d:.0f} km de Rodez (> {RADIUS_KM})')
    except Exception: errors.append(f'{tag}: lat/lng invalides')
    if len(str(e.get('summary', ''))) > 160: warnings.append(f'{tag}: summary long ({len(e["summary"])} car.)')
    if e.get('date') and e['date'] < str(datetime.date.today() - datetime.timedelta(days=1)) and not e.get('end_date'):
        warnings.append(f'{tag}: événement passé ({e["date"]})')
    for k in ('url', 'source', 'booking_url'):
        if e.get(k) and not str(e[k]).startswith('http'): errors.append(f'{tag}: {k} doit être une URL http(s)')

for w in warnings: print('AVERTISSEMENT', w)
for er in errors: print('ERREUR', er)
print(f'{len(events)} événements, {len(errors)} erreur(s), {len(warnings)} avertissement(s)')
sys.exit(1 if errors else 0)
