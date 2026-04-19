#!/usr/bin/env python3
"""
build_global_manifest.py — seragone, clôture globale du dataset.

Politique par défaut :
  B,C,D,F -> ACTIVE_CANON
  E       -> TECHNICAL_ARTIFACT
  G       -> classification par entrée (en dur)
Surcharge possible via 'classification' ou 'class' dans les audits.
"""
from __future__ import annotations
import argparse, hashlib, json, os, sys
from pathlib import Path
from datetime import datetime, timezone

LOT_G_CLASSIFICATION = {
    "data/btc_daily.csv": "ACTIVE_CANON",
    "data/btc_daily.csv.bak_20260419T083333Z": "TO_ARCHIVE",
    "data/btc_daily.csv.bak_fix_20260419T083814Z": "BACKUP_ONLY",
    "data/btc_daily_fresh.csv": "REDONDANT",
    "data/sp500_daily.csv": "ACTIVE_CANON",
    "data/sp500_daily.csv.bak": "BACKUP_ONLY",
    "data/fear_greed_complet.csv": "ACTIVE_CANON",
    "data/klines_1min.db": "ACTIVE_CANON",
    "data/vitesse_24h.txt": "TECHNICAL_ARTIFACT",
    "data/C1_btcusdt_2026-03-30_15min.csv": "TECHNICAL_ARTIFACT",
    "data/dim_btcusdt_2026-03-30_15min.csv": "TECHNICAL_ARTIFACT",
    "data/dim_btcusdt_2026-03-30_5min.csv": "TECHNICAL_ARTIFACT",
    "data/dim_btcusdt_2026-03-30_60min.csv": "TECHNICAL_ARTIFACT",
    "data/n_act_btcusdt_2026-03-30_15min.csv": "TECHNICAL_ARTIFACT",
}

HARDCODED_INVENTORY = {
    # --- Lot B : macro / on-chain daily (scories de tri + séries 4ans) ---
    "data/btc_active_addresses.csv.bak_sort":            ("B", "BACKUP_ONLY"),
    "data/btc_difficulty_daily.csv.bak_sort":            ("B", "BACKUP_ONLY"),
    "data/btc_hashrate_daily.csv.bak_sort":              ("B", "BACKUP_ONLY"),
    "data/btc_transactions_daily.csv.bak_sort":          ("B", "BACKUP_ONLY"),
    "data/binance_fr_8h_4ans.csv":                       ("B", "ACTIVE_CANON"),
    "data/btc_15min_4ans.csv":                           ("B", "ACTIVE_CANON"),
    "data/btc_5min_4ans.csv":                            ("B", "ACTIVE_CANON"),
    "data/btc_5min_part1.csv":                           ("B", "ACTIVE_CANON"),
    "data/btc_5min_part2.csv":                           ("B", "ACTIVE_CANON"),
    "data/btc_hourly_4ans.csv":                          ("B", "ACTIVE_CANON"),
    "data/eth_daily.csv":                                ("B", "ACTIVE_CANON"),
    "data/onchain/exchange_netflow.csv.bak_sort":        ("B", "BACKUP_ONLY"),
    "data/onchain/funding_rate.csv.bak_sort":            ("B", "BACKUP_ONLY"),
    "data/onchain/mvrv.csv.bak_sort":                    ("B", "BACKUP_ONLY"),
    "data/onchain/nupl.csv.bak_sort":                    ("B", "BACKUP_ONLY"),
    "data/onchain/open_interest.csv.bak_sort":           ("B", "BACKUP_ONLY"),
    "data/onchain/puell_multiple.csv.bak_sort":          ("B", "BACKUP_ONLY"),
    "data/onchain/whale_ratio.csv.bak_sort":             ("B", "BACKUP_ONLY"),

    # --- Lot C : intraday / microstructure ---

    # --- Lot D : depth / trades multi-jours ---
    "data/trades_btcusdt_2026-03-30.csv.bak_nul":        ("D", "TO_ARCHIVE"),
    "data/trades_btcusdt_2026-04-04.csv":                ("D", "ACTIVE_CANON"),
    "data/trades_btcusdt_2026-04-05.csv":                ("D", "ACTIVE_CANON"),
    "data/trades_btcusdt_2026-04-06.csv":                ("D", "ACTIVE_CANON"),
    "data/trades_btcusdt_2026-04-07.csv":                ("D", "ACTIVE_CANON"),
    "data/trades_btcusdt_2026-04-08.csv":                ("D", "ACTIVE_CANON"),

    # --- Lot E : états, caches, mémoire moteur ---
    "data/chaines_epurees_state.json":                   ("E", "TECHNICAL_ARTIFACT"),
    "data/communicants_history.json":                    ("E", "TECHNICAL_ARTIFACT"),
    "data/ec_latest.json":                               ("E", "TECHNICAL_ARTIFACT"),
    "data/live_metrics.json":                            ("E", "TECHNICAL_ARTIFACT"),
    "data/mondes_paralleles_cache.json":                 ("E", "TECHNICAL_ARTIFACT"),
    "data/phi_engine_memory.json":                       ("E", "TECHNICAL_ARTIFACT"),
    "data/phi_local_20m.json":                           ("E", "TECHNICAL_ARTIFACT"),
    "data/phi_local_100m.json":                          ("E", "TECHNICAL_ARTIFACT"),
    "data/phi_local_500m.json":                          ("E", "TECHNICAL_ARTIFACT"),
    "data/recursif_v1_config.json":                      ("E", "TECHNICAL_ARTIFACT"),

    # --- Lot F : mondes, chaînes et corpus canoniques ---
    "data/mondes_paralleles_history.csv":                ("F", "ACTIVE_CANON"),
    "data/mondes_recursifs_20m.csv":                     ("F", "ACTIVE_CANON"),
    "data/mondes_recursifs_100m.csv":                    ("F", "ACTIVE_CANON"),
    "data/mondes_recursifs_500m.csv":                    ("F", "ACTIVE_CANON"),
    "data/seragone_4126j_canon.csv":                     ("F", "ACTIVE_CANON"),
    "data/seragone_4126j_canon_meta.json":               ("F", "ACTIVE_CANON"),
    "data/seragone_4126j_complet_canon.csv":             ("F", "ACTIVE_CANON"),
    "data/seragone_4126j_complet_canon_meta.json":       ("F", "ACTIVE_CANON"),
    "data/seragone_canon_4117j.csv":                     ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_F0.csv":                  ("F", "REDONDANT"),
    "data/archive_chains/chain_F0.5.csv":                ("F", "REDONDANT"),
    "data/archive_chains/chain_F1.csv":                  ("F", "REDONDANT"),
    "data/archive_chains/chain_F1.5.csv":                ("F", "REDONDANT"),
    "data/archive_chains/chain_F2.csv":                  ("F", "REDONDANT"),
    "data/archive_chains/chain_F3.csv":                  ("F", "REDONDANT"),
    "data/archive_chains/chain_F4.csv":                  ("F", "REDONDANT"),
    "data/archive_chains/chain_F6.csv":                  ("F", "REDONDANT"),
    "data/archive_chains/chain_propre_F0.csv":           ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_propre_F0.5.csv":         ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_propre_F1.csv":           ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_propre_F1.5.csv":         ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_propre_F2.csv":           ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_propre_F3.csv":           ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_propre_F4.csv":           ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_propre_F6.csv":           ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_v3_F0.csv":               ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_v3_F0.5.csv":             ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_v3_F1.csv":               ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_v3_F1.5.csv":             ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_v3_F2.csv":               ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_v3_F3.csv":               ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_v3_F4.csv":               ("F", "ACTIVE_CANON"),
    "data/archive_chains/chain_v3_F6.csv":               ("F", "ACTIVE_CANON"),
}

AUDIT_SOURCES = [
    ("A", "output/lot_a_audit.json"),
    ("B", "output/lot_b_audit.json"),
    ("C", "output/lot_c_audit_v1.json"),
    ("D", "output/lot_d_audit_v2.json"),
    ("E", "output/lot_e_audit.json"),
    ("F", "output/lot_f_audit_v1.json"),
]

DEFAULT_CLASSIFICATION_BY_LOT = {
    "A": "ACTIVE_CANON",
    "B": "ACTIVE_CANON", "C": "ACTIVE_CANON", "D": "ACTIVE_CANON",
    "E": "TECHNICAL_ARTIFACT", "F": "ACTIVE_CANON", "G": None,
}

def sha256_of(p: Path, bs: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(bs), b""):
            h.update(chunk)
    return h.hexdigest()

def extract_entries(obj):
    """Renvoie une liste de tuples (rel_path, classification_or_None)."""
    found = []
    def looks_like_path(k):
        return isinstance(k, str) and (
            "/" in k or k.endswith((".csv", ".json", ".db", ".txt", ".parquet"))
        )
    def walk(x):
        if isinstance(x, dict):
            p = x.get("path") or x.get("file") or x.get("filepath") or x.get("relpath")
            if isinstance(p, str):
                cls = x.get("classification") or x.get("class")
                found.append((p, cls if isinstance(cls, str) else None))
            for k, v in x.items():
                if looks_like_path(k):
                    cls = None
                    if isinstance(v, dict):
                        cls = v.get("classification") or v.get("class")
                    found.append((k, cls if isinstance(cls, str) else None))
                walk(v)
        elif isinstance(x, list):
            for it in x:
                walk(it)
    walk(obj)
    norm = []
    seen = set()
    ROOT_PREFIX = "home/ubuntu/seragone/"
    for pth, c in found:
        pth = pth.strip()
        if pth.startswith("/"):
            pth = pth[1:]
        if pth.startswith(ROOT_PREFIX):
            pth = pth[len(ROOT_PREFIX):]
        pth = pth.lstrip("./")
        if pth and "/" not in pth:
            pth = "data/" + pth
        if pth and pth not in seen:
            seen.add(pth)
            norm.append((pth, c))
    return norm

def build(root: Path):
    entries, seen = [], set()
    stats = {"by_lot": {}, "by_classification": {}}
    def add(rel, lot, cls):
        if rel in seen: return
        ap = root / rel
        ex = ap.is_file()
        classification = cls or DEFAULT_CLASSIFICATION_BY_LOT.get(lot)
        entries.append({
            "lot": lot, "path": rel, "exists": ex,
            "size_bytes": ap.stat().st_size if ex else None,
            "sha256": sha256_of(ap) if ex else None,
            "classification": classification,
        })
        seen.add(rel)
        stats["by_lot"][lot] = stats["by_lot"].get(lot, 0) + 1
        k = classification or "UNSPECIFIED"
        stats["by_classification"][k] = stats["by_classification"].get(k, 0) + 1
    for lot, rel in AUDIT_SOURCES:
        ap = root / rel
        if not ap.is_file():
            print(f"[warn] audit absent pour Lot {lot} : {rel}", file=sys.stderr); continue
        try:
            obj = json.loads(ap.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[warn] audit illisible {rel}: {e}", file=sys.stderr); continue
        for p, cls in extract_entries(obj):
            add(p, lot, cls)
    for rel, (lot, cls) in HARDCODED_INVENTORY.items():
        add(rel, lot, cls)
    for rel, cls in LOT_G_CLASSIFICATION.items():
        add(rel, "G", cls)
    return entries, stats

def find_orphans(root: Path, data_dir: str, paths: set):
    base = root / data_dir
    orphans = []
    if not base.is_dir(): return orphans
    for dp, _, files in os.walk(base):
        for name in files:
            ap = Path(dp) / name
            rel = str(ap.relative_to(root)).replace(os.sep, "/")
            if rel not in paths:
                orphans.append({"path": rel, "size_bytes": ap.stat().st_size, "sha256": sha256_of(ap)})
    return orphans

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="/home/ubuntu/seragone")
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--out", default="output/global_manifest.json")
    ap.add_argument("--orphans", default="output/orphans_report.json")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    entries, stats = build(root)
    manifest = {
        "project": "seragone",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "root": str(root), "data_dir": a.data_dir,
        "lots_included": ["B","C","D","E","F","G"],
        "default_classification_policy": DEFAULT_CLASSIFICATION_BY_LOT,
        "count": len(entries), "stats": stats,
        "entries": sorted(entries, key=lambda e: (e["lot"], e["path"])),
    }
    (root / a.out).parent.mkdir(parents=True, exist_ok=True)
    (root / a.out).write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    paths = {e["path"] for e in entries}
    orphans = find_orphans(root, a.data_dir, paths)
    (root / a.orphans).write_text(json.dumps({
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "data_dir": a.data_dir, "count": len(orphans),
        "orphans": sorted(orphans, key=lambda e: e["path"]),
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    missing = [e["path"] for e in entries if not e["exists"]]
    print(f"[ok] manifest : {a.out} ({len(entries)} entrées)")
    print(f"[ok] orphans  : {a.orphans} ({len(orphans)} fichiers)")
    if missing:
        print(f"[warn] {len(missing)} entrées manquantes sur disque :")
        for m in missing: print(f"   - {m}")

if __name__ == "__main__":
    main()
