# DECRET — QUARANTAINE FROIDE PALETTE BTC 1MIN

TS_UTC=20260515T202648Z
CIBLE=./palette_claude/btc_1min_historique_complet.csv
HASH_CIBLE=8f18732fed70a7a40194294f0e6e7b1bf667c54e44ae85993b1edc498665ebe5
TAILLE_CIBLE=533620487

## Fondements

- SONDEFROIDEDOUBLONSTOPLARGE20260515T202301Z : doublon hashé avec ./btc_1min_historique_complet.csv.
- SONDEFROIDEREFERENCESDOUBLONSTOPLARGE20260515T202516Z : lectures script explicites observées sur la version racine, pas sur la version palette.
- ATTESTATIONREFERENCESDOUBLONSTOPLARGE20260515T202619Z : version palette classée candidat prioritaire à quarantaine ultérieure.

## Décision

La cible est autorisée uniquement à une quarantaine froide réversible.
Aucune suppression définitive n'est autorisée.
Aucun lien symbolique n'est autorisé.
Aucune modification du fichier racine ./btc_1min_historique_complet.csv n'est autorisée.
Aucune action sur multivers_state.json n'est autorisée.

## Activation séparée requise

Ce décret n'exécute rien.
Une activation séparée devra créer un dossier de quarantaine, déplacer la cible, écrire un manifeste, puis hasher les preuves.
