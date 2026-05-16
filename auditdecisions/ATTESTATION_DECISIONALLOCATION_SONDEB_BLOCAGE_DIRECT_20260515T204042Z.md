# ATTESTATION DECISIONALLOCATION SONDE B - BLOCAGE BRANCHEMENT DIRECT

Date UTC: 20260515T204042Z

## Source
- SONDEFROIDE_DECISIONALLOCATION_V1_20260515T203830Z
- SONDEB_BLOQUEURS_DECISIONALLOCATION_20260515T203947Z
- CONTRATORCHESTRATEURDEMOV12026-05-132330VALIDATED
- DECRETA73SEMANTIQUENEUTRALPOSITIONDEMO2026-05-15

## Constat
La sonde froide DECISIONALLOCATION a lu 42 fichiers.
La sonde B a qualifié 9 bloqueurs.

Verdicts mécaniques:
- aplomb.py: WRITE_LEGACY_REEL_OU_PROBABLE
- demo/generator/decision_to_order.py: RISQUE_REEL_A_ISOLER
- demo/prudence/prudence_demo.py: RISQUE_REEL_A_ISOLER
- demo/reports/RACCORDEMENT_CHAINE_REELLE_VERS_DEMO_20260507_211559/grep_ordre_execution_broker_head2000.txt: RISQUE_REEL_A_ISOLER
- doubletempo.py: WRITE_LEGACY_REEL_OU_PROBABLE
- money_manager.py: RISQUE_REEL_A_ISOLER
- money_manager_perplexity_97L.py: WRITE_LEGACY_REEL_OU_PROBABLE
- prudence_module.py: WRITE_LEGACY_REEL_OU_PROBABLE
- tireur_aplomb.py: WRITE_LEGACY_REEL_OU_PROBABLE

## Décision documentaire
Le branchement direct de DECISIONALLOCATION sur les fichiers legacy sondés est interdit.

Les fichiers RISQUE_REEL_A_ISOLER sont exclus de tout branchement démo direct.

Les fichiers WRITE_LEGACY_REEL_OU_PROBABLE ne peuvent être utilisés qu'après création et validation séparée de wrappers purs, sans write legacy, sans import caché dangereux, sans exchange, sans cron et sans effet runtime.

## Compatibilité contrat V1
Le contrat V1 exige:
- modules traités comme calculateurs
- orchestrateurdemo seul writer
- writes uniquement dans statesv1
- aucun write legacy
- aucun exchange
- aucun runtime automatique

Les résultats de Sonde B ne satisfont pas encore ces conditions pour les 9 bloqueurs.

## Statut A7.3
La sémantique TARGETFLAT / CLOSETOFLAT reste HOLDREADONLY.
Aucune clôture, aucun ordre, aucun patch decisiontoorder.py, aucun patch demobroker.py.

## Interdits
- Aucun ordre réel
- Aucune finance réelle
- Aucun patch runtime
- Aucun cron modifié
- Aucun service relancé
- Aucun branchement automatique
- Aucun write legacy
- Aucun module legacy appelé comme producteur direct

## Suite autorisée
Produire une matrice de wrappers purs candidats.
Chaque wrapper devra être sondé séparément avant tout décret de branchement.
