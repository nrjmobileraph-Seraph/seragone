# V2AH RECONCILIATION GIT - MANIFEST GLOBAL

**Verdict chaine finale nette** : `V2AH_RECONCIL_GIT_OK` (7/7 phases finales OK)
**Parcours complet trace** : 10 dossiers (3 tentatives intermediaires + 7 phases finales effectives)
**Date UTC** : 2026-05-06T10:02:10.791288+00:00
**HEAD final** : `5e9a13df` (local == origin/main : `True`)

## Phases finales effectives (7)

| Phase | Verdict |
|---|---|
| PHASE0_PRECHECK | `V2AH_PHASE0_PRECHECK_OK` |
| PHASE1_FETCH | `V2AH_PHASE1_FETCH_OK` |
| PHASE2_FASTFORWARD | `V2AH_PHASE2_FASTFORWARD_OK` |
| PHASE3BIS_RESET_RECOMMIT | `V2AH_PHASE3_COMMITS_OK_CLEAN` |
| PHASE4_COMMIT_MPE | `V2AH_PHASE4_COMMIT_MPE_OK` |
| PHASE5_CLEAN_BAK | `V2AH_PHASE5_CLEAN_BAK_OK` |
| PHASE6TER_RETRY_PUSH_POST_UNBLOCK | `V2AH_PHASE6TER_PUSH_OK` |

## Tentatives intermediaires tracees (3 - transparence)

| Phase | Verdict | Supersedee par |
|---|---|---|
| PHASE3_COMMITS | `V2AH_PHASE3_PARTIAL_6_de_7` | PHASE3BIS_RESET_RECOMMIT |
| PHASE6BIS_RETRY_PUSH | `V2AH_PHASE6BIS_PUSH_OK` | PHASE6TER_RETRY_PUSH_POST_UNBLOCK |
| PHASE6_PUSH | `V2AH_PHASE6_BLOQUE_NON_SYNCED` | PHASE6TER_RETRY_PUSH_POST_UNBLOCK |


## Invariants preserves

- `vrais_yeux.py` sha256 = `f8de03b6...e5850` (INCHANGE)
- 9 ancetres 27D : TOUS OK
- HEAD local == origin/main : `True`

## Incidents resolus durant V2AH

- Token GitHub PAT ghp_LcNK revoque a 08:30 UTC apres detection en clair dans /tmp/push_bulletin.sh
- Backup local /tmp/push_bulletin.sh.bak.20260506_083001 supprime (Phase 5)
- 3 bugs assistant Phase 6/6-bis: git pull -m non supporte, NB_CONFLICT pollu par || echo 0, exit 1 fermant SSH (corriges Phase 6-ter)
- GitHub Push Protection sur ancien token detecte dans commit 40d572ac path V2ACBIS/push_bulletin_sh_content.txt - resolu Option delta
- bulletin_mobile.json modifie en continu par cron update_live.py - gere par checkout HEAD avant chaque merge

## Retombees pour chaines futures

- V2AG-bis: rectifier inscription cage statique (14 inscrits != 9 reels) + sortir data/communicants_history.json du perimetre P1
- V2AG-ter: caviarder ancien token revoque dans push_bulletin_sh_content.txt commit 40d572ac
- V2AI_CHANTIER6_VILLAGE: reprise (doublon village_le_vrai.py vs village_le_vrai_vps.py sha 19055958)
- V2AJ_HARDENING_API_DASHBOARD: audit transitif production.utils.config_manager + firewall port 5000
