# MICRO SONDE FROIDE APLOMB WRITE POTENTIEL DECISIONALLOCATION V1
Date UTC: 2026-05-15T23:21:50.130586+00:00
## Statut
Sonde froide documentaire pure.
Aucun runtime modifie.
Aucun cron modifie.
Aucun systemd modifie.
Aucun import du fichier cible.
Aucune execution du fichier cible.
Aucun branchement effectif.
Aucune activation.
Aucune finance reelle.
## Cible
- chemin: `auditphasee/wrapper_aplomb_v1_inert.py`
- existe: `True`
- sha256: `a42ba83d38b7160e6ed2ac70feb9bbb9c6b5e6e39af0ded4f6e5479624759132`
- lignes: `44`
## Methode
- lecture texte uniquement
- parsing AST uniquement
- extraction imports
- extraction fonctions
- extraction appels top-level
- extraction appels write/open/json.dump/path.write_text/os.replace potentiels
- extraction litteraux state/path
- aucun import metier
- aucune execution metier
## Resultats
- ast_ok: `True`
- fonctions: `1`
- imports: `0`
- appels top-level: `0`
- appels write-like: `1`
- marqueurs legacy: `aucun`
- verdict: `ALERTE_WRITE_NESTED_NON_EXECUTEE_PAR_SONDE`
## Appels write-like detectes
| ligne | fonction | callee | raison | gardes |
|---:|---|---|---|---|
| 25 | `wrapper_aplomb_v1_inert` | `'aplom bcontext'.replace` | `WRITE_METHOD_replace` | `` |
## Bornage
Un appel write-like detecte par AST ne prouve pas une ecriture runtime.
Un appel write-like non appele reste une alerte documentaire.
Un write potentiel ne donne pas droit au branchement.
Un AST propre ne donne pas droit a l'import.
Un AST propre ne donne pas droit a l'execution.
## Artefacts
- csv: `auditphasee/MICROSONDEFROIDE_APLOMB_WRITE_POTENTIEL_DECISIONALLOCATION_V1_20260515T232150Z.csv`
- details json: `auditphasee/MICROSONDEFROIDE_APLOMB_WRITE_POTENTIEL_DECISIONALLOCATION_V1_20260515T232150Z.details.json`
- manifest: `auditphasee/MICROSONDEFROIDE_APLOMB_WRITE_POTENTIEL_DECISIONALLOCATION_V1_20260515T232150Z.manifest.json`

FIN MICRO SONDE FROIDE.
