# DECRET A7.3 — SEMANTIQUE NEUTRAL POSITION DEMO — 2026-05-15

## Objet

Définir la sémantique canonique de `Money Manager = NEUTRAL finale 0.0` lorsqu'un ledger démo contient encore une position ouverte.

## Constat

La sonde A7.3 établit une position demo nette de -0.081 BTC SHORT.
Le Money Manager actuel expose une cible NEUTRAL finale 0.0.
Le PnL latent net estimé est positif à 126.42 USD après frais.
La position est non réalisée car A7 V0 ne possède pas encore de clôture opérationnelle activée.

## Décision sémantique

`NEUTRAL finale 0.0` signifie `TARGET_FLAT`.

Il ne signifie pas conserver une exposition ouverte.
Il ne signifie pas ignorer le ledger démo.
Il signifie que la cible théorique de position est zéro.

## Règle canonique

- Si `target = 0` et `ledger_net = 0`, alors action sémantique : `SKIP`.
- Si `target = 0` et `ledger_net < 0`, alors action sémantique : `CLOSE_TO_FLAT` par rachat/couverture candidat.
- Si `target = 0` et `ledger_net > 0`, alors action sémantique : `CLOSE_TO_FLAT` par vente/réduction candidat.
- Tant qu'aucun décret d'activation séparé n'existe, l'état opérationnel reste : `HOLD_READONLY`.

## Application au cas A7.3

- `target = 0`
- `ledger_net = -0.081 BTC`
- Position ouverte : SHORT
- Sémantique décrétée : `CLOSE_TO_FLAT`
- Action runtime autorisée maintenant : aucune
- État opérationnel provisoire : `HOLD_READONLY`
- Suite autorisée : sonde froide de faisabilité CLOSE, puis décret d'activation séparé si validé

## Interdits

Ce décret ne crée aucun ordre.
Ce décret ne modifie aucun fichier runtime.
Ce décret ne modifie aucun cron.
Ce décret ne modifie pas `decisiontoorder.py`.
Ce décret ne modifie pas `demobroker.py`.
Ce décret ne modifie pas `moneymanagerstate.json`.
Ce décret ne modifie pas `state.json`.
Ce décret n'autorise aucune finance réelle.

## Statut

DECRET SEMANTIQUE LECTURE SEULE.
AUCUNE ACTIVATION.
AUCUN RUNTIME TOUCHE.
