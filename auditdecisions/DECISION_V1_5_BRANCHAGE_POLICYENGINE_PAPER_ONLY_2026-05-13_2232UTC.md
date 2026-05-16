# DECISION_V1_5_BRANCHAGE_POLICYENGINE_PAPER_ONLY

Date UTC: 2026-05-13 22:32
Auteur souverain: Raphael Boussy
Statut: DECISION_CANONIQUE_CONSTRUCTION_V1_5

Contexte:
- V1-4B a produit SQUELETTE_OK.
- Le couloir demo_v1 existe.
- Les states V1 sont separes.
- Le broker est demobroker_paper_only.
- Aucun ordre reel n'est autorise.

Decision:
- Brancher le premier organe reel qualifie: policyengine.
- Source cible: productiondecisionpolicyengine.py seulement.
- Mode: appel pur via adapter V1.
- Si la signature decide est incompatible, ne pas forcer.
- Ecrire le resultat dans demo_v1/states/policyengine_state.json.
- Garder l'ordre broker en simulation seulement.

Interdits maintenus:
- Aucun ordre reel.
- Aucune cle API exchange.
- Aucun ccxt actif dans demo_v1.
- Aucun crontab.
- Aucun systemd.
- Aucune modification legacy.
- Aucune ecriture state.json racine.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- D11_ARBITRAGES_V1: policyengine cible = productiondecisionpolicyengine.py seul.

Issue attendue:
- V1-5 produit une pulsation paper only avec policyengine_state.
- Le broker reste SIMULATED_ONLY.
