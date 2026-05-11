# ACTE 24-bis — Précision : le silence du pipeline A7 est DU DESIGN

**Date (UTC)** : 2026-05-11T20:55:47Z
**Hash univers** : `2f1e2cccff95252a`

## Précision apportée à l'acte 24

L'acte 24 a attribué le silence du pipeline A7 à la variable `$SERAGONE`
non définie en environnement cron. Diagnostic Doctrine 12 complet :

1. Le fix `$SERAGONE` → chemins absolus est une amélioration réelle
   (meilleure pratique), mais n'était PAS la cause du silence.
2. Preuve cron : syslog montre que cron déclenchait déjà les 3 scripts
   avant le fix (timestamp logs 10 mai 20:22 UTC).
3. Cause RÉELLE du silence : le script `decision_to_order.py` est
   **idempotent par design** (DECRET_A7 §4.2 étape 7). Il compare le hash
   de (direction, finale, tireurs_alignes) au hash précédent et fait
   SKIP_IDEMPOTENT + exit 0 sans écrire si identique.
4. Depuis 08:52 UTC ce matin, `last_decision_hash` = 46179f12e7706390
   n'a pas changé → position nette stable → pipeline au repos normal.

## Démonstration end-to-end (injection signal test)

Le hash `last_decision_hash` a été volontairement invalidé à 20260511T205437Z
pour forcer une nouvelle génération d'ordre. Les artefacts produits
dans les 70 secondes suivantes sont archivés dans ce dossier comme
preuve end-to-end du pipeline A7 fonctionnel.

## Leçon Doctrine 12 (seconde application)

Deuxième acte-bis de la soirée (après 23-bis). Tous deux pour la
même cause : conclure avant d'avoir lu TOUTES les preuves. Doctrine 12
s'applique particulièrement à Perplexity dans ces sessions.
