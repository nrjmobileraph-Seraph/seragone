# DECISION_V1_2C_ATTRIBUTION_WRITER_STATE_RACINE

Date UTC: 2026-05-13 22:18
Sources:
- auditphasee/v1states/v1_minicycle_2_snapshot_readonly.json
- auditphasee/v1states/v1_minicycle_2b_runtime_divergence_readonly.json
- auditphasee/v1states/v1_minicycle_2c_codepath_readonly.txt
- auditdecisions/ALERTE_V1_2_DIVERGENCE_RUNTIME_2026-05-13_2214UTC.md
- auditdecisions/ALERTE_V1_2B_SERAGONE_PILOT_CRON_ACTIF_2026-05-13_2216UTC.md

Constat initial:
- Reference Document 19: state.json racine mtime 2026-04-30 22:36 UTC.
- Reference Document 19: crontab observatoire 34 lignes actives.
- Observation V1-2: state.json racine mtime 2026-05-13 22:13 puis 22:15 puis 22:17 UTC.
- Observation V1-2: crontab actif observe 91 lignes actives.

Preuves V1-2B:
- crontab actif ligne 42:
  * * * * * cd /home/ubuntu/seragone && python3 seragone_pilot.py >> logs/pilot.log 2>&1
- pilot.log racine contient:
  [2026-05-13 22:13:01] BRUIT ... Temperance seule
- logs/pilot.log contient:
  [2026-05-13 22:13:01] BRUIT ... Temperance seule
- state.json, pilot.log racine et logs/pilot.log ont des mtimes synchrones autour de 22:15:03 UTC.

Preuves V1-2C:
- sha256 seragone_pilot.py:
  661f50815c876e79ff26f2d15d44ce44b39f590c01fed53a98b2793880e61cdd
- seragone_pilot.py ligne 7:
  STATE = '/home/ubuntu/seragone/state.json'
- seragone_pilot.py ligne 8:
  LOG = '/home/ubuntu/seragone/pilot.log'
- seragone_pilot.py ligne 16:
  with open(LOG, 'a') as f: f.write(line + '\n')
- seragone_pilot.py ligne 73:
  state = json.load(open(STATE)) if os.path.exists(STATE) else {}
- seragone_pilot.py lignes 94-96:
  tmp = STATE + '.tmp'
  with open(tmp, 'w') as f: json.dump(state, f, indent=2, default=str)
  os.replace(tmp, STATE)
- tools/seragone_one.py ne reference pas seragone_pilot.py dans l'extraction ciblee V1-2C.

Decision:
- WRITER_COURANT_STATE_RACINE_ATTRIBUE_MECANIQUEMENT = seragone_pilot.py
- DECLENCHEUR_COURANT_ATTRIBUE_MECANIQUEMENT = crontab ligne 42 chaque minute
- DIVERGENCE_RUNTIME_DOCUMENT19_CONFIRMED = true
- CAUSE_INSTALLATION_CRONTAB_91_LIGNES = NON_ATTRIBUEE
- CORRECTION_RUNTIME = INTERDITE_NON_EFFECTUEE
- STOP_BRANCHAGE_V1 = MAINTENU

Portee:
- Cette decision attribue le writer observe de state.json racine au 2026-05-13 22:13-22:17 UTC.
- Cette decision n'attribue pas qui a installe ou restaure le crontab 91 lignes.
- Cette decision ne modifie pas le legacy.
- Cette decision ne relance aucun module.
- Cette decision ne tue aucun process.
- Cette decision n'envoie aucun ordre reel.

Consequence V1:
- V1 ne doit pas consommer state.json racine comme etat propre.
- V1 doit continuer uniquement par states V1 separes.
- V1-3 reste interdit tant que l'arbitrage humain n'a pas decide quoi faire de la divergence runtime.
