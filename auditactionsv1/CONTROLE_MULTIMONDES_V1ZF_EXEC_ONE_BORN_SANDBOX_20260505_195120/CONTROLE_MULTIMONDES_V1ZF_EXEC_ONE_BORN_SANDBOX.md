# CONTROLE MULTIMONDES V1Z-F EXEC ONE BORN SANDBOX

Date UTC: 2026-05-05T19:51:20+00:00

Mode: execution unique sandbox, timeout, aucun patch, aucun cron, aucun broker, aucun branchement runtime

Script: born_temps_validation.py

Return code: 1

CWD: auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs

## Fichiers sandbox

- Created: []
- Modified: []

## Inputs

- Absolute input exists: True (/home/ubuntu/labo_27d/banc_27d_enrichi_v4.csv)
- Local sandbox input exists: True (auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/inputs/banc_27d_enrichi_v4.csv)

## Stdout tail

```text

```

## Stderr tail

```text
Traceback (most recent call last):
  File "/home/ubuntu/seragone/auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs/born_temps_validation.py", line 16, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

```

## Verdict provisoire

- EXEC_FAIL_SANDBOX: ne pas relancer avant lecture stderr/stdout et chemins attendus.
