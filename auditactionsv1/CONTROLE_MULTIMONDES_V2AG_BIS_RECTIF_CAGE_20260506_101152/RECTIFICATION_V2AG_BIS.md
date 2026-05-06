# V2AG-bis : Rectification cage statique 14 -> 9 fichiers reels

## Contexte

Decoule de la decouverte D1 du precheck Phase 0 V2AH : la cage statique
inscrite a 14 fichiers depuis V1ZW etait incorrecte. Seuls 9 fichiers
sont reellement presents et stables sur le systeme.

## Liste des 9 fichiers reels

1. vrais_yeux.py (sha256 f8de03b6...e5850 - INTOUCHABLE)
2. voix_seragone_92/seragone_92.py
3. voix_seragone_92/seragone_92_chef.py
4. voix_seragone_92/data/regards_brut.json
5. voix_seragone_92/data/regards_clean.json
6. voix_seragone_92/data/regards_chef.json
7. data/born_state.json
8. data/born_temps_state.json
9. data/multivers_state.json

## Fichiers absents historiquement listes

5 entrees du perimetre1.sha256 historique pointaient vers des fichiers
absents du systeme :

- voix_seragone_92/seragone_92_state.json
- voix_seragone_92/data/seragone_92_state.json
- 3 autres references a des etats jamais persistes sous ces noms exacts

## Sortie de communicants_history.json du perimetre P1

data/communicants_history.json etait dans certains perimetres P1 mais est
modifie en continu par le runtime (decouverte D2 V2AH Phase 0 : hash
4a8fca11 -> 707c8e96 entre V2AC et V2AH Phase 0).

DECISION : sortir de P1 (cage statique vraie).
- Si suivi necessaire : deplacer en P2 (dynamique trace) ou P3 (libre).

## Decision opposable

A partir de cette rectification, toute future chaine d'audit doit utiliser
le fichier perimetre_p1_reel_9fichiers.sha256 comme reference du perimetre P1.
Les inscriptions "14 fichiers" anterieures sont SUPERSEDEES par cette
rectification documentaire.

## Verdict

V2AG_BIS_RECTIF_CAGE_OK_9_REELS_INSCRITS
