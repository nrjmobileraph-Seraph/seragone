# DECISION_V1_6B_METEO_MONDES_SCHEMA_CANONIQUE

Date UTC: 2026-05-13 22:39
Auteur souverain: Raphael Boussy
Statut: CONSTRUCTION_CANONIQUE_V1_6B

Contexte:
- V1-6A est validee.
- policyengine est appele reellement.
- raw_policy_action LONG est observe.
- safe_action FLAT filtre correctement le placeholder.
- allocation paper shadow observe raw_policy_sizing 0.05.
- allocated_size reste 0.0.
- broker side reste FLAT.
- real_order_sent reste false.
- V1 next_step proposait meteo mondes ou moneymanager wrapper explicite.

Decision:
- Brancher meteo mondes avant moneymanager wrapper.
- Creer demo_v1/adapters/meteo_mondes_adapter.py.
- Produire un mondes_state V1 structure selon le schema canonique Day 8.
- Les mondes restent METEO_SEULEMENT.
- Les mondes ne produisent aucune action broker.
- Les mondes ne modifient ni policy_action ni safe_action.
- Ajouter raw_signal, interpretation, decision, traceability_id.
- Ajouter minute_profile et second_profile.
- Source provisoire: V1_SKELETON_METEO_CANONIQUE.
- Ne pas importer multiversv2 a ce stade.
- Ne pas lire mondesrecursifs100m.csv.
- Ne pas lire state.json racine.
- Ne pas modifier legacy, crontab, systemd.
- Ecrire uniquement states V1.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- R1: les mondes ne tirent pas, les mondes donnent la meteo.
- R3: rawsignal, interpretation, decision, traceabilityid obligatoires.

Issue observee:
- V1_6B_OK.
- mondes_state.module meteo_mondes_adapter.
- mondes_state.usage METEO_SEULEMENT.
- mondes_state.decision.action FLAT.
- mondes_state.decision.decision_directe false.
- policyengine_called true.
- safe_action FLAT.
- allocated_size 0.0.
- broker_side FLAT.
- real_order_sent false.
