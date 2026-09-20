# Routine hebdomadaire « Veille hebdo Sorties Enfants Rodez »

Planification : **chaque mercredi à 6h (heure de Paris)**, soit `0 4 * * 3` en UTC l'été (5h en hiver).
Notifications : push + e-mail à la fin de chaque exécution.

## Prérequis

La session lancée par la Routine doit disposer :
- du dépôt `hacuubo/ACTIVITES-ENFANT-RODEZ` **attaché comme source** (checkout + droits de push sur la branche par défaut) ;
- des outils WebSearch, WebFetch, Agent et Bash (réseau sortant autorisé : sites des mairies, musées, presse, nominatim.openstreetmap.org).

Une Routine créée depuis une session Claude Code n'attache pas le dépôt : la créer depuis l'interface **claude.ai → Routines** en sélectionnant ce dépôt et sa branche par défaut, puis coller le prompt ci-dessous.

## Prompt

```
Tu es l'agent de veille hebdomadaire de l'application PWA « Sorties Enfants Rodez » (dépôt GitHub hacuubo/ACTIVITES-ENFANT-RODEZ). Nous sommes mercredi : mets à jour le recueil des activités pour enfants de 1 à 15 ans (seuls, en famille ou entre amis) à Rodez et dans un rayon de 20 km, puis publie-le.

Procédure à suivre à la lettre : le fichier `.claude/skills/veille-rodez/SKILL.md` du dépôt (procédure « veille-rodez »). Résumé :
1. Se placer dans le dépôt (déjà cloné dans la session), se mettre à jour sur la branche par défaut (`git fetch origin` puis `git checkout <branche>` et `git pull`), lire `docs/SCHEMA.md` et le `data/events.json` actuel.
2. Lancer 5 à 6 agents de recherche en parallèle, un par famille de sources de la procédure : (A) institutions, mairies, office de tourisme, département ; (B) lieux culturels : musées, médiathèques, salles, cinémas, théâtres ; (C) fêtes et loisirs : fête foraine, cirques, Halloween, Noël, marché de Noël, patinoire, parcs de loisirs ; (D) associations, ateliers, ados 11-15 ; (F) associations et clubs sportifs : portes ouvertes, séances d'essai, baptêmes, stages de vacances, tournois jeunes, courses enfants, événements jeune public des clubs (RAF, rugby, basket, hand, Aquavallon) ; (E) agrégateurs et presse locale. Couverture : aujourd'hui → 16 semaines. Chaque événement doit provenir d'une page réellement consultée (WebSearch + WebFetch) : ne jamais inventer. Géocoder chaque lieu avec Nominatim (1 requête/seconde, user-agent « activites-enfant-rodez/1.0 »), rejeter au-delà de 20 km de Rodez.
3. Fusionner avec `python3 scripts/merge.py --keep-existing --from <aujourd'hui> --to <aujourd'hui+16 semaines> <fichiers>`, re-vérifier les anciens événements non vérifiés depuis 3 semaines, puis `python3 scripts/validate.py` jusqu'à 0 erreur.
4. Committer `data/events.json` (« Veille du <date> : N activités (M nouvelles) ») et pousser sur la branche par défaut du dépôt avec `git push -u origin <branche>` (4 tentatives avec attente 2/4/8/16 s en cas d'erreur réseau). Ne pas ouvrir de pull request : le push déclenche le redéploiement GitHub Pages. Si le push échoue malgré les tentatives, l'indiquer clairement dans le compte rendu avec le message d'erreur exact.
5. Terminer par un compte rendu de 10 lignes maximum : total d'événements, nouveaux, supprimés, sources injoignables, événements notables à venir, anomalies à corriger dans l'application, et confirmation du commit poussé (hash). Ajouter à la section « Retours d'expérience » de la procédure toute source nouvellement bloquée ou nouvellement utile.

Ne modifie pas le code de l'application (index.html, app.js, styles.css, sw.js) sauf si `scripts/validate.py` ou la procédure l'exige ; dans ce cas, décris la correction dans le compte rendu.
```

## Vérifier qu'une exécution a marché

- Un nouveau commit « Veille du … » apparaît sur la branche par défaut.
- Le workflow « Déployer l'application (GitHub Pages) » est vert.
- Le pied de page de l'application affiche la nouvelle date de mise à jour.
