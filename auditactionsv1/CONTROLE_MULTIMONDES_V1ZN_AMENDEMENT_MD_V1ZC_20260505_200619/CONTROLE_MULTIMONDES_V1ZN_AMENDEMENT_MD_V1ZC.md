# AMENDEMENT NOMINAL V1Z-N — REENONCIATION DES 6 REGLES TRANSVERSALES V1ZC

Date UTC: 2026-05-05T20:06:19+00:00

Mode: amendement documentaire nominal, lecture seule absolue sur le V1ZC canon, aucune execution, aucun patch, aucun cron, aucun broker, Phase 115 preservee.

## 0. Pourquoi cet amendement

V1ZM a etabli mecaniquement que le MD V1ZC canon present sur le VPS ne reenonce pas explicitement les 6 regles transversales du cadre Seragone (tableau §3 du V1ZM : 6 x MANQUE).

Ces regles existent dans le cadre doctrinal amont (Doc 20 §10, Doc 26 §3, skill seragone-canon) et sont compressees dans la colonne interdits du CSV V1ZC ligne par script (`broker/api/ordre/cron/systemd/runtime/state racine/cle api`).

Cet amendement est purement **nominal** au sens du Doc 20 §8 : il ajoute, il n efface rien, il ne modifie ni le CSV ni le MD V1ZC originaux.

Fonction unique : eviter que la prochaine IA lise le tableau §3 du V1ZM comme absence de doctrine, alors que les interdits sont actifs au niveau ligne CSV et dans le cadre canon amont.

## 1. Ancrage mecanique sur le V1ZC canon

- Dossier V1ZC canon : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZC_OFFLINE_TEST_PLAN_20260505_194728`
- MD V1ZC  : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZC_OFFLINE_TEST_PLAN_20260505_194728/CONTROLE_MULTIMONDES_V1ZC_OFFLINE_TEST_PLAN.md` size=5550  sha256=`12c1faeb662ebd03767d013f16a3d913be9cf4bf76e4f0a816ed7133641716ae`
- CSV V1ZC : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZC_OFFLINE_TEST_PLAN_20260505_194728/controle_multimondes_v1zc_offline_test_plan.csv` size=10619 sha256=`996331d7a7a96fbc499a86cb26ac21473e1ac0477f13b75538d58424770e1c77`

Si l un de ces sha256 evolue ulterieurement, cet amendement reste ancre au point fige ci-dessus.

- V1ZM associe : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZM_CROSSCHECK_CORRIGE_V1ZC_V1ZJ_V1ZK_20260505_200220/CONTROLE_MULTIMONDES_V1ZM_CROSSCHECK_CORRIGE_V1ZC_V1ZJ_V1ZK.md` sha256=`6cf159b3c582587ed6a724fc1776f4542ea1bf209a4c74d9f3eccb90b94f46b7`

## 2. Les 6 regles transversales reenoncees

### 2.1 Phase 115 LIVE_TEST_TOTAL_EN_CAGE
Le systeme reste en Phase 115. Aucune sortie sans validation explicite Raphael apres audit complet (Doc 20 §10.3).

### 2.2 decision_weight = 0.0
Poids de decision a zero dans tous les chemins live. Observatoire pur (Doc 20 preambule, skill canon §Constantes).

### 2.3 Aucun broker / aucun ordre exchange
Aucune cle API broker activee. Cible Kraken paper exclusivement (skill canon §Constantes, Doc 26 §11).

### 2.4 Aucun cron / aucun systemd modifie
Aucun crontab edite, aucun service redemarre, aucune unite systemd ajoutee/modifiee/desactivee (Doc 26 §3 et §11).

### 2.5 Aucune ecriture dans les caches live
Les 3 caches mondes_paralleles_cache.json (data/, cache/, production/mondes/data/), born_state.json, multivers states, communicants_history.json et states 92mondes restent intouches. Toute reproduction passe par sandbox isolee (Doc 26 §5).

### 2.6 vrais_yeux.py INTOUCHABLE
Module vrais_yeux.py (558 lignes, 22 equations canon, fige 16/04/2026) intouchable. Phi*_CANON et W_CANON figes (Doc 20 §10.1, skill canon §Modules INTOUCHABLES).

## 3. Statut canonique de cet amendement

- Type : amendement nominal (pattern Doc 20 §8 : on ajoute, on n efface rien)
- Effet sur V1ZC canon : zero. CSV et MD `..._194728/` inchanges.
- Effet runtime : zero. Aucun script lance, aucun fichier modifie hors `auditactionsv1/`.
- Lecture pour la prochaine IA : a lire conjointement avec le V1ZC canon ; tableau §3 du V1ZM = absence de reennonciation textuelle dans le MD V1ZC, pas absence de cadre.

## 4. Verdict V1ZN

- V1ZN_AMENDEMENT_NOMINAL_OK : 6 regles reenoncees, ancrage mecanique sha256 sur V1ZC canon.
- V1ZN_SECURITE : aucune execution, aucun patch, aucun cron, aucun broker, aucune sortie Phase 115, aucune ecriture caches live, vrais_yeux.py INTOUCHABLE.
- V1ZN_SUITE : arbitrage humain libre (capture stdout BORN complet, autre script PRET_SANDBOX, ou pause).

---

Aucun fichier runtime modifie. Aucun fichier du V1ZC canon modifie. Phase 115 preservee. decision_weight reste a 0.0.
