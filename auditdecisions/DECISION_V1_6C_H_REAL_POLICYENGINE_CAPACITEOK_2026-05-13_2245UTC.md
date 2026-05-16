# DECISION_V1_6C_H_REAL_POLICYENGINE_CAPACITEOK

Date UTC: 2026-05-13 22:45
Auteur souverain: Raphael Boussy
Statut: HYGIENE_CANONIQUE_V1_6C_VALIDEE

Contexte:
- V1-6C a produit CAPACITEOK meteo.
- rawsignal, interpretation, decision, traceabilityid sont presents.
- decision_state transmet meteo_traceabilityid.
- allocation reste zero.
- broker reste FLAT.
- real_order_sent reste false.
- Un premier passage V1-6C avait perdu la preuve d'appel reel policyengine.
- V1-6C-H corrige ce point.
- policyengine_state.real_call_ok est true.
- policyengine_state.signature est non null.
- raw_result.adapter_exception est absent.
- raw_policy_action LONG est observe depuis policyengine reel.
- safe_action reste FLAT.

Decision:
- Valider V1-6C-H comme hygiene canonique V1-6C.
- Conserver l'appel reel policyengine avec real_call_ok obligatoire.
- Conserver CAPACITEOK strict avec check POLICYENGINE_real_call.
- Interdire fallback adapter silencieux.
- Garder les mondes METEO_SEULEMENT.
- Garder l'allocation en shadow paper.
- Garder le broker paper FLAT.
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

Issue validee:
- V1_6C_H_OK.
- capaciteok_ok true.
- policyengine_state.real_call_ok true.
- policyengine_state.signature non null.
- raw_result.adapter_exception absent.
- failed_checks vide.
- safe_action FLAT.
- allocated_size 0.0.
- broker_side FLAT.
- real_order_sent false.

Next step:
- V1-6D moneymanager wrapper explicite.
- Le wrapper devra passer capital, aplomb et tempo explicitement.
- Le wrapper ne devra pas importer les chemins legacy implicites.
- Le wrapper ne devra pas ecrire dans le legacy.
