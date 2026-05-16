# PLAN BRANCHEMENT INERTE DECISIONALLOCATION V1

Date UTC: 2026-05-15T23:15:46Z

## Statut

Plan documentaire pur.

Aucun runtime modifié.
Aucun cron modifié.
Aucun systemd modifié.
Aucun import Python.
Aucune exécution orchestrateur.
Aucune exécution wrapper.
Aucun branchement effectif.
Aucune activation.
Aucune finance réelle.

## Autorisation documentaire amont

Ce plan est rédigé uniquement parce que la décision documentaire suivante l'autorise:

- fichier: auditphasee/DECISION_DOCUMENTAIRE_AUTORISATION_PLAN_BRANCHEMENT_INERTE_DECISIONALLOCATION_V1_20260515T231442Z.md
- sha256: b45fb8c5f16a554f7f88a0bc7f7e3d5e0cfe777113e6976711e2143ce7c6a247
- effet: autorisation de rédaction d'un plan de branchement inerte uniquement

Cette décision ne vaut pas activation.

Cette décision ne vaut pas branchement.

Cette décision ne vaut pas compatibilité runtime.

## Pièces préalables

### Sonde initiale

- fichier: auditphasee/SONDEFROIDE_CONCEPTION_BRANCHEMENT_WRAPPERS_DECISIONALLOCATION_V1_20260515T231125Z.md
- sha256 md: 4ad005520b2ff3131089db0d27638a318a03614d4dacc328ae5b85466b54ee12
- classification: CONCEPTION_BRANCHEMENT_BLOCKING
- blocking_count: 3

### Sonde rectificative

- fichier: auditphasee/SONDEFROIDE_RECTIFICATIVE_CHEMINS_CONTRAT_SQUELETTE_APLOMB_DECISIONALLOCATION_V1_20260515T231300Z.md
- sha256 md: 54b0f855de992c581384717ba4378d66ffb2c763c903cfb9221ec4f8c5695a52
- classification: RECTIFICATIF_CHEMINS_ET_APLOMB_POSSIBLE
- blocking_count: 0

### Attestation rectificative

- fichier: auditphasee/ATTESTATION_RECTIFICATIVE_CHEMINS_CONTRAT_SQUELETTE_APLOMB_DECISIONALLOCATION_V1_20260515T231351Z.md
- sha256: 41b71a6f9973eedf5778b66505625f92bec30f66aa4a7f0e0ce3f8a6e4e07db9
- effet: capitalisation documentaire de la levée des trois blocages

### Contrat orchestrateur démo V1

- fichier: auditphasee/CONTRAT_ORCHESTRATEUR_DEMO_V1_2026-05-13_2330_VALIDATED.md
- sha256: 2445e4776e234169e4d0e3c4be3bd14df284c1d593c8feefdfe18c02dcdf8c2d
- statut: contrat V1 validé, préparation documentaire uniquement

### Squelette orchestrateur démo V1

- fichier: auditphasee/orchestrateur_demo_v1_skeleton_2026-05-13_2352_SYNTAX_OK.py
- sha256: f3f5512fc4a5453d005a8dc4dbc1aff8b41d889f281ef3d541b5f2c3c0f3353d
- statut: squelette inerte, syntaxe valide, non runtime

## Objet du plan

Décrire une chaîne candidate de branchement inerte DECISIONALLOCATION V1.

Le plan ne crée aucun fichier Python.

Le plan ne modifie aucun fichier Python.

Le plan ne lit aucun module par import.

Le plan ne valide aucune exécution.

Le plan ne valide aucun write.

Le plan ne valide aucun ordre réel.

## Principe D11

Le plan applique le principe suivant:

- aucun périmètre déduit d'un nom de fichier
- aucun rôle canonique attribué sans preuve mécanique
- aucune lecture implicite
- aucun write implicite
- aucun producteur décrété par simple proximité de nom
- chaque entrée, sortie, rôle et trace doit rester déclaré explicitement

## Chaîne candidate décrite

La chaîne conceptuelle candidate est:

1. marketcontext -> wrapper_aplomb -> aplombcontext ou équivalent sémantique
2. marketcontext + policydecision -> wrapper_double_tempo -> tempobudgets
3. marketcontext + policydecision + allocationcandidate -> wrapper_prudence_measure -> prudencemeasure
4. capital + policydecision + tempobudgets + prudencemeasure -> wrapper_allocation -> allocationstate

Cette chaîne reste candidate.

Elle n'est pas active.

Elle n'est pas décrétée compatible runtime.

Elle n'est pas décrétée productrice de state legacy.

Elle n'est pas décrétée productrice de statecanon.json.

## Interfaces candidates

### 1. wrapper_aplomb

Entrées candidates:

- marketcontext
- parameters éventuels

Sortie candidate:

- aplombcontext ou équivalent sémantique

Rôle candidat:

- produire un contexte de permission ou d'aplomb lisible par la suite

Statut:

- wrapper lisible AST selon sonde rectificative
- nom aplombcontext non obligatoire tant que l'équivalence sémantique est explicitée

### 2. wrapper_double_tempo

Entrées candidates:

- marketcontext
- policydecision
- capital ou capital total disponible si requis par le calculateur réel

Sortie candidate:

- tempobudgets

Rôle candidat:

- produire des budgets de poche capital
- ne pas décider la direction marché
- ne pas supplanter Aplomb
- ne pas supplanter les protections terminales

### 3. wrapper_prudence_measure

Entrées candidates:

- marketcontext
- policydecision
- allocationcandidate

Sortie candidate:

- prudencemeasure

Rôle candidat:

- mesurer une prudence ou contrainte de risque
- ne pas exécuter
- ne pas écrire
- ne pas décider seul

### 4. wrapper_allocation

Entrées candidates:

- capital
- policydecision
- tempobudgets
- prudencemeasure

Sortie candidate:

- allocationstate

Rôle candidat:

- produire un état d'allocation V1 candidat
- rester sous contrôle de l'orchestrateur démo
- ne jamais écrire dans un state legacy

## Writes interdits

Les écritures suivantes restent interdites:

- state.json
- aplombstate.json
- states/policystate.json
- doubletempostate.json legacy
- stateprudencestate.json
- states/prudencestate.json
- statecanon.json
- tout fichier broker
- tout fichier exchange
- tout fichier cron
- tout fichier systemd
- tout fichier service
- tout fichier runtime non déclaré

## Writes V1 théoriques

Les seuls chemins théoriques pouvant être décrits par un futur décret séparé seraient des chemins V1 isolés, par exemple:

- statesv1/aplombstatev1.json
- statesv1/policystatev1.json
- statesv1/allocationstatev1.json
- statesv1/prudencemeasurev1.json
- statesv1/orchestrateurtracev1.jsonl

Ces chemins ne sont pas créés par ce plan.

Ces chemins ne sont pas écrits par ce plan.

Ces chemins ne sont pas activés par ce plan.

## Garde-fous

Tout futur passage au-delà de ce plan devra exiger au minimum:

1. une sonde froide des wrappers candidats exacts
2. une sonde froide des signatures réelles
3. une sonde froide des chemins lus et écrits
4. une attestation de non-import runtime
5. une attestation de non-write legacy
6. une décision documentaire séparée avant tout squelette ou amendement
7. un décret séparé avant toute activation, si activation envisagée un jour

## Tests froids nécessaires

Avant tout document plus engageant, les tests froids suivants devront être produits:

- inventaire des fichiers candidats exacts
- hash sha256 de chaque fichier candidat
- lecture AST des signatures
- extraction des fonctions publiques candidates
- extraction des chemins littéraux éventuels
- vérification absence d'import dangereux
- vérification absence d'appel réseau
- vérification absence d'appel broker
- vérification absence d'écriture legacy
- vérification absence d'appel subprocess
- vérification absence d'effet au chargement

## Non-décisions explicites

Ce plan ne décide pas:

- que wrapper_aplomb est le producteur réel d'aplombcontext
- que wrapper_double_tempo est branchable
- que wrapper_prudence_measure est branchable
- que wrapper_allocation est branchable
- que l'orchestrateur démo peut être exécuté
- que les states V1 peuvent être écrits
- que statecanon.json peut être consommé
- que le réel peut être approché

## Verdict

Le branchement inerte DECISIONALLOCATION V1 est descriptible conceptuellement.

Aucun branchement effectif n'est autorisé.

Aucune activation n'est autorisée.

La prochaine étape possible est uniquement une sonde froide des wrappers candidats exacts et de leurs interfaces réelles.

FIN PLAN BRANCHEMENT INERTE.
