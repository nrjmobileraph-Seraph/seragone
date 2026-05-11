# RAPPORT A7 END-TO-END — 2026-05-11

## Statut

PIPELINE_A7_OPERATIONNEL_EN_MODE_DEMO_TOTAL.

## Chaîne démontrée

| Étape | Cron | Horodatage UTC | Artefact |
|---|---|---|---|
| Injection reset hash | manuel | 20:54:37 | decision_to_order_state.json |
| Générateur A7 | * * * * * | 20:55:02 | AUTO_A7_20260511T205502.json |
| Prudence runner | * * * * * | 20:56:01 | prudence PASS + archivage processed/ |
| Demobroker | * * * * * | 20:57 | DEMO_EXEC_ccd1b550a4d7.json |

## Preuves jointes (dans audit/acte25_A7_ENDTOEND_DEMONTRE_20260511T205953Z/)

- 01_ordre_genere.json
- 02_prudence_state.json
- 03_execution.json
- 04_statedemo_final.json
- 05_syslog_cron_declenche.log

## Garde-fous respectés (DECRET_A7 §7.2)

- real_finance_allowed : false
- real_finance_used : false
- exchange_reel : false
- ordres_internes_autorises : true

## Conclusion

Pipeline A7 conforme à DECRET_A7 (sha256 543dcb9b20c82b8f…),
opérationnel en production VPS avec 3 crons minute, idempotent,
traçable hash-to-hash, réactif sous 3 minutes de bout en bout.
