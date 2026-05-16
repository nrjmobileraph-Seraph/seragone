# DECISION_V1_6B_HYGIENE_CANONIQUE_METADATA_REPORT

Date UTC: 2026-05-13 22:40
Auteur souverain: Raphael Boussy
Statut: CORRECTION_CANONIQUE_V1_6B

Contexte:
- V1-6B a produit V1_6B_OK.
- mondes_state est structure selon le schema meteo canonique.
- policyengine reste appele.
- raw_policy_action LONG reste observe.
- safe_action FLAT reste applique.
- allocation shadow reste size zero.
- broker reste FLAT, real_order_sent false.
- Des incoherences metadata restent visibles:
  - report suffix encore V1_6A.
  - scanned_files ne liste pas meteo_mondes_adapter.py.
  - certains reason strings mentionnent V1-6A.
  - le fichier decision V1-6B peut avoir ete pollue par sortie terminal.

Decision:
- Regraver proprement la decision V1-6B.
- Corriger les metadonnees orchestrateur V1-6B.
- Ajouter meteo_mondes_adapter.py dans scanned_files.
- Produire rapport suffixe V1_6B.
- Harmoniser reason strings V1-6B.
- Ajouter mondes_state dans status.
- Ne pas modifier le legacy.
- Ne pas lire state.json racine.
- Ne pas modifier crontab/systemd.
- Ecrire uniquement states V1.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: la preuve canonique doit etre lisible et rattachee aux lectures/ecritures reelles.
- R1: les mondes ne tirent pas, les mondes donnent la meteo.
- R3: rawsignal, interpretation, decision, traceabilityid obligatoires.

Issue attendue:
- V1_6B_OK.
- report suffix V1_6B.
- scanned_files inclut meteo_mondes_adapter.py.
- reasons mentionnent V1-6B.
- decision files propres.
- real_order_sent false.
