# DOCTRINE 12 — LIRE AVANT DE CONCLURE

**Date de gravure** : 2026-05-11
**Contexte** : ACTE 23 (mask multivers basé sur diagnostic faux) + ACTE 23-bis (annulation)

## Énoncé

Avant d'émettre un diagnostic sur un composant Séragone, ou de proposer
une action destructive (mask, disable, rm, stop définitif), toute IA
intervenant sur le système DOIT :

### Règle 1 — Logs réels, pas noms de dossiers
Lire les logs réels du composant via `journalctl -u <service>` ou les
fichiers `.log` datés. Les noms de dossiers (`*_fail`, `*_stop`,
`*_cloture`) ne prouvent RIEN sur l'état actuel du composant.

### Règle 2 — Type systemd
Distinguer les trois types de services systemd :
- **oneshot** : exécute puis meurt → `inactive (dead)` entre deux
  déclenchements est l'ÉTAT NORMAL.
- **simple/forking** : daemon persistant → `inactive (dead)` = problème.
- **timer** : déclencheur, toujours `active (waiting)` s'il fonctionne.

### Règle 3 — Preuve datée
Avant toute action destructive, exiger une preuve log-based datée de
moins de 24h du dysfonctionnement allégué. Sans preuve : pas d'action.

### Règle 4 — Désambiguïsation des chantiers
Un dossier `audit/suiteX_chantierY_fail` ne prouve PAS qu'un composant
nommé différemment est cassé. Lire le contenu du dossier d'audit avant
de lier deux composants.

### Règle 5 — Réversibilité par défaut
Toute action destructive doit être formulée pour être réversible en
une commande (stop plutôt que rm, mask plutôt que delete, backup
avant toute modification).

## Sanction

Tout acte gravé en violation de cette doctrine doit être annulé par
acte-bis dans les 24h suivant détection. L'acte-bis reconnaît
explicitement la faute, en capture la cause, et rétablit l'état
antérieur.

## Précédent

- ACTE 23 (11 mai 2026 22:43 CEST) — mask seragone-multivers sur
  diagnostic faux
- ACTE 23-bis (11 mai 2026 22:45 CEST) — annulation, réactivation
  3 minutes après détection de l'erreur
