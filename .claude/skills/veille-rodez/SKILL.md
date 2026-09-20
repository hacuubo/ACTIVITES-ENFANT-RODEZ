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

## 2. Géocodage

Pour chaque lieu (une fois par lieu) :
```
curl -sS -A "activites-enfant-rodez/1.0" "https://nominatim.openstreetmap.org/search?q=<lieu, ville>&format=json&limit=1"
```
Max 1 requête/seconde. Si introuvable : géocoder la mairie de la commune et le signaler dans `description`. Rejeter tout lieu à plus de 20 km de Rodez (44.3506, 2.5750).

## 3. Assemblage et contrôle

1. Fusionner : `python3 scripts/merge.py --keep-existing --from <aujourd'hui> --to <aujourd'hui + 16 semaines> <fichiers de recherche>` (dédoublonne, retire le passé, trie, écrit `updated_at`).
2. Re-vérifier les événements conservés de l'ancien fichier dont `source_checked` a plus de 3 semaines : rouvrir la source ; supprimer ceux annulés ou introuvables ; mettre à jour `source_checked`.
3. `python3 scripts/validate.py` doit passer sans erreur (corriger jusqu'à 0 erreur).
4. Contrôle qualité : `summary` d'une phrase claire, `age_min`/`age_max` cohérents, `audience` juste (`ados` si réservé aux 11-15), `price` renseigné, téléphone au format `05 65 00 00 00`, catégories exactes.

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
