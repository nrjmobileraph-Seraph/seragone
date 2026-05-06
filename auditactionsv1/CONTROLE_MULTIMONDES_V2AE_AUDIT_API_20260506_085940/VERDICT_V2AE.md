# V2AE AUDIT API PROFOND

Lecture seule pure. Aucun kill. Aucune execution / import de l'api.
Aucun curl/wget/nc. Cage statique preservee.

## Cible
- PID: 1759106
- Source: /home/ubuntu/seragone/production/execution/api.py
- Reference decret: auditactionsv1/CONTROLE_MULTIMONDES_V2AD_DECRET_3_CAGES_20260506_085108

## Ancrages
- HEAD: 782a6f70bb5c9641fa3cc91d7b8df0212af01e8c (OK)
- vrais_yeux.py sha256: f8de03b6025d5a9fddbd9e9cfc69ac342e9f26e651e9be57a876910c499e5850
- vrais_yeux.py mtime: 2026-04-05 22:45:53.784275696 +0000

## Cage statique
- diff_P1_bytes: 0
- statut: INTACTE

## Classification inputs
- exec_calls_count: 0
- exec_imports_empty: 1
- dry_run_hit: 0
- kraken_in_net: 0
- non_kraken_in_net: 0
- dashboard_framework: 1
- process_alive: 1

## Verdict
V2AE_AUDIT_API_ENDPOINT_PASSIF_DASHBOARD

## Artefacts
VERDICT_V2AE.md
api_metadata.txt
api_source_copy.py
ast_calls_suspects.txt
ast_imports.txt
carte_api.json
grep_mots_cles_credentials.txt
grep_mots_cles_exchanges.txt
grep_mots_cles_execution.txt
lsof_pid_1759106.txt
manifest.json
network_connections.txt
perimetre1_apres.sha256
perimetre1_avant.sha256
perimetre1_diff.txt
ps_pid_1759106.txt
ss_pid_1759106.txt
verdict.txt
vrais_yeux_check.txt
