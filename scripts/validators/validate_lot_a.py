#!/usr/bin/env python3
import csv
import json
import re
from pathlib import Path
from datetime import datetime

ROOT = Path("/home/ubuntu/seragone")
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

FILES = {
    "btc_daily.csv": {
        "path": ROOT / "data" / "btc_daily.csv",
        "header": ["Date", "Close", "High", "Low", "Open", "Volume"],
        "date_col": 0,
        "numeric_cols": [1, 2, 3, 4, 5],
        "mode": "strict",
    },
    "eth_daily.csv": {
        "path": ROOT / "data" / "eth_daily.csv",
        "header": ["date", "open", "high", "low", "close", "volume"],
        "date_col": 0,
        "numeric_cols": [1, 2, 3, 4, 5],
        "mode": "strict",
    },
    "sp500_daily.csv": {
        "path": ROOT / "data" / "sp500_daily.csv",
        "header": ["Date", "Close", "High", "Low", "Open", "Volume"],
        "date_col": 0,
        "numeric_cols": [1, 2, 3, 4, 5],
        "mode": "strict",
    },
}

def is_float(x):
    try:
        float(x)
        return True
    except:
        return False

def validate_strict(path, header, date_col, numeric_cols):
    res = {
        "exists": path.exists(),
        "readable": False,
        "header_ok": False,
        "bad_lines": 0,
        "duplicate_dates": 0,
        "date_sorted": True,
        "numeric_ok": True,
        "status": "FAIL",
        "action": "INSPECT",
        "sample_bad_lines": [],
    }
    if not path.exists():
        res["action"] = "MISSING_FILE"
        return res

    dates = []
    seen = set()

    try:
        with open(path, newline='') as f:
            r = csv.reader(f)
            first = next(r, None)
            res["readable"] = True
            res["header_ok"] = first == header

            prev_dt = None
            for i, row in enumerate(r, start=2):
                causes = []
                if len(row) != len(header):
                    causes.append(f"len={len(row)}")
                if len(row) <= date_col or DATE_RE.match((row[date_col] or "").strip()) is None:
                    causes.append("date_non_conforme")
                else:
                    cur_dt = datetime.strptime(row[date_col].strip(), "%Y-%m-%d")
                    dates.append(row[date_col].strip())
                    if prev_dt and cur_dt < prev_dt:
                        res["date_sorted"] = False
                    prev_dt = cur_dt

                for c in numeric_cols:
                    if len(row) <= c or not is_float((row[c] or "").strip()):
                        causes.append(f"numeric_col_{c}_invalid")
                        res["numeric_ok"] = False

                if causes:
                    res["bad_lines"] += 1
                    if len(res["sample_bad_lines"]) < 5:
                        res["sample_bad_lines"].append({
                            "line": i,
                            "row": row,
                            "causes": causes
                        })

        for d in dates:
            if d in seen:
                res["duplicate_dates"] += 1
            else:
                seen.add(d)

        if res["header_ok"] and res["bad_lines"] == 0 and res["duplicate_dates"] == 0 and res["date_sorted"] and res["numeric_ok"]:
            res["status"] = "OK"
            res["action"] = "NONE"
        elif res["readable"]:
            res["status"] = "WARN"
            res["action"] = "INSPECT"

        return res
    except Exception as e:
        res["status"] = "FAIL"
        res["action"] = "READ_ERROR"
        res["error"] = str(e)
        return res

def validate_yahoo_raw(path):
    res = {
        "exists": path.exists(),
        "readable": False,
        "header_ok": False,
        "bad_lines": None,
        "duplicate_dates": None,
        "date_sorted": None,
        "numeric_ok": None,
        "status": "FAIL",
        "action": "INSPECT",
        "detected_pattern": None,
    }
    if not path.exists():
        res["action"] = "MISSING_FILE"
        return res

    try:
        with open(path, newline='') as f:
            r = csv.reader(f)
            rows = [next(r, None) for _ in range(3)]
            res["readable"] = True

        if rows[0] == ["Price", "Close", "High", "Low", "Open", "Volume"] \
           and rows[1] and len(rows[1]) >= 1 and rows[1][0] == "Ticker" \
           and rows[2] == ["Date", "", "", "", "", ""]:
            res["detected_pattern"] = "YAHOO_RAW_MULTIHEADER"
            res["status"] = "FAIL_RAW_YAHOO"
            res["action"] = "NORMALIZE_YAHOO_HEADER"
            return res

        res["detected_pattern"] = "UNKNOWN"
        res["status"] = "WARN"
        res["action"] = "INSPECT"
        return res
    except Exception as e:
        res["status"] = "FAIL"
        res["action"] = "READ_ERROR"
        res["error"] = str(e)
        return res

def main():
    audit = {}
    for name, cfg in FILES.items():
        if cfg["mode"] == "strict":
            audit[name] = validate_strict(
                cfg["path"], cfg["header"], cfg["date_col"], cfg["numeric_cols"]
            )
        elif cfg["mode"] == "detect_yahoo_raw":
            audit[name] = validate_yahoo_raw(cfg["path"])

    order = ["btc_daily.csv", "eth_daily.csv", "sp500_daily.csv"]
    for name in order:
        r = audit[name]
        print(
            f"{name} | STATUS={r['status']} | EXISTS={r['exists']} | "
            f"HEADER_OK={r.get('header_ok')} | BAD_LINES={r.get('bad_lines')} | "
            f"DUPLICATE_DATES={r.get('duplicate_dates')} | DATE_SORTED={r.get('date_sorted')} | "
            f"NUMERIC_OK={r.get('numeric_ok')} | ACTION={r['action']}"
        )

    with open(OUT / "lot_a_audit.json", "w") as f:
        json.dump(audit, f, indent=2)

if __name__ == "__main__":
    main()
