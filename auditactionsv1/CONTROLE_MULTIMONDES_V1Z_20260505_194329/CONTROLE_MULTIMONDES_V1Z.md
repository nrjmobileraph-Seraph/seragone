# CONTROLE MULTIMONDES V1Z
Date UTC: 2026-05-05T19:43:31Z
Mode: lecture seule, AST parse seulement, aucun import, aucune execution, aucun patch
## Verdicts
- A_REVOIR_HUMAIN: 1
- GARDER_CANON_DORMANT: 79
- NEPASBRANCHER: 13
- TESTER_OFFLINE: 21

## Familles couvertes
- 27D: 5
- 92MONDES: 33
- AUTONOMES: 2
- BORN: 7
- BRAINCHEF: 40
- CHAINES: 2
- COMMUNICANTS: 3
- MULTIVERS: 5
- PARALLELES: 8
- RECURSIFS: 5
- SUBDAILY: 5

## Regle
- NEPASBRANCHER si danger broker/exec/cron/systemd/API ordre detecte.
- GARDER_CANON_DORMANT si module lisible avec states/ecritures mais non qualifie runtime.
- TESTER_OFFLINE si lisible et peu dangereux.
- A_REVOIR_HUMAIN si parse impossible ou ambiguite.

## Prochaine action
Lire le CSV, traiter d'abord NEPASBRANCHER et A_REVOIR_HUMAIN, puis choisir les TESTER_OFFLINE par famille.
