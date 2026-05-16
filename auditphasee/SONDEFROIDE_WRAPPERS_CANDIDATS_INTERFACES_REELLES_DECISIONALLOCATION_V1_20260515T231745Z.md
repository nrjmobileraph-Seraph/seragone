# SONDE FROIDE WRAPPERS CANDIDATS INTERFACES REELLES DECISIONALLOCATION V1

Date UTC: 2026-05-15T23:17:45Z

## Statut

Sonde froide documentaire pure.

Aucun runtime modifie.
Aucun cron modifie.
Aucun systemd modifie.
Aucun import des fichiers candidats.
Aucune execution des fichiers candidats.
Aucune execution orchestrateur.
Aucune execution wrapper.
Aucun branchement effectif.
Aucune activation.
Aucune finance reelle.

## Objet

Verifier en lecture seule les wrappers candidats exacts et leurs interfaces reelles.

Cette sonde ne decide aucun branchement.

Cette sonde ne decrete aucune compatibilite runtime.

Cette sonde ne transforme aucun fallback en wrapper canonique.

## Methode

- verification ciblee de chemins candidats
- lecture texte uniquement
- parsing AST uniquement
- extraction fonctions publiques
- extraction imports
- extraction appels top-level
- extraction appels write/exec potentiels
- extraction litteraux de chemins/state
- aucun import metier
- aucune execution metier

## Resultats synthetiques

| role | statut candidat | chemin | lignes | fonctions | verdict |
|---|---|---|---:|---|---|
| wrapper_aplomb | EXACT_CANDIDATE_FOUND | auditphasee/wrapper_aplomb_v1_inert.py | 44 | wrapper_aplomb_v1_inert | ALERTE_WRITE_POTENTIEL |
| wrapper_double_tempo | EXACT_CANDIDATE_FOUND | auditphasee/wrapper_double_tempo_v1_inert.py | 45 | wrapper_double_tempo_v1_inert | WRAPPER_LISIBLE_AST_SANS_ALERTE_MAJEURE |
| wrapper_prudence_measure | EXACT_CANDIDATE_FOUND | auditphasee/wrapper_prudence_measure_v1_inert.py | 53 | wrapper_prudence_measure_v1_inert | WRAPPER_LISIBLE_AST_SANS_ALERTE_MAJEURE |
| wrapper_allocation | EXACT_CANDIDATE_FOUND | auditphasee/wrapper_allocation_v1_inert.py | 55 | wrapper_allocation_v1_inert | WRAPPER_LISIBLE_AST_SANS_ALERTE_MAJEURE |

## Synthese

- roles sondes: 4
- lignes CSV: 4
- alertes ou blocages techniques: 1
- verdict global: SONDE_A_LIRE_AVANT_DECISION

## Bornage

Les fichiers fallback eventuels sont seulement des candidats documentaires sous reserve.

Un fallback lisible ne devient pas wrapper canonique.

Un AST propre ne donne pas droit a l'import.

Un AST propre ne donne pas droit a l'execution.

Un AST propre ne donne pas droit au branchement.

## Artefacts

- csv: auditphasee/SONDEFROIDE_WRAPPERS_CANDIDATS_INTERFACES_REELLES_DECISIONALLOCATION_V1_20260515T231745Z.csv
- details json: auditphasee/SONDEFROIDE_WRAPPERS_CANDIDATS_INTERFACES_REELLES_DECISIONALLOCATION_V1_20260515T231745Z.details.json
- manifest: auditphasee/SONDEFROIDE_WRAPPERS_CANDIDATS_INTERFACES_REELLES_DECISIONALLOCATION_V1_20260515T231745Z.manifest.json

FIN SONDE FROIDE.
