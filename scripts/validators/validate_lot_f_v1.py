#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path("/home/ubuntu/seragone")
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

FILES = [
    "data/archive_chains/chain_F0.csv",
    "data/archive_chains/chain_F0.5.csv",
    "data/archive_chains/chain_F1.csv",
    "data/archive_chains/chain_F1.5.csv",
    "data/archive_chains/chain_F2.csv",
    "data/archive_chains/chain_F3.csv",
    "data/archive_chains/chain_F4.csv",
    "data/archive_chains/chain_F6.csv",
    "data/archive_chains/chain_propre_F0.csv",
    "data/archive_chains/chain_propre_F0.5.csv",
    "data/archive_chains/chain_propre_F1.csv",
    "data/archive_chains/chain_propre_F1.5.csv",
    "data/archive_chains/chain_propre_F2.csv",
    "data/archive_chains/chain_propre_F3.csv",
    "data/archive_chains/chain_propre_F4.csv",
    "data/archive_chains/chain_propre_F6.csv",
    "data/archive_chains/chain_v3_F0.csv",
    "data/archive_chains/chain_v3_F0.5.csv",
    "data/archive_chains/chain_v3_F1.csv",
    "data/archive_chains/chain_v3_F1.5.csv",
    "data/archive_chains/chain_v3_F2.csv",
    "data/archive_chains/chain_v3_F3.csv",
    "data/archive_chains/chain_v3_F4.csv",
    "data/archive_chains/chain_v3_F6.csv",
    "data/mondes_recursifs_20m.csv",
    "data/mondes_recursifs_100m.csv",
    "data/mondes_recursifs_500m.csv",
    "data/seragone_4126j_canon.csv",
    "data/seragone_4126j_canon_meta.json",
    "data/seragone_4126j_complet_canon.csv",
    "data/seragone_4126j_complet_canon_meta.json",
    "data/seragone_canon_4117j.csv",
]

def is_float(x):
    try:
        float(str(x).strip().replace(",", ""))
        return True
    except:
        return False

def validate_csv(path):
    res = {
        "type": "csv",
        "exists": path.exists(),
        "rows": 0,
        "header": [],
        "status": "FAIL",
        "action": "INSPECT",
        "bad_lines": 0,
        "sample_bad_lines": [],
        "null_bytes": 0,
    }
    if not path.exists():
        res["action"] = "MISSING_FILE"
        return res

    raw = path.read_bytes()
    res["null_bytes"] = raw.count(b"\x00")

    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            r = csv.reader(f)
            header = next(r, None)
            rows = list(r)

        if not header:
            res["action"] = "EMPTY_FILE"
            return res

        res["header"] = header
        res["rows"] = len(rows)

        if len(rows) == 0:
            res["status"] = "WARN"
            res["action"] = "NO_DATA_ROWS"
            return res

        numeric_cols = []
        for i, h in enumerate(header):
            ok = 0
            checked = 0
            for row in rows[:50]:
                if len(row) <= i:
                    continue
                v = str(row[i]).strip()
                if v == "":
                    continue
                checked += 1
                if is_float(v):
                    ok += 1
            if checked > 0 and ok / checked >= 0.7:
                numeric_cols.append(i)

        for line_no, row in enumerate(rows, start=2):
            causes = []
            if len(row) != len(header):
                causes.append(f"len={len(row)}")
            if numeric_cols:
                any_numeric = False
                for i in numeric_cols:
                    if len(row) > i and str(row[i]).strip() != "" and is_float(row[i]):
                        any_numeric = True
                        break
                if not any_numeric:
                    causes.append("no_numeric_value")
            if causes:
                res["bad_lines"] += 1
                if len(res["sample_bad_lines"]) < 3:
                    res["sample_bad_lines"].append({
                        "line": line_no,
                        "causes": causes,
                        "row": row
                    })

        if res["bad_lines"] == 0 and res["null_bytes"] == 0:
            res["status"] = "OK"
            res["action"] = "NONE"
        else:
            res["status"] = "WARN"
            res["action"] = "INSPECT"

        return res

    except Exception as e:
        res["status"] = "FAIL"
        res["action"] = "READ_ERROR"
        res["error"] = str(e)
        return res

def validate_json(path):
    res = {
        "type": "json",
        "exists": path.exists(),
        "status": "FAIL",
        "action": "INSPECT",
        "root_type": None,
        "keys": [],
        "null_bytes": 0,
    }
    if not path.exists():
        res["action"] = "MISSING_FILE"
        return res

    raw = path.read_bytes()
    res["null_bytes"] = raw.count(b"\x00")

    try:
        obj = json.loads(raw.decode("utf-8-sig"))
        if isinstance(obj, dict):
            res["root_type"] = "object"
            res["keys"] = list(obj.keys())[:20]
        elif isinstance(obj, list):
            res["root_type"] = "list"
        else:
            res["root_type"] = type(obj).__name__

        if res["null_bytes"] == 0:
            res["status"] = "OK"
            res["action"] = "NONE"
        else:
            res["status"] = "WARN"
            res["action"] = "REMOVE_NULL_BYTES"
        return res

    except Exception as e:
        res["status"] = "FAIL"
        res["action"] = "BAD_JSON"
        res["error"] = str(e)
        return res

def validate_file(rel):
    path = ROOT / rel
    if path.suffix.lower() == ".json":
        return validate_json(path)
    return validate_csv(path)

def main():
    audit = {rel: validate_file(rel) for rel in FILES}

    for rel, r in audit.items():
        if r["type"] == "json":
            print(
                f"{rel} | STATUS={r['status']} | ROOT={r['root_type']} | "
                f"KEYS={len(r['keys'])} | NULL_BYTES={r['null_bytes']} | ACTION={r['action']}"
            )
        else:
            print(
                f"{rel} | STATUS={r['status']} | ROWS={r['rows']} | COLS={len(r['header'])} | "
                f"BAD_LINES={r['bad_lines']} | NULL_BYTES={r['null_bytes']} | ACTION={r['action']}"
            )

    with open(OUT / "lot_f_audit_v1.json", "w", encoding="utf-8") as f:
        json.dump(audit, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
