#!/usr/bin/env python3
"""Croise l'agenda enfants de kefesh.fr avec data/events.json.

kefesh.fr (agenda de sorties à Rodez) est propulsé par GoodBarber, qui expose une API JSON publique.
Rubriques : 67483833 = « Pour les enfants », 67463422 = « L'agenda » (tout public).

Usage :
  python3 scripts/kefesh.py                      # affiche les événements Kefesh absents de data/events.json
  python3 scripts/kefesh.py --out manquants.json # les écrit en JSON (pré-remplis au format SCHEMA.md, à VÉRIFIER)
  python3 scripts/kefesh.py --all                # inclut aussi « L'agenda » tout public (à trier à la main)
  python3 scripts/kefesh.py --dump tous.json     # écrit tous les événements Kefesh normalisés

Les entrées produites ne sont PAS à copier telles quelles : la procédure veille-rodez impose de retrouver
la source d'origine (champ `source_hint` = lien fourni par Kefesh, souvent le site de l'organisateur),
de vérifier date/horaire/prix/âge, puis de compléter les champs manquants.
"""
import argparse, datetime, difflib, html, json, pathlib, re, sys, time, unicodedata, urllib.request, urllib.error

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP_ID = '4014385'
SECTIONS = {'enfants': '67483833', 'agenda': '67463422'}
API = 'https://api.goodbarber.net/front/get_items/{app}/{section}/?page={page}&per_page=50'
UA = 'activites-enfant-rodez/1.0 (+https://github.com/hacuubo/ACTIVITES-ENFANT-RODEZ)'
COMMUNES = ['Rodez', 'Onet-le-Château', 'Onet le Château', 'Luc-la-Primaube', 'Luc la Primaube', 'La Primaube', 'Sébazac-Concourès', 'Sébazac',
            'Olemps', 'Le Monastère', 'Sainte-Radegonde', 'Druelle', 'Balsac', 'Baraqueville', 'Marcillac-Vallon', 'Marcillac', 'Bozouls',
            'Laissac', 'Salles-la-Source', 'Pont-de-Salars', 'Flavin', 'Agen-d\'Aveyron', 'Calmont', 'Ceignac', 'Montrozier', 'Gages',
            'Moyrazès', 'Clairvaux', 'Espalion', 'Villefranche', 'Millau', 'Decazeville', 'Naucelle', 'Rignac']

def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def fetch(url, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception as ex:  # connexion réinitialisée fréquente sur ce site
            last = ex; time.sleep(2 * (i + 1))
    raise SystemExit(f'kefesh.fr injoignable ({last}) : {url}')

def fetch_section(section):
    items, page = [], 1
    while page < 20:
        data = fetch(API.format(app=APP_ID, section=section, page=page))
        batch = data.get('items') or []
        if not batch: break
        items += batch; page += 1; time.sleep(1)
    return items

def strip_html(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def guess_city(address):
    for c in sorted(COMMUNES, key=len, reverse=True):
        if re.search(r'\b' + re.escape(c) + r'\b', address or '', flags=re.I): return c.replace('Onet le Château', 'Onet-le-Château').replace('Luc la Primaube', 'Luc-la-Primaube')
    return (address or '').split()[-1] if address else ''

def ages_from_tags(tags):
    t = ' '.join(tags).lower()
    lo, hi = 15, 1
    if 'tout-petits' in t or 'tout petits' in t: lo, hi = min(lo, 1), max(hi, 4)
    if '5 - 12' in t or '5-12' in t: lo, hi = min(lo, 5), max(hi, 12)
    if 'ados' in t: lo, hi = min(lo, 11), max(hi, 15)
    if lo > hi: lo, hi = 1, 15
    return lo, hi

def normalize(it, section_key):
    title = it.get('title') or ''
    venue = ''
    if ' @ ' in title: title, venue = [x.strip() for x in title.split(' @ ', 1)]
    d = (it.get('date') or '')[:19]; e = (it.get('endDate') or '')[:19]
    date, time_ = d[:10], (None if it.get('allDay') else d[11:16] or None)
    end_date = e[:10] if e and e[:10] != date else None
    end_time = (None if it.get('allDay') else (e[11:16] if e else None))
    tags = []
    for v in (it.get('subsections') or {}).values(): tags += [x for x in v if x != 'Tous']
    tags = sorted(set(tags))
    amin, amax = ages_from_tags(tags)
    address = strip_html(it.get('address') or '')
    return {
        'kefesh_id': it.get('id'), 'kefesh_url': it.get('url'), 'section': section_key,
        'title': title, 'venue': venue or address, 'summary': strip_html(it.get('summary') or '')[:140],
        'description': strip_html(it.get('content') or '')[:600],
        'date': date, 'end_date': end_date, 'time': time_, 'end_time': end_time,
        'address': address, 'city': guess_city(address),
        'lat': float(it['latitude']) if it.get('latitude') else None, 'lng': float(it['longitude']) if it.get('longitude') else None,
        'age_min': amin, 'age_max': amax, 'price': 'Gratuit' if 'Gratuit' in tags else 'Non communiqué',
        'phone': it.get('phoneNumber') or None, 'email': it.get('email') or None,
        'source_hint': it.get('urlEvent') or it.get('urlShop') or None, 'tags': [norm(t) for t in tags],
    }

def same(a, b):
    """a = événement Kefesh normalisé, b = événement de data/events.json."""
    if a['date'] != b['date'] and not (b.get('end_date') and b['date'] <= a['date'] <= b['end_date']): return False
    ta, tb = norm(a['title']), norm(b['title'])
    ratio = difflib.SequenceMatcher(None, ta, tb).ratio()
    if ratio >= 0.6 or ta in tb or tb in ta: return True
    same_place = norm(a['venue'])[:12] == norm(b.get('venue'))[:12] or (a['lat'] and abs(a['lat'] - float(b['lat'])) < 0.0015 and abs(a['lng'] - float(b['lng'])) < 0.002)
    return bool(same_place and (a.get('time') or '') == (b.get('time') or '') and ratio >= 0.35)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--all', action='store_true', help="inclure aussi la rubrique « L'agenda » (tout public)")
    ap.add_argument('--out', help='fichier JSON des événements manquants')
    ap.add_argument('--dump', help='fichier JSON de tous les événements Kefesh normalisés')
    ap.add_argument('--events', default=str(ROOT / 'data' / 'events.json'))
    args = ap.parse_args()

    ours = json.loads(pathlib.Path(args.events).read_text(encoding='utf-8')).get('events', [])
    today = str(datetime.date.today())
    seen, kefesh = set(), []
    for key in (['enfants', 'agenda'] if args.all else ['enfants']):
        for it in fetch_section(SECTIONS[key]):
            if it.get('id') in seen: continue
            seen.add(it.get('id'))
            n = normalize(it, key)
            if n['date'] and (n['end_date'] or n['date']) >= today: kefesh.append(n)
    kefesh.sort(key=lambda e: (e['date'], e['time'] or ''))
    if args.dump: pathlib.Path(args.dump).write_text(json.dumps(kefesh, ensure_ascii=False, indent=2), encoding='utf-8')

    missing = [k for k in kefesh if not any(same(k, o) for o in ours)]
    print(f'{len(kefesh)} événements à venir sur Kefesh ({"enfants + agenda" if args.all else "rubrique enfants"}), {len(kefesh) - len(missing)} déjà présents, {len(missing)} manquants :')
    for k in missing:
        print(f"  - {k['date']} {k['time'] or 'journée'} | {k['title']} | {k['venue']}, {k['city']} | {', '.join(k['tags']) or 'tous'} | source : {k['source_hint'] or 'aucune'}")
    if args.out:
        pathlib.Path(args.out).write_text(json.dumps(missing, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'→ écrit dans {args.out}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
