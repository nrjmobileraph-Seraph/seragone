
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
