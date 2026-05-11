# ACTE 24 — Pipeline A7 end-to-end vérifié + fix variable $SERAGONE

**Date (UTC)** : 2026-05-11T20:52:16Z
**Hash univers** : `efea64be79b3af5b`

## Exposé

Le pipeline A7 (decision_to_order → prudence_demo_runner → demobroker)
était silencieux depuis le 10 mai 20:22 UTC. Diagnostic Doctrine 12 :
les logs étaient vides de 0 ligne, pas juste "rien d'intéressant".

## Cause identifiée

Les 3 lignes crontab utilisaient la variable `$SERAGONE` non définie
dans l'environnement cron (cron n'hérite pas des variables shell).
Conséquence : `cd $SERAGONE` = `cd ` (vide) = reste dans $HOME,
puis `python3 demo/generator/...` introuvable, échec silencieux.

## Disposition

1. Crontab corrigée : `$SERAGONE` → `/home/ubuntu/seragone` (chemin absolu)
2. Backup crontab pré-fix conservé : `backups_crontab/crontab_pre_fix_SERAGONE_20260511T205215Z.txt`
3. Preuve : logs repeuplés après 70s d'attente (voir fichiers joints)
4. Pipeline A7 démontré end-to-end fonctionnel

## Leçon Doctrine 12 appliquée

Diagnostic fondé sur les logs réels (0 ligne = cron ne s'exécute pas),
pas sur les noms de dossiers. Distinction faite entre "pipeline cassé"
et "pipeline non déclenché par cron" — le code était sain.

## Successeur prévu

ACTE 25 — rapport end-to-end markdown dans demo/reports/ (maillon manquant)
