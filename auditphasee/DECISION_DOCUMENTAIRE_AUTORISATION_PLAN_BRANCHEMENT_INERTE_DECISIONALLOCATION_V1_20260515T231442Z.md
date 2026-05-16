# DECISION DOCUMENTAIRE AUTORISATION PLAN BRANCHEMENT INERTE DECISIONALLOCATION V1

Date UTC: 2026-05-15T23:14:42Z

## Statut

Décision documentaire pure.

Aucun runtime modifié.
Aucun cron modifié.
Aucun systemd modifié.
Aucun import Python.
Aucune exécution orchestrateur.
Aucune exécution wrapper.
Aucun branchement effectif.
Aucune activation.
Aucune finance réelle.

## Objet

Autoriser uniquement la rédaction d'un plan de branchement inerte DECISIONALLOCATION V1.

Cette décision ne branche rien.

Cette décision ne modifie aucun fichier runtime.

Cette décision ne donne aucun droit d'exécution.

Elle autorise seulement un document futur de conception: PLAN_BRANCHEMENT_INERTE_DECISIONALLOCATION_V1.

## Pièces préalables

### Sonde initiale

- fichier: auditphasee/SONDEFROIDE_CONCEPTION_BRANCHEMENT_WRAPPERS_DECISIONALLOCATION_V1_20260515T231125Z.md
- sha256: 4ad005520b2ff3131089db0d27638a318a03614d4dacc328ae5b85466b54ee12
- classification: CONCEPTION_BRANCHEMENT_BLOCKING
- blocking_count: 3

### Sonde rectificative

- fichier: auditphasee/SONDEFROIDE_RECTIFICATIVE_CHEMINS_CONTRAT_SQUELETTE_APLOMB_DECISIONALLOCATION_V1_20260515T231300Z.md
- sha256: 54b0f855de992c581384717ba4378d66ffb2c763c903cfb9221ec4f8c5695a52
- classification: RECTIFICATIF_CHEMINS_ET_APLOMB_POSSIBLE
- blocking_count: 0

### Attestation rectificative

- fichier: auditphasee/ATTESTATION_RECTIFICATIVE_CHEMINS_CONTRAT_SQUELETTE_APLOMB_DECISIONALLOCATION_V1_20260515T231351Z.md
- sha256: 41b71a6f9973eedf5778b66505625f92bec30f66aa4a7f0e0ce3f8a6e4e07db9
- effet: capitalisation documentaire de la levée des trois blocages

## Décision

La rédaction d'un plan de branchement inerte DECISIONALLOCATION V1 est autorisée.

Le plan futur devra rester strictement documentaire.

Le plan futur devra décrire les interfaces candidates sans les activer.

Le plan futur devra conserver la séparation suivante:

1. lire les artefacts
2. décrire les entrées et sorties
3. décrire la chaîne candidate
4. lister les garde-fous
5. lister les tests froids nécessaires
6. interdire explicitement toute activation

## Bornage obligatoire du plan futur

Le plan futur devra maintenir les interdits suivants:

- aucun import runtime
- aucune exécution orchestrateur
- aucune exécution wrapper
- aucune écriture state legacy
- aucune écriture dans statecanon.json
- aucune modification cron
- aucune modification systemd
- aucune modification de service
- aucun ordre broker
- aucune API exchange privée
- aucune finance réelle
- aucun branchement automatique

## Chaîne candidate autorisée à décrire

Le plan futur pourra décrire uniquement la chaîne conceptuelle candidate déjà sondée:

- marketcontext -> wrapper_aplomb -> aplombcontext ou équivalent sémantique
- marketcontext + policydecision -> wrapper_double_tempo -> tempobudgets
- marketcontext + policydecision + allocationcandidate -> wrapper_prudence_measure -> prudencemeasure
- capital + policydecision + tempobudgets + prudencemeasure -> wrapper_allocation -> allocationstate

Cette chaîne reste candidate.

Elle n'est pas décrétée active.

Elle n'est pas décrétée compatible runtime.

Elle n'est pas décrétée productrice de state legacy.

## Condition d'étape suivante

Après cette décision, l'étape suivante possible est uniquement:

- rédiger PLAN_BRANCHEMENT_INERTE_DECISIONALLOCATION_V1

Cette étape suivante devra être un document de conception, pas un script d'exécution.

FIN DECISION DOCUMENTAIRE.
