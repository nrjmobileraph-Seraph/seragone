# CONTROLE MULTIMONDES V1Z-B ACTIVE PATHS

Date UTC: 2026-05-05T19:44:17+00:00

Source: V1Z 20260505_194329

Mode: filtrage CSV seulement, aucune lecture script, aucune execution, aucun patch

## Verdicts

- A_REVOIR_HUMAIN: 1
- GARDER_CANON_DORMANT: 53
- NEPASBRANCHER: 11
- TESTER_OFFLINE: 20

## Familles

- 27D: 5 (GARDER_CANON_DORMANT=3, TESTER_OFFLINE=2)
- 92MONDES: 33 (GARDER_CANON_DORMANT=25, NEPASBRANCHER=1, TESTER_OFFLINE=7)
- AUTONOMES: 2 (GARDER_CANON_DORMANT=2)
- BORN: 7 (GARDER_CANON_DORMANT=2, TESTER_OFFLINE=5)
- BRAINCHEF: 12 (GARDER_CANON_DORMANT=6, NEPASBRANCHER=6)
- CHAINES: 2 (GARDER_CANON_DORMANT=1, NEPASBRANCHER=1)
- COMMUNICANTS: 3 (GARDER_CANON_DORMANT=3)
- MULTIVERS: 4 (GARDER_CANON_DORMANT=2, TESTER_OFFLINE=2)
- PARALLELES: 8 (A_REVOIR_HUMAIN=1, GARDER_CANON_DORMANT=4, TESTER_OFFLINE=3)
- RECURSIFS: 5 (GARDER_CANON_DORMANT=4, NEPASBRANCHER=1)
- SUBDAILY: 5 (GARDER_CANON_DORMANT=2, NEPASBRANCHER=2, TESTER_OFFLINE=1)

## A traiter avant tests

- NEPASBRANCHER | CHAINES | phase55_selection_chaines_shadow.py | dangers=binance
- NEPASBRANCHER | BRAINCHEF | production/moteurs/seragone_brain.py | dangers=binance
- NEPASBRANCHER | BRAINCHEF | production/moteurs/seragone_brain_cwt.py | dangers=ORDER
- NEPASBRANCHER | SUBDAILY | production/orchestration/subdaily_runner.py | dangers=ORDER|binance
- NEPASBRANCHER | RECURSIFS | recursif_v1_signal.py | dangers=Kraken|Pionex
- NEPASBRANCHER | BRAINCHEF | seragone_brain.py | dangers=binance
- NEPASBRANCHER | BRAINCHEF | seragone_brain_cwt.py | dangers=ORDER
- NEPASBRANCHER | BRAINCHEF | seragone_brain_v2.py | dangers=Binance
- NEPASBRANCHER | BRAINCHEF | seragone_brain_v3.py | dangers=order
- NEPASBRANCHER | SUBDAILY | subdaily_runner.py | dangers=ORDER|binance
- A_REVOIR_HUMAIN | PARALLELES | t_import_mondes_paralleles.py | dangers=
- NEPASBRANCHER | 92MONDES | voix_seragone_92/diag_nouveaux_modules.py | dangers=Binance|binance

## Testables offline candidats

- BORN | backtest_born.py
- BORN | born_local.py
- BORN | born_recalibre.py
- BORN | born_temps_validation.py
- PARALLELES | mondes_paralleles_engine_v4_canon.py
- PARALLELES | mondesparallelesengine.py
- MULTIVERS | multivers_v2.py
- MULTIVERS | production/mondes/multivers_v2.py
- BORN | research/backtest_born.py
- 27D | research/test_27d_4approches.py
- 27D | test_27d_4approches.py
- PARALLELES | test_import_mondes_paralleles.py
- 92MONDES | voix_seragone_92/adapter_seragone_92.py
- 92MONDES | voix_seragone_92/diag_avril_2024.py
- 92MONDES | voix_seragone_92/diag_nc_engine_labels.py
- 92MONDES | voix_seragone_92/diag_nc_vs_V9.py
- 92MONDES | voix_seragone_92/simulation_finale_v9_seragone_guardian.py
- 92MONDES | voix_seragone_92/test_regle_v2G.py
- 92MONDES | voix_seragone_92/test_v2G_fenetres.py
- SUBDAILY | vrais_yeux_subdaily.py

## Regle

- Rien ne devient runtime depuis cette passe.
- Les NEPASBRANCHER sont geles tant qu'une preuve d'absence broker/ordre n'est pas faite.
- Les TESTER_OFFLINE peuvent seulement tourner sur copies de donnees, sans cle API, sans cron, sans systemd.
