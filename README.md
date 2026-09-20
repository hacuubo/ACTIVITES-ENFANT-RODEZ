# 🎈 Sorties Enfants Rodez

Application web progressive (PWA) à installer sur l'écran d'accueil du téléphone : l'agenda des activités pour enfants de **1 à 15 ans** à **Rodez et dans un rayon de 20 km** (spectacles, ateliers, musées, fêtes, cirques, stages, sport, nature…), à faire seul, en famille ou entre amis.

Les données sont mises à jour **chaque mercredi** par une Routine Claude qui parcourt les sites des mairies, musées, salles, associations, offices de tourisme, presse locale et agrégateurs, puis pousse `data/events.json` dans ce dépôt.

## Fonctionnalités

- **📅 Mois** : calendrier avec le nombre d'activités par jour. Toucher un jour liste les activités par ordre chronologique (heure, titre, résumé, ville, tranche d'âge, catégorie).
- **Fiche détaillée** : toucher une activité ouvre la fiche : description, âge et public, lieu avec lien Google Maps, prix, téléphone de réservation (appel direct), billetterie, site officiel, source vérifiée.
- **⭐ Favoris** : l'étoile enregistre une sélection sur le téléphone (conservée entre les mises à jour).
- **🗺️ Carte** : carte plein écran de Rodez et alentours avec les activités du jour pointées par couleur ; toucher un repère ouvre la fiche. La barre de date déroule le calendrier du mois, et une colonne à droite filtre par type d'activité.
- **Filtre par âge** : 1-2, 3-5, 6-10, ados 11-15 (cumulables).
- **Hors ligne** : l'application et la dernière liste d'activités restent consultables sans réseau (les fonds de carte nécessitent le réseau).

## Installer sur le téléphone

L'application est publiée par GitHub Pages à l'adresse : `https://hacuubo.github.io/ACTIVITES-ENFANT-RODEZ/`

- **iPhone (Safari)** : ouvrir l'adresse → bouton Partager → « Sur l'écran d'accueil ».
- **Android (Chrome)** : ouvrir l'adresse → bouton « Installer » dans l'application, ou menu ⋮ → « Ajouter à l'écran d'accueil ».

> Première publication : dans les réglages du dépôt GitHub, *Settings → Pages → Source : GitHub Actions* (le workflow tente de l'activer seul ; si la publication échoue, activer cette option puis relancer le workflow).

## Structure

```
index.html            coquille de l'application
app.js                logique (calendrier, liste, fiche, favoris, carte, filtre âge)
styles.css            styles (clair / sombre)
sw.js                 service worker (hors ligne)
manifest.webmanifest  manifeste PWA
icons/                icônes (SVG + PNG générées par scripts/make_icons.py)
data/events.json      LES DONNÉES (mises à jour chaque mercredi)
docs/SCHEMA.md        format des données
scripts/validate.py   validation du fichier de données (utilisé en CI)
scripts/merge.py      fusion des fichiers de recherche → data/events.json
.claude/skills/veille-rodez/SKILL.md   procédure suivie par la Routine hebdomadaire
.github/workflows/pages.yml            validation + déploiement GitHub Pages
```

Aucune étape de build : ouvrir `index.html` via un serveur statique suffit (`python3 -m http.server`).

## Mise à jour hebdomadaire

La Routine (Claude Code, chaque mercredi matin) suit `.claude/skills/veille-rodez/SKILL.md` :
1. recherche large (institutions, lieux culturels, fêtes et loisirs, associations, agrégateurs et presse) sur les 16 semaines à venir ;
2. géocodage des lieux (Nominatim / OpenStreetMap) ;
3. fusion, dédoublonnage, validation (`scripts/validate.py`) ;
4. commit + push de `data/events.json` → redéploiement automatique.

Pour lancer une mise à jour à la main : ouvrir une session Claude Code sur ce dépôt et demander « suis la procédure veille-rodez ». Configuration de la Routine : voir `docs/ROUTINE.md`.

## Licence des données

Fonds de carte © contributeurs [OpenStreetMap](https://www.openstreetmap.org/copyright). Les informations sur les événements proviennent des sites indiqués dans chaque fiche (champ *source*) ; vérifier auprès de l'organisateur avant de se déplacer.
