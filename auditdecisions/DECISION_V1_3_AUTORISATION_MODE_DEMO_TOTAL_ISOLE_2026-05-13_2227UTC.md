# DECISION_V1_3_AUTORISATION_MODE_DEMO_TOTAL_ISOLE

Date UTC: 2026-05-13 22:27
Auteur souverain: Raphael Boussy
Statut: DECISION_CANONIQUE_CONSTRUCTION_V1

Contexte:
- V1-2 a confirme une divergence runtime.
- STOP_BRANCHAGE_V1 reste maintenu pour tout branchement legacy/runtime.
- L'objectif souverain reste une demo totale de Sragone.
- Seul le mode financier reel doit etre inexistant.

Decision:
- AUTORISATION_MODE_DEMO_TOTAL_ISOLE = OUI.
- Objectif: tester Sragone dans sa totalite fonctionnelle.
- Sragone doit pouvoir penser, calculer, simuler, arbitrer, journaliser et produire ses states demo.
- Aucune execution financiere reelle n'est autorisee.

Frontiere absolue:
- Aucun ordre reel.
- Aucune cle API exchange.
- Aucun appel broker reel.
- Aucun ccxt actif capable d'ordre.
- Aucun branchement Kraken, OKX, Binance execution.
- Broker obligatoire: demobroker paper only.

Legacy:
- Legacy non modifie.
- Legacy non corrige.
- Legacy non relance.
- Crontab non modifie.
- Systemd non modifie.
- state.json racine non ecrit.
- state.json racine non consomme comme verite V1.

Construction V1:
- Creation autorisee d'un couloir parallele demo_v1.
- States V1 separes obligatoires.
- Logs V1 separes obligatoires.
- Rapports V1 separes obligatoires.
- Orchestrateur demo autorise uniquement en execution manuelle.
- Aucun daemon.
- Aucun cron.
- Aucun service systemd.

Doctrine appliquee:
- D7: vraie utilisation, fausse realite financiere.
- D9: un writer par state V1.
- D11: primetre prouve par lectures/ecritures reelles.
- D11_ARBITRAGES_V1: V1 contourne le legacy par orchestration explicite.

Issue:
- V1-4 peut construire le squelette MODE_DEMO_TOTAL_ISOLE.
- V1-5 pourra executer une premiere pulsation paper only apres verification.
