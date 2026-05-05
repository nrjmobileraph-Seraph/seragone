# CONTROLE MULTIMONDES V1Z-D SANDBOX PRECHECK BORN

Date UTC: 2026-05-05T19:48:46+00:00

Mode: precheck sandbox seulement, copie de scripts/inputs, aucune execution, aucun import, aucun patch

Source: auditactionsv1/CONTROLE_MULTIMONDES_V1ZC_OFFLINE_TEST_PLAN_20260505_194728/controle_multimondes_v1zc_offline_test_plan.csv

Sandbox: auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs

## Bilan

- INPUT_PRET_COPIE: 2
- SCRIPT_PRET_COPIE: 5
- Sandbox prete pour test manuel ulterieur: True

## Scripts BORN copies

- SCRIPT_PRET_COPIE | backtest_born.py | size=10897 | sha256=50ad513dd33e093935c0ced9a3564568145f20fbc9c10ca9e7618fcf8ba8c14b
- SCRIPT_PRET_COPIE | born_local.py | size=10086 | sha256=f7bc2b3ecaead4c3d94bb8091f1e1371117832c71b9c3bc43bfb3d4e138029c7
- SCRIPT_PRET_COPIE | born_recalibre.py | size=11295 | sha256=f818824c2284b8f991f69538c8ef78191c8dea65fc4fdf58b135db4eeb97ff70
- SCRIPT_PRET_COPIE | born_temps_validation.py | size=9401 | sha256=d9acb122719206a370f1058254d1cfc6b51d3586cce1d379426915c2bac1367d
- SCRIPT_PRET_COPIE | research/backtest_born.py | size=10897 | sha256=50ad513dd33e093935c0ced9a3564568145f20fbc9c10ca9e7618fcf8ba8c14b

## Inputs copies

- INPUT_PRET_COPIE | banc_27d_enrichi_v4.csv | size=5020673 | sha256=6850e7f0bb0673498c5db86910570dcf3f6dccb098422c8fd51754f1803ab634
- INPUT_PRET_COPIE | seragone_v3_final.csv | size=399265 | sha256=18320500a19a9b9d3d4840bbafe524865705201a0806bfd0f32c3ec5eb14c655

## Interdits

- Ne pas executer les scripts depuis cette passe.
- Ne pas ecrire dans la racine runtime.
- Toute execution future doit se faire depuis la sandbox, sur copies, avec inspection prealable des scripts copies.
