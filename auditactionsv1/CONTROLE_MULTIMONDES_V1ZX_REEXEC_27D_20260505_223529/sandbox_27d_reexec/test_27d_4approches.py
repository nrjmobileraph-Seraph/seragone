#!/usr/bin/env python3
"""
4 tests pour savoir à quoi sert vraiment le 27D.
Test 1 : 27D comme filtre du 10D
Test 2 : Jugé sur lift, recall bear, DD futur
Test 3 : Agrégation par régime
Test 4 : Cible souple (max forward sur fenêtre)
"""
import numpy as np, pandas as pd, json
from datetime import datetime
import warnings; warnings.filterwarnings('ignore')

# ═══ CHARGER DONNÉES UNIFIÉES ═══
hist = pd.read_csv('historique_27eq.csv')
hist['Date'] = pd.to_datetime(hist['Date'])
real_123 = pd.read_csv('couches_123_daily.csv')
real_123['date'] = pd.to_datetime(real_123['date'])

mapping = {
    'shock_24h':'c3_shock','echoes_24h':'c3_echo','damping_24h':'c3_damp',
    'mom_1h':'c2_mom','burst_1h':'c2_burst','compress_1h':'c2_comp',
    'tick_burst':'c1_burst','ofi':'c1_ofi','size_change':'c1_size',
}
df = hist.merge(real_123, left_on='Date', right_on='date', how='inner')
for old, new in mapping.items(): df[old] = df[new]

EQUATIONS = ['halving','mayer','vol_an','saison','skew','macro','corrections','levy90','hurst','sir','omori','autocorr','hopf7','levy7','dow','range_pos','range_intra','gap','shock_24h','echoes_24h','damping_24h','mom_1h','burst_1h','compress_1h','tick_burst','ofi','size_change']

# Ajouter plusieurs cibles
df['forward_3d'] = df['Close'].pct_change(3).shift(-3)
df['forward_10d'] = df['Close'].pct_change(10).shift(-10)
# Max forward 5j (plus haut des 5 prochains jours, cible souple)
df['forward_max_5d'] = df['Close'].rolling(5).max().shift(-5) / df['Close'] - 1
df['forward_min_5d'] = df['Close'].rolling(5).min().shift(-5) / df['Close'] - 1

df = df[['Date','Close']+EQUATIONS+['forward_5d','forward_3d','forward_10d','forward_max_5d','forward_min_5d']].dropna().reset_index(drop=True)

# Ajouter régime basé sur Mayer + return 90d
df['ret_90d'] = df['Close'].pct_change(90)
def classify_regime(row):
    if row['ret_90d'] < -0.20 or row['mayer'] < 0.2: return 'CRISE'
    if row['ret_90d'] > 0.30 or row['mayer'] > 0.7: return 'EXPLOSION'
    return 'RESPIRATION'
df['regime'] = df.apply(classify_regime, axis=1)

train = df[(df['Date'] >= '2022-01-01') & (df['Date'] < '2025-01-01')].reset_index(drop=True)
test = df[(df['Date'] >= '2025-01-01')].reset_index(drop=True)
print(f"Train : {len(train)}, Test : {len(test)}")
print(f"Régimes train : {train['regime'].value_counts().to_dict()}")
print(f"Régimes test  : {test['regime'].value_counts().to_dict()}")

# ═══ GÉNÉRATION MONDES ═══
N_CANDIDATES = 50000
SH, SB = 0.6, 0.4
np.random.seed(42)
cands = []
for _ in range(N_CANDIDATES):
    n = np.random.randint(5, 11)
    dims = tuple(sorted(np.random.choice(len(EQUATIONS), size=n, replace=False).tolist()))
    orients = tuple(np.random.choice([-1,1], size=n).tolist())
    cands.append((dims, orients))
cands = list(set(cands))

def sig(dims, orients, data):
    s = np.ones(len(data), dtype=bool)
    for d, o in zip(dims, orients):
        v = data[EQUATIONS[d]].values
        s &= (v > SH) if o == 1 else (v < SB)
    return s

# ═══════════════════════════════════════════════════════
# TEST 1 — 27D COMME FILTRE DU 10D
# ═══════════════════════════════════════════════════════
print("\n" + "="*60)
print("TEST 1 — 27D comme FILTRE du 10D")
print("="*60)

# Simuler 10D = utiliser seulement les 15 premières équations (couches 4-9)
DIMS_10D = list(range(15))  # équations 0-14
DIMS_27D_ONLY = list(range(15, 27))  # équations 15-26 (couches 1-4)

# Construire mondes 10D sur train
scored_10d = []
for dims, orients in cands:
    if not all(d in DIMS_10D for d in dims): continue
    s = sig(dims, orients, train)
    n = s.sum()
    if n < 10: continue
    fwd = train['forward_5d'].values[s]; fwd = fwd[~np.isnan(fwd)]
    if len(fwd) < 10: continue
    wr = np.mean(fwd > 0); mr = np.mean(fwd)
    if wr >= 0.55 and mr > 0:
        scored_10d.append((wr * np.log(1+n) * mr, dims, orients, s))
scored_10d.sort(key=lambda x: -x[0])
# Sélection
sel_10d = []
for e, d, o, s in scored_10d:
    if len(sel_10d) >= 500: break
    ss = set(np.where(s)[0])
    ok = True
    for _, _, _, sp in sel_10d[-50:]:
        sp_set = set(np.where(sp)[0])
        u = len(ss | sp_set)
        if u > 0 and len(ss & sp_set)/u > 0.30: ok = False; break
    if ok: sel_10d.append((e, d, o, s))
print(f"Mondes 10D sélectionnés : {len(sel_10d)}")

# Construire mondes 27D-only (couches 1-4)
scored_27o = []
for dims, orients in cands:
    if not all(d in DIMS_27D_ONLY for d in dims): continue
    s = sig(dims, orients, train)
    n = s.sum()
    if n < 10: continue
    fwd = train['forward_5d'].values[s]; fwd = fwd[~np.isnan(fwd)]
    if len(fwd) < 10: continue
    wr = np.mean(fwd > 0); mr = np.mean(fwd)
    scored_27o.append((abs(wr - 0.5) * np.log(1+n) * abs(mr), dims, orients, s, wr, mr))
scored_27o.sort(key=lambda x: -x[0])
sel_27o = []
for e, d, o, s, wr, mr in scored_27o[:2000]:
    if len(sel_27o) >= 300: break
    ss = set(np.where(s)[0])
    ok = True
    for _, _, _, sp, _, _ in sel_27o[-50:]:
        sp_set = set(np.where(sp)[0])
        u = len(ss | sp_set)
        if u > 0 and len(ss & sp_set)/u > 0.30: ok = False; break
    if ok: sel_27o.append((e, d, o, s, wr, mr))
print(f"Mondes 27D-only sélectionnés : {len(sel_27o)}")

# Calculer signaux sur test
sig_10d_test = np.zeros(len(test), dtype=int)
for _, d, o, _ in sel_10d:
    sig_10d_test += sig(d, o, test).astype(int)

# 27D-bear = mondes 27D qui signalent du bear (mr < 0 sur train)
bear_27d_signal = np.zeros(len(test), dtype=int)
bull_27d_signal = np.zeros(len(test), dtype=int)
for _, d, o, _, wr, mr in sel_27o:
    s = sig(d, o, test)
    if mr < -0.005:  # monde "bear" (return train négatif)
        bear_27d_signal += s.astype(int)
    elif mr > 0.005:  # monde "bull"
        bull_27d_signal += s.astype(int)

# Filtre : long 10D OK seulement si bear_27d pas trop fort
threshold_10d = 40
threshold_bear_27d = np.percentile(bear_27d_signal, 80)
print(f"Seuil bear 27D : {threshold_bear_27d:.0f} (percentile 80)")

longs_bruts = sig_10d_test >= threshold_10d
longs_filtrés = longs_bruts & (bear_27d_signal < threshold_bear_27d)

n_bruts = longs_bruts.sum()
n_filtrés = longs_filtrés.sum()
n_bloqués = n_bruts - n_filtrés

rets_bruts = [test['forward_5d'].iloc[i] for i in range(len(test)) if longs_bruts[i] and not np.isnan(test['forward_5d'].iloc[i])]
rets_filtrés = [test['forward_5d'].iloc[i] for i in range(len(test)) if longs_filtrés[i] and not np.isnan(test['forward_5d'].iloc[i])]

if rets_bruts:
    print(f"Longs 10D bruts       : {n_bruts} trades, WR {np.mean([r>0 for r in rets_bruts])*100:.1f}%, return {np.mean(rets_bruts)*100:+.2f}%")
if rets_filtrés:
    print(f"Longs 10D + filtre 27D: {n_filtrés} trades ({n_bloqués} bloqués), WR {np.mean([r>0 for r in rets_filtrés])*100:.1f}%, return {np.mean(rets_filtrés)*100:+.2f}%")

# ═══════════════════════════════════════════════════════
# TEST 2 — MÉTRIQUES NON-WR (lift, recall bear, DD futur)
# ═══════════════════════════════════════════════════════
print("\n" + "="*60)
print("TEST 2 — Métriques alternatives")
print("="*60)

# Mondes 27D complets
print("Construction mondes 27D complets...")
scored = []
for dims, orients in cands:
    s = sig(dims, orients, train)
    n = s.sum()
    if n < 10: continue
    fwd = train['forward_5d'].values[s]; fwd = fwd[~np.isnan(fwd)]
    if len(fwd) < 10: continue
    wr = np.mean(fwd > 0); mr = np.mean(fwd)
    if wr >= 0.55 and mr > 0:
        scored.append((wr * np.log(1+n) * mr, dims, orients, s))
scored.sort(key=lambda x: -x[0])
sel_27d = []
for e, d, o, s in scored:
    if len(sel_27d) >= 500: break
    ss = set(np.where(s)[0])
    ok = True
    for _, _, _, sp in sel_27d[-50:]:
        sp_set = set(np.where(sp)[0])
        u = len(ss | sp_set)
        if u > 0 and len(ss & sp_set)/u > 0.30: ok = False; break
    if ok: sel_27d.append((e, d, o, s))
print(f"  {len(sel_27d)} mondes 27D complets")

conv_test = np.zeros(len(test), dtype=int)
for _, d, o, _ in sel_27d:
    conv_test += sig(d, o, test).astype(int)

mean_baseline = test['forward_5d'].mean()
# Lift : rendement conditionnel / rendement baseline
print("\nLIFT par seuil de convergence (return 5d vs baseline) :")
for t in [1, 10, 20, 40, 80]:
    days = (conv_test >= t).sum()
    if days < 3: continue
    rets = [test['forward_5d'].iloc[i] for i in range(len(test)) if conv_test[i] >= t and not np.isnan(test['forward_5d'].iloc[i])]
    if not rets: continue
    lift = np.mean(rets) - mean_baseline
    print(f"  ≥{t:3d} : {days:3d} jours, return moyen {np.mean(rets)*100:+.2f}% (baseline {mean_baseline*100:+.2f}%), lift {lift*100:+.2f}%")

# Recall bear : parmi les jours bear (forward < -2%), combien détectés par conv forte ?
bear_days = test['forward_5d'] < -0.02
print(f"\nRECALL BEAR ({bear_days.sum()} jours bear dans test) :")
for t in [10, 20, 40]:
    detected = (conv_test >= t) & bear_days
    recall = detected.sum() / bear_days.sum() * 100 if bear_days.sum() > 0 else 0
    print(f"  ≥{t:3d} mondes détecte {detected.sum()}/{bear_days.sum()} jours bear ({recall:.0f}% recall)")

# DD futur : quand on entre, quel DD en face ?
print(f"\nDRAWDOWN FUTUR sur fenêtre 5j (min 5d) :")
for t in [1, 10, 20, 40]:
    days = [i for i in range(len(test)) if conv_test[i] >= t and not np.isnan(test['forward_min_5d'].iloc[i])]
    if len(days) < 3: continue
    dds = [test['forward_min_5d'].iloc[i] for i in days]
    print(f"  ≥{t:3d} : DD moyen {np.mean(dds)*100:+.2f}%, DD min {np.min(dds)*100:+.2f}%")

# ═══════════════════════════════════════════════════════
# TEST 3 — AGRÉGATION PAR RÉGIME
# ═══════════════════════════════════════════════════════
print("\n" + "="*60)
print("TEST 3 — Mondes calibrés par régime")
print("="*60)

for regime in ['CRISE', 'RESPIRATION', 'EXPLOSION']:
    train_r = train[train['regime'] == regime].reset_index(drop=True)
    if len(train_r) < 50: 
        print(f"\n{regime}: trop peu de jours train ({len(train_r)})")
        continue

    # Mondes calibrés sur ce régime
    scored_r = []
    for dims, orients in cands[:20000]:
        s = sig(dims, orients, train_r)
        n = s.sum()
        if n < 5: continue
        fwd = train_r['forward_5d'].values[s]; fwd = fwd[~np.isnan(fwd)]
        if len(fwd) < 5: continue
        wr = np.mean(fwd > 0); mr = np.mean(fwd)
        if wr >= 0.60:
            scored_r.append((wr * np.log(1+n), dims, orients, s, wr))
    scored_r.sort(key=lambda x: -x[0])

    # Top 100 uniques
    sel_r = []
    for e, d, o, s, wr in scored_r:
        if len(sel_r) >= 100: break
        ss = set(np.where(s)[0])
        ok = True
        for _, _, _, sp, _ in sel_r[-20:]:
            sp_set = set(np.where(sp)[0])
            u = len(ss | sp_set)
            if u > 0 and len(ss & sp_set)/u > 0.30: ok = False; break
        if ok: sel_r.append((e, d, o, s, wr))
    
    # Test sur jours du même régime
    test_r = test[test['regime'] == regime].reset_index(drop=True)
    if len(test_r) < 10:
        print(f"\n{regime}: {len(sel_r)} mondes, test trop court ({len(test_r)} jours)")
        continue
    
    conv = np.zeros(len(test_r), dtype=int)
    for _, d, o, _, _ in sel_r:
        conv += sig(d, o, test_r).astype(int)
    
    rets_all = [test_r['forward_5d'].iloc[i] for i in range(len(test_r)) if conv[i] >= 10 and not np.isnan(test_r['forward_5d'].iloc[i])]
    print(f"\n{regime}: {len(sel_r)} mondes, {len(test_r)} jours test")
    if rets_all:
        print(f"  ≥10 conv : {len(rets_all)} tirs, WR {np.mean([r>0 for r in rets_all])*100:.1f}%, return {np.mean(rets_all)*100:+.2f}%")

# ═══════════════════════════════════════════════════════
# TEST 4 — CIBLE SOUPLE (max forward 5j)
# ═══════════════════════════════════════════════════════
print("\n" + "="*60)
print("TEST 4 — Cible SOUPLE (peut-on capter un PIC dans les 5j ?)")
print("="*60)

# Calibrer mondes sur max_forward_5d > 3% (tirer quand le prix PEUT faire +3% dans les 5j)
scored_soft = []
for dims, orients in cands:
    s = sig(dims, orients, train)
    n = s.sum()
    if n < 10: continue
    max_fwd = train['forward_max_5d'].values[s]; max_fwd = max_fwd[~np.isnan(max_fwd)]
    if len(max_fwd) < 10: continue
    # hit = a atteint +3% dans 5j
    hit_rate = np.mean(max_fwd > 0.03)
    if hit_rate >= 0.70:
        scored_soft.append((hit_rate * np.log(1+n), dims, orients, s, hit_rate))
scored_soft.sort(key=lambda x: -x[0])

sel_soft = []
for e, d, o, s, hr in scored_soft:
    if len(sel_soft) >= 300: break
    ss = set(np.where(s)[0])
    ok = True
    for _, _, _, sp, _ in sel_soft[-30:]:
        sp_set = set(np.where(sp)[0])
        u = len(ss | sp_set)
        if u > 0 and len(ss & sp_set)/u > 0.30: ok = False; break
    if ok: sel_soft.append((e, d, o, s, hr))
print(f"Mondes cible souple : {len(sel_soft)}")

conv_soft = np.zeros(len(test), dtype=int)
for _, d, o, _, _ in sel_soft:
    conv_soft += sig(d, o, test).astype(int)

for t in [10, 20, 40, 80]:
    days = (conv_soft >= t).sum()
    if days < 3: continue
    hits = [test['forward_max_5d'].iloc[i] > 0.03 for i in range(len(test)) if conv_soft[i] >= t and not np.isnan(test['forward_max_5d'].iloc[i])]
    if not hits: continue
    print(f"  ≥{t:3d} mondes : {days:3d} jours, HIT RATE (+3% dans 5j) {np.mean(hits)*100:.1f}%")

print("\n" + "="*60)
print("RÉSUMÉ DES 4 TESTS")
print("="*60)
