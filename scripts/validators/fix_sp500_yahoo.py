#!/usr/bin/env python3
import csv
import shutil
from pathlib import Path

p = Path("/home/ubuntu/seragone/data/sp500_daily.csv")
bak = Path("/home/ubuntu/seragone/data/sp500_daily.csv.bak")

if not bak.exists():
    shutil.copy2(p, bak)

with open(p, newline='') as f:
    rows = list(csv.reader(f))

if len(rows) < 4:
    raise SystemExit("Fichier trop court")

if rows[0] != ["Price", "Close", "High", "Low", "Open", "Volume"]:
    raise SystemExit(f"Header ligne 1 inattendu: {rows[0]}")

if not rows[1] or rows[1][0] != "Ticker":
    raise SystemExit(f"Header ligne 2 inattendu: {rows[1]}")

if rows[2] != ["Date", "", "", "", "", ""]:
    raise SystemExit(f"Header ligne 3 inattendu: {rows[2]}")

cleaned = []
for row in rows[3:]:
    if len(row) >= 6:
        cleaned.append([row[0], row[1], row[2], row[3], row[4], row[5]])

with open(p, "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["Date", "Close", "High", "Low", "Open", "Volume"])
    w.writerows(cleaned)

print("backup:", bak)
print("rows_written:", len(cleaned))
