# CONTROLE MULTIMONDES V1Z-T — PHASE 2 EXEC BORN FULL LOG

Date UTC: 2026-05-05T21:49:24Z

Mode : execution born_temps_validation.py dans sandbox V1ZR-bis. Phase 115 preservee. decision_weight=0.0. vrais_yeux.py INTOUCHABLE.

## 1. Verdict

V1ZT_PHASE2_OK

## 2. Resultats execution

- Exit code : 0
- Duree : 44s
- Timeout : 60s (fidelite V1ZJ)
- stdout_full.log : 7997 octets, 140 lignes
- stderr_full.log : 0 octets, 0 lignes

## 3. Cibles

- REEXEC : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351`
- SANDBOX : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351/sandbox_born_full_log`
- AUDIT : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZT_PHASE2_EXEC_BORN_20260505_214840`

## 4. Ancrages Git

- V1ZQ decret : 72f9b18f
- V1ZQ-bis amendement : 03fd4c75
- V1ZS archive accident : 9b41951f
- V1ZR-bis preparation Phase 1 : e759ab84
- HEAD au lancement : `e759ab84c15126c803fcd49f8da95d6611c3d4c6`

## 5. Durcissements appliques

- #1 sha256(script) = d9acb122719206a370f1058254d1cfc6b51d3586cce1d379426915c2bac1367d verifie
- #2 sha256(sitecustomize) = 9abaa362fcb7b78eb2f2e933794a3df9e8413012a9edf3b212f9ae0298d0fedf verifie
- #3 hash caches live JUSTE AVANT et JUSTE APRES exec
- #4 phase2_signed.txt verifie en premiere ligne
- CSV input sha256 = 6850e7f0bb0673498c5db86910570dcf3f6dccb098422c8fd51754f1803ab634 verifie

## 6. Attestation non-pollution

- Diff caches live avant/apres exec : vide (sha256 e3b0c442... = empty)
- POLLUTION : 0

## 7. Comparaison fidelite V1ZJ

Voir section V1ZT.8 dans la sortie console.

## 8. Interdits maintenus

Aucun ordre exchange. Aucun broker. Aucun cron edite. Aucun systemd modifie. Aucune sortie Phase 115. Aucune ecriture caches live au-dela des lectures pandas via sitecustomize redirect. vrais_yeux.py INTOUCHABLE.
