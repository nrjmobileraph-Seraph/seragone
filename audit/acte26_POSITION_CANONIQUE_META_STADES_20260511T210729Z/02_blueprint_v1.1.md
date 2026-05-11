# META Global Engine — Blueprint final (v1.1)

**Document** : `META_GLOBAL_ENGINE.md`  
**Version** : 1.1 – figée  
**Date** : 2026-04-28  
**Statut canonique** : `CANDIDAT_CANONISABLE_COMME_BLUEPRINT`  
**Statut opérationnel** : `OBSERVATOIRE_STADE_1`  
**Droit d'influence** : `AUCUNE_DECISION_DIRECTE`  
**Auteur** : Raphaël + Assistant IA (chantier META‑0)

---

## 📌 Pourquoi ce document existe

Séragone possède déjà plus de 50 voix vivantes, un chef, des books, des pépites.
Mais il n'a pas encore **d'organe capable de se regarder lui‑même**,
de détecter ses propres angles morts et de proposer **où et comment s'améliorer**.

Le moteur META global est cet organe.
Il ne décide pas. Il ne trade pas.
Il observe, diagnostique, garde la mémoire, compare, et **sollicite** la création
de nouveaux modules lorsque la courbe n'est plus lisible.

Ce document est le **blueprint** de ce moteur.
Il ne demande aucune modification immédiate de la production.
Il définit ce que META sera, en trois stades, et comment il sera gouverné.


## 1. Objet

META Global Engine est l'organe de **surveillance, diagnostic et proposition d'évolution**.
Sa fonction première : **mesurer si Séragone lit correctement la courbe à tout moment**,
et quand ce n'est pas le cas, **spécifier exactement ce qui manque** pour y parvenir.

META ne peut pas :
- Décider d'un trade.
- Modifier Aplomb, Policy Engine ou Money Manager.
- Changer la production sans validation humaine.


## 2. Architecture cible (résumé de l'audit META‑0)

| Module | Rôle | Score (0‑5) |
|--------|------|---------------|
| `memoire_evenementielle.py` | Collecte des signaux, stockage vectorisé, analogues passés. | 4 |
| `memoire_proactive.py` | Feedback moteur/policy, synthèse de santé. | 4 |
| `module_ranker.py` | Classement des modules par utilité/stabilité. | 4 |
| `module_contract_validator.py` | Vérification des schémas de sortie (outil). | 2 |
| `meta_controller.py` | Application bornée de propositions (après validation humaine). | 3 |
| `module_lifecycle_controller.py` | Propositions de transition de statut des modules. | 3 |
| `memoirerouter.py` (à créer) | Orchestrateur interne (calendrier, routage). | 0 |


## 3. Flux de données

### Stade 1 (collecte seule)
- **memoire_evenementielle.py** : lit sources historiques → écrit `ANALOGUES_FILE` et `HISTORY_CSV`.
- **memoire_proactive.py** : lit signaux et prix → écrit `ANALOGUES_FILE`, `MEMOIRE_STATE`, `SYNTHESE_FILE`.
- **module_ranker.py** : lit `REGISTRY_FILE` → écrit `SNAPSHOT_FILE` (classement).

### Stade 2 (analyse)
- **module_contract_validator.py** vérifie la conformité des états de sortie.
- **module_lifecycle_controller.py** (mode dry‑run) propose des changements de statut sans les exécuter.
- **meta_controller.py** (mode rapport) lit les propositions et génère des suggestions.

### Stade 3 (proposition)
- Les modules de décision bornée peuvent **soumettre** des ajustements (seuils, statuts) et surtout **produire une spécification de manque** (`META_MISSING_MODULE_SPEC.md`) quand une zone aveugle persiste. Cette spécification est transmise à Raphaël qui décide de la suite.


## 4. Règles de gouvernance (intangibles)

1. META ne **décide jamais** à la place d'Aplomb, du Policy Engine ou du Money Manager.
2. Toute proposition d'ajustement ou de nouveau module doit être **validée par Raphaël**.
3. Aucun module META ne peut **s'auto‑promouvoir**.
4. Chaque changement est **réversible** (rollback documenté).
5. META ne **lance jamais** d'ordre live.
6. META écrit **uniquement** dans ses propres fichiers (`states/meta_*.json`, `audit/meta/`).


## 5. Déploiement : trois stades, un seul est autorisé aujourd'hui

### Stade 1 — META observatoire (autorisé immédiatement)

**Modules activés** :  
- `memoire_evenementielle.py`  
- `memoire_proactive.py`  
- `module_ranker.py`

**Règles** :  
- Écriture uniquement dans `states/meta_*.json` et `audit/meta/`.  
- Aucune modification du registre des modules.  
- Objectif : 14 jours de données mémoire pour avoir une base d'observation fiable.

**Pourquoi seulement le Stade 1 ?**  
Parce que les modules META n'ont pas encore fait leurs preuves en conditions réelles.
Le blueprint est bon, le moteur actif ne l'est pas encore.
On commence par observer, pas par agir.

### Stade 2 — META assistant (verrouillé, nécessite 14 jours de Stade 1 + validation)

**Ajouts** :  
- `module_contract_validator.py`  
- `module_lifecycle_controller.py` en mode `--dry-run`  
- `meta_controller.py` en mode rapport  

**Sortie** : un rapport hebdomadaire `META_WEEKLY_REPORT.json` contenant diagnostic, alertes et propositions (non exécutées).

### Stade 3 — META proposant (verrouillé, nécessite validation humaine du Stade 2)

**Ajout** : capacité de **spécification de manque**.  
META pourra produire une fiche `META_MISSING_MODULE_SPEC.md` lorsqu'une zone aveugle est identifiée. Cette fiche sera soumise à Raphaël, qui pourra alors demander la génération assistée d'un nouveau module.


## 6. Métriques de succès

- **Couverture mémoire** : jours de signaux enregistrés sans erreur.
- **Zones aveugles détectées** : nombre de périodes où la confluence est faible et le drawdown conditionnel anormal.
- **Qualité des spécifications** : taux de validation humaine des propositions.
- **Absence de dérive** : zéro modification non autorisée du registre ou des décisions de production.


## 7. Dépendances

- `modulesregistry.json` (inventaire des modules à observer).
- `associationscandidates_v5_2.json` (hypothèses de confluence).
- États quotidiens de production (lecture seule).
- **A046 à A049** : les associations META déjà définies (pipeline mémoire, contrôle de schéma, dérive, ajustement borné) **restent référencées comme briques internes observatoires** du moteur META.  
- **A060** : nouvelle entrée dans le registre candidat, qui coiffe l'ensemble.


## 8. A060 — META Global Engine observatoire

**Famille** : `META_GOUVERNANCE`  
**Statut** : `OBSERVATOIRE`  
**Droit d'influence** : `SANTE_META / PROPOSITION_SEULE`  
**Hypothèse** : META Global Engine, en tant que blueprint, peut devenir l'organe de diagnostic et de proposition d'évolution de Séragone, à condition de faire ses preuves au Stade 1.  
**Métriques de validation** : stabilité des états mémoire pendant 14 jours, détection d'au moins une zone aveugle confirmée, respect des règles de gouvernance.

A060 ne remplace pas A046‑A049, elle les orchestre.


## 9. Évaluation canonique

**Statut canonique** : `CANDIDAT_CANONISABLE_COMME_BLUEPRINT`  
Ce statut signifie que **la conception est jugée bonne**, mais que le moteur n'a pas encore le droit de modifier quoi que ce soit dans le système.  
Il devra suivre le chemin suivant avant toute activation au‑delà du Stade 1 :

1. Déploiement du Stade 1 pendant 14 jours.
2. Rapport d'observation (`META_STAGE1_REPORT.md`).
3. Décision de Raphaël : passage ou non au Stade 2.
4. Si le Stade 2 est concluant, le blueprint pourra évoluer vers `CANDIDAT_CANONISABLE_MOTEUR` puis `ACTIF` uniquement après validation complète.


## 10. Prochaines actions immédiates (Stade 1)

1. Sauvegarder ce document sur le VPS : `audit/meta/META_GLOBAL_ENGINE.md`
2. Ajouter l'entrée **A060** dans le registre candidat `associationscandidates_v5_2.json`, sans modification de `modulesregistry.json` ni des fichiers de production.
3. Lancer manuellement une première exécution des trois modules mémoire/classement.
4. Inspecter les fichiers produits.
5. Si trois exécutions manuelles successives sont propres, prévoir un cron quotidien séparé pour le Stade 1, après validation explicite de Raphaël.


**Règle d'or** : META ne touche pas au volant. Il regarde la route, lit la carte, et quand il voit un trou, il lève la main. C'est Raphaël qui décide s'il faut construire un nouveau moteur.
