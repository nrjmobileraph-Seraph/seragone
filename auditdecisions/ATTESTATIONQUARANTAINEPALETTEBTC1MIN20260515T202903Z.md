# ATTESTATION — QUARANTAINE FROIDE PALETTE BTC 1MIN

TS_UTC=20260515T202903Z

## Pieces scellees

- DECRET=auditdecisions/DECRETQUARANTAINEPALETTEBTC1MIN20260515T202648Z.md
- HASH_DECRET=7c7442bdb24b6907f3e03b94208b94c654d9dcf470020f707dc8d3312f62d6be
- ACTIVATION=auditdecisions/ACTIVATIONQUARANTAINEPALETTEBTC1MIN20260515T202722Z.md
- HASH_ACTIVATION=5b525ed4aa13596764c1c7f2e63b8197b6ddd5f3b50d9673a8d17412009621ae
- SONDE_POST=auditdecisions/SONDEFROIDEPOSTQUARANTAINEPALETTEBTC1MIN20260515T202812Z.txt
- HASH_SONDE_POST=ce96e809ecc2ecc9702ebb836beba192e13899f76893df88b8547a82da15ba61

## Resultat mecanique

- ROOT_EXISTS=YES
- SRC_PALETTE_EXISTS=NO
- DST_QUARANTINE_EXISTS=YES
- DST_HASH_EXPECTED=YES
- HASH_CIBLE=8f18732fed70a7a40194294f0e6e7b1bf667c54e44ae85993b1edc498665ebe5
- TAILLE_RACINE=533620487
- TAILLE_QUARANTAINE=533620487

## Decision attestee

La quarantaine froide reversible de ./palette_claude/btc_1min_historique_complet.csv est attestee comme reussie.
Le fichier racine ./btc_1min_historique_complet.csv reste present.
La source palette n'est plus presente a son emplacement initial.
La copie quarantinee est presente et conserve le hash attendu.

## Interdits respectes

- Aucune suppression definitive attestee.
- Aucun lien symbolique cree.
- Aucune modification du fichier racine attestee par la sonde.
- Aucune action sur multivers_state.json.

## Statut canonique

Statut=QUARANTAINE_FROIDE_REVERSIBLE_ATTESTEE
Suite=STOP_ACTION_RUNTIME
Action suivante autorisee=lecture seule ou indexation documentaire separee
