# DECISION_V1_4B_CORRECTION_GARDE_FOU_AUTOSCAN

Date UTC: 2026-05-13 22:30
Auteur souverain: Raphael Boussy
Statut: CORRECTION_CANONIQUE_SQUELETTE_V1_4

Contexte:
- V1-4 a cree le couloir demo_v1.
- La premiere pulsation a ete refusee par DEMO_SAFETY_REFUSED.
- Cause: safety_v1.py scannait son propre fichier et detectait ses propres motifs interdits.
- Aucun ordre reel n'a ete envoye.
- Le blocage est sain, mais le scan doit exclure le fichier garde-fou lui-meme.

Decision:
- Corriger uniquement demo_v1/core/safety_v1.py.
- Exclure safety_v1.py de son propre scan.
- Ne pas modifier le legacy.
- Ne pas modifier crontab.
- Ne pas modifier systemd.
- Ne pas ecrire state.json racine.
- Relancer uniquement l'orchestrateur manuel V1.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- V1 contourne le legacy par orchestration explicite.

Issue attendue:
- La pulsation V1-4 doit produire SQUELETTE_OK.
