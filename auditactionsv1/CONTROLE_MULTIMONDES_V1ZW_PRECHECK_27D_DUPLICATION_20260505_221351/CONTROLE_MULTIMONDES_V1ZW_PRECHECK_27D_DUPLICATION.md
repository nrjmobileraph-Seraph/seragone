# CONTROLE MULTIMONDES V1Z-W — PRECHECK 27D DUPLICATION

Date UTC: 2026-05-05T22:13:52+00:00

Mode : PRECHECK documentaire elargi, lecture seule pure. Aucune execution Python du candidat. Aucun import. Aucun touch caches live. Aucun mv/cp hors auditactionsv1. Phase 115 preservee. decision_weight=0.0. vrais_yeux.py INTOUCHABLE.

## 1. Verdict

V1ZW_PRECHECK_27D_OK_IDENTIQUE_PRET_DECRET

## 2. Selection paire canonique (autodetection)

- Pattern de detection (case-insensitive) : `*27d*4*approch*.py`
- Inventaire total : 14 occurrences, 1 groupes sha256 uniques
- Classification :
  - RACINE_CANONIQUE_CANDIDATE : 1
  - RESEARCH_CANONIQUE_CANDIDATE : 1
  - PALETTE_CLAUDE_COPY : 1
  - AUTRE_COPY : 11
- Paire canonique RACINE   : `./test_27d_4approches.py` (sha256 = 2debd5d63c04d64ca8311e7f316c282e5c1ba32b2ced8056334b9bd9364ae36f)
- Paire canonique RESEARCH : `./research/test_27d_4approches.py` (sha256 = 2debd5d63c04d64ca8311e7f316c282e5c1ba32b2ced8056334b9bd9364ae36f)
- Paire dans le meme groupe sha256 : True

## 3. Compteurs decisifs

- side_effects + broker racine : 0
- side_effects + broker research : 0
- diff non vide racine vs research : False
- cache_pollution detectee : False

## 4. Ancrage Git

- V1ZV precheck : 4c1f2f70
- HEAD au lancement : `4c1f2f706962cd0fe701a86a94ae474be3068c79`

## 5. Artefacts produits

| Fichier | Description |
|---------|-------------|
| inventory_27d_candidates.tsv | Inventaire complet path/size/mtime/sha256/classification/groupe |
| inventory_27d_candidates.sha256 | Grouping sha256 -> [paths] |
| selection_paire.json | Paire canonique selectionnee + comptes par classification |
| diff_racine_vs_research.diff | diff -u si paire identifiee |
| ast_scan_racine.json | Scan AST racine (open write, write_attrs, fs_attrs, subprocess, imports reseau/broker) |
| ast_scan_research.json | Scan AST research (idem) |
| hashes_live_avant.sha256 / hashes_live_apres.sha256 / diff_caches_v1zw.txt | Preuve non-pollution caches |
| manifest.json | Manifest avec sha256 de chaque artefact |

## 6. Posture maintenue

Aucune execution Python du candidat. Aucun import du candidat. Aucun touch caches live. Aucun mv/cp hors auditactionsv1. Aucun broker. Aucun cron. Aucun systemd. Aucune sortie Phase 115. vrais_yeux.py INTOUCHABLE.

## 7. Suite conditionnelle

- Si verdict = OK_IDENTIQUE_PRET_DECRET : decret signable a rediger.
- Si verdict = DIFF_A_LIRE : Raphael lit diff_racine_vs_research.diff avant tout decret.
- Si verdict = BLOQUE_CHEMIN_ABSENT : Raphael clarifie le nommage ou cree le fichier manquant.
- Si verdict = BLOQUE_SIDE_EFFECT : Raphael decide whitelist ou abandon.
- Si verdict = BLOQUE_DUPLICATION_AMBIGUE : Raphael tranche quel candidat racine/research fait foi.
