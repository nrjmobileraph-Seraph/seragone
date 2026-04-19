#!/usr/bin/env python3
import csv
import shutil
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path("/home/ubuntu/seragone")

FILES = [
    "data/btc_active_addresses.csv",
    "data/btc_difficulty_daily.csv",
    "data/btc_hashrate_daily.csv",
    "data/btc_transactions_daily.csv",
    "data/fear_greed.csv",
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
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M:%S.%f",
    "%d/%m/%Y",
    "%m/%d/%Y",
    "%Y-%m",
]

TIME_HINTS = ["date", "time", "timestamp", "datetime", "ds"]

def parse_dt(x):
    s = str(x).strip().strip('"')
    if s == "":
        return None

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt)
        except:
            pass

    try:
        v = float(s)
        if v > 1e12:
            return datetime.fromtimestamp(v / 1000.0, tz=timezone.utc).replace(tzinfo=None)
        if v > 1e9:
            return datetime.fromtimestamp(v, tz=timezone.utc).replace(tzinfo=None)
    except:
        pass

    return None

def detect_time_col(header, rows):
    low = [str(h).strip().lower() for h in header]
    for i, h in enumerate(low):
        if any(k in h for k in TIME_HINTS):
            return i

    best_col = 0
    best_score = -1
    for c in range(len(header)):
        ok = 0
        checked = 0
        for row in rows[:50]:
            if len(row) <= c:
                continue
            v = str(row[c]).strip()
            if v == "":
                continue
            checked += 1
            if parse_dt(v) is not None:
                ok += 1
        score = ok / checked if checked else -1
        if score > best_score:
            best_score = score
            best_col = c
    return best_col

for rel in FILES:
    path = ROOT / rel
    if not path.exists():
        print(f"{rel} | MISSING")
        continue

    backup = path.with_suffix(path.suffix + ".bak_sort_v2")
    if not backup.exists():
        shutil.copy2(path, backup)

    with open(path, newline="", encoding="utf-8-sig") as f:
        r = csv.reader(f)
        header = next(r, None)
        rows = list(r)

    if not header or not rows:
        print(f"{rel} | SKIP_EMPTY")
        continue

    tcol = detect_time_col(header, rows)

    sortable = []
    unsortable = []
    for row in rows:
        if len(row) <= tcol:
            unsortable.append(row)
            continue
        dt = parse_dt(row[tcol])
        if dt is None:
            unsortable.append(row)
        else:
            sortable.append((dt, row))

    sortable.sort(key=lambda x: x[0])

    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for _, row in sortable:
            w.writerow(row)
        for row in unsortable:
            w.writerow(row)

    print(f"{rel} | SORTED_V2 | time_col={tcol} | rows={len(rows)} | unsortable={len(unsortable)}")
