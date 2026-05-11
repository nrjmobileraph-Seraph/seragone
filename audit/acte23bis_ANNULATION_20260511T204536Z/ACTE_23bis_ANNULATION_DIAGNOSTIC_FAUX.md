# ACTE 23-bis — ANNULATION de l'acte 23 (diagnostic erroné)

**Date (UTC)** : 2026-05-11T20:45:37Z

## Fait

L'acte 23 a désactivé et masqué `seragone-multivers.service` et son timer
au motif d'un service "dead avec writer cassé".

## Vérité mesurée

Le service est un **ONESHOT** déclenché par timer toutes les 30 min.
"inactive (dead)" est son état **normal** entre deux ticks.
Les logs montrent 5 exécutions successives le 11 mai avec
`status=0/SUCCESS` et ~4 min CPU par run (191 mondes × 8 couches).

## Cause de l'erreur

L'IA (Perplexity) a extrapolé un "writer cassé" à partir des noms de
dossiers `audit/suite6g1_paralleles_fail` → `g5_stop_paralleles` sans
lire leur contenu. Ces dossiers concernaient un AUTRE chantier
(paralléles CSV writer), pas le service multivers.

## Disposition

1. L'acte 23 est **annulé**.
2. Le timer est réactivé (enable + start).
3. Le service reprendra son cycle normal toutes les 30 min.
4. Les fichiers unit n'ont jamais été effacés (mask avait échoué car
   les fichiers existaient déjà — heureux hasard protecteur).

## Leçon gravée

Avant tout `mask`/`disable`/suppression de service, **LIRE LES LOGS
RÉELS** (journalctl) et distinguer oneshot vs daemon. Un oneshot
inactive entre deux ticks est NORMAL.
