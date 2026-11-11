---
name: veille-rodez
description: Procédure hebdomadaire de veille des activités enfants (1-15 ans) à Rodez et 20 km alentour, qui régénère data/events.json et le publie. Utilisée par la Routine du mercredi.
---

# Veille hebdomadaire « Sorties Enfants Rodez »

Objectif : produire un `data/events.json` **exhaustif, vérifié et à jour** couvrant les **16 prochaines semaines** (à partir d'aujourd'hui), pour des enfants de 1 à 15 ans, en famille, seuls ou entre amis, à **Rodez et dans un rayon de 20 km**. Puis valider, committer et pousser.

Ne jamais inventer un événement. Chaque entrée doit provenir d'une page consultée (champ `source`).

## 0. Préparation

1. Se placer dans le dépôt (`git status`). S'il n'est pas cloné : `git clone https://github.com/hacuubo/ACTIVITES-ENFANT-RODEZ` (attacher le dépôt avec `add_repo` si nécessaire).
2. `git fetch origin` puis se placer sur la branche par défaut (`git remote show origin | grep 'HEAD branch'`) à jour.
3. Lire `docs/SCHEMA.md` (format des données) et le `data/events.json` courant (pour conserver les événements encore valides et leurs `id`, qui servent aux favoris des utilisateurs).
4. Créer un dossier de travail dans le scratchpad : un fichier JSON par famille de sources.

## 1. Collecte (répartir sur 5 à 6 agents en parallèle, un par famille A à F)

Pour chaque famille, faire des recherches web (WebSearch, requêtes en français, avec le mois et l'année) puis lire les pages (WebFetch) pour extraire : titre, date(s), horaires, lieu, adresse, tranche d'âge, prix, téléphone, lien de réservation.

### A. Institutions
- Ville de Rodez : https://www.ville-rodez.fr/agenda/ ; Médiathèque : https://mediatheque.ville-rodez.fr/agenda/ ; Ludothèque, Maison des jeunes, centres sociaux, MJC : https://www.mjcrodez.fr/agenda/
- Rodez Agglomération : https://www.rodezagglo.fr/informations-pratiques/agenda-des-manifestations/ ; Musée Fenaille, Musée Soulages (https://musee-soulages-rodez.fr), Musée Denys-Puech, piscine Aquavallon, conservatoire.
- Office de tourisme : https://www.rodez-tourisme.fr/agenda/ (rubriques famille, grands événements, marchés, Noël)
- Département de l'Aveyron : https://aveyron.fr (agenda, archives départementales, Aveyron Culture), https://www.tourisme-aveyron.com
- Mairies (agenda / actualités) : Onet-le-Château, Luc-la-Primaube, Sébazac-Concourès, Olemps, Le Monastère, Sainte-Radegonde, Druelle-Balsac, Baraqueville, Marcillac-Vallon, Bozouls, Laissac-Séverac-l'Église, Salles-la-Source, Pont-de-Salars, Flavin, Agen-d'Aveyron, Calmont, Clairvaux-d'Aveyron, Moyrazès.

### B. Lieux culturels
- Salles : Le Club (Onet), La Baleine (Onet), Amphithéâtre de Rodez, Salle des fêtes de Rodez, La Menuiserie, Maison du Peuple, théâtres et compagnies (marionnettes, cirque, conte).
- Cinémas : CGR Rodez (séances jeune public, ciné-goûter, avant-premières), festivals de cinéma jeune public.
- Musées et patrimoine : ateliers vacances, visites famille, nocturnes, Journées du patrimoine, Nuit des musées, Fête de la science.
- Librairies et médiathèques : bébés lecteurs, heure du conte, dédicaces jeunesse, salons du livre.

### C. Fêtes, loisirs, saisons
- Fête foraine et foires de Rodez, cirques de passage (Medrano, Zavatta, etc.), carnaval, Halloween, Marché de Noël, patinoire, Père Noël, spectacles de Noël, feux d'artifice, Téléthon, fêtes votives des communes, chasse aux œufs, fête de la musique, 14 juillet, festivals d'été (Estivada…), Rodez plage.
- Loisirs : trampoline park, laser game, bowling, escape game, accrobranche, parcs de loisirs, fermes pédagogiques, poney-clubs, Haras national, Cascades de Salles-la-Source, Terra Memoria (Bozouls), base de loisirs de Pont-de-Salars, piscines : **inclure uniquement des créneaux datés** (animations, horaires vacances, stages), pas l'ouverture permanente.
- Sport : matchs avec animations jeunes (RAF, rugby…), courses familles, fête du sport, baptêmes, tournois ouverts.

### D. Associations, ateliers, ados
- Ateliers datés : éveil musical, créatifs, cuisine, sciences (Petits Débrouillards, Fête de la science), codage, nature (CPIE, LPO Aveyron), parents-enfants, bébés nageurs.
- Stages de vacances (multi-sports, arts, cirque, théâtre, langues) : vérifier le calendrier scolaire zone C.
- Ados 11-15 : concerts, e-sport, ateliers vidéo/podcast, soirées, sorties organisées par les espaces jeunes / PIJ.
- Sources : sites des associations, https://www.helloasso.com (événements Rodez), pages publiques Facebook via recherche, Familles Rurales, Francas, Léo Lagrange, UFOLEP/USEP.

### F. Associations et clubs sportifs (balayage systématique)
Objectif : ne rater aucune occasion sportive ouverte aux enfants **datée** (pas les entraînements hebdomadaires réservés aux licenciés) :
- Portes ouvertes, journées découverte, séances d'essai gratuites (rentrée septembre, janvier, après chaque vacances), baptêmes (plongée, escalade, poney, kayak, voile, tir à l'arc), initiations.
- Stages de vacances (multisports, foot, rugby, tennis, judo, gym, danse, natation, escalade, équitation, cirque, échecs) : programmes de Toussaint, Noël, février, Pâques, été.
- Tournois et compétitions jeunes ouverts au public ou aux non-licenciés, galas de fin d'année, fêtes de club, courses enfants (Rose de Rodez, Monas'trail, trails avec courses kids, Octobre rose), randonnées familles, sorties nature encadrées.
- Événements jeune public des clubs pros ou semi-pros : Rodez Aveyron Football (animations enfants, stages RAF), Rodez Rugby, Rodez Basket, Rodez Handball, Ruthénois volley, Aquavallon (bébés nageurs, animations vacances, nocturnes), patinoire.
- Sources : annuaire des associations de la Ville de Rodez (ville-rodez.fr, rubrique sport / vie associative), Office municipal des sports de Rodez, Rodez Agglomération (équipements : Aquavallon, gymnases, stade), annuaires des communes voisines (Onet-le-Château, Luc-la-Primaube, Sébazac, Olemps, Le Monastère, Baraqueville, Bozouls, Marcillac), comités départementaux de l'Aveyron (CDOS 12, district de football Aveyron, comité rugby Aveyron, judo, gym, tennis, natation, escalade, équitation/CDE 12, cyclisme, athlétisme, handball, basket), UFOLEP/USEP Aveyron, Familles Rurales, MJC (sections sportives), sites et pages Facebook publiques des clubs (via WebSearch), HelloAsso (inscriptions stages), Sport Adapté / handisport Aveyron.
- Requêtes : `club <sport> Rodez portes ouvertes <année>`, `stage <sport> vacances <Toussaint|Noël|février|Pâques|été> Rodez enfants`, `séance d'essai <sport> enfants Rodez`, `tournoi jeunes <sport> Aveyron <mois> <année>`, `baptême poney Rodez`, `course enfants Rodez <année>`, `Aquavallon animations vacances`, `Rodez Aveyron Football stage enfants`.
- Catégorie `sport`, `audience` = `enfant` pour un stage déposé, `famille` pour une course ou une journée découverte parents-enfants, `ados` si 11-15 uniquement.

### E. Agrégateurs et presse (pour ne rien rater)
- https://12.agendaculturel.fr/jeune-public/ , https://oazis.app/sorties/rodez/enfants , Unidivers Rodez, Kidiklik / Citizenkid Aveyron, https://www.ladepeche.fr (Rodez sorties), https://www.centrepresseaveyron.fr (agenda), Sortir en Aveyron, Bougeenfamille, Le Petit Moutard.

Requêtes utiles : `"Rodez" enfants <mois> <année>`, `spectacle jeune public Rodez <mois>`, `atelier enfants Onet-le-Château`, `marionnettes Aveyron <année>`, `cirque Rodez <année>`, `fête foraine Rodez`, `Halloween Rodez`, `marché de Noël Rodez <année>`, `stage vacances <Toussaint|Noël|février|Pâques|été> Rodez enfants`, `ados Rodez sortie <mois>`.

### G. Croisement avec Kefesh (obligatoire, après la collecte A-F)
[Kefesh](https://www.kefesh.fr) est un agenda de sorties à Rodez tenu par des bénévoles ; sa rubrique « Pour les enfants » (https://www.kefesh.fr/pour-les-enfants) sert de **filet de sécurité** : tout ce qu'elle contient et que nous n'avons pas doit être retrouvé à la source et ajouté.
1. Lancer `python3 scripts/kefesh.py --out <scratch>/kefesh_manquants.json` : le script interroge l'API du site (rubrique enfants) et liste les événements à venir absents de `data/events.json`. Avec `--all`, il ajoute la rubrique « L'agenda » (tout public) : y repérer les sorties familiales (spectacles tout public, fêtes, matchs, marchés de Noël) et ignorer les conférences, concerts de bar, soirées adultes.
2. Pour **chaque** événement manquant : ouvrir le lien `source_hint` (site de l'organisateur fourni par Kefesh) ou, s'il manque, chercher l'organisateur (WebSearch `"<titre>" <lieu> <année>`) et lire la page officielle. Vérifier date, horaire, âge, prix, réservation, téléphone. Créer l'entrée au format `docs/SCHEMA.md` avec `source` = page officielle ; si aucune page officielle n'existe, `source` = fiche Kefesh (`kefesh_url`) et ajouter le tag `a-confirmer`. Dans tous les cas, ajouter le tag `kefesh` et renseigner `secondary_sources` avec l'URL de la fiche Kefesh.
3. Si Kefesh donne une date ou un horaire différent des nôtres pour un événement déjà présent, retourner à la source officielle et corriger.
4. Ne rien copier du texte de Kefesh : rédiger `summary` et `description` à partir de la source officielle.
5. Dans le compte rendu : nombre d'événements Kefesh croisés, ajoutés, corrigés, et ceux écartés (hors cible ou hors zone) avec la raison.

## 2. Géocodage

Pour chaque lieu (une fois par lieu) :
```
curl -sS -A "activites-enfant-rodez/1.0" "https://nominatim.openstreetmap.org/search?q=<lieu, ville>&format=json&limit=1"
```
Max 1 requête/seconde. Si introuvable : géocoder la mairie de la commune et le signaler dans `description`. Rejeter tout lieu à plus de 20 km de Rodez (44.3506, 2.5750).

## 3. Assemblage et contrôle

1. Fusionner : `python3 scripts/merge.py --keep-existing --from <aujourd'hui> --to <aujourd'hui + 16 semaines> <fichiers de recherche>` (dédoublonne, retire le passé, trie, écrit `updated_at`).
2. Re-vérifier les événements conservés de l'ancien fichier dont `source_checked` a plus de 3 semaines : rouvrir la source ; supprimer ceux annulés ou introuvables ; mettre à jour `source_checked`.
3. **Contrôle de pertes, obligatoire** — garder une copie de l'ancien fichier avant la fusion
   (`git show HEAD:data/events.json > <scratch>/avant.json`), puis :
   ```
   python3 scripts/qa.py --before <scratch>/avant.json --inputs <fichiers de collecte>
   ```
   `--inputs` attrape les créneaux où la fusion a avalé des séances distinctes (deux stages d'âges différents
   au même endroit), `--before` attrape les fiches de la base qu'aucun agent n'avait reprises et qui ont
   disparu. **Toute disparition qui n'est pas une décision explicite est une perte : la rétablir.**
4. **Réconciliation des champs, obligatoire** — `merge.py` ne remplit que les champs vides, donc toute
   correction d'un agent sur un champ déjà rempli est perdue. Relire les fichiers de collecte, comparer champ
   par champ (`time`, `end_time`, `end_date`, `age_min`, `age_max`, `price`, `days_of_week`, `venue`,
   `address`, `phone`) et réappliquer. Quand deux agents proposent deux valeurs différentes pour le même
   champ, garder celle de la base et trancher à la main.
5. **Appliquer les corrections de date, les suppressions et les déduplications directement dans
   `data/events.json` après la fusion**, jamais par un fichier d'entrée : `merge.py` retrouve l'ancienne fiche
   par son `id` et garde « la plus complète », donc l'ancienne valeur.
6. Vérifier la cohérence entre le slug de chaque `id` et son `title` : un écart révèle une fusion ratée d'une
   veille précédente (cas vécu : un `id` « carnet secret » portant le titre d'un atelier de soda).
7. **Réinscrire `source_checked`, obligatoire** — `fuse()` ne remplissant que les champs vides, le
   `source_checked` mis à jour par un agent est écarté dès que la version de la base est jugée « la plus
   complète ». Toute la passe de re-vérification devient alors invisible et la veille suivante redemande le
   même travail (82 fiches concernées le 04/11, dont 77 de l'agent de re-vérification). Après fusion, pour
   chaque `id` qu'un fichier d'agent a émis avec `source_checked` = aujourd'hui, forcer la valeur dans
   `data/events.json`. Ne forcer que ceux-là : une fiche que personne n'a rouverte garde sa date d'origine.
8. Retirer les fiches dont `end_date` (ou `date`) est antérieure au `from` de la période : `merge.py` garde
   tout ce qui finit « après hier », ce qui laisse passer 2 ou 3 événements de la veille du jour J.
9. `python3 scripts/validate.py` doit passer sans erreur (corriger jusqu'à 0 erreur).
10. Contrôle qualité : `summary` d'une phrase claire, `age_min`/`age_max` cohérents, `audience` juste (`ados` si réservé aux 11-15), `price` renseigné, téléphone au format `05 65 00 00 00`, catégories exactes.

## 4. Publication

1. `git add data/events.json` (uniquement les données, sauf correction nécessaire d'un script).
2. Commit : `Veille du <date> : N activités (M nouvelles)`.
3. `git push -u origin <branche par défaut>` (retenter 4 fois avec attente 2/4/8/16 s en cas d'erreur réseau). Le workflow GitHub Pages redéploie l'application automatiquement.

## 5. Compte rendu (fin de session)

Donner en 10 lignes maximum : nombre total d'événements, nouveaux, supprimés, sources injoignables cette semaine, événements notables à venir (fête foraine, cirque, Noël…), et toute anomalie à corriger dans l'application.

## Retours d'expérience (mis à jour à chaque veille)

- **mediatheque.ville-rodez.fr** répond souvent 503 : réessayer plus tard dans la session, sinon passer par les fiches Diffusio de ville-rodez.fr ou par oazis.app.
- **Listes Diffusio** (ville-rodez.fr/agenda, rodezagglo.fr) : seuls ~15 items sont rendus côté serveur et la pagination AJAX ne fonctionne pas ; compléter par les sites des musées et des communes, et par des recherches web ciblées (`site:ville-rodez.fr <mois>`).
- **oazis.app**, **onet-le-chateau.fr** : accessibles via WebFetch uniquement (curl bloqué).
- **aveyron.fr** : anti-bot, contenu inaccessible → utiliser tourisme-aveyron.com et la presse.
- **12.agendaculturel.fr**, **helloasso.com** (listes), **maisondulivre.com** : 403 → passer par WebSearch avec `site:` pour lire les extraits, ou ignorer.
- **Programmes publiés tardivement** : stages MJC (≈3 semaines avant les vacances), Halloween au Haras de Rodez et Noël à Rodez (marché place Foch, patinoire, village du Père Noël : publication en novembre), patinoire d'Onet, Téléthon, animations Aquavallon des vacances. Les rechercher explicitement à chaque veille tant qu'ils ne sont pas publiés.
- **Cirques de passage** : rechercher `cirque Rodez <mois> <année>` et les pages Facebook publiques via la recherche ; aucun n'était annoncé au 19/09/2026.
- **Nominatim** renvoie parfois 429 : attendre 2 s et réessayer ; si un lieu est introuvable, géocoder la mairie et le signaler dans `description`.
- Exclus car au-delà de 20 km : Espalion (Calmont d'Olt), Salmiech, Villefranche-de-Rouergue, Conques, Naucelle.
- **Sport (collecte du 20/09/2026)** : calendriers de courses fiables pour les épreuves enfants : le-sportif.com, running.life, gotrail.run, jogging-international.net ; matchs de rugby : rodez-rugby.com + rugbyamateur.fr ; judo : calendrier judo-jra.ffjudo.com ; poney : poneyvillage.com ; concours équestres Combelles : rodez-tourisme.fr. Bloqués : HelloAsso (403), kikourou.net (403), rodez.asptt.com (403), Facebook (connexion). Les stages vacances du RAF, du Stade Rodez Athlétisme, de la MJC et du P'tit Club sont publiés 3 à 4 semaines avant chaque période : les rechercher à chaque veille. Les animations vacances d'Aquavallon ne sont annoncées que sur les réseaux sociaux : chercher aussi la presse (Centre Presse, La Dépêche) qui les relaie.
- **Croisement Kefesh (20/09/2026)** : l'API GoodBarber du site répond bien (parfois une connexion réinitialisée : le script réessaie). Sources d'organisateurs bloquées : maisondulivre.com (403), lm-calligraphie.com (403), billetterie.festik.net (JS uniquement) → passer par la presse (12actu.com, lepetitjournal.net) pour confirmer, sinon fiche Kefesh + tag `a-confirmer`. Calendrier du RAF : le site officiel est un widget illisible ; utiliser fotmob.com (heures en UTC, +2 h l'été / +1 h l'hiver) recoupé avec beinsports.com ; une heure « 00:00 » chez beIN signifie « à définir » → laisser `time` à null.
- **Croisement Kefesh (2e passage, 20/09/2026)** : sur 43 événements Kefesh absents, la quasi-totalité étaient adultes (conférences, soirées bar au Krill, dédicaces littéraires, comedy/impro) → aucun ajouté. Un écart de date signalé par Kefesh pour le match RAF-Montpellier (16/10 chez Kefesh vs 19/10 chez nous) s'est révélé être une erreur de Kefesh (slug d'URL beIN trompeur) : la date 19/10 était correcte, confirmée par fotmob.com et footmercato.net. Ne pas corriger aveuglément sur un simple écart Kefesh : toujours recouper avec au moins deux sources sportives avant de changer une date. **la-baleine.eu** publie parfois un PDF de programmation resté sur l'ancienne saison : vérifier la saison affichée avant d'utiliser une info. **ffhandball.fr / rochandball.com** : calendrier en image/JS illisible par WebFetch, passer par de.rodez-tourisme.fr (Terminkalender) ou rodez-tourisme.fr/agenda pour les dates de matchs (l'heure précise y manque souvent). **eterritoire.fr** : 403. **tourisme-aveyron.com** : certaines fiches d'événements renvoient 410 Gone (contenu expiré) même si trouvées par recherche — ne pas les utiliser comme source si la page ne charge plus.
- **Pagination des agendas Diffusio : résolue (veille du 23/09/2026)**. Contrairement à ce qui était noté plus haut, la
  pagination n'est pas morte : ajouter `?id1[currentPage]=N` à l'URL de la liste (ville-rodez.fr, rodezagglo.fr,
  pontdesalars.fr, olemps.fr, lemonastere.fr, moyrazes.fr) et `?ReactWay[currentPage]=N` sur tourisme-aveyron.com.
  On récupère ainsi la totalité des fiches (224 sur ville-rodez.fr, 316 sur rodezagglo.fr) au lieu des 15 premières.
  **C'est la méthode à utiliser en priorité pour les familles A, B et C.**
- **terramemoria.fr** : le domaine n'appartient plus au musée de Bozouls, il redirige vers un comparateur de casinos
  en ligne. Ne plus l'utiliser : passer par tourisme-aveyron.com ou l'office de tourisme Terres d'Aveyron.
- **maisondulivre.com** : Cloudflare (403) en WebFetch comme en curl avec un user-agent de navigateur ; le miroir
  `placedeslibraires.fr` est également en 403. Les animations jeunesse de la librairie ne sont donc vérifiables que
  par la fiche Kefesh → `source` = fiche Kefesh + tag `a-confirmer`, téléphone 05 65 73 36 14 pour confirmation.
- **Rugby (veille du 23/09/2026)** : `rugbyamateur.fr/club/rodez-rugby/calendrier/` donne le calendrier complet de la
  saison avec les horaires (Fédérale 2 : coup d'envoi à 15 h 15) — source la plus fiable, le site du club n'a pas de
  page `/calendrier`. Attention, la page mêle deux lignes le 18/10 (« Rodez - Albi 15 h 00 » et
  « Rodez - Decazeville 15 h 15 ») : l'agenda officiel de la Ville et l'office de tourisme ne connaissent que
  Rodez - Decazeville, retenu seul. À retrancher si un match Albi se confirme.
- **Handball ROC (veille du 23/09/2026)** : `rochandball.com/calendrier/` publie ses calendriers en **images**.
  Utiliser les fiches individuelles `de.rodez-tourisme.fr/terminkalender/<id>-match-n1m-roc-handball---<adversaire>`
  (trouvées par `site:rodez-tourisme.fr Match Roc Handball`) et `unidivers.fr` : les dates y sont fiables, mais
  **l'heure manque toujours** ; la fiche Kefesh donne 19 h pour les matchs N1M.
- **Piège de `scripts/merge.py`** : deux rencontres différentes le même jour dans la même salle sont fusionnées
  (le 26/09/2026, le N1M contre Libourne a écrasé le N3F contre Tournefeuille en gardant l'ancien `id`).
  **Après chaque fusion, comparer les titres des `id` conservés avec la version précédente** et rétablir à la main
  les événements écrasés.
- **Croisement Kefesh (23/09/2026)** : 81 événements à venir, 17 déjà présents, 64 manquants dont la très grande
  majorité d'adultes (conférences, concerts de bar, dédicaces, comedy). Retenus : les 4 matchs N1M du ROC,
  « Chat fait boum ! » (13/01/2027, Krill), l'après-midi T'Choupi et la soirée manga de la Maison du Livre.
  Kefesh redonne **encore** une date fausse pour RAF - Montpellier (16/10 au lieu du 19/10, confirmé par fotmob) :
  ne jamais corriger une date de match sur la seule foi de Kefesh.
- **Nouvelles sources bloquées (23/09/2026)** : staderodez.athle.fr et cda12.athle.fr (503), poneyvillage.ffe.com (503),
  lepetitmoutard.fr (403), conques-marcillac.c3rb.org (403), mediatheque.aveyron.fr (403),
  mediatheque-onet-le-chateau.fr (403), mediatheque.bozouls.fr (503), france-voyage.com (403),
  placedeslibraires.fr (403), mjcllp.fr (rendu 100 % JS, sous-pages en 404 : passer par les fiches de l'office de
  tourisme). Sites de mairie injoignables : marcillac-vallon.fr, laissac-severac-leglise.fr, salles-la-source.fr,
  flavin.fr, calmont12.fr, clairvaux-aveyron.fr, sebazac-concoures.fr, druelle-balsac.fr ; bozouls.fr/agenda est en
  404, la bonne URL est `bozouls.fr/fr/actualites/agenda`.
- **Budget de recherche** : chaque agent épuise ses 200 WebSearch avant la fin. Privilégier WebFetch sur les agendas
  paginés (voir la première puce) et réserver WebSearch aux pistes précises.
- **Orthographe des communes** : écrire `Laissac-Séverac-l'Église` (forme retenue dans les données), pas
  « Laissac-Sévérac l'Église » — sinon l'application affiche deux communes distinctes.
- **Programmes publiés en image : lisibles (veille du 30/09/2026)**. Ce qui bloquait jusqu'ici (« calendrier en
  images », « flyer en JPG ») se règle en téléchargeant le visuel puis en l'ouvrant avec l'outil Read, qui affiche
  l'image : `curl -sS -o /tmp/prog.jpg -A "Mozilla/5.0" <url>` puis Read sur `/tmp/prog.jpg`. C'est ainsi que le
  programme Toussaint 12-17 ans de la Ville de Rodez (`ville-rodez.fr/uploads/2026/09/2026_VACtoussaintS2-Web.jpg`)
  a été dépouillé jour par jour. **À appliquer aussi aux calendriers du ROC Handball.** Aucun OCR n'est installé
  (pytesseract absent) et il n'en faut pas.
- **Pagination : corrections importantes (30/09/2026)**. `rodez-tourisme.fr` **n'accepte pas** `?id1[currentPage]=N` :
  la vraie liste est `/agenda/les-sorties-a-rodez/?listpage=N` (22 pages, 256 fiches). `ville-rodez.fr/agenda`
  exige le **slash final** avant la query. `rodezagglo.fr/agenda/` redirige (301) vers
  `/informations-pratiques/agenda-des-manifestations/?id1[currentPage]=N` (317 fiches) : c'est la **seule** source
  paginée couvrant Onet, Luc-la-Primaube, Olemps, Sainte-Radegonde, Druelle-Balsac, Le Monastère et Sébazac.
  `tourisme-aveyron.com` : `/fr/evenements/agenda-aveyron?ReactWay[d]=~AAAA-MM-JJ~AAAA-MM-JJ&ReactWay[currentPage]=N`.
  `bozouls.fr` sert ses fiches sur `/fr/diffusio/bozouls/<slug>_TFO…`, pas sur `/fiche/agenda/`.
- **`onet-le-chateau.fr/evenements/page/N/`** (WebFetch uniquement) : 104 fiches sur 9 pages, dont tout le programme
  du Patio Centre Social — **la source la plus riche pour Onet-le-Château**, absente des agendas Diffusio. Elle a
  fourni à elle seule une trentaine d'activités le 30/09/2026.
- **`pontdesalars.fr/agenda` et `moyrazes.fr/agenda`** listent les fiches des communes voisines **avec leur distance**
  et affichent les **coordonnées GPS** de chaque lieu : géocodage gratuit, sans passer par Nominatim. Très utile pour
  le Lévezou et le Ségala.
- **`ville-rodez.fr/fiche/agenda/<slug>_TFO…` répond 200** là où `rodez-tourisme.fr/fiche/agenda/<même slug>` renvoie
  404 ou 503 : en cas d'échec sur un slug Tourinsoft, réessayer sur le domaine de la Ville (ou tourisme-occitanie.com).
- **`fest.fr`** : agenda par ville avec rayon de 10 km (`/agenda/aveyron/rodez`), pagination `?start=N`, filtres par
  catégorie, fiches avec adresse et coordonnées. Accessible en WebFetch seulement (curl refusé).
- **`centrepresseaveyron.fr` et `ladepeche.fr`** sont refusés par WebFetch mais **répondent en curl**
  (`centrepresseaveyron.fr/recherche?q=…`, sans slash final).
- **PDF** : `pypdf` est cassé dans l'environnement (`_cffi_backend` manquant). Utiliser **`pdfminer.six`**
  (`pip install pdfminer.six`, puis `extract_text`). WebFetch refuse les PDF de plus de 10 Mo : chercher la version
  basse définition.
- **Rugby, ambiguïté du 18/10 résolue (30/09/2026)** : ce n'était **pas** un doublon comme supposé le 23/09, mais deux
  rencontres réelles le même jour au stade Paul-Lignon — Fédérale 2 masculine Rodez - Decazeville à 15 h 15 et
  Fédérale 2 féminine Rodez - SC Albi à 15 h 00. Les deux sont désormais en base.
- **Erreurs de saisie des agendas municipaux sur le rugby (30/09/2026)** : sur ville-rodez.fr et rodezagglo.fr, la
  fiche « Rodez - Stade Belvesois » est datée du 13/12 mais son texte annonce le 10 janvier, et la fiche
  « Rodez - Levezou Segala XV » (17/01) contient le texte du match Belvesois. **Faire foi à
  `rugbyamateur.fr/club/rodez-rugby/calendrier/`**, pas aux fiches Diffusio, pour les dates de rugby.
- **Horaires des matchs de Ligue 2** : ne pas mettre `time` à null trop vite. Le 30/09/2026, un calendrier affichait
  « à définir » pour RAF - Reims (04/12) alors que footmercato.net **et** fotmob donnaient tous deux 20 h 00.
  Recouper au moins deux sources avant d'effacer un horaire déjà en base. Rappel du fuseau : fotmob affiche l'**UTC**
  (+2 h jusqu'au 25/10, +1 h ensuite).
- **Kefesh se trompe pour la 3e semaine consécutive** sur RAF - Montpellier (16/10 au lieu du 19/10, confirmé par
  fotmob et footmercato). Ce n'est plus un accident : **ignorer par principe les dates de match données par Kefesh.**
- **Fête foraine de Rodez : pas d'édition d'automne.** Elle se tient au Val de Bourran en mai-juin. En automne, la
  Ville n'organise qu'une foire annuelle et un marché aux chrysanthèmes (fin octobre, sans date fixe). Inutile de la
  rechercher d'octobre à janvier.
- **Piège `days_of_week`** : ne jamais s'en servir pour des dates isolées. Un `dow=[5]` du 23/10 au 11/12 affiche
  8 vendredis au lieu de 2 séances. Pour des dates non régulières, **créer une entrée par date**.
- **Tags** : les agents produisent volontiers des tags accentués et espacés (`Noël`, `marché de Noël`, `à revérifier`),
  affichés tels quels en badges `#…` par l'application. Normaliser systématiquement après collecte : minuscules,
  sans accents, tirets ; et `à revérifier` → `a-confirmer`.
- **Nouvelles sources bloquées (30/09/2026)** : fr.milesrepublic.com (429 + checkpoint Vercel), trainerday.com (403),
  liguesdefoot.fr (403), footmercato.net/club/<club>/calendrier (404 ; les pages `/live/<id>-<match>` fonctionnent),
  worldfootball.net (402), maxifoot.fr (404), aquavallon.fr (DNS inexistant → passer par
  `rodezagglo.fr/informations-pratiques/le-pole-aquatique/`), le-sportif.com/calendrier (404),
  judo-jra.ffjudo.com/agenda (404, utiliser `/evenement`), scorenco.com (JS vide), mjcrodez.fr/en-famille (404),
  luc-la-primaube.fr/agenda (vide sans JS → passer par rodezagglo.fr), aveyron-culture.com (agenda vide).
  Mairies toujours injoignables : sainte-radegonde12.fr, druelle-balsac.fr, laissac-severac-leglise.fr,
  salles-la-source.fr, agen-daveyron.fr, calmont12.fr, clairvaux-aveyron.fr, sebazac-concoures.fr,
  marcillac-vallon.fr, flavin.fr. **Leurs programmes Halloween et Téléthon communaux restent invérifiables.**
- **Hors zone, à ne plus proposer** : Ségur (21,8 km), Bertholène est en revanche à 16,8 km et donc éligible.
- **À rechercher explicitement à la prochaine veille** : le programme définitif de **Noël à Rodez** (marché place
  Foch, patinoire place de la Cité, village du Père Noël, grande roue, petit train : la page
  `rodez-tourisme.fr/agenda/noel/` affichait encore l'édition 2025 au 30/09 — la fiche actuelle repose sur l'appel à
  manifestation d'intérêt et porte `a-confirmer`, **à remplacer dès la publication**) ; patinoire d'Onet à
  l'Athyrium ; **Téléthon de Rodez et de l'agglo** (seul Druelle-Balsac est annoncé, en provisoire) ; **Halloween au
  Haras de Rodez** (toujours rien) ; **stages de Noël** de la MJC de Rodez, de la MJC d'Onet (inscriptions le 28/11),
  du RAF, du Stade Rodez Athlétisme et du Patio — tous attendus vers la mi-novembre ; ateliers « Mes vacances au
  musée » de Noël (Soulages, Fenaille, Denys-Puech) ; avant-premières et ciné-goûters du **CGR Rodez** (publiés à
  2 semaines, son API est bloquée par le proxy) ; animations de Noël des musées et de la médiathèque du 23/12 au
  04/01 ; programmes Toussaint de **Terra Memoria** (05 65 44 69 27) et de l'espace archéologique de **Montrozier**
  (05 65 70 71 45) ; **heures des matchs N3F du ROC** ; calendriers de **Rodez Basket** et du volley ruthénois,
  introuvables cette semaine ; **Fête de la science en Aveyron** (aucun programme départemental publié).

### Veille du 07/10/2026

- **Le piège le plus coûteux de la semaine : les fiches d'agenda qui décrivent l'édition précédente.** Deux cas, tous
  deux détectés par le croisement Kefesh, pas par la collecte :
  - `rodez-tourisme.fr/offres/mes-vacances-de-la-toussaint-au-musee-soulages-rodez-fr-3895769/` est passée en **404** et
    décrivait le programme de l'an dernier : les 5 ateliers « Cinéma d'animation » / « Machinations créatives » qu'elle
    avait fournis le 20/09 étaient **absents du programme officiel** publié le 01/10 par le musée. Supprimés et
    remplacés par les 9 vrais ateliers.
  - `kiwanis.fr/agenda/15eme-salon-chocolat-delices/` est une page d'archive **sans année** annonçant la 15e édition les
    31/10-01/11 ; la vraie édition 2026 est la **20e, les 21 et 22 novembre** (fiche de la Ville).
  **Règle à appliquer :** pour tout événement annuel récurrent, se fier à la **page de l'organisateur** (le musée, le
  club, l'association), jamais à une fiche d'agrégateur ou d'office de tourisme seule ; un numéro d'édition ou une page
  sans millésime est un signal d'alarme. L'**agenda propre du musée Soulages** (`musee-soulages-rodez.fr/fr/agenda/`)
  est plus fiable que les fiches Tourinsoft qui le recopient.
- **Piège de l'ordre des fichiers passés à `merge.py`** : les fichiers sont traités **dans l'ordre de la ligne de
  commande**. Si un fichier de re-vérification **renomme** un événement, il est appliqué *après* les fichiers de
  collecte, et l'événement renommé se retrouve en double (cas vécu : « Extrem'Ados » renommé « NovAdo invite le
  Conservatoire » alors que la collecte avait déjà créé l'entrée sous ce nom). **Passer le fichier de re-vérification
  en premier**, et dans tous les cas faire après fusion un balayage « même date + même heure + même lieu », qui attrape
  ce que `same_event()` laisse passer (noms de salle divergents : « Athyrium » vs « Espace Athyrium », tiret cadratin
  vs trait d'union).
- **`kefesh.py` peut faire un faux positif de doublon** : `same()` conclut à l'identité sur le seul ratio de titre
  (≥ 0,6) sans contrôler la commune. Un « Yoga enfant et famille » à Onet-le-Château a été masqué par un « Atelier yoga
  en famille » à Laissac, même jour même heure. Relire la liste `--dump` et pas seulement les « manquants ».
- **Croisement Kefesh (07/10/2026)** : 172 événements à venir, 57 déjà présents, 115 manquants. 25 ajoutés (ateliers de
  Toussaint du musée Soulages, explorations sensibles du musée Denys-Puech, journée « Onet Cap », yoga enfants/famille),
  2 corrections de fond (Soulages, salon du chocolat), ~85 écartés comme adultes, ~25 hors fenêtre.
  **Kefesh se trompe pour la 4e semaine consécutive** sur RAF - Montpellier (16/10 au lieu du 19/10).
- **Sources nouvellement utiles**
  - **`12actu.com` : la meilleure trouvaille de la semaine.** Agenda structuré en **JSON-LD**, sans paywall :
    `https://www.12actu.com/agenda?categorie=<famille|spectacles|litterature|fetes|sport|cinema|expos|marches|concerts>&page=N`
    (et `/rodez/agenda?...`). Fournit **lat/lng, adresse et âges** → géocodage gratuit, pas besoin de Nominatim.
    À mettre en source paginée prioritaire.
  - `bases.athle.fr/asp.net/liste.aspx?frmbase=calendrier&frmmode=1&frmespace=0&frmdepartement=012&frmsaison=2026|2027`
    (calendrier FFA Aveyron complet — remplace staderodez.athle.fr et cda12.athle.fr, tous deux en 503).
  - `allocine.fr/salle/cinema-W1200/avant-premiere/` (W1200 = CGR Rodez) : les avant-premières, là où l'API du CGR est
    bloquée par le proxy.
  - `unidivers.fr/events/categorie/rodez/` (8 pages) et les fiches `unidivers.fr/event/<slug>-<ville>-aveyron-<date>/` :
    donnent horaire **+ âge + tarif** là où les autres agrégateurs sont muets.
  - `cpie-rouergue.com` (et non `.fr`, qui n'a pas de DNS) : `/cpie-du-rouergue/agenda/month/0/year/0`.
  - `la-baleine.eu/la-baleine-le-theatre/programmation-la-baleine/` affiche bien la saison 2026-2027 (le piège du vieux
    PDF signalé le 20/09 n'existe plus).
  - Les agendas paginés de **ville-rodez.fr et rodezagglo.fr répondent en `curl`** (encoder les crochets :
    `?id1%5BcurrentPage%5D=N`), nettement plus rapide que WebFetch ; les fiches Diffusio `rodezagglo.fr/fiche/agenda/<slug>`
    contiennent **toutes les dates multiples, les âges et les tarifs** (les 9 ateliers Soulages tiennent dans une fiche).
  - `tourisme-aveyron.com` : le filtre de dates `ReactWay[d]` **n'est pas appliqué côté serveur** (4 051 résultats),
    mais la **recherche plein texte `ReactWay[q]=<mot-clé>` marche très bien**.
  - **PDF : `pdftotext` (`/usr/bin/pdftotext`) est installé et fonctionne** — le plus simple. `pdfminer.six` s'installe
    avec `pip install --break-system-packages` mais ne tourne que sous `python3.13` (`python3` est un 3.11 sans le module).
- **Sources nouvellement bloquées** : archives.aveyron.fr (403), ludotheque.ville-rodez.fr (DNS inexistant — la
  ludothèque est intégrée à la médiathèque), competitions.ffbb.com et resultats.ffbb.com (403 / 503),
  ffecompet.ffe.com (403), sport-flash.com (403), lepetitjournal.net (403 en WebFetch **et** en curl),
  sortirenaveyron.com et bougeenfamille.com (**domaines inexistants**), kidiklik.fr/12 (404, pas d'édition Aveyron),
  itftennis.com (page vide), mjc-onet*.fr (502), parc-saint-hubert.com (502), zamcreatif.fr/ateliers (liste les
  ateliers mais **sans dates ni âges**). **HelloAsso est en 403 même sur la page d'un événement précis** : piste à
  abandonner. **`mediatheque.ville-rodez.fr` : 503 sur une dizaine de tentatives réparties sur toute la session**, en
  WebFetch comme en curl — les animations de la médiathèque de Rodez sont invérifiables depuis trois veilles.
- **Pièges de fiabilité** : `fest.fr` **mélange les descriptifs d'une fiche à l'autre** (« Tourne fête » porte le texte
  de « Fa'a'amu ») — ne jamais reprendre ses descriptions, recouper sur 12actu ou unidivers.
  `ladepeche.fr/recherche` répond 200 mais **ignore la requête** (renvoie les derniers articles) : inutilisable.
  `rodez-tourisme.fr/agenda` est désormais **100 % JS** : seules les fiches sont statiques, passer par la pagination de
  ville-rodez.fr et rodezagglo.fr. `oazis.app` a fourni une **représentation fantôme** de Colinet 2026 le 19/11 : la
  fiche officielle de l'agglo ne donne que les **20, 21, 27 et 28 novembre**.
  `centrepresseaveyron.fr` en curl : le corps de l'article est lisible **en entier avant le mur d'abonnement**
  (extraire `<article>` puis dé-baliser).
- **Sport** : **Rodez Basket est descendu en Prénationale** (Centre Presse du 14/09/2026), d'où son absence des pages
  nationales de la FFBB — son calendrier reste introuvable, comme celui du volley (club = **MJC Rodez volley**,
  Prénationale F et Régionale 1 M). Les **heures des matchs N3F du ROC** restent introuvables : rochandball.com publie
  en images (lisibles avec l'astuce `curl` + Read) mais ne donne que des week-ends, et api-dofa.ffhandball.fr est
  injoignable (502). Les 4 matchs N3F de la fenêtre sont en base aux bonnes dates, sans horaire.
  `rugbyamateur.fr/club/rodez-rugby/calendrier/` a confirmé tous les matchs de rugby déjà en base, sans changement.
- **Noël à Rodez : toujours pas de programme au 07/10.** `rodez-tourisme.fr/agenda/noel/` et ses sous-pages affichent
  **encore l'édition 2025-2026** ; `ville-rodez.fr/vivre-a-rodez/.../noel-a-rodez/` est en 404. Seul document officiel :
  l'appel à manifestation d'intérêt `ville-rodez.fr/uploads/2026/07/Appel-a-Manifestation-Noel-2026.pdf`, qui fixe
  l'occupation du domaine public **du 05/12/2026 au 03/01/2027** (marché place Foch + animation familiale place
  d'Armes). ⚠️ **Une recherche web renvoie volontiers « 6 déc. - 4 janv., 27 chalets, grande roue » : c'est le
  programme 2025, à ne pas reprendre.**
- **Fête foraine d'automne : confirmé inexistant** (rappel). Le **marché aux chrysanthèmes** se tient à la salle des
  fêtes « fin octobre / début novembre » **sans date ferme** (`ville-rodez.fr/quotidien/cadre-vie/marches-foires/`) :
  ne pas le saisir tant qu'aucune date n'est publiée. Aucun cirque de passage, aucun feu d'artifice, aucune animation
  Nouvel An dans la fenêtre.
- **Anomalie non tranchée** : le flyer MJC de la Toussaint place la « découverte du flamenco » au **20/10**, la base
  l'a au **23/10**. L'extraction du PDF peut désaligner les étiquettes de date des encadrés : à vérifier par téléphone
  (05 65 67 01 13) ou sur `mjcrodez.mapado.com`.
- **À rechercher explicitement à la prochaine veille** : programme détaillé de **Noël à Rodez** (l'entrée actuelle
  repose sur l'AMIC et porte `a-confirmer`) ; **patinoires** (place de la Cité et Athyrium d'Onet) ; **Téléthon de Rodez
  et de l'agglo** (seul Druelle-Balsac est annoncé) ; **Halloween au Haras de Rodez** (annoncé comme récurrent mais sans
  date 2026 — revérifier vers le 20/10) ; **stages de Noël** de la MJC de Rodez, de la MJC d'Onet (inscriptions le
  28/11), du Patio, du RAF et du Stade Rodez Athlétisme (attendus mi-novembre) ; **« Mes vacances au musée » de Noël**
  (Soulages, Fenaille, Denys-Puech : leurs agendas s'arrêtent au 16/12) ; animations de Noël des musées et de la
  médiathèque du 23/12 au 04/01 ; **ciné-goûters et avant-premières du CGR Rodez** ; **Nuits de la lecture 2027, du 20
  au 24 janvier, thème « l'enfance »** (confirmées au niveau national, aucun programme local publié — dans la fenêtre,
  à chercher en décembre) ; **heures des matchs N3F du ROC**, **calendriers de Rodez Basket (Prénationale) et du volley
  ruthénois** ; marchés de Noël d'Onet, Luc-la-Primaube, Sébazac, Le Monastère, Baraqueville et Pont-de-Salars
  (rien publié) ; **Games of Geek**, de retour à Rodez en 2027 à une date encore inconnue.

### Veille du 14/10/2026

- **La leçon de la semaine : une page officielle peut décrire un état périmé, et l'outil de réservation de
  l'organisateur fait foi contre son propre dépliant.** Trois cas, tous détectés par recoupement, aucun par la
  collecte initiale :
  - **MJC de Rodez** : le flyer PDF des vacances d'automne (`mjcrodez.fr/uploads/.../stages-et-activites-decouvertes-vacances-dautomne-2026.pdf`)
    a été **remanié après publication**. Il plaçait « découverte du flamenco » au 23/10 alors que la billetterie
    **`mjcrodez.mapado.com` donne le mardi 20/10** (deux fiches : 5-7 ans à 10 h, 8-12 ans à 14 h), et il **omet
    8 stages** pourtant ouverts à la réservation (reportage photo « La cathédrale a 500 ans », multisport 6-8,
    couture porte-monnaie, flamenco 8-12, cirque 7-11, cirque 4-6, théâtre enfants 8-12, calligraphie japonaise).
    **`mjcrodez.mapado.com` devient la source primaire de la MJC** ; le PDF n'est qu'un indice. La page d'accueil
    Mapado liste les 37 stages avec date, heure et âge (parsing de `__NEXT_DATA__`), mais **pas les tarifs**
    (12 € + adhésion, lu sur la fiche de chaque stage).
  - **`rugbyamateur.fr` a perdu son statut de référence.** Son calendrier de club affichait le 18/10 **deux matchs
    à domicile incompatibles** (Rodez - Decazeville ET Rodez - Albi) et **réutilisait un même identifiant de match**
    pour la Fédérale 2 masculine et la féminine. Sa fiche de match donnait « sam 17 Oct 2026 » là où **12actu
    (article du 12/10/2026) donne « dimanche 18 octobre à 15 h 15 »**, comme la Ville, l'agglo et unidivers.
    **Nous avons retenu le 18/10** : une page prouvée fausse sur une ligne n'est pas une autorité pour la ligne
    voisine. La règle du 30/09 (« faire foi à rugbyamateur.fr ») est **annulée** : utiliser en priorité la
    chronique hebdomadaire Fédérale 2 de **12actu.com**, et ne corriger une date de rugby que sur deux sources
    concordantes. Conséquence : le match **Rodez - SC Albi féminine du 18/10**, ajouté le 30/09 sur la seule foi
    de cette page, porte désormais `a-confirmer`.
  - **« Le Club » (Rodez) programme hors les murs, et les agendas attribuent ses concerts à Rodez.** « La mère Noël
    est une rockeuse » (12/12) était en base à Rodez : la page de l'organisateur (`leclubrodez.com/etn/...`) la
    situe **salle René Rieux à MILLAU**, hors zone → supprimée. Idem « Crash Test » du 16/01, qui a lieu **au
    Studio d'Onet-le-Château**, pas au Club à Rodez. **Vérifier systématiquement la commune réelle des dates du
    Club** : ses fiches s'intitulent « Le Club à Millau ! », « Le Club à Marcillac ! », « Le Club à Combelles ! ».
- **Deux doublons de fond que `merge.py` ne peut pas voir** (dates de début différentes, donc jamais comparés) :
  deux entrées « bébés nageurs » d'Aquavallon (du 19/09 et du 26/09, même créneau du samedi) affichaient l'activité
  **deux fois chaque samedi** ; et le cross des jeunes de La Primaube existait au 05/11 (article 12actu) et au 07/11
  (calendrier officiel FFA, qui tranche). **Ajouter au contrôle d'après-fusion un balayage « même lieu + même heure
  + même `days_of_week` » sur les récurrents, en plus du balayage par date.**
- **`merge.py` : deux pièges confirmés, à contrôler à chaque fusion.**
  1. `same_event()` fusionne **deux séances d'âges différents le même jour au même lieu** (flamenco 5-7 / 8-12,
     cirque 7-11 / 4-6, yoga enfant 9 h 30 / 14 h, yoga famille 11 h / 15 h 30). Sur cette veille, **23 événements
     distincts ont été avalés** et ont dû être restaurés. Écrire un contrôle de pertes : pour chaque événement
     d'entrée, vérifier qu'un survivant partage sa date **et son heure**.
  2. Une **correction passée par un fichier de fusion peut être annulée** : `merge.py` retrouve l'ancienne fiche
     par son `id` et garde « la plus complète », donc l'ancienne date. La correction du flamenco a été perdue
     ainsi. **Appliquer les corrections de date directement dans `data/events.json` après la fusion**, pas via un
     fichier d'entrée.
- **Sources nouvellement utiles**
  - **`tourisme-aveyron.com` : filtre géographique non documenté** `?ReactWay[geo]=44.53~2.82~44.17~2.32&ReactWay[currentPage]=N`
    → 1 323 fiches, 430 dans la zone, **pagination serveur fonctionnelle**. Bien supérieur à la recherche plein
    texte `ReactWay[q]` (qui ne marche plus, et dont les tirets cassent la requête : écrire `noel`, pas `marche-de-noel`).
    C'est la meilleure source pour les **petites communes** (Arvieu, Bertholène, Laissac, Salles-la-Source, Mayran,
    Goutrens, Clairvaux).
  - **`ville-rodez.fr/fiche/agenda/...` relaie la médiathèque de Rodez** alors que `mediatheque.ville-rodez.fr` est
    en 503 depuis cinq veilles : c'est par là qu'on obtient la soirée jeux de la ludothèque et les lectures partagées.
  - `liguesdefoot.fr` répond en ajoutant **`.md`** à l'URL (`/en/clubs/r/rodez-af.md`) ; `foot-direct.com/live/<id>-<slug>` ;
    `api.sofascore.com/api/v1/team/<id>/events/next/0` (dates fiables, horaires génériques) ;
    `www.athle.fr/competitions/<id>` pour les fiches FFA. `judo-jra.ffjudo.com/evenement` (pas `/agenda`).
  - `allocine.fr/salle/cinema-W1200/evenements/` (onglet Événements du CGR, en plus de `/avant-premiere/`).
  - `curl -sSL` **obligatoire** sur `pontdesalars.fr/agenda` et `moyrazes.fr/agenda` (0 octet sans `-L`), et sur
    `cpie-rouergue.com` (redirige vers `www.`).
- **Sources nouvellement bloquées ou inutiles** : `rodezaf.fr` (502), `haras-rodez.fr` (502), `occitanie.basketball`,
  `basketoccitanie.fr`, `occitanie.ffvb.org`, `api.ffbb.app` (403), `science-en-aveyron.com` (406),
  `salleslasource.fr` (refuse curl, passe en WebFetch), `la-baleine.eu` (tue la connexion en curl, passe en WebFetch),
  `aveyron.lpo.fr/agenda` (vide), `lesfrancasderodez.fr` (périmé), `musees.aveyron.fr`, `theatredes2points.fr`.
  `unidivers.fr` et `fest.fr` ne sont que des **miroirs du même flux DATAtourisme** que tourisme-aveyron : rien de
  neuf à y chercher. `centrepresseaveyron.fr/recherche` répond mais son classement ignore largement la requête.
  `rodez-tourisme.fr/agenda/noel/` affiche **toujours l'édition 2025-2026**.
- **Fiabilité des agrégateurs** : 12actu **et** tourisme-aveyron datent « Rugby Rodez - Stade Belvésois » au
  13/12/2026 alors que le **descriptif de leur propre fiche dit « le 10 janvier »** (date retenue en base). Lire le
  corps des fiches, pas seulement leur champ date. Une fiche « fibule » de Montrozier portait une **note de
  l'éditeur demandant sa suppression** → écartée.
- **Noël 2026 : absence désormais établie, pas un échec de recherche.** Les 229 fiches de `ville-rodez.fr/agenda` et
  les 324 de `rodezagglo.fr` ont été parcourues : **zéro** occurrence de « patinoire », « Père Noël », « grande
  roue », « petit train », « marché de Noël Rodez », « Téléthon ». Seul document officiel : l'AMI
  `ville-rodez.fr/uploads/2026/07/Appel-a-Manifestation-Noel-2026.pdf` (domaine public **du 05/12/2026 au
  03/01/2027**), qui fonde l'entrée actuelle avec `a-confirmer`. Aucune patinoire (place de la Cité ni Athyrium),
  aucun marché de Noël communal (Onet, Luc, Sébazac, Monastère, Olemps, Bozouls, Baraqueville, Marcillac), aucun
  Téléthon hors Druelle-Balsac, aucun cirque de passage. **Halloween au Haras de Rodez : rien à trois semaines de
  l'échéance, sur trois veilles — l'édition 2026 n'aura probablement pas lieu.**
- **Fête de la science en Aveyron : déjà passée** (début octobre, Pont-de-Salars et Saint-Affrique le 10/10). Ne pas
  la chercher en novembre. **« Games of Geek » a été renommé Anim'Aveyron et déplacé à Druelle-Balsac**, édition
  2026 en septembre : la piste « retour en 2027 » est caduque.
- **Question de zone à arbitrer avec le propriétaire du projet** : Arvieu (19,1 km) et Goutrens (19,2 km) sont dans
  le rayon **à vol d'oiseau**, comme le prescrit la procédure, mais à **≈ 30 km par la route**. 9 activités en
  dépendent. Si le critère doit devenir routier, le préciser dans `docs/SCHEMA.md` et dans `scripts/validate.py`.
- **À rechercher explicitement à la prochaine veille** : programme de **Noël à Rodez** (l'entrée repose toujours sur
  l'AMI) ; **patinoires** ; **Téléthon** de Rodez et de l'agglo ; **marchés de Noël** communaux ; **stages de Noël**
  de la MJC de Rodez (aucune offre JPS2 sur Mapado au 14/10), de la MJC d'Onet (inscriptions le 28/11), du Patio, du
  RAF et du Stade Rodez Athlétisme ; **« Mes vacances au musée » de Noël** (les agendas des trois musées s'arrêtent
  au 16/12) ; animations de Noël de la médiathèque et des musées du 23/12 au 04/01 ; **ciné-goûters du CGR** ;
  **Nuits de la lecture 2027 (20-24 janvier, thème « l'enfance »)**, à chercher en décembre ; **heures des 4 matchs
  N3F du ROC** (`api-dofa.ffhandball.fr` en 502 depuis 3 veilles) ; **calendriers de Rodez Basket** (Prénationale,
  site figé en août 2025) **et du volley MJC Rodez** ; les 5 matchs à domicile de **Rodez AF 2 en National 2**
  (dates et horaires connus, **stade non confirmé** — le Domaine de Vabre est le centre de formation) ; programmes
  de vacances de **Terra Memoria** (05 65 44 69 27) et de **Montrozier** (05 65 70 71 45). **Janvier restera creux
  jusqu'à une veille de décembre** : les programmes MJC, centres sociaux, médiathèques et musées de janvier ne sont
  pas publiés au 14/10.

### Veille du 21/10/2026

- **La leçon de la semaine : `merge.py` avale aussi les événements de la base que personne ne ré-émet.**
  Le contrôle de pertes écrit le 14/10 comparait les *fichiers d'agents* au résultat ; il ne voyait donc pas
  disparaître une fiche déjà en base qu'aucun agent n'avait reprise. Huit événements ont été perdus ainsi
  (les 3 créneaux de yoga du Studio Sport Santé des 21 et 28/10, l'initiation couture d'Aubéria du 23/10,
  la boule de Noël en art floral du 05/12), absorbés par un événement voisin du même lieu au titre proche.
  **Faire les deux contrôles à chaque fusion** : `python3 scripts/qa.py --before <events.json d'avant>
  --inputs <fichiers d'agents>`. Le premier bloc attrape les créneaux réduits, le second les titres disparus.
  Toute disparition qui n'est pas une décision explicite est une perte à rétablir.
- **`merge.py` ne remplace jamais un champ déjà rempli** (`fuse()` ne complète que le vide) : **toutes les
  corrections des agents sur un champ non vide sont silencieusement perdues**. Cette semaine, **209 valeurs**
  (âges du dessin et du BMX de la MJC, horaires, tarifs, `end_time`) ont dû être réappliquées après fusion en
  relisant les fichiers d'agents et en comparant champ par champ. **Prévoir systématiquement cette passe de
  réconciliation**, et traiter les désaccords entre agents à part : quand deux agents proposent deux valeurs
  différentes pour le même champ, garder celle de la base et trancher à la main (13 cas, dont 11 de simple
  formulation).
- **Une fiche corrompue survit aux veilles.** L'identifiant `atelier-fabrique-ton-carnet-secret_2026-10-22_rodez`
  portait depuis le 14/10 le **titre, le lieu, l'heure et le tarif de l'atelier « réalise ton soda naturel »**
  d'Aubéria, avec la *description* du carnet secret : une fusion de deux ateliers distincts. Les deux ont été
  séparés. **Contrôler la cohérence entre le slug de l'`id` et le `title`** : un écart signale une fusion ratée
  d'une veille précédente, invisible pour `validate.py`.
- **Halloween au Haras de Rodez a bien eu lieu — l'absence d'arrêté n'est pas une preuve d'absence.**
  Un agent avait conclu à l'annulation en constatant qu'aucun arrêté d'occupation du domaine public ne la
  mentionnait. Le raisonnement est faux : **la Ville, organisatrice, ne s'auto-délivre pas d'autorisation.**
  Le programme officiel existe : `ville-rodez.fr/uploads/2026/10/2026_PROG-halloween.pdf` (31/10, 16 h-21 h,
  escape game, maquillage, lectures, chemin de la peur de 18 h 30 à 21 h). Kefesh, seul à l'annoncer, avait
  raison. Indice utile : sur Kefesh, un slug **sans `copie-de-`** désigne une fiche créée pour l'édition en
  cours, pas un report de l'an dernier.
- **Sources nouvellement utiles**
  - **`ville-rodez.fr/sports-loisirs/culture-loisirs/animations/`** : la page qui porte les **PDF de programmes
    municipaux** (`uploads/2026/10/2026_PROG-halloween.pdf`). **C'est par là qu'arrivera le programme de Noël**,
    pas par l'agenda Diffusio. À ouvrir à chaque veille.
  - **`ville-rodez.fr/quotidien/vie-municipale/actes-reglementaires/?id1%5BcurrentPage%5D=N`** (8 pages, curl) :
    **les noms de fichiers des arrêtés datent les manifestations avant leur publication dans l'agenda.** Ils ont
    livré le marché aux chrysanthèmes (29/10 → 01/11), le manège forain de la place du Bourg (02/10 → 03/01) et
    la bourse aux jouets de l'APE Jeanne d'Arc. Le PDF lui-même ne contient qu'un accusé de réception
    préfectoral : **le nom du fichier est la seule information exploitable**, mais il porte l'objet et les dates.
    La patinoire y apparaîtra en novembre (elle avait son arrêté en 2024).
  - **`https://www.ville-rodez.fr` (page d'accueil nue, en curl)** : porte des blocs d'actualité **absents de
    l'agenda paginé** — c'est là qu'étaient les dates du marché de Noël.
  - **`billetterie.rodezaveyronfootball.com`** : rendu côté serveur, les 3 prochains matchs avec journée, jour,
    date, heure et stade. **Source primaire du RAF** (`rodezaf.fr` toujours 502 ; le calendrier de
    `rodezaveyronfootball.com` est un widget Opta vide, son flux en 403). En revanche
    `rodezaveyronfootball.com/classement-calendrier-2026-2027-division-3-feminine/` sert le **calendrier D3F
    complet en HTML statique**.
  - **`ffvbbeach.org/ffvbapp/resu/`** : tout le volley de la Ligue Occitanie, **code ligue `LILR`** (pas `LIOC`).
    `vbspo_calendrier_export.php?saison=2026/2027&codent=LILR&poule=<CODE>&calend=COMPLET` renvoie un **CSV**
    (cp1252, `;`, colonnes Date/Heure/EQA/EQB/Salle). Poules du MJC Rodez volley : `M1O`, `F1O`, `COM`, `FCA`.
    A débloqué 9 matchs — et corrigé le niveau du club : **Régionale 1 masculine et féminine**, pas Prénationale.
  - **`mjcrodez.mapado.com/event/<id>-<slug>`** : le slug nu est en 404, il faut le préfixe `/event/`. La fiche
    expose `entities.eventDates` (dates réelles) et `ticketPrices` (en centimes), que la page d'accueil n'a pas.
    **`eventDates` fait foi contre le texte de la fiche** (celle de « Minecraft le Grand Studio » annonce le
    22/10 alors que ses dates sont les 28-29). `mjcrodez.fr/agenda/` complète Mapado avec les rendez-vous
    **gratuits des clubs** (Roll'Dez, échecs, impro), que la billetterie ne porte pas.
  - **Les agendas propres des trois musées**, tous en curl : `musee-soulages-rodez.fr/fr/agenda/` (**`-L`
    obligatoire**, fiches `/fr/fiche/agenda/<slug>` sans slash final), `musee-fenaille.rodezagglo.fr/agenda/`
    (fiches `/fiche/agenda/<slug>/` **avec** slash) et `musee-denys-puech.rodezagglo.fr/agenda/` (fiches
    `/agenda/fiche/<slug>`, **ordre inversé**). Ils donnent heure de début **et** de fin, âge et tarif détaillé.
    Les domaines `musee-fenaille-rodez.fr` et `musee-denys-puech-rodez.fr` **n'existent pas**.
  - **`centrepresseaveyron.fr/aveyron/<commune>/`** : pages de rubrique par commune (≈ 20 derniers articles),
    lisibles en curl — **la** source des programmes de vacances des médiathèques et des réunions Téléthon
    (`?page=N` est ignoré). Et `recherche?q=<mots+séparés+par+des+plus>` **marche** avec `curl -sSL` (le `-L`
    est obligatoire) quand on empile des mots-clés précis ; le corps de l'article est entier dans `<article>`,
    ou dans le champ `articleBody` du JSON-LD, avant le mur d'abonnement.
  - **`12actu.com/recherche?q=<mots>`** : la seule recherche de presse locale réellement fiable — idéale pour
    **prouver une absence** (« patinoire » ne renvoie que des articles de 2024-2025). ⚠️ sur son agenda, le
    paramètre `?categorie=` n'est pas appliqué sur les premières pages, et le JSON-LD est un **`ItemList`** :
    il faut parcourir `itemListElement[].item`, un `finditer` sur `"@type":"Event"` ne trouve rien.
  - `bases.athle.fr/...` **redirige** (« Object moved ») vers `www.athle.fr/bases/liste.aspx?...` : utiliser
    `curl -sSL`. Et `frmsaison=2026|2027` ne renvoie que l'**année civile 2026** : pour janvier-février 2027,
    interroger `frmsaison=2027|2028`. Les fiches `athle.fr/competitions/<id>` donnent les catégories admises,
    ce qui permet d'écarter les courses sans épreuve enfants.
  - `rochandball.com/billetterie-roc-aveyron-handball-4.html` : **gratuit pour les moins de 16 ans**, portes à
    18 h, Amphithéâtre. `liguesdefoot.fr/en/clubs/r/rodez-af.md` (avec le `www.` et `-L`) donne tous les
    championnats d'un club avec horaires ISO (`00:00` = horaire non fixé) et la liste de ses terrains.
    `api.sofascore.com/api/v1/search/all?q=<nom>` pour les ids : **Rodez AF = 6925** (4120 est l'id fotmob),
    Onet-le-Château = 455821, Rodez 2 = 398297.
  - `tourisme-aveyron.com` : le filtre géo `?ReactWay[geo]=44.53~2.82~44.17~2.32&ReactWay[currentPage]=N` donne
    **1 289 occurrences sur 62 pages, soit 537 fiches uniques dont 460 dans la zone**. La liste expose
    `data-lat`/`data-lng` : géocodage gratuit. La recherche `ReactWay[q]` **remarche** (sans tirets).
    ⚠️ sa pagination s'arrête vers le 15/01/2027 : les fiches de fin janvier et de février n'y sont pas encore.
- **Sources nouvellement bloquées ou à abandonner**
  - **`fest.fr` : toutes ses dates sont décalées d'un jour** (Monas'trail, soirée fluo UpZone et Bec Verseur
    annoncés le 30/10 au lieu du 31 ; salon du mariage et pickleball le 23 au lieu du 24). S'ajoute au mélange
    de descriptifs déjà connu → **source à abandonner**.
  - **`oazis.app` : 5e représentation fantôme** (une séance de flamenco à la MJC le 23/10 que la billetterie ne
    connaît pas). Au passage, cela **tranche l'anomalie laissée ouverte le 07/10** : le flamenco était bien le
    20/10, il n'y a jamais eu de séance le 23. À ne plus utiliser qu'en dernier recours, toujours recoupé.
  - `mediatheque.ville-rodez.fr` : ce n'est plus un 503 mais une **connexion réinitialisée**, 7e veille sans
    accès. `conservatoire-aveyron.fr` : **502** (nouveau). `billetterie.rodezagglo.fr` : refusé par le proxy.
    `rugbyamateur.fr` : **403 en curl mais accessible en WebFetch** (et il n'affiche plus le doublon du 18/10).
    `onet-le-chateau.fr` : **418** en curl, WebFetch continue de marcher.
    `medias.hit.enaveyron.fr/fiches/.../documents/*.pdf` : 403, les PDF de programme des fiches Tourinsoft ne
    sont plus téléchargeables. `scorenco.com`, `api-dofa.ffhandball.fr` (4e veille), `rodez-rugby.com`,
    `upzone360.fr`, `occitanie.ffbb.com`, `aveyron.basketball`, `rodezbasket.fr`, `mjcrodezvolley.fr`,
    `leptitclub12.fr` : morts ou injoignables. `ladepeche.fr` est **inutilisable dans son ensemble**
    (sa recherche comme ses pages de commune, qui servent des articles d'autres départements).
  - **`terramemoria.fr` : un avis en ligne dit « closed indefinitely »** et « Terra Memoria » ne renvoie plus
    aucune fiche d'agenda. **Vérifier par téléphone au 05 65 44 69 27** avant de le rechercher encore.
- **Noël 2026 : le robinet s'est ouvert, mais à moitié.** Le **marché de Noël de Rodez se tient du 11 au 31
  décembre** (et non du 05/12 au 03/01 comme le laissait croire l'appel à manifestation d'intérêt de juillet) :
  **la Ville reprend l'organisation en régie**, 20 chalets « 100 % aveyronnais », ouverture dim.-jeu. 10 h-19 h
  et ven.-sam. 10 h-21 h. **L'emplacement n'est pas arrêté** (place Foch ou carrefour Saint-Étienne, mais ni
  place de la Cité, ni place du Bourg, ni place Emma-Calvé). Sources : page d'accueil de `ville-rodez.fr` et
  Centre Presse du 15/10. Le « village féérique » est commandé (marché public attribué 99 995,50 € HT, décision
  `uploads/2026/09/DEC2026-271-26007-festivites-de-noel.pdf`) mais **patinoire, grande roue, village du Père
  Noël et petit train ne sont toujours pas datés** ; l'adjointe les annonce « prochainement ».
  ⚠️ Rappel : une recherche web ressort « 6 déc. - 4 janv., 27 chalets » = **édition 2025**.
  `rodez-tourisme.fr/agenda/noel/` affiche encore 2025 pour la **4e veille**.
- **RAF - Reims a été déplacé au lundi 7 décembre à 20 h 45** (au lieu du 04/12 à 20 h). Confirmé
  indépendamment par trois agents et six sources (billetterie officielle, footmercato, fotmob à 19 h 45 UTC,
  liguesdefoot, lesnouvellesdufoot). **Kefesh annonçait 04/12, comme notre base** : la règle « ignorer les dates
  de match de Kefesh » reste bonne, mais elle ne suffit pas — **notre propre base peut être périmée**. Recouper
  les matchs à domicile avec la billetterie du club à chaque veille.
- **Questions de zone à arbitrer avec le propriétaire du projet** (le critère de la procédure est le vol
  d'oiseau) : **Salmiech est à 18,6 km**, donc dans le rayon, alors que la procédure la liste en hors zone —
  3 ateliers enfants y ont été écartés par respect de la consigne. **Arvieu (19,1 km) et Goutrens (19,2 km)**
  sont dans le rayon mais à ≈ 30 km par la route, et 9 activités en dépendent. **Castanet ressort à 20,2 km**
  (écartée). Si le critère doit devenir routier, le préciser dans `docs/SCHEMA.md` et dans `scripts/validate.py`.
  Une coordonnée visiblement fausse chez tourisme-aveyron : **Viala-du-Tarn** donné à 18,9 km alors que la
  commune est près de Millau.
- **Trous enfin comblés cette semaine** : volley ruthénois (9 matchs), Halloween au Haras, cirque de passage
  (**Cirque Olympia à Sébazac-Concourès**, 30/10, 31/10 et 01/11 — le premier depuis six veilles), Téléthon hors
  Druelle-Balsac (Le Vibal, Saint-Christophe-Vallon, Muret-le-Château, Marcillac, Olemps), marché aux
  chrysanthèmes, animations de vacances d'Aquavallon, médiathèque d'Olemps, cyber-base de Marcillac.
- **À rechercher explicitement à la prochaine veille** : le **programme des fêtes de fin d'année de Rodez**
  (patinoire, grande roue, village du Père Noël, petit train, forêt lumineuse — surveiller
  `ville-rodez.fr/sports-loisirs/culture-loisirs/animations/` et les actes réglementaires de novembre) ;
  **l'emplacement du marché de Noël** ; **Téléthon de Rodez et d'Onet** (toujours rien) ; **patinoire de
  l'Athyrium** ; **stages de Noël** de la MJC de Rodez (guetter des offres « JPS2 » sur Mapado), de la MJC
  d'Onet (inscriptions le 28/11), du Patio, du RAF et du Stade Rodez Athlétisme ; **« Mes vacances au musée »
  de Noël** (les trois agendas s'arrêtent entre le 27/11 et le 16/12) ; **programme vacances de Noël 11-17 ans
  de la Ville** (chercher un `2026_VACnoel*-Web.jpg` dans `uploads/2026/11/` et `/12/`) ; **programmes mensuels
  de novembre et décembre des maisons de quartier** ; **ciné-goûters du CGR** (rien pour la 3e veille) ;
  **Nuits de la lecture du 20 au 24 janvier 2027, thème « l'enfance »** (confirmées au national, aucun programme
  local) ; **heures des 4 matchs N3F du ROC** (5e échec) et **calendrier de Rodez Basket** en Prénationale
  (3e échec — les deux demandent probablement un appel au club) ; **jour et stade des 4 matchs à domicile de
  Rodez AF 2** en National 2 (liguesdefoot et Sofascore se contredisent d'un jour) ; **programmes de janvier**
  des MJC, centres sociaux, médiathèques et musées, qui laissent le mois à 37 entrées.
- **Anomalies restées ouvertes** : l'horaire de « Passages » au Théâtre des 2 Points (08/01/2027) est donné à
  **20 h** par le producteur et l'agglo, à **20 h 30** par la MJC exploitante et par Kefesh — deux sources de
  chaque côté, entrée laissée à 20 h avec `a-confirmer`. L'expo « Chambres adolescentes » aux Capucines est
  donnée au **22/11** par l'agenda et au **26/11** par Centre Presse. « NovAdo fait court » est en base au
  **15/11 à 17 h** alors que la billetterie ne connaît qu'un « NovAdo fait son cinéma » le **06/03/2027**.
  L'horaire de « L'après-midi T'Choupi » (24/10) a été aligné sur Kefesh (15 h 30) faute d'accès à
  `maisondulivre.com`, en 403 depuis le début.

### Veille du 28/10/2026

- **La leçon de la semaine : le contrôle de pertes doit se faire par `id`, pas par titre.** Le bloc
  « titres disparus » de `qa.py` compare les titres à 0,85 de similarité : il ne voit donc **pas** une fiche
  écrasée par une voisine au titre proche. Cinq pertes lui ont échappé et n'ont été trouvées qu'en comparant
  les **ensembles d'`id`** avant/après (les séances BMX 4-6 ans et dès 11 ans de la MJC des 28 et 30/10,
  la 2e séance de crochet du 28/10). **`qa.py` porte désormais trois contrôles nouveaux**, à lire à chaque
  fusion : `== IDS DISPARUS ==` (chaque ligne doit être une suppression voulue), `== CHANGEMENTS D'ID ==`
  (un id refait fait perdre les favoris de l'utilisateur : rendre l'ancien) et
  `== COMMUNE DE L'ID ≠ CHAMP city ==`.
- **Deux fiches corrompues, toutes deux par le préfixe de lieu sur 12 caractères.** `same_event()` considère
  deux lieux identiques si `norm(venue)[:12]` concorde : or **« Salle des fêtes de Bertholène » et « Salle des
  fêtes de Pont-de-Salars » donnent tous deux `salle-des-fe`**. Le 13/12, l'id du marché de Noël de Bertholène
  s'est retrouvé avec le titre, le lieu et la source de celui de Pont-de-Salars (et Pont-de-Salars avait
  disparu) ; le 31/10, l'id de la soirée Halloween de l'APE de Clairvaux portait le contenu de celle de Rodez.
  **Le contrôle `COMMUNE DE L'ID ≠ CHAMP city` attrape ce cas en une ligne** — c'est le plus rentable des trois.
  Un troisième cas, sans écart de commune : l'id de l'« Atelier Archi » de la galerie Sainte-Catherine portait
  le titre de l'expo « Pierres en mouvement » (même lieu, mêmes dates), et l'expo avait disparu.
- **Noël à Rodez : la percée est venue des actes réglementaires, pas de l'agenda.** La décision du Maire
  `ville-rodez.fr/uploads/2026/10/DEC2026-303-contrat-de-cession-spectacles-Noel-2026.pdf` (23/10) **date les
  5 déambulations de la Cie Les Enjoliveurs** : 12/12 « Noël enchanté », 13/12 « Le manège aux écureuils »,
  19/12 « Ça Cartoon !!! », 20/12 « Pachy, la danse des éléphants », 22/12 « Happy Noël » (gratuit, 2 × 50 min
  ou parade d'1 h 30, horaires « à déterminer sur la feuille de route »). L'arrêté
  `AG-2026-0847-ODP-C-S_Reglement-marche-de-noel_du-11-12-au-31-12.pdf` **confirme le marché du 11 au 31/12**.
  **Contrairement aux arrêtés AG/VP dont seul le nom de fichier est exploitable, les décisions du Maire
  `DEC2026-xxx` ont un contenu lisible intégral** (contrats de cession : dates, lieux, montants). À ouvrir en
  priorité à chaque veille. ⚠️ **L'URL des actes a déménagé** : `ville-rodez.fr/ville/mairie/conseil-municipal/
  actes-reglementaires/` (l'ancienne `/quotidien/vie-municipale/...` renvoie 0 octet sans `-L`), et sa
  pagination `?id1[currentPage]=N` **ne fait rien** : les 552 PDF tiennent sur une page unique.
- **Restent introuvables au 28/10, après deux agents et une recherche de presse exhaustive** : patinoire
  (place de la Cité et Athyrium d'Onet), grande roue, village du Père Noël, petit train, forêt lumineuse, et
  **l'emplacement du marché de Noël** (la délibération tarifaire DEL2026122 liste Bourg/Cité/Foch/Armes sans
  trancher). Aucun `2026_PROG-noel*.pdf/.jpg` dans `uploads/2026/{10,11,12}` (8 noms testés). Aucun arrêté
  patinoire parmi les 552. `rodez-tourisme.fr/agenda/noel/` affiche **encore 2025-2026, 5e veille**.
  ⚠️ Le piège « 6 déc. - 4 janv., 27 chalets, grande roue, place d'Armes » est identifié : c'est **l'article
  12actu du 4 décembre 2025**.
- **Téléthon de Rodez et d'Onet : rien, 4e veille** (agenda d'Onet dépouillé page par page, rubriques Centre
  Presse de Rodez et d'Onet, recherches 12actu). Trouvés ailleurs : pompiers de Baraqueville 05/12, randonnée
  d'Arques/Le Vibal 05/12 13 h 30.
- **Stages de Noël : absence établie, pas un échec de recherche.** `mjcrodez.mapado.com` n'a **aucune offre
  JPS2** (seulement des reliquats JPS1 de la Toussaint) ; `rodezaveyronfootball.com/stages/` n'annonce que
  « vos stages de juillet » ; l'agenda du Patio saute du 24/12 au 13/01 ; aucun `2026_VACnoel*.jpg` dans
  `uploads/2026/11|12`. **Les stages de Noël de la MJC de Rodez, de la MJC d'Onet (inscriptions le 28/11), du
  Patio, du RAF et du Stade Rodez Athlétisme sont donc à rechercher à la veille de mi-novembre.**
- **Sources nouvellement utiles**
  - **`billetterie.rodezaveyronfootball.com`** reste la source primaire du RAF, et
    **`rochandball.com/billetterie-roc-aveyron-handball-4.html` porte tout le calendrier N1M à domicile en
    clair dans son JavaScript** (`const MATCHES = [...]` : journée, date, heure). C'est ainsi qu'on a trouvé
    **ROC - USAM Nîmes reporté du week-end des 10-11/10 au samedi 31/10 à 19 h**.
  - **`foot-direct.com/equipe/rodez-aveyron-football-ii`** donne enfin le stade de la réserve du RAF :
    **« Stade de Vabre – terrain n° 2 », à Onet-le-Château**. Les **5 réceptions de Rodez AF 2 en National 2**
    (01/11, 22/11, 13/12, 24/01, 14/02), absentes de la base depuis le début, sont saisies.
    `livefoot.fr/direct/national-3-groupe-a-france/match-<slug>` donne le jour et l'heure en toutes lettres.
  - **Les poules `COM` et `FCA` du CSV FFVB sont les championnats JEUNES M21/M18** du MJC Rodez volley, jamais
    exploitées jusqu'ici : 6 matchs à entrée libre au gymnase Frugère. Le paramètre `poule=` est d'ailleurs
    **ignoré** par l'export, qui rend toute la ligue `LILR` — un seul appel suffit.
  - `athle.fr/bases/liste.aspx?frmpostback=true&frmbase=calendrier&frmmode=1&frmespace=0&frmsaisonffa=2027&frmdate1=2026-09-01&frmdate2=2027-08-31&frmdepartement=012`
    rend **toute la saison FFA en un seul appel** (remplace les deux requêtes `frmsaison`).
  - **`mjcrodez.fr` expose son agenda complet** par `POST /wordpress/wp-admin/admin-ajax.php` avec
    `action=loadmore_agenda`, et **une page par spectacle avec âge, durée et tarif** sous
    `mjcrodez.fr/<discipline>/agenda/<slug>/` (`/theatre-des-2-points/agenda/passages/`,
    `/marionnette/agenda/faubourg/`), listées par `mjcrodez.fr/agenda-sitemap.xml`.
  - **`centrepresseaveyron.fr/aveyron/<commune>/page-N` fonctionne** (alors que `?page=N` est ignoré) ;
    `/aveyron/rodez/sorties/` et `/culture-et-loisirs/` existent aussi.
  - **Les identifiants des fiches tourisme-aveyron (`…-FMA-AAAAMMJJhhmmss…`) datent leur création** : filtrer
    sur `>= <date de la veille précédente>` isole en une passe les fiches nouvelles de la semaine. **C'est la
    méthode la plus rentable pour une veille hebdomadaire.** Sa pagination géo va désormais **jusqu'à fin
    avril 2027** (le blocage au 15/01 est levé).
  - **Les images statiques d'`onet-le-chateau.fr` passent en curl** alors que ses pages sont en 403/418 : le
    programme du Patio (`/app/uploads/2026/09/programme-du-Patio-sept-dec-2026_Page_N.jpg`, pages 3 à 7) a
    confirmé jour par jour les 21 fiches d'Onet. **`pdftoppm -png` + outil Read rend un PDF que
    `pdftotext` ne lit qu'au tiers** (PDF de programme des maisons de quartier).
  - `musee-denys-puech.rodezagglo.fr/expositions/exposition-temporaire/` donne les dates des expos
    temporaires, absentes de son agenda (nouvelle expo gratuite « Dropy », 20/11 → 30/05).
- **Sources nouvellement bloquées ou fausses** : **`liguesdefoot.fr` est passé en Cloudflare 403** (le `.md` ne
  suffit plus) et **`api.sofascore.com` renvoie 403** — deux sources clefs du foot perdues la même semaine ;
  `fff.fr` et `api-dofa.fff.fr` 403 ; `mjc-onet*.fr` n'a **plus de DNS** (mort, plus seulement 502) ;
  `conservatoire-aveyron.fr` 502 (2e veille) ; `levezou-aveyron.com` certificat auto-signé en curl et 503 en
  WebFetch ; `12actu.com/recherche` est **rendu 100 % JS, inutilisable en curl** (contredit le REX du 21/10) et
  son agenda paginé s'arrête vers le 16/11 ; `api-dofa.ffhandball.fr` 502 (5e veille) ;
  `mediatheque.ville-rodez.fr` **8e veille sans accès**. **`trainerday.com` donne des dates fausses** : il
  plaçait la Ronde de Noël au 7 ou au 8/12 alors que le site de l'organisateur
  (`toutlemondecourt.wixsite.com/rondedenoelrodez`) écrit « rendez-vous dimanche 6 décembre 2026 ».
- **Anomalies tranchées cette semaine** : *Passages* au Théâtre des 2 Points (08/01) est bien à **20 h 30** (la
  MJC exploitante, sa billetterie et sa fiche agglo contre les deux fiches « Passages » de l'agenda) ;
  *Chambres adolescentes* finit le **22/11** (le 26/11 de Centre Presse est le début de l'expo suivante,
  « Les Invisibles ») ; *NovAdo fait court* est bien le **15/11 à 17 h**, « NovAdo fait son cinéma » étant un
  autre rendez-vous des **6-7 mars 2027** ; *Je suis trop vert* (05/12) est à **20 h 30** et non 17 h (la fiche
  Tourinsoft annonçait « mardi » pour un samedi) ; *On court à la Baleine* se joue du **03 au 05/12** (le 03
  en séances scolaires). **« Croire aux fauves » (24/11) est annulé** (mention « SPECTACLE ANNULÉ » sur
  mjcrodez.fr) : supprimé.
- **Croisement Kefesh (28/10)** : 148 événements à venir, 69 déjà présents, 79 manquants dont 56 dans la
  fenêtre. **2 ajoutés** (bungee d'Halloween enfants à l'ASPTT le 28/10, atelier attrape-soleil en duo
  parent-enfant au Monastère le 30/10 — aucune page officielle, `source` = fiche Kefesh + `a-confirmer`) ;
  ~50 écartés comme adultes (conférences, dégustations Trinquons, soirées DJ, comedy, drag show) ou hors cible
  (goûter allaitement : nourrissons ; projections « Chante-Coucou » du musée Fenaille : **la fiche officielle
  ne donne ni âge ni mention jeune public**). Les 2 seuls vrais manques signalés par Kefesh (ROC - Pays d'Aix
  du 13/02 et RAF - Guingamp du 12/02) ont été trouvés en parallèle par la collecte sportive.
  **Relire les faux positifs de `same()` reste payant** : il a masqué l'atelier attrape-soleil du Monastère
  derrière un atelier d'Onet, et il donne encore RAF - Reims au 04/12 alors que le match est au **07/12**.
- **Zone** : **Salmiech (18,6-18,9 km) est désormais incluse** (5 entrées en dépendent), conformément à la
  règle du vol d'oiseau. Écartés avec leurs distances mesurées : Pruines 20,4-20,7 km (dont un spectacle jeune
  public « Baoum ! » le 14/11), Castanet 20,2 km, Escandolières/Goutrens 22,9 km pour la soirée karaoké de
  l'APE, Ségur 21,8 km. **Arvieu (19,1 km) et Goutrens (19,2 km) restent dans le rayon à vol d'oiseau mais à
  ≈ 30 km par la route** : question toujours à arbitrer avec le propriétaire du projet. Le Laissac Biathlon
  Trail se court en réalité **à Séverac-l'Église (≈ 22,8 km)** ; l'entrée est conservée avec les coordonnées du
  bourg de Laissac (19,8 km), comme dans la base.
- **À rechercher explicitement à la prochaine veille** : **patinoire, grande roue, village du Père Noël, petit
  train, forêt lumineuse et emplacement du marché de Noël** (surveiller les **décisions du Maire
  `DEC2026-xxx`** et `ville-rodez.fr/sports-loisirs/culture-loisirs/animations/`, et les **horaires** des
  5 déambulations des Enjoliveurs) ; **Téléthon de Rodez et d'Onet** ; **stages de Noël** (MJC de Rodez sur
  Mapado, MJC d'Onet le 28/11, Patio, RAF, Stade Rodez Athlétisme) ; **« Mes vacances au musée » de Noël** et
  les animations du 23/12 au 04/01 (les trois agendas de musée s'arrêtent entre le 27/11 et le 16/12) ;
  **ciné-goûters du CGR** (4e veille sans rien) ; **Nuits de la lecture du 20 au 24 janvier 2027** (aucun
  programme local) ; **heures des 4 matchs N3F du ROC** (6e échec) et **calendrier de Rodez Basket** en
  Pré-Nationale masculine (4e échec — les deux demandent probablement un appel au club) ; les **4 réceptions
  de la Pré-Nationale du ROC** (07-08/11, 28-29/11, 12-13/12, 30-31/01), sans salle ni horaire publiés ;
  **programmes de janvier** des MJC, centres sociaux, médiathèques et musées (la série « Activités
  parents-enfants » du centre social de Rodez paraît **mois par mois vers le 21** : celle de décembre est
  attendue vers le 21/11) ; **carnavals 2027** (seul celui de Luc-la-Primaube est publié, le 13/03, hors
  fenêtre) ; **Terra Memoria**, à vérifier par téléphone au 05 65 44 69 27 (un avis en ligne dit « closed
  indefinitely », aucune fiche d'agenda ni article depuis septembre 2025).
- **Déjà repérés pour la fenêtre suivante (après le 17/02)** : rugby Rodez - Canton d'Alban et foot D3F
  Rodez - Troyes le 21/02, « Juste Iréna » au Théâtre des 2 Points le 23/02, « Numéro Deux » à La Baleine le
  24/02, handball N3F Muret et N1M Montpellier le 27/02, volley F1O/M1O le 27/02, quine de l'APE
  d'Escandolières à Goutrens le 28/02, **visite dansée de l'expo Nevelson le 18/02/2027** (3 représentations,
  un jour après la fenêtre de cette semaine).

### Veille du 04/11/2026

- **La leçon de la semaine : une erreur dans le briefing de l'orchestrateur se propage dans les conclusions
  des agents.** J'avais écrit que les vacances d'hiver de la zone C allaient du 20/02 au 08/03/2027 ; elles
  vont du **samedi 6 au lundi 22 février 2027** (vérifié : franceinfo, académie de Toulouse, arrêté JO du
  22/10/2025). Conséquences : la quinzaine entière tombait dans la fenêtre sans que personne ne la cherche,
  et un agent a signalé comme « incohérent » le stage « comédie musicale Encanto » de la MJC de Luc
  (08-12/02) au motif qu'il tombait « en période scolaire ». Un seul agent a relevé l'erreur, en citant ses
  sources. **À faire désormais au début de chaque veille : vérifier le calendrier scolaire de la zone C et
  l'inscrire dans le briefing.** Les cinq agents encore en cours ont été relancés avec la correction, ce qui
  a produit 3 entrées de février de plus et surtout des absences *établies* au lieu d'un angle mort.
- **`merge.py` a silencieusement annulé toute la passe de re-vérification.** 82 fiches rouvertes ce jour (dont
  77 des 85 de l'agent de re-vérification) ont gardé un `source_checked` périmé, parce que `fuse()` ne
  remplit que le vide et que la version de la base était « la plus complète ». Sans correction, la veille
  suivante aurait redemandé les 87 mêmes vérifications. **C'est désormais l'étape 7 de la procédure.**
- **Les deux motifs de corruption du 28/10 se sont reproduits à l'identique**, plus un troisième :
  1. `atelier-archi-maquettes-et-kapla-a-sainte-catherine_2026-10-14` a repris le titre et l'heure de
     l'expo « Pierres en mouvement » (même galerie, mêmes dates), dont l'`id` a disparu — **exactement le
     cas décrit le 28/10**.
  2. `marche-de-noel-de-bertholene_2026-12-13` a repris le titre, le lieu **et la commune** du marché de
     Noël de Pont-de-Salars (préfixe `salle-des-fe` sur 12 caractères), dont l'`id` a disparu.
  3. **12 fiches de la base qu'aucun agent ne ré-émettait ont été purement avalées** (5 matchs de volley au
     gymnase Frugère, l'escape game du musée Soulages, Extrem'Ados théâtre, l'accueil Mix'Art du vendredi,
     l'art floral du 05/12, la 2e séance de « Tourne fête », l'expo Pierres en mouvement, le marché de Noël
     de Pont-de-Salars). Le bloc `== IDS DISPARUS ==` de `qa.py --before` les a toutes trouvées : **c'est le
     contrôle le plus rentable, à lire ligne par ligne, chaque ligne devant être une suppression voulue.**
  Toutes rétablies depuis `avant.json`, avec leur `source_checked` d'origine.
- **`merge.py` ne peut pas garder deux séances d'un même spectacle le même jour au même lieu**, même quand
  les titres portent l'heure : `same_event()` renvoie vrai dès que le ratio des titres atteint 0,6, et
  « … (séance de 15 h) » et « … (séance de 19 h) » sont à 0,98. Quatre séances ont dû être réinsérées à la
  main après fusion (Vive la Magie 19 h, « Fabrique ta ville » 15 h, conte « Le Voyage de Cora » 11 h, et la
  lecture dans la cabane de Lucie Félix, qui avait en plus légué son horaire de 14 h 30 à l'exposition
  d'un mois qu'elle côtoyait). **Ne jamais compter sur la fusion pour les séances multiples : les ajouter
  après, directement dans `data/events.json`.**
- **Aubéria l'Atelier : la meilleure source de la semaine, et un champ de mines pour la fusion.**
  `auberia.fr/ateliers`, `/ateliers/noel` et surtout `auberia.fr/product/<id>/<slug>` donnent date, horaire,
  **âge minimum explicite** et tarif pour 27 ateliers datés de novembre, **relayés par aucun agenda Diffusio
  ni par tourisme-aveyron**. Mais l'atelier enchaîne deux à trois séances différentes par créneau au même
  endroit : la fusion en a avalé 4 et a laissé 3 `id` porteurs du titre d'un voisin. **Méthode retenue :
  après fusion, supprimer tout le bloc `venue == "Aubéria l'Atelier"` et le réinsérer tel quel depuis le
  fichier de l'agent** (aucun de ces `id` n'existait avant, donc aucun favori en jeu). Plus sûr et plus
  rapide que de rapiécer les titres un par un.
- **Noël à Rodez : l'emplacement est tranché — place Foch.** L'arrêté
  `ville-rodez.fr/uploads/2026/10/AG-2026-0847-ODP-C-S_Reglement-marche-de-noel_du-11-12-au-31-12.pdf`,
  illisible avec `pdftotext` (il ne rend que l'accusé préfectoral) mais **lisible page par page avec
  `pdftoppm -png -r 110` puis l'outil Read**, donne : marché **place Foch du 11/12 08 h au 31/12 19 h**,
  20 chalets, **fermé le 25/12**, lun-jeu 10 h-19 h, ven+sam 10 h-21 h, dim 10 h-20 h, entrée gratuite
  (« aucune voiture place Foch ou place Tristan Richard »). Deux agents l'ont lu indépendamment. Le tag
  `a-confirmer` est levé. **Restent introuvables pour la 6e veille** : patinoire (place de la Cité et
  Athyrium d'Onet), grande roue, village du Père Noël, petit train, forêt lumineuse, et les **horaires des
  5 déambulations des Enjoliveurs** (la DEC2026-303 dit « à déterminer sur la feuille de route » et aucune
  décision postérieure n'est parue). 561 actes réglementaires dépouillés, à jour au 03/11 (dernier
  AG-2026-0854, dernière décision DEC2026-304) ; 36 noms de `uploads/2026/{10,11,12}/2026_PROG-noel*`,
  `2026_VACnoel*` testés, tous en 404. Le visuel de la page « animations » est encore
  `uploads/2024/11/2025_NOEL.jpg`, avec un texte générique citant « forêt lumineuse » **sans aucune date**.
  ⚠️ Piège reconfirmé : « 6 déc.-4 janv., 27 chalets, grande roue » = **articles 12actu des 25/11 et
  04-05/12/2025**. `rodez-tourisme.fr/agenda/noel/` affiche l'édition 2025 pour la 6e veille.
- **Téléthon de Rodez et d'Onet : rien, 5e veille** (552 puis 561 actes, page d'accueil, `?s=telethon`,
  17 rubriques de commune de Centre Presse sur 3 pages de profondeur, 3 287 URLs d'articles). Mais la semaine
  a livré **4 Téléthons inédits** : Sébazac-Concourès 14-15/11 (avec initiation au pickleball dès 10 ans),
  la **boum du conseil municipal des enfants de Druelle le 20/11**, la kermesse sportive familiale et le
  quine de Pont-de-Salars les 5-6/12, et Goutrens le 28/11.
- **Sources nouvellement utiles**
  - **`alentoor.fr` : la trouvaille de la semaine.** **403 en WebFetch, 200 en `curl -sSL`.** Agenda par ville
    et par rubrique : `alentoor.fr/<commune>/agenda/<rubrique>?page=N` (`activites-enfants`,
    `activites-loisirs`, `spectacles`, `expositions`, `brocantes-vide-greniers`, `sports`), plus `/aujourdhui`
    et `/weekend`. **Chaque fiche de la liste porte son propre JSON-LD `Event` complet** (pas un `ItemList`) :
    `startDate` avec heure et fuseau, `offers.price`, `isAccessibleForFree`, adresse, et une `description`
    qui contient le programme détaillé. Il couvre les communes voisines et il est le **seul des huit
    agrégateurs testés à connaître le Festival Vive la Magie**.
  - **`baraqueville.fr` répond de nouveau (200)** — le REX du 23/09 la donnait injoignable :
    `/activites/evenements/` + fiches `/agenda/<slug>/`, affiches en `wp-content/uploads/AAAA/MM/`.
    **C'est par là qu'arrivent les cirques** : le Cirque Olympia des 14-15/11 vient de son affiche JPG.
  - **`vide-greniers.org/evenements/<Commune>-12` puis `/evenement/<id>`** : horaires, salle exacte,
    organisateur et gratuité des bourses aux jouets et braderies dans un rayon de 50 km.
  - **`theatredes2points.mapado.com`** (trouvé dans `minisite.moduleList` de `mjcrodez.mapado.com`) :
    27 ticketings de la saison du Théâtre des 2 Points, fiches `/event/<id>-<slug>` avec `entities.eventDates`
    et `ticketPrices` en centimes. ⚠️ **les titres préfixés d'un `*` sont les séances SCOLAIRES**
    (`*Juste Iréna` = 23/02 14 h 30) : à écarter systématiquement.
  - **MJC `loadmore_agenda` remarche** : il faut POSTER
    `action=loadmore_agenda&page=N&query=<la chaîne JSON du bloc `loadmore_agenda_params` de /agenda/>`.
    Sans `query` la réponse est vide — c'était le blocage constaté en début de session. 7 pages donnent tout
    l'agenda jusqu'en mai 2027. En revanche `mjcrodez.fr` renvoie sa **page d'accueil pour toute URL en
    `curl`** : passer par WebFetch.
  - **`tourisme-aveyron.com`** : le JSON-LD de la liste porte **`dateCreated`/`dateModified`** — plus besoin
    de décoder le suffixe `FMA` : filtrer `dateCreated >= <date de la veille précédente>` isole les fiches de
    la semaine (22 cette fois). Et **le filtre de dates `ReactWay[d]=~AAAA-MM-JJ~AAAA-MM-JJ` est désormais
    appliqué côté serveur** quand on le combine au filtre géo (67 fiches pour janvier-février au lieu de
    4 051) : le REX des 07 et 14/10 est périmé. C'est la méthode pour sonder un mois précis.
  - **`12actu.com/agenda?page=N` va maintenant jusqu'à la page 51** (1 092 événements, `startDate` max
    05/12/2027) : le blocage « s'arrête au 16/11 » du 28/10 est levé. `?categorie=` reste ignoré sur
    `/agenda` mais **marche sur `/rodez/agenda?categorie=famille&page=N`**. `12actu.com/recherche` est
    inutilisable en curl (100 % JS) mais **exploitable en WebFetch**. ⚠️ son **slug d'URL est recyclé**
    (« La cabane de Lucie Félix » vit sous `/agenda/exposition-loucidou-le-loup-et-les-5-sens-…`) et son
    champ `description` reprend parfois le titre de la fiche voisine.
  - **`ville-rodez.fr/agenda/?id1%5BcurrentPage%5D=N` marche en curl et reste le relais de la médiathèque**
    (9e veille sans `mediatheque.ville-rodez.fr`) : les deux séances « Lectures en famille » du 07 et du
    14/11 tenaient dans une seule fiche. La liste embarque un JSON `{"oiId":…,"url":"/fiche/agenda/…"}`
    plus fiable que les `href` du HTML, et chaque fiche porte `data-lat`/`data-lng`.
  - **`ville-rodez.fr` (accueil nu, curl)** portait `uploads/2026/10/Programme-Inauguration-Paul-Lignon.pdf`,
    absent de l'agenda, qui a livré trois animations gratuites du 04/11 (entraînement public du RAF avec
    dédicaces, portes ouvertes du stade, expo photos au jardin public jusqu'à fin novembre).
  - `starting11.com/fixtures/rodez-vs-<adversaire>` : date, journée, stade et coup d'envoi **en GMT**
    (+1 h en hiver) — remplace `api.sofascore.com` et `liguesdefoot.fr`, tous deux passés en 403.
  - `centrepresseaveyron.fr/recherche?q=…` en `curl -sSL` a donné la **première information sur Rodez Basket
    depuis 5 veilles** : le club joue **à l'Amphithéâtre**, J6 contre Jegun le samedi 07/11 à 20 h.
  - `judo-jra.ffjudo.com/evenement` confirme la Coupe Zone Nord Minimes au Dojo de Rodez le 10/01/2027.
- **Sources nouvellement bloquées ou faussées**
  - **`athle.fr/bases/liste.aspx` et `bases.athle.fr` : 502 du proxy sur 7 tentatives curl, 503 en WebFetch**
    — nouveau blocage, le calendrier FFA de l'Aveyron n'a pas pu être dépouillé cette semaine (régression par
    rapport au 28/10, où un seul appel rendait toute la saison).
  - **Les images statiques d'`onet-le-chateau.fr` sont 403 avec un User-Agent de navigateur et 200 sans
    aucun UA** — l'inverse exact de l'astuce notée le 28/10. Le programme du Patio n'a pu être relu que
    comme ça. Les pages restent en 418 en curl et passent en WebFetch.
  - **`foot-direct.com` décale systématiquement les matchs de National 2 d'un jour** : ne s'en servir que
    pour l'adversaire, jamais pour le jour. `onet-le-chateau.fr/evenements/page/N/` fait foi (OCF au
    samedi 18 h).
  - **Ne pas conclure à la disparition d'un récurrent d'Onet sur sa fiche individuelle**, qui n'affiche
    qu'une occurrence : lire la liste paginée. (« Un mercredi autrement » a lieu le 18/11 **et** le 16/12
    alors que sa fiche n'annonce que le 28/10.)
  - `moyrazes.fr` : la liste répond mais ses fiches sont en **erreur critique WordPress**.
  - `conservatoire-aveyron.fr` 502 (3e veille) ; `maisondulivre.com` et `terramemoria.fr` 403 ;
    `musees.aveyron.fr` et `aveyron.fr` répondent 200 avec un corps vide de 222 octets ;
    `mjc-onet*.fr` sans DNS ; `api-dofa.ffhandball.fr` 502 (6e veille) ; tous les domaines du basket
    aveyronnais sans DNS. `jds.fr/rodez/agenda/` répond mais ses listings Rodez sont vides : utile comme
    **test d'absence en une requête**.
- **Arbitrages tranchés cette semaine**
  - **Rodez Rugby - SO Millau du 08/11 : 15 h 30** (fiche de la Ville créée le 30/10 « dimanche 8 novembre à
    15 h 30 » + rugbyamateur, deux sources). Le **14 h 45** du programme municipal est l'heure des
    **animations d'inauguration** du stade rénové (défilé des sections jeunes et féminines, jeu-concours), ce
    qui explique précisément pourquoi ce match seul sort du 15 h 15 habituel. Un troisième agent citait une
    fiche Tourinsoft **plus ancienne** (`FMA-20260825153036044`), qui ne donne aucune heure : son objection
    tombe. **Leçon : comparer les horodatages `FMA` des fiches avant de les opposer.**
  - **Opéras du CGR** : le critère n'est pas le genre mais **l'heure de fin**. « Carmen » reste en base
    (séances de 15 h 45 et de 10 h 30, des matinées) ; « Le Crépuscule des Dieux » (03/02, 17 h 45, Wagner
    ≈ 5 h) et « Cosi fan tutte » (23/02, 19 h 45) sont écartés car ils finissent vers 23 h. Il n'y a donc
    pas d'incohérence à avoir des opéras en base et à en refuser d'autres.
  - **« NovAdo fait court » et « NovAdo invite le Conservatoire »** : les **deux pages officielles de la MJC**
    annoncent « Dimanche 15 novembre 2026 à 17:00 » au Théâtre des 2 Points, participation libre. Deux
    spectacles ne peuvent pas occuper la même salle à la même heure : les deux fiches ont été **fusionnées en
    une** (id `novado-fait-court_…` conservé), avec le doute consigné dans la description et le tag
    `a-confirmer`. À confirmer au 05 65 67 01 13.
  - **Bourse puériculture de l'APE à Souyri : le 15/11, pas le 21/11** (trois agents concordants ; le 21/11
    est la **gratounade de Pont-les-Bains**, un autre événement). L'`id` historique
    `…_2026-11-21_salles-la-source` est **conservé** malgré la date corrigée, pour ne pas perdre les favoris.
  - **VR « Outrenoir » au musée Soulages : interdite aux moins de 12 ans** (`rodez.tickeasy.com` :
    « interdit aux personnes souffrant d'épilepsie, au moins de 12 ans ») → `age_min` passé de 8 à 12.
  - **« Chambres adolescentes » finit bien le 22/11** (« Les Invisibles » démarre le 26/11) : tag levé.
  - **« Tourne fête » du 23/01** : spectacle de 35 min avec une 2e séance à 10 h 45, donc la séance de
    9 h 30 ne peut pas finir à 11 h 15 → `end_time` corrigé à 10 h 05.
- **Kefesh (croisement du 04/11)** : 123 fiches normalisées, 102 dans la fenêtre, 59 « manquants » **et** les
  43 que `same()` donnait pour présents ont été recomparés à la main. **6 ajoutés** (les 2 « Lectures en
  famille » de la médiathèque, l'entraînement public du RAF et les portes ouvertes de Paul-Lignon, la soirée
  roller de Sébazac, le rugby Canton d'Alban du 21/02), **1 correction**, **51 écartés** (≈ 40 adultes :
  conférences de musée, ateliers Trinquons, cafés des langues, concerts de bar, comedy, drag show, one man
  show ; hors cible : goûter allaitement, Mois du doc à thème adulte ; hors zone : « Le Club à Millau »).
  **Kefesh a encore eu raison seul** sur l'entraînement du RAF et les portes ouvertes. Deux pièges nouveaux :
  `same()` a masqué la soirée roller de **Sébazac** derrière une soirée Halloween de **Mayran** du même jour
  (il ne contrôle pas la commune), et **Kefesh décale ses slugs d'un cran sur les matchs du RAF**
  (`copie-de-raf-annecy…` porte le titre « RAF - FC Nantes ») : **ne jamais lire un slug Kefesh comme une
  confirmation**. Rappel toujours valable : ignorer par principe les dates de match données par Kefesh, mais
  recouper aussi notre propre base à la billetterie du club.
- **Vacances d'hiver (6-22/02/2027) : absence établie, pas un échec de collecte.** Trois agents ont cherché
  séparément : aucun programme de vacances publié (musées — l'agenda de Soulages va pourtant jusqu'au
  07/03 —, MJC et Mapado, Patio, CGR, médiathèques, Aquavallon, clubs sportifs). `rodezagglo.fr` n'a **aucune**
  fiche de février ; `12actu` n'a que **33 événements en février pour tout l'Aveyron** contre 595 en novembre.
  C'est cohérent avec les délais de publication constatés (musées et MJC ≈ 3 semaines, CGR ≈ 2 semaines) :
  **à rechercher à la veille de mi-janvier**, pas avant.
- **Janvier-février restent structurellement creux** (52 et 20 entrées) : même constat chez les agrégateurs.
  Les programmes de janvier des MJC, centres sociaux, médiathèques et musées ne sont pas parus. La série
  « Activités parents-enfants » du centre social de Rodez paraît mois par mois **vers le 21** : celle de
  décembre est attendue vers le 21/11.
- **Choix assumé sur le rugby** : les matchs de **Fédérale B** des 10/01, 17/01, 31/01 et 21/02 sont décrits
  **dans la description du match masculin du même jour** plutôt qu'en fiches propres, parce que `merge.py`
  fusionne deux rencontres du même jour au même stade. Les trois dates où la Fédérale B joue sans match de
  Fédérale 2 (08/11, 22/11, 13/12) ont bien leur fiche. Les matchs de **Fédérale 2 Féminine** portent tous
  `a-confirmer` : `rugbyamateur.fr` **réutilise les identifiants des matchs masculins** pour ses lignes
  féminines et aucune deuxième source ne les confirme.
- **À rechercher explicitement à la prochaine veille** : **patinoire, grande roue, village du Père Noël,
  petit train, forêt lumineuse** et les **horaires des 5 déambulations des Enjoliveurs** (surveiller les
  décisions `DEC2026-xxx`, les arrêtés `AG-2026-xxxx` et
  `ville-rodez.fr/sports-loisirs/culture-loisirs/animations/`) ; **Téléthon de Rodez et d'Onet** (6e veille) ;
  **stages de Noël** de la MJC de Rodez (offres « JPS2 » sur Mapado), de la MJC d'Onet (**inscriptions le
  28/11**), du Patio, du RAF et du Stade Rodez Athlétisme — l'absence est établie au 04/11, ils étaient
  attendus mi-novembre ; **« Mes vacances au musée » de Noël** et les animations du 23/12 au 04/01
  (`rodez.tickeasy.com` est l'outil pour prouver leur absence) ; **programme vacances de Noël 11-17 ans de la
  Ville** (chercher un `2026_VACnoel*.jpg` dans `uploads/2026/11|12`) ; **programme de décembre des
  « Activités parents-enfants »** du centre social (vers le 21/11) et des maisons de quartier ;
  **ciné-goûters du CGR** (5e veille) ; **Nuits de la lecture du 20 au 24 janvier 2027, thème « l'enfance »**
  (aucun programme local, à chercher début janvier) ; **heures des 4 matchs N3F du ROC** (7e échec) et des
  4 réceptions de Pré-Nationale, **calendrier de Rodez Basket** (une seule date obtenue, par la presse) ;
  **calendrier FFA de l'Aveyron**, non dépouillé cette semaine (`athle.fr/bases` en 502) ; **Terra Memoria**,
  à trancher par téléphone au 05 65 44 69 27 ; **téléphone de la médiathèque de Rodez**, sur lequel trois
  agents ont donné trois numéros différents.
- **Anomalies restées ouvertes** : heure de début de la soirée roller de Sébazac du 07/11 (la fiche n'écrit
  que « jusqu'à 18 h 30 ») ; heure et salle du quine Jean Auzel à Marcillac du 15/11 ; horaire de
  l'après-midi jeux de société de Laissac du 09/12 (fiche Tourinsoft qui se contredit, 14 h-16 h retenu
  d'après son corps de texte, à confirmer au 05 65 69 60 56) ; les **3 horaires de la visite dansée Nevelson
  du 18/02** et le tarif réel du **Festival Vive la Magie** ; « Quine gourmand » d'Agen-d'Aveyron du 28/11
  (« 14 h » dans le texte, « 20 h 30 » dans le champ horaire) ; le « Super quine du Rodez Rugby » du 13/11,
  classé à Onet-le-Château par l'agglo mais dont l'adresse (1 bd du 122e RI) est la salle des fêtes de
  **Rodez** — retenu à Rodez par deux agents ; **« Croire aux fauves » (24/11), supprimé le 28/10 pour
  annulation, est de nouveau listé** sur mjcrodez.fr, ville-rodez.fr, 12actu, unidivers, alentoor et
  tourisme-aveyron sans mention d'annulation : **ne pas le réintroduire sans appeler la MJC**
  (05 65 67 01 13). « La mère Noël est une rockeuse » (12/12, en réalité à Millau) revient de même chez les
  quatre agrégateurs : les deux suppressions antérieures sont justifiées, un garde-fou les retire désormais
  automatiquement après fusion.
- **Zone** : nouvelle commune en base, **La Loubière (7,6 km)**. Mesurées et dans le rayon mais sans rien à
  retenir : Calmont/Ceignac 9,6 km, Trémouilles 12,2 km, Manhac 13,5 km, Gramond 19,4 km. **Arvieu (19,1 km)
  et Goutrens (19,2 km) restent dans le rayon à vol d'oiseau mais à ≈ 30 km par la route** : question
  toujours à arbitrer avec le propriétaire du projet (9 activités en dépendent, dont la soirée Téléthon de
  Goutrens du 28/11).
- **Déjà repérés pour la fenêtre suivante (après le 24/02)** : « Les dimanches du Conservatoire » au musée
  Soulages le 28/02, handball N1M ROC - Montpellier et N3F Muret le 27/02, volley F1O/M1O le 27/02, quine de
  l'APE d'Escandolières le 28/02, sortie du club Jeux de société de la MJC au **Festival International des
  Jeux de Cannes du 25 au 28/02/2027** (ado 13-18 ans 100 €, enfant de moins de 13 ans gratuit — hors zone),
  « NovAdo fait son cinéma » les **6-7 mars 2027**, et le **carnaval de Luc-la-Primaube le 13/03/2027**
  (défilé en musique live, spectacle, boum, goûter — le seul carnaval publié de la saison).

### Veille du 11/11/2026

- **La leçon de la semaine : les trois motifs de corruption de `merge.py` se reproduisent chaque semaine à
  l'identique, et le seul contrôle qui les attrape tous est `qa.py --before` lu ligne par ligne.**
  Cette semaine : **19 `id` perdus et 3 `id` survivants porteurs du contenu d'un voisin** —
  `atelier-archi-…-sainte-catherine` reprenait le titre de l'expo « Pierres en mouvement » (**3e semaine
  consécutive, même galerie, mêmes dates**), `boules-de-noel-en-tissu-seance-de-9-h-30` portait
  « Couronne de Noël en tissu » (Aubéria), et `marche-de-noel-de-bertholene` portait le titre, le lieu
  **et la commune** de celui de Pont-de-Salars (**3e semaine, toujours le préfixe `salle-des-fe`**).
  Les 5 matchs de volley masculins avalés par leur homologue féminin du même jour au gymnase Frugère,
  les 6 ateliers Aubéria, Extrem'Ados théâtre avalé par Extrem'Ados danse, la séance de 19 h de Vive la
  Magie et celle de 10 h 45 de « Tourne fête » complètent la liste. **Méthode retenue, à refaire telle
  quelle : restaurer chaque `id` perdu depuis `avant.json` *ou*, mieux, depuis le fichier de l'agent qui
  l'a ré-émis** (un dictionnaire `id -> événement` construit sur les 8 fichiers d'agents, avec repli sur
  `avant.json`), puis **réécrire le contenu des `id` corrompus depuis la même source**.
- **`merge.py` a de nouveau annulé toute la passe de re-vérification : 132 `source_checked` ont dû être
  forcés** (contre 82 le 04/11). L'étape 7 n'est pas une précaution, c'est un passage obligé.
- **Nouveau motif de doublon, à ajouter aux contrôles : une fiche longue ré-émise avec sa date de début
  tronquée au `from` de la semaine devient un second événement.** `same_event()` ne compare que
  `date`, donc une expo du 15/10 au 31/12 ré-émise « du 12/11 au 31/12 » n'est jamais rapprochée de
  l'originale. 11 doublons de ce type cette semaine (Atelier Archi, Les 30 ans de La Menuiserie,
  expo Dess(e)ins, la cabane de Lucie Félix, **trois** fiches du même manège Dubief de la place du Bourg,
  Colinet ×2, l'atelier poterie du Patio ×2). **Contrôle à faire à chaque fusion : pour chaque paire de
  même commune dont les plages de dates se chevauchent et dont les titres sont à ≥ 0,72 de similarité,
  trancher à la main et garder l'`id` le plus ancien.** Corollaire pour le briefing des agents :
  **leur demander de ré-émettre une fiche longue avec sa date de début D'ORIGINE**, pas tronquée.
- **Les corrections d'un agent peuvent dégrader un champ déjà juste.** Trois `venue` précis ont été
  remplacés par des « (salle à confirmer) » venus d'une fiche plus pauvre
  (salle d'animations de Gages, salle des fêtes de Marcillac, espace parents-enfants de la rue
  Louis-Dausse). **Dans la passe de réconciliation, refuser tout remplacement d'une valeur précise par
  une valeur vague** — « X (à confirmer) », « Non communiqué », « Sur place » — même venu d'une source
  fraîche. Même piège sur les `description` : un agent a réécrit sans accents une description correcte.
- **Arbitrage inversé : « Je suis trop vert » (05/12) est à 17 h, pas à 20 h 30.** La décision du 28/10
  était fausse. Trois sources concordantes : `entities.eventDates` de
  `theatredes2points.mapado.com/event/731210-…` (= 2026-12-05T17:00), la page officielle
  `mjcrodez.fr/agenda/je-suis-trop-vert/` (« Samedi 5 décembre 2026 à 17:00 », 60 min, dès 7 ans) et la
  page `/theatre-des-2-points/agenda/je-suis-trop-vert/`. **Kefesh avait raison, et notre propre
  `description` disait déjà « de 17 h à 18 h » : relire ses propres descriptions avant de défendre un
  horaire.**
- **Noël 2026 à Rodez : l'absence est désormais EXPLIQUÉE, pas seulement constatée (7e veille).**
  La décision `DEC2026-271` attribue le lot « **Village féérique de Noël** » à **Eveniums Concept
  (Rodez), 99 995,50 € HT**, et l'appel à manifestation d'intérêt montre que 2026 passe par un
  **concessionnaire** : patinoire, grande roue, village du Père Noël, petit train et forêt lumineuse
  **ne feront donc plus l'objet d'arrêtés municipaux**. Inutile de continuer à les chercher dans les
  actes réglementaires : **surveiller Eveniums Concept, l'office de tourisme et la presse**. Seuls faits
  acquis : marché place Foch du 11/12 au 31/12 (`AG-2026-0847`) et les 5 déambulations des Enjoliveurs
  (`DEC2026-303`), dont les horaires restent « à déterminer sur la feuille de route » — aucune décision
  postérieure n'est parue (derniers actes au 10/11 : `AG-2026-0856`, `DEC2026-316`, tous des concessions
  de cimetière).
- **Sources nouvellement utiles**
  - **`ville-rodez.fr/wp-json/wp/v2/media?per_page=100&page=N&orderby=date&order=desc` : la trouvaille de
    la semaine.** L'API REST WordPress de la Ville **liste tous les fichiers déposés avec leur date** ;
    3 pages = 300 fichiers = tout depuis le 15/10. C'est **l'outil de preuve d'absence le plus net** pour
    les programmes municipaux, et c'est ainsi qu'a été trouvé
    `uploads/2026/10/2026_MERC12-17ans_NovDec.pdf` (programme « Les mercredis 12-17 ans », 5 dates).
    ⚠️ la base d'URL des fichiers est `/uploads/…`, **pas** `/wp-content/uploads/…` (qui répond 200 avec
    une page HTML : piège silencieux). ⚠️ **`&search=` est tokenisé par mot** et ne trouve pas
    `2026_VACtoussaintS2-Web.jpg` sur `search=toussaint` : **ne jamais prouver une absence avec `search`,
    seulement avec la liste chronologique.** Même API utile sur
    `baraqueville.fr/wp-json/wp/v2/media?per_page=40&orderby=date&order=desc` (ses fiches d'agenda sont
    vides, tout est dans l'affiche JPG) — c'est par là qu'arrive la tombola de Noël du 13/12.
  - **`ville-rodez.fr/quotidien/enfance-jeunesse/jeunesse/activites-extra-scolaires/`** (curl) porte les
    **PDF de programme ados** : à ouvrir à chaque veille, le prochain couvrira janvier-février.
  - **`vide-greniers.org/evenement/<id>` : son JSON-LD porte `eventStatus`** — c'est la **seule façon de
    détecter une annulation** (`EventCancelled` sur la bourse aux jouets de Muret-le-Château du 14/11,
    déjà en base, et sur le vide-grenier de Montrozier du 05/12). ⚠️ en revanche
    `vide-greniers.org/evenements/<Commune>-12` **ignore la commune** et sert un rayon fixe : une seule
    requête suffit, la liste va jusqu'en mai 2027.
  - **`rodez.tickeasy.com`** : la liste est en JS mais `curl -sSL https://rodez.tickeasy.com/` rend
    **les 6 tuiles produits en clair**, et `…/fr-FR/produits?fbq_zilzrtTY0J=<id>` rend chaque fiche avec
    ses tarifs. **Preuve d'absence la plus rapide pour les ateliers des musées** (aucun produit
    « Mes vacances au musée », aucun atelier daté).
  - **Fiches Tourinsoft « saison complète »** : une seule fiche porte tout un calendrier annuel dans son
    `description` JSON-LD — `…galerie-les-capucines-les-expositions-20262027…` a livré les 4 expos de la
    galerie avec leurs dates, `…stages-artistiques-pour-les-vacances-scolaires…` les 2 stages de Sonia
    Privat, et `…les-dimanches-du-conservatoire…` les 9 dates de la série. **Les chercher est très
    rentable.** ⚠️ cette dernière fiche est intitulée « Druelle-Balsac » alors que son corps dit
    **Rodez, 8 rue Sainte-Catherine** : le corps tranche.
  - **`athle.fr/bases/liste.aspx` remarche** (il était en 502 le 04/11) : l'URL avec
    `frmpostback=true&frmbase=calendrier&frmmode=1&frmespace=0&frmsaisonffa=2027&frmdate1=…&frmdate2=…&frmdepartement=012`
    rend les **25 compétitions FFA de l'Aveyron** de la saison en un appel `curl -sSL` (HTML **cp1252**).
    Et **`staderodez.athle.fr/asp.net/espaces.html/html.aspx?id=51371`** (curl, cp1252) donne la page
    complète de la Ronde de Noël : horaires, catégories, tarifs.
  - **`rochandball.com/wp-content/uploads/2026/09/3.jpg`** ouvert avec l'outil Read a livré les
    **5 réceptions de Pré-Nationale du ROC**, dont une inédite le 27-28/02.
  - **`my.weezevent.com/colinet-2026`** (curl) : dates officielles **et** mention « guichet fermé ».
    `espacegeorgesrouquier.fr` (accueil, `/cine-club` est en 404) : film et horaires du ciné-club de
    Goutrens. `ch-rodez.fr/evenement/…` pour les ateliers santé du CESU.
  - **Les fiches `12actu.com/agenda/<slug>` en curl** portent, hors JSON-LD, un bloc
    « Le programme / Bon à savoir / Tarifs / Prochaines dates » plus riche que le JSON-LD : c'est là que
    se trouvent les tarifs par tranche d'âge et les dates suivantes d'une série.
  - **Téléphone de la médiathèque-ludothèque de Rodez : 05 65 77 89 10**, 7 rue Camille-Douls
    (`ville-rodez.fr/sports-loisirs/culture-loisirs/mediatheque-ludotheque/`). Les deux autres numéros
    qui circulaient sont faux. 10e veille sans `mediatheque.ville-rodez.fr`.
- **Sources nouvellement bloquées, faussées ou à corriger dans le briefing**
  - **`alentoor.fr` a changé sa pagination et ses slugs de rubrique.** `?page=N` est **ignoré** (toutes
    les pages renvoient la page 1) : il faut **`?p=N`**. Les rubriques au pluriel `spectacles`,
    `expositions`, `brocantes-vide-greniers`, `sports` renvoient **404** ; les nouvelles sont au
    **singulier** (`spectacle`, `exposition`, `brocante-vide-grenier`, `sport`, plus `concert`,
    `festival`, `festivites`, `foire-salon`, `marche`, `theatre`, `visite`). Le plus simple :
    `alentoor.fr/<commune>/agenda?p=N`. Et **son JSON-LD de liste n'a plus ni `geo`, ni `offers.price`,
    ni `isAccessibleForFree`** : il faut ouvrir la fiche `…/agenda/<id>-<slug>`. Slugs de commune :
    `laissac` et `druelle` (pas `laissac-severac-l-eglise` ni `druelle-balsac`, qui sont en 404).
  - **`centrepresseaveyron.fr/aveyron/<commune>/page-N` ne filtre plus par commune** pour
    onet-le-chateau, luc-la-primaube, sebazac-concoures, olemps et bozouls (les 5 servent le même digest
    départemental) ; seul `/aveyron/rodez/page-N` filtre encore. Et sa **recherche s'est dégradée** :
    elle ne ramène quasi que des archives 2019-2025, y compris sur « telethon rodez 2026 ».
  - **`rodezaveyronfootball.com/classement-calendrier-2026-2027-ligue-2-bkt/` : 403 en curl et calendrier
    vide en WebFetch** — or c'est le `source_hint` que Kefesh donne pour **tous** les matchs du RAF, il ne
    prouve donc rien. Autorités de remplacement : `billetterie.rodezaveyronfootball.com` (source primaire)
    + **`fotmob.com/api/data/teams?id=4120`** (toute la saison, **en UTC**) + `starting11.com`.
  - `competitions.ffbb.com` répond 200 mais toutes ses pages `/ligues/occ/…` sont en **403 Cloudflare** ;
    `resultats.ffbb.com`, `occitanie.basketball`, `basketball-occitanie.fr`, `v2.ffbb.com` sans DNS.
    **Rodez Basket : 5e échec.** `mjc-onet.com` (le `.com`, contrairement aux `.fr` morts) répond mais
    sert **une page de printemps 2026** périmée. `onet-le-chateau.fr/wp-json` : 418 sans UA, 403 avec UA
    vide — l'inverse de ses images ; seul WebFetch passe. `aveyron.fr` et `musees.aveyron.fr` : 200 avec
    un corps de 222-228 octets (10e veille). `ted.europa.eu/…/pdf` : 0 octet.
  - **`alentoor.fr` et `tourisme-aveyron.com` recyclent des coordonnées d'une fiche à l'autre** : la
    randonnée du Téléthon du 29/11 est donnée à **Rignac** alors que la fiche dit **Belcastel** (19,6 km,
    en zone), et le quine de l'APE d'Escandolières du 28/02 à « Rignac, 43 allée des mots » alors que la
    fiche dit **salle des fêtes de Goutrens**. **Contrôler la plausibilité commune/adresse/coordonnée.**
  - **Aubéria recopie le corps de ses fiches sans le mettre à jour** : deux produits datés du 12/12 et du
    16/12 affichent tous deux « Quand : mercredi 9 décembre ». **Le titre/slug du produit tranche**
    (un produit = une séance datée). Et **`auberia.fr/ateliers` seule n'expose pas tout** : 4 produits de
    décembre n'apparaissent que dans les sous-rubriques `/ateliers/<bijoux|bougie|ceramique|couture|
    linogravure|noel|paper-kraft|peinture|vitrail>`.
- **Absences établies cette semaine (à ne pas re-chercher avant la date indiquée)**
  - **Stages de Noël : absence établie pour la 2e semaine.** `mjcrodez.mapado.com` expose ses 17
    ticketings au complet, **aucun code « JPS2 »**, et annonce que **les inscriptions aux stages de
    vacances n'ouvrent que le 29 novembre** — c'est la date à retenir, pas « mi-novembre ».
    `mjcrodez.fr/agenda/stages-vacances-de-noel/` sert encore l'édition **2022**.
    `rodezaveyronfootball.com/stages/` n'annonce que « vos stages de juillet ». MJC d'Onet : page de
    printemps 2026. Patio : agenda arrêté au 24/12.
  - **« Mes vacances au musée » de Noël et animations du 23/12 au 04/01 : rien** (agenda Soulages 8 fiches
    s'arrêtant au 03/12 pour les créneaux datés, Fenaille 6 fiches jusqu'au 16/12, Denys-Puech 2 fiches le
    06/12, et **`rodez.tickeasy.com` ne vend que 6 produits permanents**).
  - **Ciné-goûters du CGR : 6e veille sans rien.** `/avant-premiere/` n'a que 4 avant-premières,
    `/evenements/` qu'une accroche générique sans date, `/prochainement/` 14 titres jusqu'au 03/02 sans
    ciné-goûter. `cgrcinemas.fr/theaters/w1200-cgr-rodez` est le bon chemin (`/rodez/evenements/` est en
    404) mais ne porte que la grille tarifaire.
  - **Téléthon de Rodez et d'Onet : 7e veille sans rien**, sur les 182 fiches de `ville-rodez.fr/agenda`,
    les 67 d'`onet-le-chateau.fr` (qui en avait 104 le 04/11) et `onet-le-chateau.fr/?s=téléthon`
    (19 résultats, tous 2023-2025).
  - **Marchés de Noël communaux : seul Flavin (12/12) s'est publié cette semaine.** Toujours rien pour
    Onet, Sébazac, Olemps, Luc, Le Monastère, Marcillac et Baraqueville, après un balayage commune par
    commune de rodezagglo (260 fiches), alentoor (18 communes) et tourisme-aveyron (388 fiches).
  - **Vacances d'hiver (6-22/02/2027) : le creux est réel, et désormais chiffré par trois agrégateurs**
    — tourisme-aveyron 24 fiches en janvier et 18 en février, 12actu 27 et 14, alentoor 26 et 13, listes
    quasi identiques et déjà en base. **À rechercher à la veille de mi-janvier**, pas avant.
  - **Montrozier (espace archéologique) est fermé sur toute la fenêtre** : ses fiches ne listent des
    horaires que d'avril à octobre. **Terra Memoria** : toujours aucun événement daté, `terramemoria.fr`
    en 403 — à trancher au 05 65 44 69 27.
  - **Aucun cirque de passage, aucun carnaval, aucune chandeleur dans la fenêtre.** Les actes de Rodez ne
    portent que Zavatta (02-03/2026) et Amar (04-05/2026), passés. Le carnaval de Luc-la-Primaube est le
    **13/03/2027 à 15 h** (hors fenêtre, confirmé).
- **Arbitrages tranchés cette semaine**
  - **Super quine du Rodez Rugby (13/11) : à Rodez.** La fiche Tourinsoft s'intitule « … Onet-le-Château »
    et classe la commune à Onet, mais son adresse « 1 bd du 122e Régiment d'Infanterie » est la salle des
    fêtes de **Rodez**. **L'adresse tranche contre le titre et le champ commune.**
  - **Biathlon Trail de Laissac (17/01) : supprimé, hors zone.** Le 28/10 l'entrée avait été conservée
    avec les coordonnées du bourg de Laissac (19,8 km) ; `biathlon-trail.fr/coursesenfants.html` situe le
    départ à la **salle des fêtes de Sévérac-l'Église**, géocodée à **21,97 km**.
  - **Manège Dubief de la place du Bourg : une seule fiche**, celle de l'arrêté `AG-2026-0831`
    (02/10 → 03/01). Trois fiches concurrentes avaient fini en base.
  - **Colinet 2026 se joue bien les 20, 21, 27 et 28/11 à 20 h 30, et les 4 séances sont COMPLETES**
    (`my.weezevent.com/colinet-2026` : « le spectacle se jouera à guichet fermé »). **Conservées**, avec
    la mention « complet » dans le prix.
  - **« Croire aux fauves » (24/11) reste supprimé** : sa page officielle porte toujours « SPECTACLE
    ANNULÉ » et le spectacle est **absent des 27 ticketings de `theatredes2points.mapado.com`** alors que
    tous les autres titres de la saison y sont. La liste `/agenda/` de la MJC, `ville-rodez.fr` (2 fiches)
    et les quatre agrégateurs ont tort.
  - **« On court à la Baleine » : le 03/12 est réservé aux scolaires** (supprimé) ; le public c'est le
    **04/12 à 14 h** et le **samedi 05/12 de 14 h 30 à 19 h** (journée famille, ajoutée).
  - **« NovAdo fait court » et « NovAdo invite le Conservatoire » : fusion confirmée.** Les deux pages
    officielles de la MJC annoncent le **15/11 à 17 h dans la même salle**, et la page du festival y place
    en plus la restitution d'Extrem'Ados. Une seule fiche (id `novado-fait-court_…`), les deux volets
    décrits dedans, `a-confirmer` levé.
  - **Opéras et ballets du CGR, suite** : « Le Crépuscule des dieux » (03/02, 17 h 45, ≈ 5 h) écarté ;
    « Cosi fan tutte » a **disparu de la programmation**. « Casse-Noisette » du 01/12 à 20 h 15 (fin
    ≈ 22 h 30) est **conservé** — un ballet de Noël en soirée reste une sortie famille assumée.
  - **« Quine gourmand » d'Agen-d'Aveyron (28/11) : anomalie toujours ouverte.** La fiche Tourinsoft se
    contredit encore (« 14h - Salle des Fêtes » dans le corps, « Samedi : à 20h30 » dans le champ
    horaire) et **aucune deuxième source n'existe** (ni alentoor, ni 12actu). Laissée à 20 h 30 avec
    `a-confirmer`.
- **Zone** : nouvelles communes mesurées et retenues — **Belcastel 19,6 km**, Muret-le-Château 16,1 km,
  Balsac 11,7 km, Comps-la-Grand-Ville 13,2 km, Le Vibal 14,7 km, Valady 14,6 km. Rejetées avec leur
  distance : Castanet 20,2 · Pruines 20,4 · Cassagnes-Bégonhès 20,5 · Ségur 21,8 · **Sévérac-l'Église
  21,97** · Escandolières 22,9 · Espalion 24,8 · Naucelle et Salles-Curan 25,2 · Rullac-Saint-Cirq 25,6 ·
  Saint-Côme-d'Olt 26,5. **Arvieu (19,1 km) et Goutrens (19,1-19,2 km) restent dans le rayon à vol
  d'oiseau mais à ≈ 30 km par la route** : question toujours à arbitrer avec le propriétaire du projet.
- **À rechercher explicitement à la prochaine veille** : **patinoire, grande roue, village du Père Noël,
  petit train, forêt lumineuse** — mais **chez Eveniums Concept, l'office de tourisme et la presse**, plus
  dans les actes réglementaires (voir ci-dessus) ; les **horaires des 5 déambulations des Enjoliveurs** ;
  **Téléthon de Rodez et d'Onet** (8e veille) ; **stages de Noël, dont les inscriptions MJC ouvrent le
  29/11** et celles de la MJC d'Onet le 28/11 ; **« Mes vacances au musée » de Noël** et les animations du
  23/12 au 04/01 (`rodez.tickeasy.com` pour prouver l'absence) ; **programme vacances de Noël 11-17 ans de
  la Ville** (via l'API `wp-json/wp/v2/media`) ; **programme de décembre des « Activités parents-enfants »**
  du centre social, attendu **vers le 21/11**, et des maisons de quartier ; **ciné-goûters du CGR** ;
  **Nuits de la lecture du 20 au 24 janvier 2027** (aucun programme local, `nuitsdelalecture.fr/programme?departement=12`
  est vide) ; **heures des 4 matchs N3F du ROC** (8e échec) et des **5 réceptions de Pré-Nationale** ;
  **calendrier de Rodez Basket** (5e échec — un appel au club est probablement le seul moyen) ;
  **jour et stade des réceptions de Rodez AF 2** ; **confirmation des 3 matchs de Fédérale 2 Féminine**
  (toujours sans deuxième source) ; **fin des récurrents « bébés nageurs » d'Aquavallon** (deux agents en
  désaccord, base laissée au 23/01, à trancher au 05 65 77 85 50) ; **Terra Memoria** (05 65 44 69 27) ;
  et les **programmes de janvier-février**, à reprendre **mi-janvier**.
- **Déjà repérés pour la fenêtre suivante (après le 03/03/2027)** : « NovAdo fait son cinéma » les
  **6-7 mars 2027** (jury ados 12-18 ans, 4 séances), rugby Fédérale 2 Rodez - Mauguio-Carnon 07/03,
  « Mérou » 09/03, « Soirée cabaret danse » de la MJC 11/03, OCF 13/03 et 20/03, **carnaval de
  Luc-la-Primaube 13/03 à 15 h**, « Los Almanos » aux Capucines à partir du 11/03, RAF - Sochaux 12/03
  à 20 h, « Madame Bovary… » 16/03, Booder « Ah… l'École ! » 17/03, « Marguerite » à l'Athyrium 18/03,
  « N.Ormes » (cirque) 19/03, Rodez Rugby - Figeac 21/03, « Le journal de Maïa » 23/03,
  « Fin, fin et fin » à La Baleine 25/03, ROC N1M 03/04 et 02/05.
