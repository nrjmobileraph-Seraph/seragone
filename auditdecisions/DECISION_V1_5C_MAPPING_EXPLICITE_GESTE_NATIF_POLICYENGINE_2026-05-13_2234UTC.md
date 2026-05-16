# DECISION_V1_5C_MAPPING_EXPLICITE_GESTE_NATIF_POLICYENGINE

Date UTC: 2026-05-13 22:34
Auteur souverain: Raphael Boussy
Statut: CORRECTION_CANONIQUE_V1_5

Contexte:
- V1-5B a produit V1_5_OK.
- policyengine source cible chargee: production/decision/policy_engine.py.
- Hash observe: 5f5b8fd0b75d6cc8c95bbcadab9aabed14accdf21c9afcf6cf91057224c5aa35.
- Signature reelle observee: decide(geste_natif, label_nc=None, composite_label=None, confluence_score=None, regime_fond=None).
- L'appel a ete refuse proprement car geste_natif manquait.
- Aucun ordre reel n'a ete envoye.

Decision:
- Fournir explicitement geste_natif depuis V1.
- Valeur provisoire: FLAT.
- Source du geste: V1_SKELETON_PLACEHOLDER.
- Ne pas deduire depuis le legacy.
- Ne pas lire state.json racine.
- Ne pas modifier le legacy.
- Ecrire uniquement states V1.
- Broker reste paper only, size zero.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- D11_ARBITRAGES_V1: parametres explicites, zero dependance chemin legacy implicite.

Issue attendue:
- policyengine_called true si decide accepte FLAT.
- action reste bornee LONG SHORT FLAT.
- broker reste SIMULATED_ONLY.
