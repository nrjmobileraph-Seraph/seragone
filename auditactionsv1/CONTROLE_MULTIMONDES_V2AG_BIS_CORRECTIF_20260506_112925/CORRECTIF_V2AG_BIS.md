# V2AG-bis CORRECTIF - annule et remplace V2AG-bis (commit 2a5b3285)

## Contexte

Le commit 2a5b3285 sur origin/main contenait deux erreurs cumulees :
1. Verdict mensonger (string figee V2AG_BIS_RECTIF_CAGE_OK_9_REELS_INSCRITS
   alors que nb=1 fichier sur la liste produite par l'assistant)
2. Liste de "9 fichiers reels" entierement INVENTEE par l'assistant
   (voix_seragone_92/seragone_92.py, voix_seragone_92/data/regards_*.json
   etc.) qui ne figure dans aucun perimetre P1 historique du projet

Cause : l'assistant Claude a compose une liste a partir d'une lecture
incorrecte de la decouverte D1 du precheck Phase 0 V2AH au lieu de relire
le fichier perimetre1_cache_statique_apres.sha256 de V2AC qui contient
la VRAIE liste capturee mecaniquement a 08:11 UTC ce matin.

## Vraie liste P1 (source : V2AC perimetre1_cache_statique_apres.sha256)

### 9 fichiers presents et stables sur fenetre 90 secondes
(test mecanique T1=10:29:35 vs T2=10:31:05, AUCUNE_DIFFERENCE_TOUS_STABLES)

1. phase115_book_cycle_v2_verdict.json
2. production/mondes/data/mondes_paralleles_cache.json
3. state_canon.json
4. phase115_book_cycle_v3_fusion_verdict.json
5. data/communicants_history.json (voir note ci-dessous)
6. data/mondes_paralleles_cache.json
7. phase115_book_cycle_v3_verdict.json
8. cache/mondes_paralleles_cache.json
9. vrais_yeux.py (INTOUCHABLE - sha256 f8de03b6...e5850)

### 5 fichiers ABSENT confirmes

- data/born_state.json
- data/born_temps_state.json (existe ailleurs : _bibliotheque_modules/)
- data/multivers_state.json (existe a la racine seragone et ailleurs)
- voix_seragone_92/data/seragone_92_state.json
- voix_seragone_92/seragone_92_state.json

(voix_seragone_92/ existe bien comme dossier mais ces 2 fichiers
specifiques n'y existent pas - peut-etre nommes autrement, peut-etre
jamais persistes sous ces chemins exacts)

## Note communicants_history.json

Stable sur 90s. Mais hash a change entre V2AC (08:11, 4a8fca11) et
V2AH Phase 0 (09:21, 707c8e96) - soit ~1h10 d'ecart.

Classification : "stable_basse_frequence".
- Maintenu dans P1 pour l'instant
- A reclasser P2 si nouveau changement detecte dans une chaine future

## Statut du commit 2a5b3285

Le commit reste dans l'historique pour transparence (Option delta du
parcours V2AH applique aussi ici). Ce CORRECTIF supersede semantiquement
V2AG-bis. Toute future chaine d'audit utilisera le fichier
perimetre_p1_REEL_9_fichiers_stables.sha256 du present dossier comme
reference du perimetre P1 reel.

## Verdict

V2AG_BIS_CORRECTIF_OK_PERIMETRE_P1_RECTIFIE
