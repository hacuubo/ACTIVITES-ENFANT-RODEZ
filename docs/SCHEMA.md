# Schéma des données — `data/events.json`

Fichier unique lu par l'application. Il est régénéré chaque mercredi par la Routine de veille.

```json
{
  "updated_at": "2026-09-19T08:00:00+02:00",
  "period": { "from": "2026-09-19", "to": "2027-01-10" },
  "events": [ { ...voir ci-dessous... } ]
}
```

## Un événement

| Champ | Type | Obligatoire | Description |
|---|---|---|---|
| `id` | string | oui | Identifiant stable : `slug-titre_YYYY-MM-DD_ville` en minuscules sans accents (ex. `spectacle-marionnettes_2026-10-14_rodez`). Sert à conserver les favoris entre deux mises à jour. |
| `title` | string | oui | Titre court (≤ 60 caractères). |
| `summary` | string | oui | Une phrase (≤ 140 caractères) : ce que c'est, pour qui. Affichée dans la case du calendrier. |
| `description` | string | non | Texte complémentaire (2 à 6 phrases) : déroulé, matériel, conseils. |
| `category` | enum | oui | `spectacle` · `atelier` · `musee` · `lecture` · `cinema` · `sport` · `nature` · `fete` · `stage` · `jeux` · `autre` |
| `date` | `YYYY-MM-DD` | oui | Premier jour. |
| `end_date` | `YYYY-MM-DD` ou `null` | non | Dernier jour pour un événement sur plusieurs jours (exposition, fête foraine, stage). L'app l'affiche chaque jour de la période. |
| `time` | `HH:MM` ou `null` | non | Heure de début (null = toute la journée). |
| `end_time` | `HH:MM` ou `null` | non | Heure de fin. |
| `days_of_week` | array d'int ou `null` | non | Pour un événement récurrent sur une période : jours où il a lieu (1 = lundi … 7 = dimanche). Null = tous les jours. |
| `age_min` | int | oui | Âge minimum conseillé (1 à 15). |
| `age_max` | int | oui | Âge maximum conseillé (1 à 15 ; 15 = ados et plus). |
| `audience` | enum | oui | `enfant` (l'enfant seul, ex. atelier déposé) · `famille` (parents + enfants) · `ados` (11-15 sans parents) · `amis` (à faire entre copains) |
| `city` | string | oui | Commune (ex. `Rodez`, `Onet-le-Château`). |
| `venue` | string | oui | Nom du lieu (ex. `Musée Soulages`). |
| `address` | string | oui | Adresse postale complète avec code postal. |
| `lat` / `lng` | number | oui | Coordonnées WGS84 (géocodage Nominatim). |
| `price` | string | oui | Texte libre court : `Gratuit`, `5 € / enfant`, `De 8 à 12 €`, `Sur inscription`. |
| `booking_required` | bool | oui | Réservation obligatoire ? |
| `phone` | string ou `null` | non | Numéro de réservation, format `05 65 00 00 00`. |
| `email` | string ou `null` | non | Adresse de contact. |
| `url` | string | oui | Page officielle de l'événement ou du lieu. |
| `booking_url` | string ou `null` | non | Lien de billetterie / inscription. |
| `source` | string | oui | URL de la page où l'info a été trouvée (traçabilité). |
| `source_checked` | `YYYY-MM-DD` | oui | Date de dernière vérification. |
| `tags` | array de string | non | Mots-clés libres : `marionnettes`, `halloween`, `noel`, `gratuit`, `pluie-ok`, `exterieur`, `vacances`... |

## Règles

- Zone : Rodez et un rayon de 20 km (Onet-le-Château, Luc-la-Primaube, Sébazac-Concourès, Olemps, Le Monastère, Sainte-Radegonde, Druelle-Balsac, Baraqueville, Marcillac-Vallon, Bozouls, Laissac, Salles-la-Source, Pont-de-Salars, Flavin, Agen-d'Aveyron, Calmont, Naucelle limite…).
- Public : au moins une tranche d'âge entre 1 et 15 ans.
- Jamais d'événement inventé : chaque entrée a une `source` consultée.
- Un événement récurrent hebdomadaire (ex. bébés lecteurs tous les mercredis) = une entrée avec `date`/`end_date` couvrant la période et `days_of_week`.
- Tri dans l'app : par `time` (les « toute la journée » en premier).
