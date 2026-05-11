# DOCTRINE — MOTEUR META SERAGONE (le moteur d'évolution)

Date : 2026-04-28 ~12:40 UTC
Auteur : Raphael Boussy
Statut : VISION CANONIQUE — à implémenter progressivement

---

## Principe fondamental

Séragone doit lire la courbe comme un livre ouvert et tradable, à n'importe
quelle temporalité — de la seconde au cycle de 4 ans.

Capacité à trader :
- toutes durées
- toutes directions : LONG, SHORT
- mode GRID si temps mort détecté ou incapacité de trouver une temporalité tradable

Posture épistémique : **JAMAIS RIEN N'EST SU.**

Toute lecture est provisoire. Toute décision est conditionnelle. Toute prédiction
est testée et reformulée. Le système accepte ses zones d'aveuglement et les
traite comme des points d'entrée pour l'évolution, pas comme des défaillances.

---

## Le moteur META — fonctionnement canonique

### 1. Détection de l'aveuglement
Quand Séragone voit des endroits de la courbe qu'il n'arrive pas à lire,
le moteur META détecte cette zone d'incompréhension.

### 2. Activation des capacités existantes
Le moteur META enclenche les modules qui peuvent permettre de savoir la réponse
par trois mécanismes complémentaires :
- **Croisement** : combiner plusieurs voix pour faire émerger une lecture cohérente
- **Assimilation** : intégrer les nouveaux signaux dans le modèle existant
- **Projection** : extrapoler depuis les modèles connus vers la zone non lue

### 3. Détection du manque
Si les modules existants ne suffisent pas à répondre, le moteur META détecte
un manque dans son arsenal.

### 4. Sollicitation de création
Le moteur META a la capacité de solliciter la création d'un nouveau module
capable de répondre au manque identifié.

Cette sollicitation est faite à travers la lecture de tous les outils existants
et l'identification précise de ce qui leur fait défaut.

---

## Arsenal en évolution permanente

Séragone doit avoir un arsenal de capacités en évolution. Pas une boîte à outils
figée — un système vivant qui :
- Identifie ses propres faiblesses
- Mesure ses propres performances
- Demande des nouveaux modules quand nécessaire
- Classe ses modules selon leur efficacité réelle

---

## Articulation avec les 6 modules production/meta/

Les modules existants posent les fondations de ce moteur :

| Module | Rôle dans le moteur META |
|---|---|
| memoire_evenementielle | Trace des événements canoniques (qu'est-ce qui s'est passé) |
| memoire_proactive | Mémoire anticipative (qu'est-ce qui pourrait se passer) |
| meta_controller | Chef d'orchestre du moteur META |
| module_contract_validator | Vérifie que les modules respectent leurs contrats |
| module_lifecycle_controller | Gère création/activation/archivage des modules |
| module_ranker | Classe les modules selon leur efficacité |

À ce stade, ces modules sont **posés mais pas pleinement intégrés** dans la
chaîne décisionnelle active.

---

## Relation avec les modes système

Le moteur META est probablement LE module qui peut décider du passage entre :
- OBSERVATOIRE_PASSIF
- PRODUCTION_OBSERVATOIRE
- PRODUCTION_ACTIVE

Quand le moteur META juge que l'arsenal est suffisant pour une zone donnée
(temporalité, direction, conditions), il peut autoriser le passage en mode
PRODUCTION_ACTIVE pour cette zone uniquement.

Le système peut donc être en plusieurs modes simultanément selon le périmètre
d'analyse.

---

## Doctrine d'humilité épistémique

"Jamais rien n'est su" — c'est la phrase canonique du moteur META.

Chaque module doit accepter de se tromper. Chaque mesure doit être contre-vérifiée.
Chaque décision doit être révisable. C'est ce qui fait la différence entre
un système rigide qui casse et un système vivant qui évolue.

---

## Statut

- VISION posée le 28/04 12:40 UTC
- 6 modules infrastructure existent (production/meta/, mtimes 23/04)
- Intégration partielle : meta_controller appelé par orchestrateur.sh
- Implémentation progressive à venir
- Ce document est canonique : il guide les futures décisions sur le moteur META


---

## ARTICULATION VISION ↔ BLUEPRINT (28/04 16:15 UTC)

Cette doctrine pose la **vision** du moteur META.
Elle est **opérationnalisée** dans le blueprint :

→ `audit/meta/META_GLOBAL_ENGINE.md` (v1.1, 28/04)

### Lecture canonique
- DOCTRINE = pourquoi (vision posée 28/04 12:40 UTC)
- BLUEPRINT = comment (plan 3 stades, gouvernance, métriques)

### Statut canonique combiné
- Vision : POSÉE (canonique)
- Blueprint : CANDIDAT_CANONISABLE_COMME_BLUEPRINT
- Modules opérationnels : OBSERVATOIRE_STADE_1 (autorisé)
- Modules avancés (Stade 2, 3) : VERROUILLÉS jusqu'à preuve

### Règle d'or (du blueprint, citée intégralement)
"META ne touche pas au volant. Il regarde la route, lit la carte,
et quand il voit un trou, il lève la main. C'est Raphaël qui
décide s'il faut construire un nouveau moteur."


---

## ARTICULATION VISION ↔ BLUEPRINT (28/04 16:15 UTC)

Cette doctrine pose la **vision** du moteur META.
Elle est **opérationnalisée** dans le blueprint :

→ `audit/meta/META_GLOBAL_ENGINE.md` (v1.1, 28/04)

### Lecture canonique
- DOCTRINE = pourquoi (vision posée 28/04 12:40 UTC)
- BLUEPRINT = comment (plan 3 stades, gouvernance, métriques)

### Statut canonique combiné
- Vision : POSEE (canonique)
- Blueprint : CANDIDAT_CANONISABLE_COMME_BLUEPRINT
- Modules opérationnels : OBSERVATOIRE_STADE_1 (autorisé)
- Modules avancés (Stade 2, 3) : VERROUILLES jusqu'à preuve

### Règle d'or (du blueprint, citée intégralement)
"META ne touche pas au volant. Il regarde la route, lit la carte,
et quand il voit un trou, il lève la main. C'est Raphaël qui
décide s'il faut construire un nouveau moteur."

