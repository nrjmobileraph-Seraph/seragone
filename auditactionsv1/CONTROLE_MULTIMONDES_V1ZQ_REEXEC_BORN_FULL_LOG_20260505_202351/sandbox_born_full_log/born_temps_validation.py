#!/usr/bin/env python3
"""
BORN TEMPS — VALIDATION PAR CYCLE + MODULE LIVE
=================================================

PARTIE A : Validation par cycle (3, 4, 5) des signaux découverts
PARTIE B : Module live born_temps_live.py pour le VPS

Signaux à valider :
  - 3/3 lentes P25 : n=64, WR10=84%, WR20=88%
  - Born pondéré P20 ≥0.40 : n=388, WR10=63%
  - Born pondéré P25 ≥0.50 : n=277, WR10=64%
"""

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

HALVINGS = [
    ('Cycle 3', '2016-07-09', '2020-05-11'),
    ('Cycle 4', '2020-05-11', '2024-04-20'),
    ('Cycle 5', '2024-04-20', '2030-01-01'),
]

LAYERS = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9']

BORN_WEIGHTS = {
    'L1': 0.06, 'L2': 0.07, 'L3': 0.08, 'L4': 0.10,
    'L5': 0.11, 'L6': 0.12, 'L7': 0.13, 'L8': 0.15, 'L9': 0.18,
}

print("=" * 80)
print("BORN TEMPS — VALIDATION PAR CYCLE")
print("=" * 80)

# ═══════════════════════════════════════════════════════
# CHARGER
# ═══════════════════════════════════════════════════════

df = pd.read_csv('/home/ubuntu/labo_27d/banc_27d_enrichi_v4.csv')
df['Date'] = pd.to_datetime(df['Date'])
n = len(df)

close_col = 'Close' if 'Close' in df.columns else 'close'
df['r5'] = df[close_col].pct_change(5).shift(-5)
df['r10'] = df[close_col].pct_change(10).shift(-10)
df['r20'] = df[close_col].pct_change(20).shift(-20)

# Distances par couche
for L in LAYERS:
    cols = [f'{L}_{m}' for m in ['d', 'n', 's'] if f'{L}_{m}' in df.columns]
    if len(cols) >= 3:
        df[f'{L}_dist'] = np.sqrt((df[cols[0]] - 0.5)**2 + (df[cols[1]] - 0.5)**2 + (df[cols[2]] - 0.5)**2)

# Cycles
df['cycle'] = 'Hors cycle'
for name, start, end in HALVINGS:
    m = (df['Date'] >= start) & (df['Date'] < end)
    df.loc[m, 'cycle'] = name

print(f"  {n} jours")
for c in ['Cycle 3', 'Cycle 4', 'Cycle 5']:
    nc = (df['cycle'] == c).sum()
    print(f"  {c} : {nc} jours")

# ═══════════════════════════════════════════════════════
# CALCULER LES SIGNAUX
# ═══════════════════════════════════════════════════════

# Signal 1 : 3/3 lentes P25 glissant
df['lentes_3sur3'] = False
# Signal 2 : Born pondéré P20 ≥ 0.40
df['born_p20_040'] = False
# Signal 3 : Born pondéré P25 ≥ 0.50
df['born_p25_050'] = False
# Signal 4 : ≥ 6/9 couches P15
df['conv_6sur9_p15'] = False

df['born_score_p20'] = 0.0
df['born_score_p25'] = 0.0
df['n_proches_p15'] = 0
df['n_lentes_p25'] = 0

for i in range(365, n):
    # Lentes P25
    n_lentes = 0
    for L in ['L7', 'L8', 'L9']:
        col = f'{L}_dist'
        if col not in df.columns: continue
        hist = df[col].iloc[max(0, i-365):i].dropna().values
        if len(hist) < 50: continue
        if df[col].iloc[i] <= np.quantile(hist, 0.25):
            n_lentes += 1
    df.iloc[i, df.columns.get_loc('n_lentes_p25')] = n_lentes
    if n_lentes >= 3:
        df.iloc[i, df.columns.get_loc('lentes_3sur3')] = True

    # Born P20
    bs20 = 0.0
    for L in LAYERS:
        col = f'{L}_dist'
        if col not in df.columns: continue
        hist = df[col].iloc[max(0, i-365):i].dropna().values
        if len(hist) < 50: continue
        if df[col].iloc[i] <= np.quantile(hist, 0.20):
            bs20 += BORN_WEIGHTS[L]
    df.iloc[i, df.columns.get_loc('born_score_p20')] = bs20
    if bs20 >= 0.40:
        df.iloc[i, df.columns.get_loc('born_p20_040')] = True

    # Born P25
    bs25 = 0.0
    for L in LAYERS:
        col = f'{L}_dist'
        if col not in df.columns: continue
        hist = df[col].iloc[max(0, i-365):i].dropna().values
        if len(hist) < 50: continue
        if df[col].iloc[i] <= np.quantile(hist, 0.25):
            bs25 += BORN_WEIGHTS[L]
    df.iloc[i, df.columns.get_loc('born_score_p25')] = bs25
    if bs25 >= 0.50:
        df.iloc[i, df.columns.get_loc('born_p25_050')] = True

    # Convergence 6/9 P15
    n_p = 0
    for L in LAYERS:
        col = f'{L}_dist'
        if col not in df.columns: continue
        hist = df[col].iloc[max(0, i-365):i].dropna().values
        if len(hist) < 50: continue
        if df[col].iloc[i] <= np.quantile(hist, 0.15):
            n_p += 1
    df.iloc[i, df.columns.get_loc('n_proches_p15')] = n_p
    if n_p >= 6:
        df.iloc[i, df.columns.get_loc('conv_6sur9_p15')] = True

# ═══════════════════════════════════════════════════════
# PARTIE A — VALIDATION PAR CYCLE
# ═══════════════════════════════════════════════════════

signals = [
    ('3/3 lentes P25', 'lentes_3sur3'),
    ('Born P20 >= 0.40', 'born_p20_040'),
    ('Born P25 >= 0.50', 'born_p25_050'),
    ('6/9 couches P15', 'conv_6sur9_p15'),
]

print(f"\n{'='*80}")
print("VALIDATION PAR CYCLE")
print(f"{'='*80}")

for sig_name, sig_col in signals:
    print(f"\n  --- {sig_name} ---")
    print(f"  {'Cycle':<12} {'n':>5} {'WR5':>6} {'WR10':>6} {'WR20':>6} {'lift10':>8} {'lift20':>8}")
    print("  " + "-" * 55)

    for cycle in ['Cycle 3', 'Cycle 4', 'Cycle 5', 'TOTAL']:
        if cycle == 'TOTAL':
            mask = df[sig_col] & (~np.isnan(df['r10']))
        else:
            mask = df[sig_col] & (df['cycle'] == cycle) & (~np.isnan(df['r10']))
        nb = mask.sum()
        if nb < 3:
            print(f"  {cycle:<12} {nb:>5}   (trop peu)")
            continue
        wr5 = (df.loc[mask, 'r5'] > 0).mean() * 100
        wr10 = (df.loc[mask, 'r10'] > 0).mean() * 100
        wr20 = (df.loc[mask, 'r20'] > 0).mean() * 100
        l10 = df.loc[mask, 'r10'].mean() * 100
        l20 = df.loc[mask, 'r20'].mean() * 100
        alive = "VIVANT" if wr10 > 55 else "FAIBLE" if wr10 > 50 else "MORT"
        print(f"  {cycle:<12} {nb:>5} {wr5:>5.0f}% {wr10:>5.0f}% {wr20:>5.0f}% "
              f"{l10:>+7.2f}% {l20:>+7.2f}%  {alive}")

    # Baseline par cycle
    print(f"  {'---':>12}")
    for cycle in ['Cycle 3', 'Cycle 4', 'Cycle 5']:
        cm = (df['cycle'] == cycle) & (~np.isnan(df['r10']))
        if cm.sum() < 50: continue
        wr_b = (df.loc[cm, 'r10'] > 0).mean() * 100
        l_b = df.loc[cm, 'r10'].mean() * 100
        print(f"  {'base '+cycle:<12} {cm.sum():>5} {wr_b:>17.0f}% {'':>6} {l_b:>+7.2f}%")

# ═══════════════════════════════════════════════════════
# DÉTAIL SIGNAL STAR : 3/3 lentes P25
# ═══════════════════════════════════════════════════════

print(f"\n{'='*80}")
print("DÉTAIL — 3/3 lentes P25 (WR 84%)")
print(f"{'='*80}")

mask_star = df['lentes_3sur3'] & (~np.isnan(df['r10']))
if mask_star.sum() > 0:
    star = df[mask_star][['Date', close_col, 'cycle', 'r5', 'r10', 'r20', 'n_lentes_p25']].copy()
    print(f"\n  {len(star)} jours :")
    for _, row in star.iterrows():
        date_str = row['Date'].strftime('%Y-%m-%d')
        r10v = row['r10'] * 100 if not np.isnan(row['r10']) else 0
        r20v = row['r20'] * 100 if not np.isnan(row['r20']) else 0
        win = "V" if row['r10'] > 0 else "X" if not np.isnan(row['r10']) else "?"
        print(f"    {date_str} | {row['cycle']:<10} | {row[close_col]:>10.0f}$ | "
              f"r10={r10v:>+5.1f}% r20={r20v:>+5.1f}% {win}")

# ═══════════════════════════════════════════════════════
# OVERLAP AVEC PROVINCES
# ═══════════════════════════════════════════════════════

print(f"\n{'='*80}")
print("OVERLAP AVEC PROVINCES EXISTANTES")
print(f"{'='*80}")

# Charger les résultats de provinces si disponibles
# On vérifie si les jours Born coïncident avec Exhaustion ou Portance
# en utilisant les colonnes q_long, score structurel etc.

if 'L9_q' in df.columns and 'L7_s' in df.columns:
    # Proxy Portance : score structurel approximé
    for c in ['Cycle 3', 'Cycle 4', 'Cycle 5']:
        cm = df['cycle'] == c
        if cm.sum() < 100: continue
        cdf = df[cm]

        # Born P25>=0.50 actif
        born_days = set(cdf[cdf['born_p25_050']].index)
        # Portance proxy : L7_s >= P70 local
        l7s_thr = cdf['L7_s'].quantile(0.70) if 'L7_s' in cdf.columns else 999
        port_days = set(cdf[cdf['L7_s'] >= l7s_thr].index) if 'L7_s' in cdf.columns else set()

        overlap = len(born_days & port_days)
        union = len(born_days | port_days)
        jaccard = overlap / union if union > 0 else 0
        print(f"  {c} : Born={len(born_days)}j, Portance~={len(port_days)}j, "
              f"overlap={overlap}j, Jaccard={jaccard:.2f}")

print(f"\n{'='*80}")
print("FIN VALIDATION")
print(f"{'='*80}")
