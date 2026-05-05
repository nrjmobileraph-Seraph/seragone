# CONTROLE MULTIMONDES V1Z-P PRECHECK REEXEC BORN

Date UTC: 2026-05-05T20:14:27+00:00

Mode: precheck lecture seule du V1ZJ. Determiner si une reexecution sandbox avec capture stdout complet est techniquement preparable. Aucune execution de script multimondes, aucun touch de fichier runtime. Phase 115 preservee, decision_weight=0.0, vrais_yeux.py INTOUCHABLE.

## 1. Source

- run_report : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK_20260505_195442/run_report.json` sha256=`fc833c8c0705c5f42fdd9a6b72fc296ac890b603a20407dc418171b99aa31a80`
- V1ZJ MD : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK_20260505_195442/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK.md` sha256=`53793630eb13991a434fa5b838bcccbba81c88c514a03ba7fcd1bb2a54e6ce62`
- V1ZJ manifest : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK_20260505_195442/manifest.json` sha256=`30a35f14acac03c56e6a9299831c89fcf47fd48387e59e163c32f087111373bc`

## 2. Cles presentes dans run_report.json

Total : 20

- `absolute_input_exists` : True
- `command` : list (4 elem)
- `created_files` : list (0 elem)
- `created_utc` : '2026-05-05T19:55:22+00:00'
- `cwd` : 'auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs_v1zj'
- `ended_utc` : '2026-05-05T19:55:22+00:00'
- `home` : '/home/ubuntu'
- `local_input_exists` : True
- `local_input_sha256` : '6850e7f0bb0673498c5db86910570dcf3f6dccb098422c8fd51754f1803ab634'
- `mode` : 'one_script_sandbox_home_real_usrbinpython3_pandas_sitecustomize_redirect_no_patch'
- `modified_files` : list (0 elem)
- `python` : '/usr/bin/python3'
- `returncode` : 0
- `script` : 'born_temps_validation.py'
- `script_sha256` : 'd9acb122719206a370f1058254d1cfc6b51d3586cce1d379426915c2bac1367d'
- `sitecustomize_sha256` : '9abaa362fcb7b78eb2f2e933794a3df9e8413012a9edf3b212f9ae0298d0fedf'
- `started_utc` : '2026-05-05T19:54:42+00:00'
- `stderr_tail` : ''
- `stdout_tail` : str (7992 chars, tronque)
- `type` : 'CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK'

## 3. Parametres de reproductibilite (cles attendues)

| Cle | Valeur |
|---|---|
| `mode` | `'one_script_sandbox_home_real_usrbinpython3_pandas_sitecustomize_redirect_no_patch'` |
| `returncode` | `0` |
| `command` | `['timeout', '60s', '/usr/bin/python3', 'born_temps_validation.py']` |
| `script` | `'born_temps_validation.py'` |
| `script_path` | `(absent)` |
| `sandbox` | `(absent)` |
| `sandbox_path` | `(absent)` |
| `python` | `'/usr/bin/python3'` |
| `python_path` | `(absent)` |
| `sitecustomize` | `(absent)` |
| `sitecustomize_path` | `(absent)` |
| `inputs` | `(absent)` |
| `outputs` | `(absent)` |
| `env` | `(absent)` |
| `timeout` | `(absent)` |
| `duration_seconds` | `(absent)` |
| `args` | `(absent)` |
| `cwd` | `'auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs_v1zj'` |
| `stdout_path` | `(absent)` |
| `log_path` | `(absent)` |
| `stdout_tail_size` | `(absent)` |
| `stdout_full_size` | `(absent)` |
| `caches_live_avant` | `(absent)` |
| `caches_live_apres` | `(absent)` |

## 4. Script detecte

- Script V1ZJ : `born_temps_validation.py`

## 5. Ce dont V1ZP_DECRET_REEXEC aura besoin (Doc 26-style)

- chemin EXACT du script .py et sha256 fige
- chemin EXACT des inputs requis et sha256 figes
- mode pandas/sitecustomize : exact (variation eventuelle enoncee explicitement)
- chemin sandbox V1ZP dedie (different de V1ZJ pour eviter pollution croisee)
- chemin capture stdout COMPLET sur disque (fichier .log dans dossier V1ZP)
- liste caches live a hasher AVANT et APRES : 3 paralleles, born_state.json, multivers states, communicants_history.json, 92mondes states
- timeout sandbox + attestation non-pollution finale

## 6. Verdict precheck

- **PRECHECK_OK_PRET_DECRET** : command est present dans run_report.json. Les parametres manquants sont reconstructibles depuis V1ZJ MD ou V1ZC CSV.
- Note : `script_path` absent : a reconstruire depuis V1ZJ MD ou V1ZC CSV ligne 5
- Note : `sandbox_path` absent : a reconstruire depuis V1ZJ MD ou V1ZC CSV ligne 5

---

Aucune execution, aucun script multimondes lance, aucun import dynamique, aucun cron, aucun broker. Phase 115 preservee. decision_weight=0.0. vrais_yeux.py INTOUCHABLE.
