# CONTROLE MULTIMONDES V1Z-E READ SANDBOX BORN

Date UTC: 2026-05-05T19:50:28+00:00

Mode: lecture AST sandbox seulement, aucun import, aucune execution, aucun patch

Source sandbox: auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs

## Bilan

- CANDIDAT_EXECUTION_OFFLINE: 4
- Premier candidat propose: born_temps_validation.py

## Scripts lus

- CANDIDAT_EXECUTION_OFFLINE | backtest_born.py | csv=seragone_v3_final.csv | writes=- | danger=-
- CANDIDAT_EXECUTION_OFFLINE | born_local.py | csv=seragone_v3_final.csv | writes=- | danger=-
- CANDIDAT_EXECUTION_OFFLINE | born_recalibre.py | csv=seragone_v3_final.csv | writes=- | danger=-
- CANDIDAT_EXECUTION_OFFLINE | born_temps_validation.py | csv=/home/ubuntu/labo_27d/banc_27d_enrichi_v4.csv | writes=- | danger=-

## Decision

- Prochaine passe possible: V1ZF_EXEC_ONE_BORN_SANDBOX sur born_temps_validation.py, avec cwd sandbox/outputs et copies inputs seulement.

## Interdits

- Ne pas executer depuis la racine du repo.
- Ne pas ecrire dans state racine ou fichiers runtime.
- Ne pas activer cron, systemd, broker, cle API ou reseau.
