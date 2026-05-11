#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
seragone_one.py — Générateur de la VISION TOTALE de Séragone.
Produit canon/SERAGONE_ONE.md en agrégeant TOUT par découverte mécanique.
Aucune liste figée. Aucune mémoire humaine. Découverte pure par filesystem.
"""
import os, sys, json, hashlib, subprocess, datetime, glob
from pathlib import Path

ROOT = Path(os.path.expanduser("~/seragone"))
OUT  = ROOT / "canon" / "SERAGONE_ONE.md"
OUT_JSON = ROOT / "canon" / "SERAGONE_ONE.json"
HASHFILE = ROOT / "canon" / "SERAGONE_ONE_HASH.txt"

def sh(cmd, timeout=30):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                           timeout=timeout, cwd=str(ROOT))
        return (r.stdout or "") + (r.stderr or "")
    except Exception as e:
        return f"[ERR] {e}"

def count_ext(ext):
    return int(sh(f"find . -type f -name '*.{ext}' ! -path './.git/*' ! -path './.venv/*' 2>/dev/null | wc -l").strip() or 0)

def count_dir(d):
    p = ROOT / d
    if not p.exists(): return 0
    return int(sh(f"find {d} -type f 2>/dev/null | wc -l").strip() or 0)

def hash_universe():
    out = sh("find . -type f ! -path './.git/*' ! -path './.venv/*' ! -path './__pycache__/*' -printf '%p %s\\n' 2>/dev/null | sort | sha256sum")
    return out.split()[0][:16] if out else "unknown"

def list_dirs_with_hash():
    res = []
    for d in sorted(os.listdir(ROOT)):
        full = ROOT / d
        if not full.is_dir(): continue
        if d in (".git", ".venv", "__pycache__", ".pytest_cache"): continue
        n = int(sh(f"find '{d}' -type f 2>/dev/null | wc -l").strip() or 0)
        h = sh(f"find '{d}' -type f 2>/dev/null | sort | xargs sha256sum 2>/dev/null | sha256sum").split()[0][:12] if n else "empty"
        res.append((d, n, h))
    return res

def list_files_glob(pattern, limit=None):
    paths = sorted(glob.glob(str(ROOT / pattern), recursive=True))
    paths = [str(Path(p).relative_to(ROOT)) for p in paths]
    return paths[:limit] if limit else paths

NOW = datetime.datetime.utcnow().isoformat() + "Z"
HASH = hash_universe()

# === Collecte ===
data = {
    "generated_at_utc": NOW,
    "hash_universe": HASH,
    "host": sh("hostname").strip(),
    "user": sh("whoami").strip(),
    "seragone_ip": sh("hostname -I").strip(),
    "uptime": sh("uptime -p").strip(),
    "disk": sh("df -h . | tail -1").strip(),
}

# Fichiers par extension
data["files_by_ext"] = {ext: count_ext(ext) for ext in
    ["py","md","txt","json","csv","sh","log","yaml","toml","ini","env","conf"]}
data["total_files"] = int(sh("find . -type f ! -path './.git/*' ! -path './.venv/*' 2>/dev/null | wc -l").strip() or 0)
data["total_size"] = sh("du -sh --exclude=.git --exclude=.venv . 2>/dev/null | cut -f1").strip()

# Hashs par dossier racine
data["root_dirs"] = list_dirs_with_hash()
data["root_dirs_count"] = len(data["root_dirs"])

# Crons + systemd + processus
data["cron_lines"] = sh("crontab -l 2>/dev/null | grep -v '^#' | grep -v '^$' | wc -l").strip()
data["cron_raw"]   = sh("crontab -l 2>/dev/null | grep -v '^#' | grep -v '^$'")
data["systemd_seragone"] = sh("systemctl list-units --type=service --all 2>/dev/null | grep -i seragone")
data["systemd_timers"]   = sh("systemctl list-timers --all 2>/dev/null | grep -i seragone")
data["ps_python"]  = sh("ps -ef | grep -E 'python|seragone' | grep -v grep | head -30")
data["ps_count"]   = int(sh("ps -ef | grep -E 'python|seragone' | grep -v grep | wc -l").strip() or 0)

# Actes, décrets, attestations, bilans
data["decrets"]       = list_files_glob("audit/decisions/DECRET_*.md")
data["attestations"]  = list_files_glob("audit/decisions/ATTESTATION_*.md")
data["grave_dirs"]    = sorted([str(Path(p).relative_to(ROOT)) for p in glob.glob(str(ROOT/"audit/grave_*"))])
data["bilans"]        = list_files_glob("**/BILAN_*.md") + list_files_glob("**/RECAPITULATIF_*.md")

# Doctrines
data["doctrines"] = list_files_glob("canon/DOCTRINE_*.md")
data["index_canon_exists"] = (ROOT/"canon/INDEX_CANON_SERAGONE.md").exists()

# Registry
reg_path = ROOT/"_bibliotheque_modules/modules_registry.json"
if reg_path.exists():
    try:
        with open(reg_path) as f:
            reg = json.load(f)
        data["registry"] = {
            "schema_version": reg.get("schema_version"),
            "module_count": reg.get("module_count"),
            "families_count": reg.get("families_count"),
            "maturity_count": reg.get("maturity_count"),
            "grade_count": reg.get("grade_count"),
            "dependency_edges_count": reg.get("dependency_edges_count"),
            "generated_at_utc": reg.get("generated_at_utc"),
        }
    except Exception as e:
        data["registry"] = {"error": str(e)}

# Git
data["git_log"]    = sh("git log --oneline -20 2>/dev/null")
data["git_status"] = sh("git status --short 2>/dev/null | head -30")

# Phases recherche
data["phases_seragone"]  = len(glob.glob(str(ROOT/"SERAGONE_PHASE*")))
data["phases_pepites"]   = len(glob.glob(str(ROOT/"PEPITES_ASSEMBLAGES_PHASE*")))
data["audit_actions"]    = len(glob.glob(str(ROOT/"auditactionsv1/*")))
data["audit_dirs_count"] = len(glob.glob(str(ROOT/"audit/*")))

# Modèles ML
data["modeles_V13"] = sorted([str(Path(p).relative_to(ROOT)) for p in glob.glob(str(ROOT/"modeles_V13_*"))])

# Runtime states
for d in ["states","state","snapshots","snapshots_valides","checkpoints","checkpoints_valides","logs"]:
    data[f"count_{d}"] = count_dir(d)

# === Écriture JSON ===
with open(OUT_JSON, "w") as f:
    json.dump(data, f, indent=2, default=str)

# === Écriture MD (vision totale humaine/IA) ===
lines = []
lines.append(f"# SERAGONE_ONE — Vision Totale")
lines.append(f"")
lines.append(f"**Généré (UTC)**: {NOW}  ")
lines.append(f"**Hash univers**: `{HASH}`  ")
lines.append(f"**Hôte**: {data['host']} | **IP**: {data['seragone_ip']} | **User**: {data['user']}  ")
lines.append(f"**Disque**: {data['disk']}  ")
lines.append(f"**Uptime**: {data['uptime']}")
lines.append("")
lines.append("## 0. Doctrine de lecture")
lines.append("- Ce fichier est **LA** source de vérité unique de Séragone.")
lines.append("- Régénéré toutes les heures par cron (`tools/seragone_one.py`).")
lines.append("- Toute IA qui entre en session doit lire ce fichier AVANT toute action.")
lines.append("- Si ce fichier ne mentionne pas X, c'est que X n'existe pas (ou que le hash est périmé).")
lines.append("")
lines.append("## 1. Volumétrie réelle")
lines.append(f"- Fichiers totaux: **{data['total_files']}**")
lines.append(f"- Taille: **{data['total_size']}**")
lines.append(f"- Dossiers racine: **{data['root_dirs_count']}**")
lines.append("")
lines.append("| Extension | Compte |")
lines.append("|---|---|")
for ext, n in data["files_by_ext"].items():
    lines.append(f"| .{ext} | {n} |")
lines.append("")
lines.append("## 2. Registry Production (bibliothèque modules)")
reg = data.get("registry", {})
if reg and "error" not in reg:
    lines.append(f"- Schema: v{reg.get('schema_version')}")
    lines.append(f"- Modules: **{reg.get('module_count')}**")
    lines.append(f"- Edges: {reg.get('dependency_edges_count')}")
    lines.append(f"- Grades: `{reg.get('grade_count')}`")
    lines.append(f"- Maturité: `{reg.get('maturity_count')}`")
    lines.append(f"- Familles: `{reg.get('families_count')}`")
lines.append("")
lines.append("## 3. Canon doctrinal")
lines.append(f"- INDEX_CANON_SERAGONE.md: {'✅ présent' if data['index_canon_exists'] else '❌ ABSENT'}")
lines.append("### Doctrines")
for d in data["doctrines"]:
    lines.append(f"- `{d}`")
lines.append("")
lines.append(f"## 4. Décrets ({len(data['decrets'])})")
for d in data["decrets"]:
    lines.append(f"- `{d}`")
lines.append("")
lines.append(f"## 5. Attestations ({len(data['attestations'])})")
for a in data["attestations"]:
    lines.append(f"- `{a}`")
lines.append("")
lines.append(f"## 6. Actes `grave_*` ({len(data['grave_dirs'])})")
for g in data["grave_dirs"]:
    lines.append(f"- `{g}`")
lines.append("")
lines.append(f"## 7. Bilans/Recaps ({len(data['bilans'])})")
for b in data["bilans"][:20]:
    lines.append(f"- `{b}`")
lines.append("")
lines.append("## 8. Runtime (exécutions vivantes)")
lines.append(f"- Crons actifs: **{data['cron_lines']}**")
lines.append(f"- Processus Python: **{data['ps_count']}**")
lines.append("### Services systemd")
lines.append("```")
lines.append(data["systemd_seragone"][:2000])
lines.append("```")
lines.append("### Timers systemd")
lines.append("```")
lines.append(data["systemd_timers"][:1500])
lines.append("```")
lines.append("### Processus actifs (top 30)")
lines.append("```")
lines.append(data["ps_python"][:3000])
lines.append("```")
lines.append("")
lines.append("## 9. Runtime states")
lines.append(f"- states/: {data['count_states']} | state/: {data['count_state']}")
lines.append(f"- snapshots/: {data['count_snapshots']} | snapshots_valides/: {data['count_snapshots_valides']}")
lines.append(f"- checkpoints/: {data['count_checkpoints']} | checkpoints_valides/: {data['count_checkpoints_valides']}")
lines.append(f"- logs/: {data['count_logs']}")
lines.append("")
lines.append("## 10. Recherche & phases")
lines.append(f"- SERAGONE_PHASE*: **{data['phases_seragone']}** dossiers")
lines.append(f"- PEPITES_ASSEMBLAGES_PHASE*: **{data['phases_pepites']}** dossiers")
lines.append(f"- auditactionsv1/*: **{data['audit_actions']}**")
lines.append(f"- audit/*: **{data['audit_dirs_count']}**")
lines.append("")
lines.append("## 11. Modèles ML V13")
for m in data["modeles_V13"]:
    lines.append(f"- `{m}`")
lines.append("")
lines.append("## 12. Git")
lines.append("### 20 derniers commits")
lines.append("```")
lines.append(data["git_log"][:3000])
lines.append("```")
lines.append("### État non committé")
lines.append("```")
lines.append(data["git_status"][:2000])
lines.append("```")
lines.append("")
lines.append("## 13. Crontab complète")
lines.append("```")
lines.append(data["cron_raw"][:8000])
lines.append("```")
lines.append("")
lines.append(f"## 14. Hash par dossier racine ({data['root_dirs_count']})")
lines.append("| Dossier | Fichiers | Hash |")
lines.append("|---|---|---|")
for d, n, h in data["root_dirs"]:
    lines.append(f"| `{d}` | {n} | `{h}` |")
lines.append("")
lines.append("---")
lines.append(f"**FIN SERAGONE_ONE** | hash: `{HASH}` | généré: {NOW}")

OUT.write_text("\n".join(lines), encoding="utf-8")
HASHFILE.write_text(f"{HASH}  {NOW}\n")

print(f"[OK] {OUT} ({OUT.stat().st_size} octets, {len(lines)} lignes)")
print(f"[OK] {OUT_JSON}")
print(f"[OK] hash univers = {HASH}")
