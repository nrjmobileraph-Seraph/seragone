# DECRET CREATION WRAPPERS NEUFS INERTES DECISIONALLOCATION V1

## Statut

Décret documentaire séparé.
Effet runtime nul au moment de la gravure.
Aucune activation.
Aucun branchement.
Aucun import legacy.
Aucun appel legacy.
Aucun ordre réel.
Aucune finance réelle.

## Sources mécaniques

- auditphasee/MATRICE_WRAPPERS_NEUFS_INERTES_DECISIONALLOCATION_V1_20260515T230419Z.md
  - sha256: 4d19517b800e7af4ea8f2d97df5481d0a3600f9c762de99004c355571b02759e

- auditphasee/SONDEFROIDE_SPEC_WRAPPERS_NEUFS_INERTES_DECISIONALLOCATION_V1_20260515T230603Z.md
  - sha256: d892f20627e85da68ad5bd9b3800b048d498515def6208d1b036802435fdb11d
  - classification: SPEC_DOCUMENTAIRE_CONFORME
  - blocking_count: 0

- auditphasee/SONDEFROIDE_SPEC_WRAPPERS_NEUFS_INERTES_DECISIONALLOCATION_V1_20260515T230603Z.csv
  - sha256: 15e859b34cbcbafc4069bc19010a309fd08c1aed24b2c7ef6eb15d7d81633be2

- auditphasee/SONDEFROIDE_SPEC_WRAPPERS_NEUFS_INERTES_DECISIONALLOCATION_V1_20260515T230603Z.manifest.json
  - sha256: 39a826d2ecc193d6264a724443199e8f693959fdcd4eaf7a1a1ebc965f779a21

## Décision

La création documentaire des quatre wrappers neufs inertes DECISIONALLOCATION V1 est autorisée en étape séparée ultérieure.

Fichiers autorisés, et eux seuls:

- auditphasee/wrapper_aplomb_v1_inert.py
- auditphasee/wrapper_double_tempo_v1_inert.py
- auditphasee/wrapper_prudence_measure_v1_inert.py
- auditphasee/wrapper_allocation_v1_inert.py

## Nature obligatoire des fichiers

Chaque wrapper devra être:

- fichier nouveau
- inerte au chargement
- sans import métier legacy
- sans lecture implicite de state legacy
- sans write disque hors éventuel test explicitement décrété plus tard
- sans réseau
- sans exchange
- sans cron
- sans systemd
- sans process lancé
- sans effet financier
- sans branchement orchestrateur
- sans branchement runtime
- sans activation automatique

## Interfaces autorisées

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

## Limite du décret

Ce décret autorise uniquement la production ultérieure de fichiers wrappers neufs inertes.

Il n'autorise pas:

- l'import dans orchestrateur_demo_v1_skeleton
- le branchement dans un runtime
- l'appel depuis cron
- l'appel depuis systemd
- l'appel depuis un process vivant
- la lecture de states legacy
- l'écriture de states legacy
- la création d'ordre
- la finance réelle
- la sortie de cage démo
- l'activation

## Suite autorisée

Étape suivante autorisée:

- produire les quatre fichiers wrappers neufs inertes dans auditphasee

Étape suivante interdite:

- les brancher
- les exécuter automatiquement
- les relier à un orchestrateur vivant
- les importer depuis un module runtime

Après création des fichiers, une sonde froide séparée devra vérifier:

- existence
- hash
- syntaxe
- absence imports legacy
- absence write legacy
- absence réseau
- absence exchange
- inertie au chargement

## Fermeture

Sonder a été fait.
Décréter est fait par le présent document.
Activer reste interdit.

Aucun runtime n'est modifié par ce décret.
