# DECISION_V1_6A_ALLOCATION_PAPER_SHADOW_EXPLICITE

Date UTC: 2026-05-13 22:37
Auteur souverain: Raphael Boussy
Statut: CONSTRUCTION_CANONIQUE_V1_6

Contexte:
- V1-5D est validee.
- policyengine est appele reellement.
- policyengine produit raw_policy_action LONG et sizing 0.05 depuis entree placeholder.
- V1 filtre correctement safe_action FLAT.
- broker reste FLAT, size 0.0, real_order_sent false.
- moneymanager legacy est documente D11 anomal:
  - capital hardcode 150000.0
  - BASEDIR incoherent
  - import modules.doubletempo casse
- V1 ne doit pas corriger le legacy.

Decision:
- Creer allocation_adapter.py dans demo_v1/adapters.
- Calculer une allocation paper shadow depuis raw_result.sizing.
- capital_paper explicite: 35000.0.
- decision_weight explicite: 0.0.
- max_policy_sizing explicite: 0.20.
- Calculer raw_policy_notional_paper pour observation.
- Garder allocated_size=0.0 tant que safe_action=FLAT.
- Garder allocated_size=0.0 tant que decision_weight=0.0.
- Broker side force FLAT si allocated_size=0.0.
- Ne pas importer moneymanager legacy.
- Ne pas lire state.json racine.
- Ne pas modifier legacy, crontab, systemd.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- D11_ARBITRAGES_V1: capital parametre explicite, pas demostate implicite.
- Phase 115: decisionweight 0.0, aucune application mecanique.

Issue attendue:
- V1_6_OK.
- policyengine_called true.
- raw_policy_action LONG possible.
- safe_action FLAT.
- raw_policy_sizing 0.05 observe.
- raw_policy_notional_paper 1750.0 possible.
- allocated_size 0.0.
- broker side FLAT.
- real_order_sent false.
