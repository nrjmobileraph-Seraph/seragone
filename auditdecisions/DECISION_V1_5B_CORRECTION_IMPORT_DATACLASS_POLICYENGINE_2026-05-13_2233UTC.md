# DECISION_V1_5B_CORRECTION_IMPORT_DATACLASS_POLICYENGINE

Date UTC: 2026-05-13 22:33
Auteur souverain: Raphael Boussy
Statut: CORRECTION_CANONIQUE_V1_5

Contexte:
- V1-5 a tente de charger policyengine via importlib.
- Le module cible contient @dataclass.
- Python 3.12 exige que le module soit inscrit dans sys.modules avant exec_module.
- L'import dynamique V1 ne l'inscrivait pas.
- Crash observe: AttributeError NoneType __dict__ dans dataclasses.py.
- Aucun ordre reel n'a ete envoye.
- Le legacy n'a pas ete modifie.

Decision:
- Corriger uniquement demo_v1/adapters/policyengine_adapter.py.
- Inserer le module dans sys.modules avant exec_module.
- En cas d'echec import/appel, retourner un state V1 explicite au lieu de crasher.
- Garder broker paper only, size zero.
- Ne pas modifier le legacy.
- Ne pas modifier crontab.
- Ne pas modifier systemd.
- Ne pas ecrire state.json racine.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- D11_ARBITRAGES_V1: appel pur, parametres explicites, legacy invisible pour V1.

Issue attendue:
- V1-5B produit V1_5_OK.
- policyengine_state documente soit called true, soit refus propre.
