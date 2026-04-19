
## Lot B — Macro / On-chain daily
Date de figement : 2026-04-19
Statut : VALIDÉ PARTIELLEMENT
Résultat : 17/18 fichiers OK
Exception : data/fear_greed.csv en quarantaine temporaire

### Fichiers validés
- data/M2SL.csv
- data/btc_active_addresses.csv
- data/btc_difficulty_daily.csv
- data/btc_hashrate_daily.csv
- data/btc_transactions_daily.csv
- data/contagion_daily.csv
- data/exogene_daily.csv
- data/funding_rate_btc.csv
- data/binance_oi_btcusdt_daily.csv
- data/binance_taker_buysell_daily.csv
- data/onchain/exchange_netflow.csv
- data/onchain/funding_rate.csv
- data/onchain/mvrv.csv
- data/onchain/nupl.csv
- data/onchain/open_interest.csv
- data/onchain/puell_multiple.csv
- data/onchain/whale_ratio.csv

### Fichier exclu temporairement
- data/fear_greed.csv

### Motif d'exclusion
Absence de schéma temporel canonique détecté automatiquement ; normalisation requise avant intégration au chargement canonique.

### Référence audit
- scripts/validators/validate_lot_b_v2.py
- output/lot_b_audit_v2.json

### Mise à jour 2026-04-19
Le fichier data/fear_greed.csv a été reconstruit au format canonique :
date,value,classification,timestamp

Résultat :
- Lot B validé complètement
- 18/18 fichiers OK
- Référence audit : output/lot_b_audit_v2.json

## Lot C — Intraday / microstructure
Date de figement : 2026-04-19
Statut : VALIDÉ COMPLÈTEMENT
Résultat : 11/11 fichiers OK

### Correctif appliqué
- Nettoyage des octets nuls dans data/trades_btcusdt_2026-03-30.csv
- Sauvegarde conservée : data/trades_btcusdt_2026-03-30.csv.bak_nul

### Référence audit
- scripts/validators/validate_lot_c_v1.py
- output/lot_c_audit_v1.json

## Lot D — Depth / Trades multi-jours
Date de figement : 2026-04-19
Statut : VALIDÉ COMPLÈTEMENT
Résultat : 15/15 fichiers OK

### Correctif appliqué
- Alignement du validateur sur le schéma réel des fichiers depth :
  timestamp,best_bid,best_bid_qty,bid_vol_total,best_ask,best_ask_qty,ask_vol_total,spread,imbalance,bids_json,asks_json

### Référence audit
- scripts/validators/validate_lot_d_v2.py
- output/lot_d_audit_v2.json

## Lot E — États, caches et mémoire moteur
Date de figement : 2026-04-19
Statut : VALIDÉ
Résultat : aucun blocage immédiat détecté

### Points constatés
- communicants_history.json : liste de 500 items
- mondes_paralleles_cache.json : dict de 305 clés
- phi_local_20m.json : dict de 20 clés
- phi_local_100m.json : dict de 100 clés
- phi_local_500m.json : dict de 500 clés
- mondes_paralleles_history.csv : 22 lignes de données, header cohérent

## Lot F — Mondes, chaînes et corpus canoniques
Date de figement : 2026-04-19
Statut : VALIDÉ COMPLÈTEMENT
Résultat : 32/32 fichiers OK

### Référence audit
- scripts/validators/validate_lot_f_v1.py
- output/lot_f_audit_v1.json

## Lot G — Reliquats techniques, backups et redondances
Date de figement : 2026-04-19
Statut : CLASSÉ PROPREMENT
Résultat : périmètre entièrement catégorisé

### Règle de lecture
- ACTIVE_CANON = source vivante utile au moteur
- BACKUP_ONLY = sauvegarde saine à conserver
- REDONDANT = doublon utile mais non prioritaire
- TECHNICAL_ARTIFACT = sortie intermédiaire / dérivée / calcul technique
- TO_ARCHIVE = ancien fichier contaminé ou obsolète à sortir du flux actif

## Clôture globale dataset — 20260419T154059Z
- Manifest : output/global_manifest.json (137 entrées)
- Snapshot : output/global_manifest_20260419T154059Z.json
- Orphelins : 0 (output/orphans_report_20260419T154059Z.json)
- Répartition lots : B=53, C=4, D=23, E=10, F=33, G=14
- Classifications : ACTIVE_CANON=80, BACKUP_ONLY=30, TECHNICAL_ARTIFACT=16, REDONDANT=9, TO_ARCHIVE=2
- Politique : B/C/D/F=ACTIVE_CANON par défaut, E=TECHNICAL_ARTIFACT, G en dur
- Scripts : scripts/validators/build_global_manifest.py (+ HARDCODED_INVENTORY)

### Ancre cryptographique du gel 20260419T154059Z
- commit git : e1d17b4e9f613289e8916a4501849297954bfd3a
- tag        : dataset-freeze-20260419T154059Z
- sha256     : fda2fa7250714fc9adcc48a19f9599ae212af59959a72aad38b87e5fc855058d  output/global_manifest_20260419T154059Z.json

## Clôture globale v2 — 20260419T154642Z
- Manifest : output/global_manifest.json (137 entrées, Lot A inclus)
- Snapshot : output/global_manifest_20260419T154642Z.json
- sha256 snapshot : 6e1626a1b8e5f68d33fcac05c88d71fdd7b6cc61845e853f738a887ebf137f72
- Orphelins : 0
- Répartition lots : A=3, B=52, C=11, D=21, E=10, F=33, G=7
- Classifications : ACTIVE_CANON=93, BACKUP_ONLY=30, TO_ARCHIVE=2, TECHNICAL_ARTIFACT=11, REDONDANT=1
- Corrections v2 :
  * intégration audit Lot A (output/lot_a_audit.json)
  * intégration audit Lot C v1 (output/lot_c_audit_v1.json)
  * normalisation des paths nus en data/<file>
  * suppression des doublons hardcoded couverts par les audits
- Note Lot F : les 8 chain_F*.csv bruts restent ACTIVE_CANON conformément à lot_f_audit_v1.json validé.

## Cleanup — 20260419T154908Z
- Tag : dataset-cleanup-20260419T154908Z (commit b668ff4)
- 17 BACKUP_ONLY hash-identiques au canon supprimés du disque et du script
- Manifest : 120 entrées, 0 orphelin
- Répartition lots : A=3, B=35, C=11, D=21, E=10, F=33, G=7
- Classifications : ACTIVE_CANON=93, BACKUP_ONLY=13, TO_ARCHIVE=2, TECHNICAL_ARTIFACT=11, REDONDANT=1
- sha256 snapshot : 93aa19720f0852ce3b635011078a9fc90957bc788403a6fefe3c72d29639dfb2
- Ancre : output/global_manifest_20260419T154908Z.json
- .gitignore renforcé (racine projet non triée, backups/, logs/, modeles_V13_*/, app_cockpit_v*.py, deepseek_python_*.py, *.bak*, etc.)


## Audit Lot E réel — 20260419T164732Z
- Source : audit GPT, 11/11 OK, 0 FAIL, 0 INSPECT
- Fichier : output/lot_e_audit.json (11 entrées TECHNICAL_ARTIFACT)
- Manifest : 120 entrées, 0 orphelin (by_lot.E=11)
- sha256 snapshot : 612f58d90ae3290bb2e20222d8696237ddb616fb4973d6b6bb1284b1145462c3
- Ancre : output/global_manifest_20260419T154656Z.json
- Tag : lot-e-audit-20260419T164732Z
- Remplace l'injection HARDCODED_INVENTORY par la source audit
