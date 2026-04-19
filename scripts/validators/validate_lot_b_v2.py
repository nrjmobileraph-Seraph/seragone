#!/usr/bin/env python3
import csv
import json
from pathlib import Path
from datetime import datetime, timezone

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

DATE_FORMATS = [
    "%Y-%m-%d",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m",
    "%d/%m/%Y",
    "%m/%d/%Y",
]

PREFERRED_TIME_NAMES = ["date", "datetime", "ds", "time", "timestamp"]

def is_float(x):
    try:
        float(str(x).strip().replace(",", ""))
        return True
    except:
        return False

def parse_dt(value):
    s = str(value).strip().strip('"')
    if not s:
        return None

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt)
        except:
            pass

    if s.isdigit():
        try:
            n = int(s)
            if 1000000000 <= n <= 2000000000:
                return datetime.fromtimestamp(n, tz=timezone.utc).replace(tzinfo=None)
            if 1000000000000 <= n <= 2000000000000:
                return datetime.fromtimestamp(n / 1000, tz=timezone.utc).replace(tzinfo=None)
        except:
            pass

    return None

def pick_time_col(header, rows):
    lowered = [str(h).strip().lower() for h in header]

    for wanted in PREFERRED_TIME_NAMES:
        for i, h in enumerate(lowered):
            if h == wanted:
                ok = 0
                for row in rows[:20]:
                    if len(row) > i and parse_dt(row[i]) is not None:
                        ok += 1
                if ok >= 2:
                    return i, h

    for i, h in enumerate(lowered):
        if "date" in h or "time" in h:
            ok = 0
            for row in rows[:20]:
                if len(row) > i and parse_dt(row[i]) is not None:
                    ok += 1
            if ok >= 2:
                return i, h

    return None, None

def pick_numeric_cols(header, rows, skip_col=None):
    cols = []
    for i, h in enumerate(header):
        if i == skip_col:
            continue
        ok = 0
        checked = 0
        for row in rows[:50]:
            if len(row) <= i:
                continue
            v = str(row[i]).strip().strip('"')
            if v == "":
                continue
            checked += 1
            if is_float(v):
                ok += 1
        if checked > 0 and ok / checked >= 0.7:
            cols.append(i)
    return cols

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

def validate_file(relpath):
    path = ROOT / relpath
    res = {
        "path": str(path),
        "exists": path.exists(),
        "readable": False,
        "header_present": False,
        "rows": 0,
        "time_col": None,
        "time_col_name": None,
        "numeric_cols": [],
        "bad_lines": 0,
        "duplicate_time_values": 0,
        "date_order": None,
        "status": "FAIL",
        "action": "INSPECT",
        "sample_bad_lines": [],
    }

    if not path.exists():
        res["action"] = "MISSING_FILE"
        return res

    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            r = csv.reader(f)
            header = next(r, None)
            if not header:
                res["action"] = "EMPTY_FILE"
                return res
            rows = list(r)

        res["readable"] = True
        res["header_present"] = True
        res["rows"] = len(rows)

        if not rows:
            res["status"] = "WARN"
            res["action"] = "NO_DATA_ROWS"
            return res

        time_col, time_col_name = pick_time_col(header, rows)
        res["time_col"] = time_col
        res["time_col_name"] = time_col_name

        numeric_cols = pick_numeric_cols(header, rows, skip_col=time_col)
        res["numeric_cols"] = numeric_cols

        seen = set()
        parsed_dts = []

        for line_no, row in enumerate(rows, start=2):
            causes = []

            if len(row) != len(header):
                causes.append(f"len={len(row)}")

            if time_col is not None:
                if len(row) <= time_col:
                    causes.append("missing_time_col")
                else:
                    dt = parse_dt(row[time_col])
                    if dt is None:
                        causes.append("time_unparseable")
                    else:
                        key = str(row[time_col]).strip()
                        if key in seen:
                            res["duplicate_time_values"] += 1
                        else:
                            seen.add(key)
                        parsed_dts.append(dt)

            if numeric_cols:
                any_numeric = False
                for c in numeric_cols:
                    if len(row) > c:
                        v = str(row[c]).strip().strip('"')
                        if v != "" and is_float(v):
                            any_numeric = True
                            break
                if not any_numeric:
                    causes.append("no_numeric_value")

            if causes:
                res["bad_lines"] += 1
                if len(res["sample_bad_lines"]) < 5:
                    res["sample_bad_lines"].append({
                        "line": line_no,
                        "causes": causes,
                        "row": row
                    })

        if parsed_dts:
            res["date_order"] = monotonic_direction(parsed_dts)

        if (
            res["readable"]
            and res["header_present"]
            and res["rows"] > 0
            and time_col is not None
            and len(numeric_cols) > 0
            and res["bad_lines"] == 0
            and res["duplicate_time_values"] == 0
            and res["date_order"] in ["ascending", "descending", "single"]
        ):
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
    audit = {rel: validate_file(rel) for rel in FILES}

    for rel, r in audit.items():
        print(
            f"{rel} | STATUS={r['status']} | EXISTS={r['exists']} | "
            f"ROWS={r['rows']} | TIME_COL={r['time_col']}:{r['time_col_name']} | "
            f"NUMERIC_COLS={len(r['numeric_cols'])} | BAD_LINES={r['bad_lines']} | "
            f"DUPLICATES={r['duplicate_time_values']} | DATE_ORDER={r['date_order']} | "
            f"ACTION={r['action']}"
        )

    with open(OUT / "lot_b_audit_v2.json", "w", encoding="utf-8") as f:
        json.dump(audit, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
