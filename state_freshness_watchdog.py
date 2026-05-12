#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
state_freshness_watchdog.py — Audit passif de fraîcheur des fichiers state Séragone.

=== SERAGONE STATE CONTRACT ===
PRODUCES: (rien — outil de lecture seule)
CONSUMES: state_registry.json
TTL_PRODUCED: N/A
CRITICALITY: LOW (audit, pas runtime décisionnel)
REGISTERED_IN: state_registry.json (pas requis car ne produit pas)
=== END CONTRACT ===

Lecture passive de state_registry.json, vérification des mtimes, rapport texte.
Mode passif : pas d'alerte externe, juste un résumé console + code retour.

Codes retour :
  0 = tous les states critiques HIGH sont frais
  1 = au moins un state HIGH est stale
  2 = registre absent ou corrompu

Usage :
  python3 state_freshness_watchdog.py               # rapport humain
  python3 state_freshness_watchdog.py --json        # rapport JSON
  python3 state_freshness_watchdog.py --quiet       # silencieux, seul code retour
"""

import json
import sys
import time
from pathlib import Path

BASE = Path.home() / "seragone"
REGISTRY = BASE / "state_registry.json"


def load_registry():
    if not REGISTRY.exists():
        return None
    try:
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"[ERREUR] registre corrompu : {e}", file=sys.stderr)
        return None


def check_state(rel_path, ttl_seconds, criticality):
    """Retourne dict {path, exists, mtime_iso, age_sec, stale, criticality}."""
    p = BASE / rel_path
    now = time.time()
    out = {
        "path": rel_path,
        "criticality": criticality,
        "ttl_seconds": ttl_seconds,
        "exists": p.exists(),
    }
    if not p.exists():
        out.update({"mtime_iso": None, "age_sec": None, "stale": True, "reason": "ABSENT"})
        return out
    mtime = p.stat().st_mtime
    age = now - mtime
    out.update({
        "mtime_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(mtime)),
        "age_sec": int(age),
        "age_human": format_age(age),
        "stale": age > ttl_seconds,
        "reason": "STALE" if age > ttl_seconds else "FRESH",
    })
    return out


def format_age(seconds):
    if seconds < 60:
        return f"{int(seconds)}s"
    if seconds < 3600:
        return f"{seconds/60:.1f}min"
    if seconds < 86400:
        return f"{seconds/3600:.1f}h"
    return f"{seconds/86400:.1f}j"


def main():
    args = sys.argv[1:]
    json_mode = "--json" in args
    quiet = "--quiet" in args

    reg = load_registry()
    if reg is None:
        if not quiet:
            print("[FATAL] state_registry.json absent ou corrompu", file=sys.stderr)
        sys.exit(2)

    results = []

    # États vivants attendus
    for path, info in reg.get("states_vivants", {}).items():
        results.append(check_state(path, info.get("ttl_seconds", 3600), info.get("criticality", "MEDIUM")))

    # États fossiles A9 v1 (TTL déjà dépassé volontairement, on les note FROZEN)
    for path, info in reg.get("states_fossiles_A9_v1_patches", {}).items():
        r = check_state(path, info.get("ttl_seconds", 3600) if "ttl_seconds" in info else 3600,
                       info.get("criticality", "MEDIUM"))
        r["reason"] = "FOSSILE_A9_v1_patche_TTL"
        r["criticality_effective"] = "ABSORBED_BY_PATCH"
        results.append(r)

    # États fossiles A10 satellites (à investiguer)
    for path, info in reg.get("states_fossiles_A10_satellites_a_investiguer", {}).items():
        r = check_state(path, 3600, "A10_OPEN")
        r["reason"] = "FOSSILE_A10_a_investiguer"
        results.append(r)

    # Compteurs
    high_stale = [r for r in results if r.get("criticality") == "HIGH" and r["stale"]
                  and r.get("criticality_effective") != "ABSORBED_BY_PATCH"]
    exit_code = 1 if high_stale else 0

    if json_mode:
        report = {
            "audit_time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "registry_version": reg.get("_meta", {}).get("version"),
            "exit_code": exit_code,
            "high_stale_count": len(high_stale),
            "total_checked": len(results),
            "results": results,
        }
        print(json.dumps(report, indent=2, ensure_ascii=False))
    elif not quiet:
        print(f"=== state_freshness_watchdog — {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())} ===")
        print(f"Registre v{reg.get('_meta', {}).get('version', '?')} — audit {reg.get('_meta', {}).get('audit_source', '?')}")
        print()
        print(f"{'STATUT':10s} {'CRIT':8s} {'AGE':10s} {'PATH':60s} {'RAISON'}")
        print("-" * 110)
        for r in sorted(results, key=lambda x: (not x["stale"], x.get("criticality", "ZZZ"), x["path"])):
            statut = "🔴 STALE" if r["stale"] else "🟢 FRESH"
            age = r.get("age_human") or "ABSENT"
            crit = r.get("criticality_effective") or r.get("criticality", "?")
            print(f"{statut:10s} {crit:8s} {age:10s} {r['path']:60s} {r.get('reason', '?')}")
        print()
        print(f"Bilan : {len(high_stale)} state(s) HIGH stale non absorbés / {len(results)} vérifiés.")
        if exit_code == 0:
            print("✅ Système sain (les fossiles A9/A10 sont attendus).")
        else:
            print("❌ ALERTE : des états HIGH sont stale et non couverts par un patch garde-fou.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
