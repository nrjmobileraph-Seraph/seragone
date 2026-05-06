# DECRET V2AD - TROIS CAGES, SIX DAEMONS, PLAN AUDIT TRANSVERSE

Decret PLAN_ONLY documentaire pur. Aucune execution, aucune mutation.

## I. INCIDENT TOKEN GITHUB (RESOLU)
6 mai 2026 08:19 UTC : V2AC' revele PAT en clair dans /tmp/push_bulletin.sh, cron actif depuis 15 avril 19:50 UTC.
Resolution Raphael 08:30 UTC : revocation, regeneration, /home/ubuntu/.github_token mode 600, patch script lecture dynamique. Verification : commit e891e9ff 10:31:02+0200 = nouveau token operationnel. SETUP=B_SECURE.
Reste : /tmp/push_bulletin.sh.bak.20260506_083001 contient ancien token revoque, a supprimer.

## II. TROIS CAGES
- Cage statique : 14 fichiers source verrouilles sha256 (V2AB perimetre 1)
- Cage runtime : aucun process Seragone, aucun cron, aucun timer, aucun handle write
- Cage Git : repo immuable hors chaine d'audit explicite

## III. ETAT MESURE 6 MAI 08:30 UTC
- Statique VRAIE : V2AC DIFF_P1_BYTES=0
- Runtime FAUSSE : V2AC 6 daemons up, timer 35j, 81 crons, 25 lsof writes
- Git FAUSSE : V2AC' 16091 autos, 497 depuis V2AA

Cage statique vraie : 9 manifests V1ZW->V2AA mecaniquement corrects.
Cage runtime fausse : formule LIVE_TEST_TOTAL_EN_CAGE repetee 9 fois etait non sourcee. Rectifier en addendum.
Cage Git fausse : nouvelle dimension, pas de rectification anterieure a faire.

## IV. CLASSIFICATION 6 DAEMONS
PID 828204  seragone_brain.py                  17j     LIVE_PRODUCTIF_INTOUCHABLE
PID 1208322 collecteur_1min.py                 12j     LIVE_PRODUCTIF_INTOUCHABLE
PID 1593923 production/protection/brisance.py  8j14h   OBSERVATION_TOLEREE
PID 1759106 production/execution/api.py        4j23h   A_AUDITER_PROFOND
PID 1980868 sentinelle_seragone.py             1j      OBSERVATION_TOLEREE
PID 1980869 securite_seragone.py               1j      OBSERVATION_TOLEREE

## V. PLAN V2AE - AUDIT PRODUCTION/EXECUTION/API.PY
Lecture seule pure : cat source, sha256, lsof -p 1759106, ss -tlnp, AST imports broker, grep mots-cles execution, verification reseau exchange.
Verdicts : PASSIF_LOCAL / PASSIF_DASHBOARD / ACTIF_DRY_RUN / ACTIF_LIVE_KRAKEN / ACTIF_LIVE_AUTRE (DANGER_CRITIQUE) / INDETERMINE.

## VI. REGLES CHANTIER 6 VILLAGE (V2AI futur)
1. Cage statique stricte 14 fichiers Village V2AB
2. Cage runtime NON appliquee
3. Cage Git suit regles V2AF
4. Doublon village_le_vrai.py vs village_le_vrai_vps.py : trancher par cross-imports runtime
5. Si production/execution/api.py reclassifie DANGER, V2AI bloque

## VII. PLAN ADDENDUM RECTIFICATION (V2AG futur)
Rectifie formule "Phase 115 LIVE_TEST_TOTAL_EN_CAGE preservee" -> "LIVE_TEST_AUDIT_STATIQUE_DANS_RUNTIME_ACTIF preservee" dans 9 manifests V1ZW->V2AA. Ne mute PAS les commits anciens.

## VIII. PLAN RECONCILIATION GIT (V2AH futur)
git pull --no-rebase origin main (merge commit honnete). Puis commit V2AC/V2AC'/V2AD/V2AE/V2AF/addendum, push.

## IX. SEQUENCEMENT
V2AD (now) -> V2AE -> V2AF -> V2AG_ADDENDUM_RECTIF -> V2AH_RECONCIL_GIT -> V2AI_CHANTIER6_VILLAGE

## X. ATTESTATIONS
Aucune mutation. HEAD 782a6f70 ancre. vrais_yeux.py sha256 f8de03b6...e5850 inchange. 9 ancetres 27D OK.
VERDICT=V2AD_DECRET_3_CAGES_OK
