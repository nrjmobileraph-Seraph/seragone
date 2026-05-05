# CONTROLE MULTIMONDES V1Z-Z-bis — PHASE 2-bis 27D EXEC ENV COMPAT

Date UTC : 2026-05-05T23:00:29Z
HEAD : 717f9c8c25903ac4c0984608b23ad44a06d788d2
Ancrages : V1ZZ (717f9c8c) / V1ZY-bis (cd39ea2b) / V1ZY (ad7afa27) / V1ZX (b2cca117) / V1ZW (4f2a18c3)

## 1. Nature du document

Phase 2-bis du decret V1ZX. Correctif env compat suite a echec V1ZZ (`ModuleNotFoundError: No module named 'pandas'` cause par PYTHONNOUSERSITE=1). Pre-diagnostic Python pour identifier les chemins reels de pandas/numpy, puis re-execution subprocess sandbox avec PYTHONPATH explicite injecte et PYTHONNOUSERSITE retire. env -i conserve, whitelist elargie minimalement.

## 2. Verdict V1ZZ-bis

**V1ZZBIS_PHASE2BIS_27D_EXEC_NONZERO**

Subprocess RC=1. Voir stderr_full_v1zzbis.log.

## 3. Pre-diagnostic Python

| Mesure | Valeur |
|---|---|
| python executable | `/usr/bin/python3` |
| python version | 3.12.3 |
| pandas imported | True |
| pandas file | `/home/ubuntu/.local/lib/python3.12/site-packages/pandas/__init__.py` |
| pandas version | 3.0.2 |
| numpy imported | True |
| numpy file | `/home/ubuntu/.local/lib/python3.12/site-packages/numpy/__init__.py` |
| numpy version | 2.4.4 |
| PYTHONPATH calcule | `/home/ubuntu/.local/lib/python3.12/site-packages` |

## 4. Resume execution

| Mesure | Valeur |
|---|---|
| Returncode | `1` |
| Duration (secondes) | 0 |
| Timeout 120s atteint | non |
| stdout lignes | 0 |
| stderr lignes | 20 |
| sha256 script match attendu | OUI |
| Caches live identiques avant/apres | OUI |
| diff_phase2bis.txt vide | OUI |

## 5. Configuration subprocess (vs V1ZZ)

```
cwd      : /home/ubuntu/seragone/auditactionsv1/CONTROLE_MULTIMONDES_V1ZX_REEXEC_27D_20260505_223529/sandbox_27d_reexec
timeout  : 120s (preserve-status)
env      : env -i (whitelist elargie minimale)
           PATH=/usr/local/bin:/usr/bin:/bin
           HOME=/home/ubuntu/seragone/auditactionsv1/CONTROLE_MULTIMONDES_V1ZX_REEXEC_27D_20260505_223529/_v1zzbis_isolated_home
           LANG=C.UTF-8
           LC_ALL=C.UTF-8
           TERM=dumb
           PYTHONDONTWRITEBYTECODE=1
           PYTHONUNBUFFERED=1
           PYTHONPATH=/home/ubuntu/.local/lib/python3.12/site-packages
home iso : /home/ubuntu/seragone/auditactionsv1/CONTROLE_MULTIMONDES_V1ZX_REEXEC_27D_20260505_223529/_v1zzbis_isolated_home
```

Difference vs V1ZZ : retrait `PYTHONNOUSERSITE=1`, ajout `PYTHONPATH=<calcule>`. Toutes les autres restrictions (broker, cron, systemd, secrets) inchangees.

## 6. Posture finale

Toujours RC non nul. Lire stderr_full_v1zzbis.log pour diagnostiquer la cause au-dela de l env compat (probable input layout, exception metier, etc.).

D12 candidate : V1ZZ-bis = VALIDATED != INSTALLED != PRODUCTION_ACTIVE.

---

*Posture L99 + OODA stricte maintenue.*
*Raphael voit. Claude calcule.*