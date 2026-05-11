# ACTE 22 — SERAGONE_ONE V1 — SOCLE DE LA VISION TOTALE

**Date (UTC)** : 2026-05-11T20:39:17Z
**Hash univers au moment de la gravure** : `439cc638637886ae`
**Hash script** : `dff3b21aa41c2212`
**Hash SERAGONE_ONE.md** : `cc557fdcb70945f2`

## Exposé

Séragone comptait 215 dossiers racine, 25 405 fichiers, 22 Go, 19 décrets,
10 attestations, 5 actes grave_*, 89 crons, 8 services systemd, 16 processus,
mais AUCUN POINT UNIQUE DE VÉRITÉ qui agrège cet état. À chaque session IA,
il fallait redécouvrir. Cet acte clôt cette ère.

## Disposition

1. Le fichier `canon/SERAGONE_ONE.md` est déclaré **source unique de vérité**
   de Séragone à toute date.
2. Le script `tools/seragone_one.py` est déclaré **générateur canonique**.
   Il découvre par filesystem (find, ls, ps, systemctl, crontab, git) sans
   aucune liste figée. Il ne peut rien oublier qui existe sur disque.
3. Un cron horaire (min 15) régénère SERAGONE_ONE.md. Git trace les diffs.
4. Le wrapper `seragone-total` affiche SERAGONE_ONE avec alerte de
   fraîcheur (> 2h = warn).
5. Protocole de session IA : toute IA qui reçoit le mot "Séragone" doit
   recevoir le contenu de `canon/SERAGONE_ONE.md` AVANT toute action.

## Garantie mécanique anti-oubli

- **Découverte pure** : le script n'a aucune liste figée. Il `find`.
- **Hash univers** : tout changement disque = hash différent = alerte.
- **Hash par dossier racine** (215) : changement ciblé détectable.
- **Cron horaire** : fraîcheur max 60 min garantie.
- **Git auto** : diff persisté si hash change.

## Couverture matérielle (mesurée à la gravure)

- 16757 fichiers totaux
- 215 dossiers racine
- 90 lignes cron
- 8 services systemd seragone
- 18 décrets
- 10 attestations
- 6 actes grave_*
- Registry production : 1756 modules

## Successeurs attendus

- **V2** : ajouter un RAG vectoriel local (ChromaDB) indexant les 25 405
  fichiers pour interrogation en langage naturel.
- **V3** : exposer via MCP server aux assistants IA (Claude Desktop,
  Perplexity) — chargement contextuel automatique.

**Signé mécaniquement par cohérence de hash.**
