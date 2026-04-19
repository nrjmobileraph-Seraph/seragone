#!/usr/bin/env python3
import csv
import json
import re
from pathlib import Path
from datetime import datetime

ROOT = Path("/home/ubuntu/seragone")
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

FILES = [
    "data/M2SL.csv",
    "data/btc_active_addresses.csv",
    "data/btc_difficulty_daily.csv",
    "data/btc_hashrate_daily.csv",
    "data/btc_transactions_daily.csv",
    "data/contagion_daily.csv",
    "data/exogene_daily.csv",
    "data/fear_greed.csv",
    "data/funding_rate_btc.csv",
    "data/binance_oi_btcusdt_daily.csv",
    "data/binance_taker_buysell_daily.csv",
    "data/onchain/exchange_netflow.csv",
    "data/onchain/funding_rate.csv",
    "data/onchain/mvrv.csv",
    "data/onchain/nupl.csv",
    "data/onchain/open_interest.csv",
    "data/onchain/puell_multiple.csv",
    "data/onchain/whale_ratio.csv",
]

DATE_PATTERNS = [
    ("%Y-%m-%d", re.compile(r"^\d{4}-\d{2}-\d{2}$")),
    ("%Y-%m-%d %H:%M:%S", re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")),
    ("%d/%m/%Y", re.compile(r"^\d{2}/\d{2}/\d{4}$")),
    ("%m/%d/%Y", re.compile(r"^\d{2}/\d{2}/\d{4}$")),
    ("%Y-%m", re.compile(r"^\d{4}-\d{2}$")),
]

TIME_HINTS = {"date", "time", "timestamp", "datetime", "ds"}
IGNORE_NUMERIC_NAMES = {"date", "time", "timestamp", "datetime"}

def is_float(x):
    try:
        float(str(x).strip().replace(",", ""))
        return True
    except:
        return False

def parse_dt(s):
    s = (s or "").strip()
    for fmt, pat in DATE_PATTERNS:
        if pat.match(s):
            try:
                return datetime.strptime(s, fmt), fmt
            except:
                pass
    return None, None

def pick_time_col(header, sample_rows):
    lowered = [str(h).strip().lower() for h in header]
    for i, h in enumerate(lowered):
        if h in TIME_HINTS or any(k in h for k in ["date", "time"]):
            return i, "header_hint"

    for c in range(len(header)):
        ok = 0
        checked = 0
        for row in sample_rows[:20]:
            if len(row) <= c:
                continue
            checked += 1
            dt, _ = parse_dt(row[c])
            if dt is not None:
                ok += 1
        if checked and ok >= max(2, checked // 2):
            return c, "sample_match"

    return None, "not_found"

def pick_numeric_cols(header, sample_rows, skip_col=None):
    cols = []
    lowered = [str(h).strip().lower() for h in header]
    for c in range(len(header)):
        if c == skip_col:
            continue
        if lowered[c] in IGNORE_NUMERIC_NAMES:
            continue
        ok = 0
        checked = 0
        for row in sample_rows[:50]:
            if len(row) <= c:
                continue
            v = str(row[c]).strip()
            if v == "":
                continue
            checked += 1
            if is_float(v):
                ok += 1
        if checked and ok >= max(2, int(checked * 0.7)):
            cols.append(c)
    return cols

def validate_file(relpath):
    path = ROOT / relpath
    res = {
        "path": str(path),
        "exists": path.exists(),
        "readable": False,
        "header_present": False,
        "rows": 0,
        "time_col": None,
        "time_detection": None,
        "numeric_cols": [],
        "bad_lines": 0,
        "duplicate_time_values": 0,
        "date_sorted": None,
        "status": "FAIL",
        "action": "INSPECT",
        "sample_bad_lines": [],
    }

    if not path.exists():
        res["action"] = "MISSING_FILE"
        return res

    try:
        with open(path, newline='', encoding='utf-8-sig') as f:
            r = csv.reader(f)
            header = next(r, None)
            if not header:
                res["action"] = "EMPTY_FILE"
                return res

            res["readable"] = True
            res["header_present"] = True
            rows = list(r)
            res["rows"] = len(rows)

        if res["rows"] == 0:
            res["status"] = "WARN"
            res["action"] = "NO_DATA_ROWS"
            return res

        time_col, time_detection = pick_time_col(header, rows)
        res["time_col"] = time_col
        res["time_detection"] = time_detection

        numeric_cols = pick_numeric_cols(header, rows, skip_col=time_col)
        res["numeric_cols"] = numeric_cols

        seen = set()
        prev_dt = None
        sorted_flag = True if time_col is not None else None

        for i, row in enumerate(rows, start=2):
            causes = []

            if len(row) != len(header):
                causes.append(f"len={len(row)}")

            if time_col is not None:
                if len(row) <= time_col:
                    causes.append("missing_time_col")
                else:
                    dt, fmt = parse_dt(row[time_col])
                    if dt is None:
                        causes.append("time_non_conforme")
                    else:
                        key = row[time_col].strip()
                        if key in seen:
                            res["duplicate_time_values"] += 1
                        else:
                            seen.add(key)
                        if prev_dt and dt < prev_dt:
                            sorted_flag = False
                        prev_dt = dt

            if numeric_cols:
                any_numeric = False
                for c in numeric_cols:
                    if len(row) > c and str(row[c]).strip() != "" and is_float(row[c]):
                        any_numeric = True
                        break
                if not any_numeric:
                    causes.append("no_numeric_value")

            if causes:
                res["bad_lines"] += 1
                if len(res["sample_bad_lines"]) < 5:
                    res["sample_bad_lines"].append({
                        "line": i,
                        "row": row,
                        "causes": causes
                    })

        res["date_sorted"] = sorted_flag

        if time_col is not None and numeric_cols and res["bad_lines"] == 0 and res["duplicate_time_values"] == 0 and (res["date_sorted"] in [True, None]):
            res["status"] = "OK"
            res["action"] = "NONE"
        elif res["readable"] and res["header_present"]:
            res["status"] = "WARN"
            if time_col is None:
                res["action"] = "ADD_TIME_SCHEMA"
            elif not numeric_cols:
                res["action"] = "ADD_NUMERIC_SCHEMA"
            else:
                res["action"] = "INSPECT"

        return res

    except Exception as e:
        res["status"] = "FAIL"
        res["action"] = "READ_ERROR"
        res["error"] = str(e)
        return res

def main():
    audit = {}
    for relpath in FILES:
        audit[relpath] = validate_file(relpath)

    for relpath in FILES:
        r = audit[relpath]
        print(
            f"{relpath} | STATUS={r['status']} | EXISTS={r['exists']} | "
            f"ROWS={r['rows']} | TIME_COL={r['time_col']} | "
            f"NUMERIC_COLS={len(r['numeric_cols'])} | BAD_LINES={r['bad_lines']} | "
            f"DUPLICATES={r['duplicate_time_values']} | DATE_SORTED={r['date_sorted']} | "
            f"ACTION={r['action']}"
        )

    with open(OUT / "lot_b_audit.json", "w", encoding="utf-8") as f:
        json.dump(audit, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
