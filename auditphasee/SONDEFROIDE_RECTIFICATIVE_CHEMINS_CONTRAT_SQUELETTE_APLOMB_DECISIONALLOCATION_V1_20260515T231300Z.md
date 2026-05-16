# SONDE FROIDE RECTIFICATIVE CHEMINS CONTRAT SQUELETTE APLOMB DECISIONALLOCATION V1

Date UTC: 2026-05-15T23:13:00.256925+00:00

## Statut
Sonde documentaire séparée.
Effet runtime nul.
Aucune activation.
Aucun branchement.
Aucun import runtime.
Aucune exécution des wrappers.
Aucun cron modifié.
Aucun systemd modifié.

## Objet
Rectifier ou confirmer les trois blocages de la sonde précédente: contrat_v1 MISSING, squelette_v1 MISSING, wrapper_aplomb BRIDGE_CONCEPTS_INCOMPLETE.

## Résultat
- classification: RECTIFICATIF_CHEMINS_ET_APLOMB_POSSIBLE
- blocking_count: 0
- rows_count: 3
- csv: auditphasee/SONDEFROIDE_RECTIFICATIVE_CHEMINS_CONTRAT_SQUELETTE_APLOMB_DECISIONALLOCATION_V1_20260515T231300Z.csv
- manifest: auditphasee/SONDEFROIDE_RECTIFICATIVE_CHEMINS_CONTRAT_SQUELETTE_APLOMB_DECISIONALLOCATION_V1_20260515T231300Z.manifest.json

## Lignes
- contrat_v1
  - resolved_path: auditphasee/CONTRAT_ORCHESTRATEUR_DEMO_V1_2026-05-13_2330_VALIDATED.md
  - resolved_sha256: 2445e4776e234169e4d0e3c4be3bd14df284c1d593c8feefdfe18c02dcdf8c2d
  - hash_exact: True
  - lines: 176
  - classification: RECTIFIABLE_OU_LISIBLE
  - blocking_reasons: 
- squelette_v1
  - resolved_path: auditphasee/orchestrateur_demo_v1_skeleton_2026-05-13_2352_SYNTAX_OK.py
  - resolved_sha256: f3f5512fc4a5453d005a8dc4dbc1aff8b41d889f281ef3d541b5f2c3c0f3353d
  - hash_exact: True
  - lines: 225
  - classification: RECTIFIABLE_OU_LISIBLE
  - blocking_reasons: 
- wrapper_aplomb
  - resolved_path: auditphasee/wrapper_aplomb_v1_inert.py
  - resolved_sha256: a42ba83d38b7160e6ed2ac70feb9bbb9c6b5e6e39af0ded4f6e5479624759132
  - hash_exact: True
  - lines: 44
  - classification: RECTIFIABLE_OU_LISIBLE
  - functions: wrapper_aplomb_v1_inert
  - args: marketcontext|parameters
  - dict_keys: schema|role|mode|realfinanceallowed|branching_allowed|final_decision
  - blocking_reasons: 

## Verdict documentaire
Les trois blocages précédents sont rectifiables: les chemins/hash sont résolus et wrapper_aplomb est lisible sans exécution.
La sonde précédente ne doit pas être interprétée comme absence canonique du contrat ou du squelette.
Le critère aplombcontext doit être considéré comme trop littéral tant qu'aucune exigence canonique n'impose ce nom exact.

## Suite autorisée
Si blocking_count vaut 0, produire une attestation rectificative documentaire séparée.
Aucune activation ni branchement ne découle de cette sonde.
