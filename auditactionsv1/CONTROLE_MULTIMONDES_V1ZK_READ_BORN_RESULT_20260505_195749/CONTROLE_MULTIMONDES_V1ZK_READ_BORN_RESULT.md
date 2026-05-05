# CONTROLE MULTIMONDES V1Z-K READ BORN RESULT

Date UTC: 2026-05-05T19:57:49+00:00

Mode: lecture run_report V1ZJ uniquement, aucune execution BORN, aucun patch, aucun cron, aucun broker

## Source

- Source report: auditactionsv1/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK_20260505_195442/run_report.json
- Return code V1ZJ: 0
- Stderr empty: True
- Created files sandbox: []
- Modified files sandbox: []

## Extraction tail stdout

- Born lines parsed in tail: 64
- Valid markers V in tail: 54
- Invalid markers X in tail: 10

## Cycles detectes dans tail

| Cycle | Rows tail | V | X |
|---|---:|---:|---:|
| Cycle 3 | 43 | 38 | 5 |
| Cycle 4 | 7 | 5 | 2 |
| Cycle 5 | 14 | 11 | 3 |

## Overlap provinces existantes

- Cycle 3 : Born=106j, Portance~=421j, overlap=33j, Jaccard=0.07
- Cycle 4 : Born=83j, Portance~=432j, overlap=27j, Jaccard=0.06
- Cycle 5 : Born=87j, Portance~=217j, overlap=22j, Jaccard=0.08

## Verdict lecture

- V1ZJ_EXEC_OK_CONFIRME: execution sandbox terminee sans stderr et sans fichiers declares crees/modifies.
- V1ZK_LIMITATION: analyse fondee sur stdout_tail seulement; ne pas extrapoler au stdout complet absent du rapport.
- NEXT_SAFE_STEP: commit V1ZK puis decider si capture stdout complet necessaire avant autres scripts.
