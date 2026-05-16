# DECISION_V1_5D_SEPARATION_RAW_POLICY_ACTION_SAFE_ACTION

Date UTC: 2026-05-13 22:36
Auteur souverain: Raphael Boussy
Statut: CORRECTION_CANONIQUE_V1_5

Contexte:
- V1-5C a appele policyengine avec succes.
- Entree explicite: geste_natif=FLAT, source=V1_SKELETON_PLACEHOLDER.
- Sortie observee policyengine: action=LONG, sizing=0.05.
- Raison observee: Fallback FLAT. Direction via regime de fond None.
- Aucun ordre reel n'a ete envoye.
- Taille broker observee: 0.0.

Probleme:
- Une entree placeholder neutre produit une direction LONG par fallback interne.
- Ce comportement doit etre observe mais pas transmis comme action executable V1.
- V1 doit separer action brute policy et action securisee broker.

Decision:
- Ajouter raw_policy_action.
- Ajouter safe_action.
- Si geste_source == V1_SKELETON_PLACEHOLDER alors safe_action=FLAT.
- Si decision_weight == 0.0 alors safe_action=FLAT.
- Si allocated_size == 0.0 alors broker side=FLAT.
- Conserver raw_result pour audit.
- Ne pas modifier le legacy.
- Ne pas lire state.json racine.
- Ne pas modifier crontab/systemd.
- Ecrire uniquement states V1.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- R1: les mondes ne tirent pas, les tireurs tirent, Policy/Aplomb garde la souverainete.
- Phase 115: decisionweight 0.0, aucune application mecanique.

Issue attendue:
- policyengine_called true.
- raw_policy_action LONG possible.
- safe_action FLAT.
- broker side FLAT.
- size 0.0.
