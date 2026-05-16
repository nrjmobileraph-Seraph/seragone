# DECISION_V1_6D_MONEYMANAGER_WRAPPER_EXPLICITE

Date UTC: 2026-05-13 22:48
Auteur souverain: Raphael Boussy
Statut: CONSTRUCTION_CANONIQUE_V1_6D

Contexte:
- V1-6C-H est validee.
- policyengine est appele reellement.
- CAPACITEOK est true.
- allocation reste zero.
- broker reste FLAT.
- real_order_sent reste false.
- Document 19 qualifie moneymanager comme integrable progressivement.
- Document 19 signale les anomalies D11 moneymanager:
  - capital hardcode 150000.0.
  - BASEDIR aplomb incoherent.
  - import modules.doubletempo casse.
- Les arbitrages D11 V1 imposent:
  - capital explicite.
  - aplomb explicite.
  - tempo explicite.
  - aucun chemin legacy implicite.
  - aucun write legacy.

Decision:
- Creer demo_v1/adapters/moneymanager_adapter.py.
- Ne pas importer production/allocation/moneymanager.py.
- Referencer son hash comme source qualifiee.
- Reproduire uniquement le contrat V1: calculer exposition theorique paper et exposition executable.
- Passer capital_paper explicitement.
- Passer decision_weight explicitement.
- Passer tempo_state explicitement.
- Passer aplomb_state explicitement.
- Ecrire demo_v1/states/moneymanager_state.json uniquement via orchestrateur.
- Integrer moneymanager_state dans statedemo.json.
- Ajouter checks CAPACITEOK:
  - MONEYMANAGER_present.
  - MONEYMANAGER_explicit_inputs.
  - MONEYMANAGER_no_legacy_import.
  - MONEYMANAGER_executable_zero.
- Garder allocated_size 0.0 tant que decision_weight vaut 0.0.
- Garder broker FLAT.
- Garder real_order_sent false.
- Ne pas modifier le legacy.
- Ne pas lire state.json racine.
- Ne pas modifier crontab/systemd.

Issue attendue:
- V1_6D_OK.
- moneymanager_state.present true.
- moneymanager_state.explicit_inputs true.
- moneymanager_state.legacy_imported false.
- moneymanager_state.executable_size 0.0.
- allocation_state.allocated_size 0.0.
- broker_state.side FLAT.
- real_order_sent false.
