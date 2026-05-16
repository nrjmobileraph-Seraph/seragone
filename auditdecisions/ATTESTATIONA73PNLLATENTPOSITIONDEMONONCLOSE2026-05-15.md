# ATTESTATION A7.3 — PNL LATENT POSITION DEMO NON CLOSE — 2026-05-15

## Source

Sonde A7.3 lecture pure.

## Mesure

- Prix spot `state.json` : 79105.64
- Exécutions `FILLED_DEMO` reconnues : 89
- Short total : 0.085 BTC
- Buy total : 0.004 BTC
- Position nette ledger demo : -0.081 BTC SHORT
- Prix moyen short : 80711.11 USD
- Frais demo cumulés : 3.62022253 USD
- PnL latent brut estimé : 130.04 USD
- PnL latent net estimé : 126.42 USD
- Money Manager actuel : NEUTRAL finale 0.0

## Statut

PNL NON REALISE.
POSITION DEMO NON CLOSE.
LEDGER DEMO SHORT OUVERT ALORS QUE CIBLE MONEY MANAGER EST FLAT.

## Conclusion

A7 V0 a produit une position gagnante mais ne sait pas encore la réaliser.
La divergence canonique est : cible Money Manager flat / ledger demo short ouvert.

## Interdits

- Aucune activation.
- Aucune modification runtime.
- Aucun patch `decisiontoorder.py`.
- Aucun patch `demobroker.py`.
- Aucun cron modifié.
- Aucun `INDEXCANON` modifié dans ce bloc.

## Suite canonique

Décréter la sémantique `NEUTRAL => HOLD / SKIP / CLOSE`.
