# DECISION_V1_4_CONSTRUCTION_SQUELETTE_MODE_DEMO_TOTAL_ISOLE

Date UTC: 2026-05-13 22:28
Auteur souverain: Raphael Boussy
Statut: DECISION_CANONIQUE_CONSTRUCTION_V1_4

Objet:
Construire le squelette MODE_DEMO_TOTAL_ISOLE pour aller vers une demo totale de Sragone.

Cap:
- Tester Sragone dans sa totalite fonctionnelle.
- Garder le legacy intact.
- Bloquer uniquement le reel financier.
- Autoriser uniquement le broker paper demo.
- Executer uniquement en manuel pendant V1-4.

Interdits:
- Aucun ordre reel.
- Aucune cle API exchange.
- Aucun appel broker reel.
- Aucun ccxt actif.
- Aucun crontab.
- Aucun systemd.
- Aucune modification legacy.
- Aucune ecriture state.json racine.

Autorises:
- Creation demo_v1.
- Creation demo_v1/states.
- Creation demo_v1/logs.
- Creation demo_v1/reports.
- Creation demobroker paper only.
- Creation orchestrateur_demo_total.py manuel.
- Premiere pulsation squelette paper only.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- D11_ARBITRAGES_V1: V1 contourne le legacy par orchestration explicite.

Issue:
V1-4 construit le couloir parallele.
V1-5 branchera progressivement les organes qualifies, un par un, sans toucher au legacy.
