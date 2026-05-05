# CONTROLE MULTIMONDES V1Z-Z — PHASE 2 27D EXEC

Date UTC : 2026-05-05T22:54:07Z
HEAD au lancement : cd39ea2bc96d57909b12a40637975f0ff514048a
Ancrages : V1ZY-bis (cd39ea2b) / V1ZY (ad7afa27) / V1ZX (b2cca117) / V1ZW (4f2a18c3) — tous ancetres verifies

## 1. Nature du document

Phase 2 du decret V1ZX. Execution subprocess de `test_27d_4approches.py` dans la sandbox V1ZY (`sandbox_27d_reexec/`), via `env -i` filtre, timeout 120s, HOME isole. Aucun broker, cron, systemd, ecriture live, branchement runtime.

## 2. Verdict V1ZZ

**V1ZZ_PHASE2_27D_EXEC_NONZERO**

Subprocess RC=1. Voir stderr_full.log pour diagnostic.

## 3. Resume execution

| Mesure | Valeur |
|---|---|
| Returncode | `1` |
| Duration (secondes) | 0 |
| Timeout 120s atteint | non |
| stdout lignes | 0 |
| stderr lignes | 4 |
| sha256 script match attendu | OUI |
| Caches live identiques avant/apres | OUI |
| diff_phase2.txt vide | OUI |

## 4. Configuration subprocess

```
cwd      : /home/ubuntu/seragone/auditactionsv1/CONTROLE_MULTIMONDES_V1ZX_REEXEC_27D_20260505_223529/sandbox_27d_reexec
cmd      : python3 test_27d_4approches.py
timeout  : 120s (preserve-status)
env      : env -i (whitelist stricte)
           PATH=/usr/local/bin:/usr/bin:/bin
           HOME=/home/ubuntu/seragone/auditactionsv1/CONTROLE_MULTIMONDES_V1ZX_REEXEC_27D_20260505_223529/_v1zz_isolated_home
           LANG=C.UTF-8
           LC_ALL=C.UTF-8
           TERM=dumb
           PYTHONNOUSERSITE=1
           PYTHONDONTWRITEBYTECODE=1
           PYTHONUNBUFFERED=1
home iso : /home/ubuntu/seragone/auditactionsv1/CONTROLE_MULTIMONDES_V1ZX_REEXEC_27D_20260505_223529/_v1zz_isolated_home
```

## 5. Inputs sandbox utilises

| Fichier | Taille | sha256 |
|---|---|---|
| `inputs/couches_123_daily.csv` | 239888 | `ae7def2ecce126d13e5a3a82f316cb126e963f9813f1e495f5d5a4ea11651fec` |
| `inputs/historique_27eq.csv` | 1836199 | `550c948a5339e0483a0aa9d286ff2295e9bf0d2fc08fc1b628ad4cf6f4a045d8` |

## 6. Artefacts V1ZZ produits dans REEXEC_DIR

Note : le manifest V1ZZ s appelle `manifest_v1zz.json` (et non `manifest.json`) pour ne pas ecraser le manifest V1ZY existant dans REEXEC_DIR.

| Fichier | Role |
|---|---|
| stdout_full.log | sortie stdout complete subprocess |
| stderr_full.log | sortie stderr complete subprocess |
| returncode.txt | code retour subprocess |
| run_report.json | metadonnees execution detaillees |
| outputs_inventory.txt | inventaire sandbox apres exec + diff avant/apres |
| outputs_sha256.txt | sha256 de tous les fichiers sandbox apres exec |
| hashes_live_avant_phase2.sha256 | snapshot caches live AVANT subprocess |
| hashes_live_apres_phase2.sha256 | snapshot caches live APRES subprocess |
| diff_phase2.txt | diff caches live (DOIT etre vide) |
| _v1zz_sandbox_inventaire_avant.txt | sha256 sandbox AVANT exec |
| _v1zz_sandbox_inventaire_apres.txt | sha256 sandbox APRES exec |
| _v1zz_time_report.txt | output /usr/bin/time -v si dispo |
| CONTROLE_MULTIMONDES_V1ZZ_PHASE2_27D_EXEC.md | ce document |
| manifest_v1zz.json | metadonnees machine-readable |

## 7. Contraintes canoniques rappelees

```
Phi*_CANON   : (M:0.28, V:0.33, S:0.26, H:0.26, G:0.42)
W_CANON      : (M:1.80, V:1.25, S:1.20, H:1.42, G:1.10)
Capital paper: 35 000 EUR
Cible exchange: Kraken (paper, decision_weight=0.0)
Phase actuelle: 115 LIVE_TEST_TOTAL_EN_CAGE
Modules INTOUCHABLES : vrais_yeux.py, vrais_yeux_stretched.py, village_le_vrai.py
```

## 8. Posture finale

Execution avec RC non nul. Lire stderr_full.log pour diagnostiquer la cause (input non resolu, exception Python, etc.). Si la cause est un layout sandbox (chemin attendu different), V1ZZ-bis pour reorganiser. Sinon retour amont (V1ZY-ter pour completer inputs).

D12 candidate : V1ZZ = VALIDATED (audit exec sandbox) != INSTALLED != PRODUCTION_ACTIVE.

---

*Posture L99 + OODA stricte maintenue.*
*Raphael voit. Claude calcule.*