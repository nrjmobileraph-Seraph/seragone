# DECISION_V1_6C_CAPACITEOK_AUDIT

Date UTC: 2026-05-13 22:41
Auteur souverain: Raphael Boussy
Statut: CONSTRUCTION_CANONIQUE_V1_6C_REPRISE_PROPRE

Contexte:
- V1-6B-H est validee.
- Le premier patch V1-6C a ete refuse par mismatch de chaines dans orchestrateur_demo_total_v1_6.py.
- Les insertions attendues meteo_traceabilityid et write_json capaciteok_state n'ont pas ete prouvees.
- La cause est un patch par remplacement exact devenu fragile.
- Aucun ordre reel n'a ete envoye.
- Le legacy ne doit pas etre modifie.

Decision:
- Reprendre V1-6C par reecriture explicite des fichiers demo_v1 uniquement.
- Creer ou regraver capaciteok_audit.py.
- Regraver meteo_mondes_adapter.py avec rawsignal et traceabilityid.
- Regraver policyengine_adapter.py comme wrapper explicite.
- Regraver allocation_adapter.py comme shadow allocation explicite.
- Regraver demobroker.py comme paper broker strict.
- Regraver orchestrateur_demo_total_v1_6.py comme orchestrateur V1-6C complet.
- Auditer la chaine mondes -> decision -> allocation -> broker.
- Produire demo_v1/states/capaciteok_state.json.
- Integrer capaciteok_state dans statedemo.json.
- Faire echouer V1-6C si CAPACITEOK echoue.
- Ne pas modifier le legacy.
- Ne pas lire state.json racine.
- Ne pas modifier crontab/systemd.
- Ecrire uniquement states V1.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- R1: les mondes ne tirent pas.
- R3: rawsignal, interpretation, decision, traceabilityid obligatoires.

Issue attendue:
- V1_6C_OK.
- capaciteok_ok true.
- capaciteok_state.status CAPACITEOK.
- mondes_state.rawsignal present.
- mondes_state.traceabilityid present.
- decision_state.meteo_traceabilityid present.
- allocated_size 0.0.
- broker_side FLAT.
- real_order_sent false.
