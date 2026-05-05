# CONTROLE MULTIMONDES V1Z-Q — DECRET REEXEC BORN FULL LOG

Date UTC: 2026-05-05T20:23:51+00:00

Mode: decret documentaire uniquement. Ce fichier ne lance aucune execution. Il prepare une reexecution sandbox signee separement pour capturer le stdout complet de born_temps_validation.py.

## 1. Ligneage

- V1ZP precheck : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZP_PRECHECK_REEXEC_BORN_20260505_201427/CONTROLE_MULTIMONDES_V1ZP_PRECHECK_REEXEC_BORN.md` sha256=`68b4b4c4cbe17c1e90bc7ff3eba5829b3cf2495a438987cedee1e01acf5ab61e`
- V1ZP manifest : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZP_PRECHECK_REEXEC_BORN_20260505_201427/manifest.json` sha256=`d5e9cfa205513389b394385f4951beea8ab6c19ffbbb59e963eef960871825bc` verdict=`PRECHECK_OK_PRET_DECRET`
- V1ZJ run_report : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK_20260505_195442/run_report.json` sha256=`fc833c8c0705c5f42fdd9a6b72fc296ac890b603a20407dc418171b99aa31a80`
- V1ZJ MD : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK_20260505_195442/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK.md` sha256=`53793630eb13991a434fa5b838bcccbba81c88c514a03ba7fcd1bb2a54e6ce62`
- V1ZJ manifest : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZJ_EXEC_ONE_BORN_SANDBOX_HOME_OK_20260505_195442/manifest.json` sha256=`30a35f14acac03c56e6a9299831c89fcf47fd48387e59e163c32f087111373bc`
- V1ZC canon MD : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZC_OFFLINE_TEST_PLAN_20260505_194728/CONTROLE_MULTIMONDES_V1ZC_OFFLINE_TEST_PLAN.md` sha256=`12c1faeb662ebd03767d013f16a3d913be9cf4bf76e4f0a816ed7133641716ae`
- V1ZC canon CSV : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZC_OFFLINE_TEST_PLAN_20260505_194728/controle_multimondes_v1zc_offline_test_plan.csv` sha256=`996331d7a7a96fbc499a86cb26ac21473e1ac0477f13b75538d58424770e1c77`

## 2. Parametres figes

| Champ | Valeur |
|---|---|
| script | `born_temps_validation.py` |
| script_sha256 V1ZJ | `d9acb122719206a370f1058254d1cfc6b51d3586cce1d379426915c2bac1367d` |
| commande V1ZJ | `timeout 60s /usr/bin/python3 born_temps_validation.py` |
| python | `/usr/bin/python3` |
| mode V1ZJ | `one_script_sandbox_home_real_usrbinpython3_pandas_sitecustomize_redirect_no_patch` |
| sitecustomize_sha256 | `9abaa362fcb7b78eb2f2e933794a3df9e8413012a9edf3b212f9ae0298d0fedf` |
| input local sha256 V1ZJ | `6850e7f0bb0673498c5db86910570dcf3f6dccb098422c8fd51754f1803ab634` |
| cwd V1ZJ source | `auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs_v1zj` |
| returncode V1ZJ | `0` |
| sandbox V1ZQ cible | `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351/sandbox_born_full_log` |
| stdout complet cible | `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351/stdout_full.log` |
| stderr complet cible | `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351/stderr_full.log` |
| run_report cible | `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351/run_report.json` |

## 3. Interdits maintenus

- Aucun broker, aucune cle API, aucun ordre exchange.
- Aucun cron, aucun systemd, aucun service modifie ou redemarre.
- Aucune ecriture dans les caches live ; hashes avant/apres obligatoires.
- Phase 115 preservee, decision_weight=0.0.
- vrais_yeux.py INTOUCHABLE.
- Pas de symlink sandbox vers runtime ; copies physiques seulement.

## 4. Phase 1 proposee

```bash
# PHASE 1 — PREPARATION SANDBOX ET HASHES AVANT — NON EXECUTEE PAR CE DECRET
set -euo pipefail
OUT="auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351"
SANDBOX="$OUT/sandbox_born_full_log"
mkdir -p "$SANDBOX/data"

# Hashes live AVANT, lecture seule
: > "$OUT/hashes_live_avant.sha256"
for p in data/mondes_paralleles_cache.json cache/mondes_paralleles_cache.json production/mondes/data/mondes_paralleles_cache.json data/born_state.json data/born_temps_state.json data/multivers_state.json data/communicants_history.json voix_seragone_92/seragone_92_state.json voix_seragone_92/data/seragone_92_state.json; do
  if [ -f "$p" ]; then
    sha256sum "$p" >> "$OUT/hashes_live_avant.sha256"
  else
    echo "ABSENT  $p" >> "$OUT/hashes_live_avant.sha256"
  fi
done

# Copie sandbox depuis le cwd V1ZJ connu, sans symlink
cp -p "auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs_v1zj/born_temps_validation.py" "$SANDBOX/"
cp -p "auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs_v1zj/sitecustomize.py" "$SANDBOX/" 2>/dev/null || true
find "auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs_v1zj" -maxdepth 2 -type f -name "*.csv" -exec cp -p {} "$SANDBOX/data/" \; 2>/dev/null || true
find "auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/outputs_v1zj" -maxdepth 2 -type f -name "*.json" -exec cp -p {} "$SANDBOX/data/" \; 2>/dev/null || true

sha256sum "$SANDBOX/born_temps_validation.py" > "$OUT/sandbox_script.sha256"
[ -f "$SANDBOX/sitecustomize.py" ] && sha256sum "$SANDBOX/sitecustomize.py" > "$OUT/sandbox_sitecustomize.sha256" || true
```

## 5. Phase 2 proposee

```bash
# PHASE 2 — REEXECUTION SANDBOX AVEC STDOUT COMPLET — A SIGNER SEPAREMENT
set -euo pipefail
OUT="auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351"
SANDBOX="$OUT/sandbox_born_full_log"
cd "$SANDBOX"

# Execution sandbox uniquement, stdout/stderr complets sur disque
timeout 60s /usr/bin/python3 born_temps_validation.py > "../stdout_full.log" 2> "../stderr_full.log"
rc=$?
echo "$rc" > "../returncode.txt"
exit "$rc"
```

## 6. Phase 3 proposee

```bash
# PHASE 3 — COLLECTE ET ATTESTATION NON-POLLUTION — APRES PHASE 2
set -euo pipefail
OUT="auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351"

: > "$OUT/hashes_live_apres.sha256"
for p in data/mondes_paralleles_cache.json cache/mondes_paralleles_cache.json production/mondes/data/mondes_paralleles_cache.json data/born_state.json data/born_temps_state.json data/multivers_state.json data/communicants_history.json voix_seragone_92/seragone_92_state.json voix_seragone_92/data/seragone_92_state.json; do
  if [ -f "$p" ]; then
    sha256sum "$p" >> "$OUT/hashes_live_apres.sha256"
  else
    echo "ABSENT  $p" >> "$OUT/hashes_live_apres.sha256"
  fi
done

diff -u "$OUT/hashes_live_avant.sha256" "$OUT/hashes_live_apres.sha256" > "$OUT/diff_hashes_live_avant_apres.txt" || true

python3 - "$OUT" <<'PY2'
import sys, json, hashlib
from pathlib import Path
from datetime import datetime, timezone

out = Path(sys.argv[1])

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() and p.is_file() else None

report = {
    "type": "V1ZQ_REEXEC_BORN_FULL_LOG_RESULT",
    "created_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    "returncode": int((out / "returncode.txt").read_text().strip()) if (out / "returncode.txt").exists() else None,
    "stdout_full_path": str(out / "stdout_full.log"),
    "stdout_full_sha256": sha(out / "stdout_full.log"),
    "stderr_full_path": str(out / "stderr_full.log"),
    "stderr_full_sha256": sha(out / "stderr_full.log"),
    "hashes_live_avant_sha256": sha(out / "hashes_live_avant.sha256"),
    "hashes_live_apres_sha256": sha(out / "hashes_live_apres.sha256"),
    "diff_hashes_live_sha256": sha(out / "diff_hashes_live_avant_apres.txt"),
    "interdits": [
        "aucun broker",
        "aucun cron",
        "aucun systemd",
        "aucune ecriture caches live attendue",
        "Phase 115 preservee",
        "decision_weight=0.0",
        "vrais_yeux.py INTOUCHABLE"
    ]
}
(out / "run_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
PY2
```

## 7. Verdict decret

- V1ZQ_DECRET_PRET_A_SIGNER : oui, sous reserve de signature humaine explicite avant Phase 1, Phase 2 et Phase 3.
- Ce decret ne vaut pas execution. Il prepare trois blocs executables separes.
- La Phase 2 est la seule phase qui relance born_temps_validation.py ; elle ne doit pas etre lancee tant que Phase 1 n est pas validee.

---

Aucune execution realisee par V1ZQ. Aucun script multimondes lance. Aucun patch. Aucun cron. Aucun broker. Phase 115 preservee. decision_weight=0.0.
