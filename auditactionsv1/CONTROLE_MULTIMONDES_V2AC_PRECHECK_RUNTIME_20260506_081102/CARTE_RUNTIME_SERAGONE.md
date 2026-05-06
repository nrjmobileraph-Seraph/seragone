# V2AC PRECHECK RUNTIME CARTOGRAPHIE

Lecture seule pure. Aucun kill, systemctl mut, crontab mut.
Aucune execution de scripts cibles. Aucun touch fichier vivant.

## Ancrages
- HEAD actuel: 782a6f70bb5c9641fa3cc91d7b8df0212af01e8c
- HEAD verdict: OK
- vrais_yeux.py sha256: f8de03b6025d5a9fddbd9e9cfc69ac342e9f26e651e9be57a876910c499e5850
- vrais_yeux.py attendu: f8de03b6025d5a9fddbd9e9cfc69ac342e9f26e651e9be57a876910c499e5850
- vrais_yeux.py mtime: 2026-04-05 22:45:53.784275696 +0000

## Cage statique (perimetre 1, 14 fichiers)
- diff_bytes: 0
- statut: INTACTE

## Runtime actif (perimetre 2, informationnel)
- changements lignes (entre AVANT et APRES snapshot): 21

## Verdict
V2AC_PRECHECK_RUNTIME_OK_CARTE_PRODUITE

## Verdicts possibles
- V2AC_PRECHECK_RUNTIME_OK_CARTE_PRODUITE
- V2AC_PRECHECK_RUNTIME_BLOQUE_CAGE_STATIQUE_VIOLEE
- V2AC_PRECHECK_RUNTIME_BLOQUE_VRAISYEUX_DRIFT
- V2AC_PRECHECK_RUNTIME_BLOQUE_HEAD_DRIFT
- V2AC_PRECHECK_RUNTIME_BLOQUE_ACCES_REFUSE

## Artefacts
CARTE_RUNTIME_SERAGONE.md
carte_runtime.json
cron_scripts_inventory.tsv
cron_writes_predicted.txt
crontab_user.sha256
crontab_user.txt
daemons_vivants.txt
lsof_seragone.txt
manifest.json
perimetre1_cache_statique_apres.sha256
perimetre1_cache_statique_avant.sha256
perimetre1_diff.txt
perimetre2_changements.txt
perimetre2_dynamique_apres_inventaire.txt
perimetre2_dynamique_avant_inventaire.txt
systemd_seragone_unit.txt
systemd_timers.txt
verdict.txt
vrais_yeux_check.txt
writes_journee_complete.txt
