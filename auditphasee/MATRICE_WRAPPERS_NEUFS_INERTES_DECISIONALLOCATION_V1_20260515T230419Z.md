# MATRICE WRAPPERS NEUFS INERTES DECISIONALLOCATION V1

Date UTC: 20260515T230419Z

## Sources
- auditdecisions/RECTIFICATIF_CHEMIN_CONTRAT_V1_RESOLU_APRES_SONDE_BORNEE_20260515T230321Z.md
- auditphasee/CONTRAT_ORCHESTRATEUR_DEMO_V1_2026-05-13_2330_VALIDATED.md
- auditphasee/orchestrateur_demo_v1_skeleton_2026-05-13_2352_SYNTAX_OK.py
- auditdecisions/RECTIFICATIF_MATRICE_WRAPPERS_PURS_DECISIONALLOCATION_20260515T204439Z.md
- auditphasee/MATRICE_WRAPPERS_PURS_DECISIONALLOCATION_20260515T204342Z.md
- auditphasee/SONDEB_BLOQUEURS_DECISIONALLOCATION_20260515T203947Z.md
- auditdecisions/ATTESTATION_DECISIONALLOCATION_SONDEB_BLOCAGE_DIRECT_20260515T204042Z.md

## Doctrine
Cette matrice ne crée aucun wrapper.
Elle ne modifie aucun runtime.
Elle ne lance aucun process.
Elle ne décrète aucun branchement.

## Règle fondatrice
Une fonction candidate lexicale dans un fichier legacy ne rend pas le fichier parent appelable.

Si le parent est classé:
- WRITE_LEGACY_REEL_OU_PROBABLE
- WRAPPER_NEUF_REQUIS_WRITE_LEGACY
- EXCLURE_RISQUE_REEL_DIRECT
- EXCLURE_PROCESS_CRON_SYSTEMD_DIRECT

alors:
- pas d'import direct
- pas d'appel direct
- pas de branchement
- wrapper neuf requis ou exclusion temporaire

## Matrice rôles V1

| Rôle | Source legacy informative | Statut parent | Wrapper neuf inerte | Statut V1 |
|---|---|---|---|---|
| APLOMB | tireur_aplomb.py / fonctions infer_aplomb_input, decide_local | WRAPPER_NEUF_REQUIS_WRITE_LEGACY | wrapper_aplomb_v1_inert.py candidat documentaire | Non branché |
| DOUBLE_TEMPO | doubletempo.py / get_tempo_budgets | WRAPPER_NEUF_REQUIS_WRITE_LEGACY | wrapper_double_tempo_v1_inert.py candidat documentaire | Non branché |
| PRUDENCE_MEASURE | prudence_module.py / prudence_parle | EXCLURE_PROCESS_CRON_SYSTEMD_DIRECT | wrapper_prudence_measure_v1_inert.py ou exclusion temporaire | Non branché |
| ALLOCATION | money_manager.py / money_manager_perplexity_97L.py | EXCLURE_RISQUE_REEL_DIRECT ou WRAPPER_NEUF_REQUIS_WRITE_LEGACY | wrapper_allocation_v1_inert.py candidat documentaire | Non branché |
| DECISION_TO_ORDER | decision_to_order.py / decision_hash | Hors orchestrateur V1 jusqu'à décret spécifique | Aucun wrapper V1 maintenant | Exclu V1 |
| DEMO_BROKER | prudence_demo_runner.py / is_already_prudenced | Hors orchestrateur V1 jusqu'à décret spécifique | Aucun wrapper V1 maintenant | Exclu V1 |

## Contrat minimal des wrappers neufs

Chaque wrapper neuf candidat devra être:
- fichier nouveau
- inerte au chargement
- sans import métier legacy
- sans lecture implicite de state legacy
- sans write disque
- sans réseau
- sans exchange
- sans cron/systemd/process
- sans effet financier
- testé séparément par sonde froide avant tout décret

## Interfaces documentaires attendues

### wrapper_aplomb_v1_inert.py
Entrée documentaire:
- marketcontext dict
- paramètres explicites

Sortie documentaire:
- aplombcontext dict

Interdits:
- import tireur_aplomb.py
- write aplombstate.json
- lecture implicite legacy

### wrapper_double_tempo_v1_inert.py
Entrée documentaire:
- marketcontext dict
- policydecision dict éventuel

Sortie documentaire:
- tempobudgets dict

Interdits:
- import doubletempo.py
- write doubletempostate.json
- décision directionnelle finale

### wrapper_prudence_measure_v1_inert.py
Entrée documentaire:
- marketcontext dict
- policydecision dict éventuel
- allocationcandidate dict éventuel

Sortie documentaire:
- prudencemeasure dict avec veto bool, score float, reason str

Interdits:
- import prudence_module.py
- cron/systemd/process
- forçage de décision finale

### wrapper_allocation_v1_inert.py
Entrée documentaire:
- capital scalar
- policydecision dict
- tempobudgets dict
- prudencemeasure dict

Sortie documentaire:
- allocationstate dict demo/paper seulement

Interdits:
- import money_manager.py
- import money_manager_perplexity_97L.py
- lecture capital hardcodé
- write moneymanagerstate.json
- ordre réel

## Statut final
- Matrice documentaire seulement
- Aucun fichier wrapper créé
- Aucun import métier
- Aucun appel legacy
- Aucun runtime touché
- Aucun cron modifié
- Aucun systemd modifié
- Aucun process lancé
- Aucune finance réelle
- Aucun branchement autorisé

## Suite autorisée
Si cette matrice est acceptée, produire ensuite une sonde froide de forme:
SONDEFROIDE_SPEC_WRAPPERS_NEUFS_INERTES_DECISIONALLOCATION_V1.

Cette sonde devra seulement vérifier les noms, interfaces et interdits avant toute création de fichiers.
