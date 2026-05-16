# DECISION_V1_6A_FIX_INTERFACE_DEMOBROKER

Date UTC: 2026-05-13 22:38
Auteur souverain: Raphael Boussy
Statut: CORRECTION_CANONIQUE_V1_6A

Contexte:
- V1-6A a compile.
- V1-6A a commence son execution.
- Crash observe:
  AttributeError: module adapters.demobroker has no attribute execute_paper_order
- Cause: mismatch de contrat entre orchestrateur_demo_total_v1_6.py et demobroker.py.
- Aucun ordre reel n'a ete envoye.
- Aucun legacy n'a ete modifie.

Decision:
- Corriger uniquement demo_v1/adapters/demobroker.py.
- Exposer execute_paper_order comme contrat canonique V1.
- Garder broker paper only.
- Forcer real_order_sent false.
- Forcer financial_reality FALSE.
- Forcer side FLAT si size <= 0.
- Ajouter alias compatibles pour anciens appels demo.
- Ne pas modifier le legacy.
- Ne pas lire state.json racine.
- Ne pas modifier crontab/systemd.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: le nom ne prouve pas le primetre, seul le contrat execute compte.
- D11_ARBITRAGES_V1: zero dependance legacy implicite.

Issue attendue:
- V1_6_OK.
- broker_side FLAT.
- size 0.0.
- real_order_sent false.
