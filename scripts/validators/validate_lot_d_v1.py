#!/usr/bin/env python3
import csv
import json
from pathlib import Path
from datetime import datetime

ROOT = Path("/home/ubuntu/seragone")
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

FILES = [
    "data/depth_btcusdt_2026-03-31.csv",
    "data/depth_btcusdt_2026-04-01.csv",
    "data/depth_btcusdt_2026-04-02.csv",
    "data/depth_btcusdt_2026-04-03.csv",
    "data/depth_btcusdt_2026-04-04.csv",
    "data/depth_btcusdt_2026-04-17.csv",
    "data/depth_btcusdt_2026-04-18.csv",
    "data/depth_btcusdt_2026-04-19.csv",
    "data/trades_btcusdt_2026-03-31.csv",
    "data/trades_btcusdt_2026-04-01.csv",
    "data/trades_btcusdt_2026-04-02.csv",
    "data/trades_btcusdt_2026-04-03.csv",
    "data/trades_btcusdt_2026-04-17.csv",
    "data/trades_btcusdt_2026-04-18.csv",
    "data/trades_btcusdt_2026-04-19.csv",
]

def parse_dt(s):
    s = str(s).strip().strip('"')
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except:
            pass
    return None

def is_float(x):
    try:
        float(str(x).strip().replace(",", ""))
        return True
    except:
        return False

def monotonic_direction(dts):
    if len(dts) < 2:
        return "single"
    asc = all(dts[i] >= dts[i-1] for i in range(1, len(dts)))
    desc = all(dts[i] <= dts[i-1] for i in range(1, len(dts)))
    if asc:
        return "ascending"
    if desc:
        return "descending"
    return "mixed"

def profile_for(path_str):
    name = Path(path_str).name
    if name.startswith("depth_"):
        return {
            "required": ["timestamp", "bids", "asks"],
            "time_col": "timestamp",
            "json_cols": ["bids", "asks"],
            "numeric_min": 0,
        }
    return {
        "required": ["timestamp", "price", "quantity", "is_buyer_maker"],
        "time_col": "timestamp",
        "json_cols": [],
        "numeric_min": 2,
    }

def validate_file(relpath):
    path = ROOT / relpath
    profile = profile_for(relpath)
    res = {
        "path": str(path),
        "exists": path.exists(),
        "rows": 0,
        "status": "FAIL",
        "action": "INSPECT",
        "bad_lines": 0,
        "duplicate_times": 0,
        "date_order": None,
        "missing_required": [],
        "null_bytes": 0,
        "sample_bad_lines": [],
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

        res["rows"] = len(rows)
        header_map = {h: i for i, h in enumerate(header)}
        missing = [c for c in profile["required"] if c not in header_map]
        res["missing_required"] = missing

        if missing:
            res["status"] = "FAIL"
            res["action"] = "ADD_REQUIRED_COLUMNS"
            return res

        if len(rows) == 0:
            res["status"] = "WARN"
            res["action"] = "NO_DATA_ROWS"
            return res

        tcol = header_map[profile["time_col"]]
        dts = []
        seen = set()

        numeric_candidates = []
        for i, h in enumerate(header):
            if h == profile["time_col"] or h in profile["json_cols"]:
                continue
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
                numeric_candidates.append(i)

        for line_no, row in enumerate(rows, start=2):
            causes = []

            if len(row) != len(header):
                causes.append(f"len={len(row)}")

            if len(row) <= tcol:
                causes.append("missing_time")
            else:
                dt = parse_dt(row[tcol])
                if dt is None:
                    causes.append("bad_time")
                else:
                    dts.append(dt)
                    key = row[tcol].strip()
                    if key in seen:
                        res["duplicate_times"] += 1
                    else:
                        seen.add(key)

            if profile["numeric_min"] > 0:
                numeric_ok = 0
                for i in numeric_candidates:
                    if len(row) > i:
                        v = str(row[i]).strip()
                        if v != "" and is_float(v):
                            numeric_ok += 1
                if numeric_ok < profile["numeric_min"]:
                    causes.append("not_enough_numeric_values")

            for jc in profile["json_cols"]:
                j = header_map[jc]
                if len(row) <= j:
                    causes.append(f"missing_{jc}")
                else:
                    txt = str(row[j]).strip()
                    if txt == "":
                        causes.append(f"empty_{jc}")
                    else:
                        try:
                            json.loads(txt)
                        except:
                            causes.append(f"bad_json_{jc}")

            if causes:
                res["bad_lines"] += 1
                if len(res["sample_bad_lines"]) < 3:
                    res["sample_bad_lines"].append({
                        "line": line_no,
                        "causes": causes,
                        "row": row
                    })

        res["date_order"] = monotonic_direction(dts) if dts else None

        if (
            res["bad_lines"] == 0
            and res["duplicate_times"] == 0
            and res["date_order"] in ["ascending", "descending", "single"]
            and len(res["missing_required"]) == 0
            and res["null_bytes"] == 0
        ):
            res["status"] = "OK"
            res["action"] = "NONE"
        else:
            res["status"] = "WARN"
            if res["null_bytes"] > 0:
                res["action"] = "REMOVE_NULL_BYTES"
            else:
                res["action"] = "INSPECT"

        return res

    except Exception as e:
        res["status"] = "FAIL"
        res["action"] = "READ_ERROR"
        res["error"] = str(e)
        return res

def main():
    audit = {rel: validate_file(rel) for rel in FILES}

    for rel, r in audit.items():
        print(
            f"{rel} | STATUS={r['status']} | ROWS={r['rows']} | "
            f"BAD_LINES={r['bad_lines']} | DUPLICATES={r['duplicate_times']} | "
            f"DATE_ORDER={r['date_order']} | NULL_BYTES={r['null_bytes']} | "
            f"ACTION={r['action']}"
        )

    with open(OUT / "lot_d_audit_v1.json", "w", encoding="utf-8") as f:
        json.dump(audit, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
