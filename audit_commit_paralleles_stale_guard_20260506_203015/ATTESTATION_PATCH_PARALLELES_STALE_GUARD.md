# ATTESTATION — PATCH PARALLÈLES STALE GUARD

Date UTC : 2026-05-06T20:30:15+00:00

Verdict : PATCH_PARALLELES_STALE_GUARD_OK

Contexte :
- HEAD local synchronisé avec origin/main avant commit.
- Patch limité à mondes_paralleles_engine.py.
- Objectif : éviter qu'une date finale avec sous-signaux 18D incomplets déclenche un signal bear/fort.
- Mécanisme : évaluer le dernier jour sain, exposer requested_date/input_lag_days/stale_input, neutraliser signal_bear et signal_fort si stale_input=true.
- Cohérent avec STATUS_PAUSE_MONDES_PARALLELES_20260506.md et DECISION_OBSERVABILITE_SERAGONE_20260506_SOIR.md.

Périmètre :
- Aucun ajout massif de fichiers non suivis.
- Aucun reset.
- Aucun nettoyage destructif.
