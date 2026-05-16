# CONTRAT_ORCHESTRATEUR_DEMO_V1

**Date :** 13 mai 2026, 23h30 CEST  
**Type :** contrat d'orchestration V1 — pas code, pas runtime  
**Auteur :** Raphaël Boussy  
**Statut :** VALIDÉ CANONIQUE — prêt dépôt VPS  
**Dépendance canonique :** `D11_ARBITRAGES_V1_2026-05-13_2315_REFIGE_V2.md`  
**Validation :** 13 mai 2026, 23h37 CEST — validation utilisateur

═══════════════════════════════════════════

## §0 — Portée du contrat

Ce document définit ce que `orchestrateur_demo` a le droit de lire, d'appeler et d'écrire en V1.

Il ne crée aucun runtime, ne modifie aucun fichier legacy, ne change aucun cron, ne branche aucun exchange.

Il transforme les arbitrages D11 en contrat d'orchestration explicite.

═══════════════════════════════════════════

## §1 — Règle fondatrice

**Tout module V1 est traité comme calculateur.**  
**Tout write V1 passe par `orchestrateur_demo`.**  
**Tout write legacy est interdit.**

Conséquence : les modules appelés par V1 doivent retourner des objets Python ou JSON en mémoire, mais ne doivent pas écrire eux-mêmes dans les states V1.

═══════════════════════════════════════════

## §2 — Répertoire state V1

Répertoire canonique des states V1 :

```text
V1_STATE_DIR = /home/ubuntu/seragone/states/v1/
```

Ce répertoire est le seul espace d'écriture autorisé pour `orchestrateur_demo`.

Aucun fichier de `/home/ubuntu/seragone/state*.json`, `/home/ubuntu/seragone/*state.json`, `/home/ubuntu/seragone/states/*.json` hors `states/v1/`, ni aucun état legacy ne doit être modifié par V1.

═══════════════════════════════════════════

## §3 — Entrées explicites

`orchestrateur_demo` reçoit ou construit explicitement les entrées suivantes :

| Entrée | Forme canonique | Source V1 | Règle |
| --- | --- | --- | --- |
| `capital_eur` | scalaire numérique | paramètre d'appel | pas de module `capital.py`, pas de fichier capital dédié |
| `market_context` | dict typé | snapshot préparé V1 | aucune lecture implicite legacy |
| `aplomb_context` | dict typé | `./aplomb.py` racine appelé en calculateur | aucun write module |
| `prudence_measure` | dict `{veto: bool, score: float}` | `production/protection/prudence_module.py` | MEASURE_ONLY |
| `tempo_budgets` | dict budgets | `production/allocation/double_tempo.py` | ne décide jamais la direction |
| `policy_decision` | dict action/sizing/raison | `production/decision/policyengine.py` | souveraineté décisionnelle bornée |

Aucune entrée V1 ne doit dépendre d'un chemin implicite codé dans un module legacy.

═══════════════════════════════════════════

## §4 — Modules appelables

| Module | Chemin canonique | Rôle V1 | Interdit |
| --- | --- | --- | --- |
| Aplomb | `./aplomb.py` | produit le contexte souverain amont testé `SHORT perm=0.5309` | écrire `aplombstate.json` legacy |
| Policy | `production/decision/policyengine.py` | transforme contexte en décision `LONG/SHORT/FLAT` et sizing signé | écrire `states/policystate.json` legacy |
| Double Tempo | `production/allocation/double_tempo.py` | produit des budgets tempo consultatifs | écrire `doubletempostate.json` |
| Prudence | `production/protection/prudence_module.py` | mesure veto/risque en `MEASURE_ONLY` | forcer la décision finale |
| Money Manager | fonction allocation pure ou wrapper V1 | convertit décision + capital + budgets en allocation démo | lire capital hardcodé ou chemin legacy |

Si un module ne peut pas être appelé sans write disque, V1 doit passer par un wrapper pur ou l'exclure temporairement.

═══════════════════════════════════════════

## §5 — Writes autorisés

`orchestrateur_demo` est le seul writer autorisé dans `V1_STATE_DIR`.

States V1 autorisés :

| State V1 | Type | Writer | Rôle |
| --- | --- | --- | --- |
| `aplomb_state_v1.json` | JSON | `orchestrateur_demo` | contexte souverain Aplomb (sortie calculée) |
| `policy_state_v1.json` | JSON | `orchestrateur_demo` | décision souveraine V1 |
| `allocation_state_v1.json` | JSON | `orchestrateur_demo` | allocation démo finale |
| `prudence_measure_v1.json` | JSON | `orchestrateur_demo` | mesure prudence sans application forte |
| `orchestrateur_trace_v1.jsonl` | JSONL append-only | `orchestrateur_demo` | trace audit D9/D11 |

Tout autre state V1 exige un amendement documentaire avant création.

═══════════════════════════════════════════

## §6 — Ordre canonique

Ordre minimal d'un cycle V1 :

1. Construire `market_context` explicitement.
2. Recevoir `capital_eur` comme scalaire d'appel.
3. Appeler Aplomb en calculateur.
4. Appeler Prudence en `MEASURE_ONLY`.
5. Appeler Double Tempo pour budgets.
6. Appeler Policy Engine pour décision souveraine.
7. Appeler allocation pure avec capital + décision + budgets + prudence mesurée.
8. Écrire uniquement les states V1 autorisés.
9. Ajouter une ligne dans `orchestrateur_trace_v1.jsonl`.

Les mondes, multivers et profils météo peuvent filtrer, freiner ou contextualiser, mais ne tirent jamais.

═══════════════════════════════════════════

## §7 — Contrat D9

D9 est respecté par construction :

```text
un state V1 = un writer = orchestrateur_demo
```

Les modules V1 ne sont pas writers. Ils sont seulement producteurs de retour calculé.

Si un module legacy écrit pendant son appel, il est non conforme au contrat V1 et doit être remplacé par un wrapper pur.

═══════════════════════════════════════════

## §8 — Contrat D11

D11 est respecté par construction :

```text
aucun périmètre n'est déduit d'un nom de fichier
tout périmètre est défini par ses lectures, paramètres, retours et writes effectifs
```

Les chemins legacy ne sont jamais considérés comme implicites. Tout chemin lu ou écrit par V1 doit être déclaré dans le présent contrat ou dans un amendement.

═══════════════════════════════════════════

## §9 — Interdits absolus

- Aucun write dans `state.json` racine.
- Aucun write dans `aplombstate.json` legacy.
- Aucun write dans `states/policystate.json` legacy.
- Aucun write dans `doubletempostate.json` legacy.
- Aucun write dans `state/prudencestate.json` ou `states/prudencestate.json` legacy.
- Aucun appel exchange.
- Aucun import croisé métier caché.
- Aucun cron, systemd, process live ou service modifié par ce contrat.

═══════════════════════════════════════════

## §10 — Critère de validation

Le contrat est validé si, à la lecture du cycle V1, on peut répondre mécaniquement à quatre questions :

1. Qui lit quoi ?
2. Qui décide quoi ?
3. Qui écrit quoi ?
4. Où est la preuve de trace ?

Si une réponse dépend d'un nom supposé, d'un chemin implicite ou d'un effet secondaire module, le contrat est non conforme D11.

═══════════════════════════════════════════

## §11 — Statut final

Ce contrat autorise uniquement la rédaction ou la préparation d'un `orchestrateur_demo` conforme.

Il n'autorise pas le branchement opérationnel, pas le live, pas l'exchange, pas la mutation du legacy.

La prochaine étape canonique est un squelette de fichier V1 sans effet runtime, relu avant exécution.

═══════════════════════════════════════════

**FIN CONTRAT_ORCHESTRATEUR_DEMO_V1**
