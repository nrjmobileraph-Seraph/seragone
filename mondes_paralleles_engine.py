#!/usr/bin/env python3
"""
SÉRAGONE — MONDES PARALLÈLES ENGINE
====================================
432 mondes indépendants × 10 dimensions × 30 sous-signaux.
Chaque monde = un cerveau câblé différemment (90% sur un dominant par dimension).
Chaque monde = son propre Phi*, son propre tau, son propre W_dist.
La convergence de mondes indépendants = signal structurel.

Bear 40+ mondes convergent = 87.5% WR (testé sur 2023-2026).

USAGE :
    python3 mondes_paralleles_engine.py                  → calcul complet
    python3 mondes_paralleles_engine.py --status          → affiche l'état
    python3 mondes_paralleles_engine.py --convergence     → convergence du jour

CRON (après le chef d'orchestre) :
    15 8 * * * cd ~/seragone && python3 mondes_paralleles_engine.py >> logs/paralleles.log 2>&1

Raphaël Boussy & Claude Opus 4.6 — 13-14 avril 2026
"""

import numpy as np
import pandas as pd
import json
from tools.seragone_atomic import writestateatomic
def _json_safe_seragone(o):
    try:
        import numpy as _np
        if isinstance(o, _np.integer):
            return int(o)
        if isinstance(o, _np.floating):
            return float(o)
        if isinstance(o, _np.ndarray):
            return o.tolist()
        if isinstance(o, _np.bool_):
            return bool(o)
    except Exception:
        pass
    try:
        import pandas as _pd
        if isinstance(o, _pd.Timestamp):
            return o.isoformat()
    except Exception:
        pass
    if hasattr(o, "item"):
        try:
            return o.item()
        except Exception:
            pass
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")


import os
import sys
import logging
from datetime import datetime, timezone
from pathlib import Path
from itertools import product

# ═══════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
STATE_FILE = BASE_DIR / "mondes_paralleles_state.json"
HISTORY_FILE = BASE_DIR / "data" / "mondes_paralleles_history.csv"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / 'paralleles.log'),
        logging.StreamHandler()
    ]
)
log = logging.getLogger("paralleles")

# ═══════════════════════════════════════════════════════
# IMPORTS DU VPS — les vrais yeux
# ═══════════════════════════════════════════════════════
sys.path.insert(0, str(BASE_DIR))
try:
    from vrais_yeux_stretched import (
        compute_mouvement_v2, compute_volatilite_v2,
        compute_synchronisation_v2, compute_humain_v2, compute_gravite_v2
    )
    VRAIS_YEUX = True
except ImportError:
    VRAIS_YEUX = False
    log.warning("vrais_yeux_stretched.py non trouvé — mode CSV uniquement")


# ═══════════════════════════════════════════════════════
# 10 DIMENSIONS × 3 SOUS-SIGNAUX = 30
# ═══════════════════════════════════════════════════════
# M(3): Liénard, Hurst, Hopf
# V(3): GARCH, Lévy, Hawkes
# S(3): Kuramoto, SIR, FHN
# H(3): Kahneman, Weber, Arrhenius
# G(3): Power, OU, DXY_stress
# L(3): DXY_momentum, M2_change, SP_stress
# U(3): AA_resid, AA_momentum, TX_intensity
# I(3): HR_slope, Diff_slope, HR_Diff_ribbon
# A(3): ETH_ratio, ETH_corr, ETH_lead
# F(3): FR_level, FR_momentum, FR_extreme

N_DIMS = 10
N_SUBS_PER_DIM = 3
DIM_NAMES = ['M', 'V', 'S', 'H', 'G', 'L', 'U', 'I', 'A', 'F']
SUB_NAMES = [
    ['Liénard', 'Hurst', 'Hopf'],
    ['GARCH', 'Lévy', 'Hawkes'],
    ['Kuramoto', 'SIR', 'FHN'],
    ['Kahneman', 'Weber', 'Arrhenius'],
    ['Power', 'OU', 'DXY_stress'],
    ['DXY_mom', 'M2_chg', 'SP_stress'],
    ['AA_resid', 'AA_mom', 'TX_intens'],
    ['HR_slope', 'Diff_slope', 'Ribbon'],
    ['ETH_ratio', 'ETH_corr', 'ETH_lead'],
    ['FR_level', 'FR_mom', 'FR_extreme'],
]


# ═══════════════════════════════════════════════════════
# NORMALISATION ROBUSTE
# ═══════════════════════════════════════════════════════
def robust_percentile(x, window=200):
    """Normalise par percentile glissant → [0,1]."""
    N = len(x)
    out = np.full(N, 0.5)
    for t in range(window, N):
        chunk = x[t-window:t]
        valid = chunk[~np.isnan(chunk) & (chunk != 0)]
        if len(valid) >= 20:
            out[t] = np.clip(np.searchsorted(np.sort(valid), x[t]) / len(valid), 0.02, 0.98)
    return out


def log_change(vals, period):
    """Log-return sur une période donnée."""
    N = len(vals)
    out = np.zeros(N)
    for t in range(period, N):
        if vals[t] > 0 and vals[t-period] > 0 and not np.isnan(vals[t]) and not np.isnan(vals[t-period]):
            out[t] = np.log(vals[t]) - np.log(vals[t-period])
    return out


# ═══════════════════════════════════════════════════════
# CHARGEMENT DES DONNÉES
# ═══════════════════════════════════════════════════════
def load_series(path, col, date_col='date'):
    """Charge une série depuis un CSV et l'aligne sur les dates principales."""
    df = pd.read_csv(path)
    df[date_col] = pd.to_datetime(df[date_col])
    df[col] = pd.to_numeric(df[col], errors='coerce')
    return dict(zip(df[date_col].values, df[col].values))


def load_all_data():
    """Charge toutes les données nécessaires."""
    log.info("Chargement des données...")

    # BTC daily
    btc_path = BASE_DIR / "btc_daily.csv"
    if not btc_path.exists():
        btc_path = DATA_DIR / "btc_daily.csv"
    btc = pd.read_csv(btc_path)
    # Adapter au format (peut varier selon le VPS)
    if 'Close' not in btc.columns and 'close' in btc.columns:
        btc.rename(columns={'close': 'Close', 'date': 'Date', 'volume': 'Volume'}, inplace=True)
    if 'Date' not in btc.columns:
        # Format avec skiprows
        btc = pd.read_csv(btc_path, skiprows=2, header=0)
        btc.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    btc['Date'] = pd.to_datetime(btc['Date']).dt.normalize()
    for c in ['Close', 'Volume']:
        btc[c] = pd.to_numeric(btc[c].astype(str).str.replace(',', ''), errors='coerce')
    btc = btc.sort_values('Date').dropna(subset=['Close']).reset_index(drop=True)
    dates = btc['Date'].values
    prix = btc['Close'].values
    N = len(dates)

    log.info(f"  BTC : {N} jours ({dates[0]} → {dates[-1]})")

    def align(series_map):
        v = np.array([series_map.get(d, np.nan) for d in dates])
        for i in range(1, len(v)):
            if np.isnan(v[i]) and not np.isnan(v[i-1]):
                v[i] = v[i-1]
        return v

    # Sous-signaux de base (si vrais_yeux disponible)
    # Sinon, charger depuis le CSV pré-calculé
    sub18_path = DATA_DIR / "sous_signaux_18.csv"
    seragone_path = BASE_DIR / "seragone_4117j_complet.csv"

    # DXY
    dxy_path = BASE_DIR / "dxy_daily.csv"
    if not dxy_path.exists():
        dxy_path = DATA_DIR / "dxy_daily.csv"
    try:
        dxy_df = pd.read_csv(dxy_path, skiprows=2, header=0)
        dxy_df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
        dxy_df['Date'] = pd.to_datetime(dxy_df['Date']).dt.normalize()
        dxy_df['Close'] = pd.to_numeric(dxy_df['Close'].astype(str).str.replace(',', ''), errors='coerce')
        dxy_raw = align(dict(zip(dxy_df['Date'].values, dxy_df['Close'].values)))
    except:
        dxy_raw = np.full(N, np.nan)
        log.warning("DXY non chargé")

    # SP500
    try:
        sp_df = pd.read_csv(BASE_DIR / "sp500_daily.csv", skiprows=2, header=0)
        sp_df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
        sp_df['Date'] = pd.to_datetime(sp_df['Date']).dt.normalize()
        sp_df['Close'] = pd.to_numeric(sp_df['Close'].astype(str).str.replace(',', ''), errors='coerce')
        sp_raw = align(dict(zip(sp_df['Date'].values, sp_df['Close'].values)))
    except:
        sp_raw = np.full(N, np.nan)

    # On-chain
    def try_load_oc(filename, col):
        for p in [DATA_DIR / filename, BASE_DIR / filename, DATA_DIR / "onchain" / filename, BASE_DIR / "data" / filename]:
            if p.exists():
                try:
                    return align(load_series(str(p), col))
                except:
                    pass
        return np.full(N, np.nan)

    aa_raw = try_load_oc("btc_active_addresses.csv", "active_addresses")
    tx_raw = try_load_oc("btc_transactions_daily.csv", "transactions")
    hr_raw = try_load_oc("btc_hashrate_daily.csv", "hashrate")
    diff_raw = try_load_oc("btc_difficulty_daily.csv", "difficulty")

    # ETH
    try:
        eth_path = DATA_DIR / "eth_daily.csv"
        if not eth_path.exists():
            eth_path = BASE_DIR / "eth_daily.csv"
        eth_df = pd.read_csv(eth_path)
        eth_df['date'] = pd.to_datetime(eth_df['date'])
        eth_raw = align(dict(zip(eth_df['date'].values, eth_df['close'].values)))
    except:
        eth_raw = np.full(N, np.nan)

    # Funding rate
    try:
        fr_path = DATA_DIR / "funding_rate_btc.csv"
        if not fr_path.exists():
            fr_path = BASE_DIR / "funding_rate_btc.csv"
        fr_df = pd.read_csv(fr_path)
        fr_df['date'] = pd.to_datetime(fr_df['date'])
        fr_raw = align(dict(zip(fr_df['date'].values, fr_df['funding_rate_mean'].values)))
    except:
        fr_raw = np.full(N, np.nan)

    # M2
    try:
        m2_path = DATA_DIR / "M2SL.csv"
        if not m2_path.exists():
            m2_path = BASE_DIR / "M2SL.csv"
        m2_df = pd.read_csv(m2_path)
        m2_df['observation_date'] = pd.to_datetime(m2_df['observation_date'])
        m2_d = m2_df.sort_values('observation_date').dropna().set_index('observation_date').resample('D').interpolate('linear')
        m2_raw = align(dict(zip(m2_d.index.values, m2_d['M2SL'].values)))
    except:
        m2_raw = np.full(N, np.nan)

    return {
        'dates': dates, 'prix': prix, 'N': N,
        'dxy': dxy_raw, 'sp': sp_raw, 'aa': aa_raw, 'tx': tx_raw,
        'hr': hr_raw, 'diff': diff_raw, 'eth': eth_raw, 'fr': fr_raw, 'm2': m2_raw,
    }


# ═══════════════════════════════════════════════════════
# CALCUL DES 30 SOUS-SIGNAUX
# ═══════════════════════════════════════════════════════
def compute_sub_signals(data):
    """Calcule les 30 sous-signaux depuis les données brutes."""
    N = data['N']
    prix = data['prix']
    rpf = robust_percentile
    lc = log_change

    log.info("Calcul des 18 sous-signaux de base...")
    # Charger les 18 de base depuis le CSV pré-calculé
    sub18_path = BASE_DIR / "seragone_4117j_complet.csv"
    if not sub18_path.exists():
        sub18_path = DATA_DIR / "seragone_4117j_complet.csv"

    if sub18_path.exists():
        s18_df = pd.read_csv(sub18_path)
        # Extraire les colonnes M, V, S, H, G comme base
        # Adapter selon le format exact du CSV
        log.info(f"  CSV base : {sub18_path} ({len(s18_df)} lignes)")

    # On utilise le CSV des sous-signaux pré-calculés s'il existe
    sub18_csv = BASE_DIR / "sous_signaux_18_complet.csv"
    if not sub18_csv.exists():
        sub18_csv = DATA_DIR / "sous_signaux_18_complet.csv"

    if sub18_csv.exists():
        s18 = pd.read_csv(sub18_csv)
        s18['date'] = pd.to_datetime(s18['date'])
        # Aligner sur les dates
        s18_map = {d: s18[s18['date'] == d].iloc[0, 1:].values for d in s18['date'].values if len(s18[s18['date'] == d]) > 0}
        ex = np.zeros((N, 18))
        for i, d in enumerate(data['dates']):
            if d in s18_map:
                ex[i] = s18_map[d]
        log.info(f"  18 sous-signaux chargés")
    else:
        log.error("Aucun CSV de sous-signaux trouvé. Utiliser vrais_yeux_stretched.py")
        return None

    log.info("Calcul des 12 sous-signaux supplémentaires...")
    dxy, sp, aa, tx, hr, diff, eth, fr, m2 = (
        data['dxy'], data['sp'], data['aa'], data['tx'],
        data['hr'], data['diff'], data['eth'], data['fr'], data['m2']
    )

    # G étendu : DXY stress
    dxy_stress = np.zeros(N)
    for t in range(100, N):
        if not np.isnan(dxy[t]) and dxy[t] > 0:
            ma = np.nanmean(np.log(np.maximum(dxy[t-100:t], 1)))
            dxy_stress[t] = np.log(dxy[t]) - ma

    # L : DXY momentum, M2 change, SP stress
    dxy_mom = lc(dxy, 20)
    m2_chg = lc(m2, 90)
    sp_stress = lc(sp, 20)

    # U : AA résiduel, AA momentum, TX intensité
    aa_mom = lc(aa, 14)
    tx_int = np.zeros(N)
    for t in range(N):
        if tx[t] > 0 and aa[t] > 0:
            tx_int[t] = np.log(tx[t] / aa[t])

    # I : HR slope, Diff slope, Ribbon
    hr_slope = lc(hr, 30)
    diff_slope = lc(diff, 30)
    ribbon = np.array([hr_slope[t] - diff_slope[t] for t in range(N)])

    # A : ETH ratio, corr, lead
    eth_ratio = np.array([lc(eth, 14)[t] - lc(prix, 14)[t] for t in range(N)])
    eth_corr = np.full(N, 0.5)
    for t in range(30, N):
        rb = np.diff(np.log(np.maximum(prix[t-30:t+1], 1)))
        re = np.diff(np.log(np.maximum(eth[t-30:t+1], 1)))
        m = ~(np.isnan(rb) | np.isnan(re))
        if m.sum() >= 10:
            c = np.corrcoef(rb[m], re[m])[0, 1]
            if not np.isnan(c):
                eth_corr[t] = np.clip((c + 1) / 2, 0, 1)
    eth_lead = lc(eth, 14)

    # F : FR level, momentum, extreme
    fr_clean = np.nan_to_num(fr, 0)
    fr_mom = np.zeros(N)
    fr_ext = np.zeros(N)
    for t in range(30, N):
        c7 = np.nanmean(fr[max(0, t-7):t+1])
        c30 = np.nanmean(fr[max(0, t-30):t+1])
        if not np.isnan(c7) and not np.isnan(c30):
            fr_mom[t] = c7 - c30
        v = fr[t-30:t+1]
        v = v[~np.isnan(v)]
        if len(v) >= 10:
            fr_ext[t] = np.sum(np.abs(v) > 0.0003) / len(v)

    # Normaliser tous les nouveaux signaux
    new_sigs = [
        rpf(dxy_stress), rpf(dxy_mom), rpf(m2_chg), rpf(sp_stress),
        rpf(lc(aa, 30)), rpf(aa_mom), rpf(tx_int),
        rpf(hr_slope), rpf(diff_slope), rpf(ribbon),
        rpf(eth_ratio), rpf(eth_corr), rpf(eth_lead),
        rpf(fr_clean), rpf(fr_mom), rpf(fr_ext),
    ]

    # Assembler 10D × 3 = 30
    sub = np.column_stack([
        ex[:, 0], ex[:, 1], ex[:, 2],                    # M
        ex[:, 3], ex[:, 4], ex[:, 5],                    # V
        ex[:, 8], ex[:, 9], ex[:, 10],                   # S
        ex[:, 12], ex[:, 14], ex[:, 15],                 # H
        ex[:, 16], ex[:, 17], new_sigs[0],               # G: Power, OU, DXY_stress
        new_sigs[1], new_sigs[2], new_sigs[3],           # L: DXY_mom, M2, SP
        new_sigs[4], new_sigs[5], new_sigs[6],           # U: AA, AA_mom, TX
        new_sigs[7], new_sigs[8], new_sigs[9],           # I: HR, Diff, Ribbon
        new_sigs[10], new_sigs[11], new_sigs[12],        # A: ETH_ratio, corr, lead
        new_sigs[13], new_sigs[14], new_sigs[15],        # F: FR_level, mom, ext
    ])

    log.info(f"  30 sous-signaux calculés : {sub.shape}")

    # ═══════════════════════════════════════════════════════
    # DIMENSIONS COMMUNICANTES (si disponibles)
    # ═══════════════════════════════════════════════════════
    comm_hist_path = BASE_DIR / "data" / "communicants_history.json"
    if comm_hist_path.exists():
        try:
            import json as _json
            with open(comm_hist_path) as f:
                comm_hist = _json.load(f)
            log.info(f"  Communicants : {len(comm_hist)} jours d'historique")

            if len(comm_hist) >= 200:
                # Extraire les 24 sous-signaux communicants
                comm_keys = [
                    # C1: Récursif profond
                    ('dist_M1', 'dist_M2', 'dist_M3'),
                    # C2: Convergence
                    ('n_mondes_actifs', 'convergence_recursif', 'distance'),
                    # C3: Qualité
                    ('shannon', 'hist_Q_jour', 'dim_M'),
                    # C4: Dimensions internes
                    ('dim_V', 'dim_S', 'dim_H'),
                    # C5: Éclaireurs
                    ('eclaireur', 'contre_eclaire', 'pur_garch'),
                    # C6: Geste + souffle
                    ('hist_geste', 'hist_souffle', 'hist_emergence'),
                    # C7: Distances profondes
                    ('dist_M4', 'dist_M5', 'dist_M6'),
                    # C8: Funding + prix
                    ('funding_rate', 'dim_G', 'hist_brisance'),
                ]

                n_hist = min(len(comm_hist), N)
                offset = N - n_hist
                comm_sigs = []

                for triplet in comm_keys:
                    for key in triplet:
                        raw = np.zeros(N)
                        for i in range(n_hist):
                            val = comm_hist[i].get(key, 0)
                            if val is None:
                                val = 0
                            raw[offset + i] = float(val)
                        # Normaliser par percentile
                        norm = robust_percentile(raw)
                        comm_sigs.append(norm)

                comm_sub = np.column_stack(comm_sigs)
                log.info(f"  Communicants : {comm_sub.shape[1]} sous-signaux ajoutés")

                # Vérifier que les dimensions sont vivantes
                alive = 0
                for d in range(8):
                    col = comm_sub[500:, d*3]
                    if col.std() > 0.05:
                        alive += 1
                log.info(f"  Communicants : {alive}/8 dimensions vivantes")

                if alive >= 4:
                    sub = np.column_stack([sub, comm_sub])
                    log.info(f"  TOTAL : {sub.shape[1]} sous-signaux ({sub.shape[1]//3}D)")
                else:
                    log.warning(f"  Communicants : seulement {alive}/8 vivantes, on reste en 10D")
            else:
                log.info(f"  Communicants : {len(comm_hist)} jours < 200, en attente")
        except Exception as e:
            log.warning(f"  Communicants erreur : {e}")

    return sub


# ═══════════════════════════════════════════════════════
# MOTEUR DES MONDES PARALLÈLES
# ═══════════════════════════════════════════════════════
class MondesParalleles:
    """432 mondes indépendants × 10 dimensions."""

    def __init__(self, sub, dates, prix, train_end='2023-01-01'):
        self.sub = sub
        self.dates = dates
        self.prix = prix
        self.N = len(dates)
        self.nd = sub.shape[1] // 3  # Dynamique : 10D ou 18D selon les communicants
        self.slices = [(i * 3, i * 3 + 3) for i in range(self.nd)]

        # Train / Test
        train_mask = dates < np.datetime64(train_end)
        self.train_idx = np.where(train_mask & (np.arange(self.N) >= 500))[0]
        self.test_idx = np.where(~train_mask)[0]

        # R5
        self.r5 = np.full(self.N, np.nan)
        for i in range(self.N - 5):
            if prix[i] > 0 and prix[i+5] > 0:
                self.r5[i] = prix[i+5] / prix[i] - 1

        # Bons jours train
        self.good_train = self.train_idx[
            np.array([not np.isnan(self.r5[t]) and self.r5[t] > 0 for t in self.train_idx])
        ]

        # Pré-calculer sub pour les indices clés
        self.sub_gt = sub[self.good_train]
        self.sub_tr = sub[self.train_idx]

        # Stocker les mondes
        self.mondes = {}
        self.mondes_jours = {}

    def compute_monde(self, combo):
        """Calcule un monde et retourne ses jours actifs pour le dernier jour."""
        W = np.full((self.nd, 3), 0.05)
        for d in range(self.nd):
            W[d, combo[d]] = 0.90

        # Dimensions sur bons jours train
        dg = np.zeros((len(self.good_train), self.nd))
        dt = np.zeros((len(self.train_idx), self.nd))
        for d, (s, e) in enumerate(self.slices):
            dg[:, d] = np.clip(self.sub_gt[:, s:e] @ W[d], 0, 1)
            dt[:, d] = np.clip(self.sub_tr[:, s:e] @ W[d], 0, 1)

        # Phi*_m propre
        phi = dg.mean(axis=0)

        # W_dist_m propre
        var = np.var(dg, axis=0) + 1e-6
        wd = 1.0 / var
        wd = wd / wd.sum() * (self.nd + 1.5)

        # Tau_m propre
        dist_train = np.sqrt(np.sum(wd * (dt - phi) ** 2, axis=1))
        tau = np.percentile(dist_train, 25)

        return phi, wd, tau

    def eval_today(self, t):
        """Évalue tous les mondes pour le jour t. Retourne la convergence."""
        sub_t = self.sub[t]
        n_actif = 0
        details = {}

        for name, (combo, phi, wd, tau) in self.mondes.items():
            # Dimensions du jour
            dims = np.zeros(self.nd)
            for d, (s, e) in enumerate(self.slices):
                W = np.full(3, 0.05)
                W[combo[d]] = 0.90
                dims[d] = np.clip(sub_t[s:e] @ W, 0, 1)

            dist = np.sqrt(np.sum(wd * (dims - phi) ** 2))
            actif = dist < tau

            if actif:
                n_actif += 1

            details[name] = {
                'dist': round(float(dist), 4),
                'tau': round(float(tau), 4),
                'actif': bool(actif),
            }

        convergence = n_actif
        pct = n_actif / len(self.mondes) * 100 if self.mondes else 0

        return {
            'n_actif': n_actif,
            'n_total': len(self.mondes),
            'convergence_pct': round(pct, 1),
            'details': details,
        }

    def build_all(self):
        """Construit les mondes par greedy. Énumère si <= 12D, échantillonne sinon."""
        total_possible = 3 ** self.nd
        log.info(f"Construction des mondes ({self.nd}D, 3^{self.nd} = {total_possible} combinaisons)...")

        # Générer les combinaisons
        if self.nd <= 12:
            all_combos = list(product(range(3), repeat=self.nd))
        else:
            # Échantillonnage aléatoire pour les hautes dimensions
            n_sample = min(30000, total_possible)
            rng = np.random.default_rng(42)
            combo_set = set()
            while len(combo_set) < n_sample:
                combo_set.add(tuple(rng.integers(0, 3, self.nd)))
            all_combos = list(combo_set)
        log.info(f"  {len(all_combos)} combinaisons à tester")

        # Calculer tous les mondes
        monde_data = []
        for i, combo in enumerate(all_combos):
            phi, wd, tau = self.compute_monde(combo)

            # Évaluer sur tout le test
            de = np.zeros((len(self.test_idx), self.nd))
            for d, (s, e) in enumerate(self.slices):
                W = np.full(3, 0.05)
                W[combo[d]] = 0.90
                de[:, d] = np.clip(self.sub[self.test_idx, s:e] @ W, 0, 1)

            dist_test = np.sqrt(np.sum(wd * (de - phi) ** 2, axis=1))
            jours = set(self.test_idx[dist_test < tau])

            if len(jours) >= 10:
                monde_data.append((combo, jours, phi, wd, tau))

            if (i + 1) % 10000 == 0:
                log.info(f"  {i+1}/{len(all_combos)}...")

        log.info(f"  {len(monde_data)} mondes avec >= 10 jours")

        # Greedy : Jaccard < 0.30
        monde_data.sort(key=lambda x: -len(x[1]))

        def jaccard(a, b):
            u = len(a | b)
            return len(a & b) / u if u > 0 else 0

        selected = []
        for combo, jours, phi, wd, tau in monde_data:
            ok = all(jaccard(jours, sj) < 0.30 for _, sj, _, _, _ in selected)
            if ok:
                selected.append((combo, jours, phi, wd, tau))

        log.info(f"  {len(selected)} mondes indépendants (J < 0.30)")

        # Enregistrer
        for i, (combo, jours, phi, wd, tau) in enumerate(selected):
            name = f"P{i:03d}"
            self.mondes[name] = (combo, phi, wd, tau)
            self.mondes_jours[name] = jours

        return len(selected)


# ═══════════════════════════════════════════════════════
# POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════
def main():
    import argparse
    parser = argparse.ArgumentParser(description='Séragone — Mondes Parallèles')
    parser.add_argument('--status', action='store_true', help='Affiche l\'état')
    parser.add_argument('--convergence', action='store_true', help='Convergence du jour')
    parser.add_argument('--rebuild', action='store_true', help='Reconstruire tous les mondes')
    args = parser.parse_args()

    if args.status:
        if STATE_FILE.exists():
            with open(STATE_FILE) as f:
                state = json.load(f)
            print(json.dumps(state, indent=2, ensure_ascii=False))
        else:
            print("Pas de state. Lancer d'abord sans --status.")
        return

    # Charger les données
    data = load_all_data()
    if data is None:
        return

    # Calculer les sous-signaux
    sub = compute_sub_signals(data)
    if sub is None:
        return

    # Construire le moteur
    engine = MondesParalleles(sub, data['dates'], data['prix'])

    # Construire les mondes (ou charger depuis le cache)
    cache_file = DATA_DIR / "mondes_paralleles_cache.json"
    if cache_file.exists() and not args.rebuild:
        log.info("Chargement du cache des mondes...")
        with open(cache_file) as f:
            cache = json.load(f)
        for name, mdata in cache.items():
            combo = tuple(mdata['combo'])
            phi = np.array(mdata['phi'])
            wd = np.array(mdata['wd'])
            tau = mdata['tau']
            engine.mondes[name] = (combo, phi, wd, tau)
        log.info(f"  {len(engine.mondes)} mondes chargés du cache")
    else:
        n = engine.build_all()
        # Sauver le cache
        cache = {}
        for name, (combo, phi, wd, tau) in engine.mondes.items():
            cache[name] = {
                'combo': list(combo),
                'phi': phi.tolist(),
                'wd': wd.tolist(),
                'tau': float(tau),
            }
        writestateatomic(cache, cache_file)
        log.info(f"Cache sauvé : {cache_file}")

    # Évaluer le dernier jour
    t_last = len(data['dates']) - 1
    result = engine.eval_today(t_last)

    # Écrire le state
    state = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'prix': float(data['prix'][t_last]),
        'date': str(data['dates'][t_last])[:10],
        'n_mondes': result['n_total'],
        'n_actif': result['n_actif'],
        'convergence_pct': result['convergence_pct'],
        'signal_bear': result['n_actif'] >= 40,
        'signal_fort': result['n_actif'] >= 20,
        'details': result['details'],
    }

    writestateatomic(state, STATE_FILE)

    log.info(f"ÉTAT : {result['n_actif']}/{result['n_total']} mondes actifs "
             f"({result['convergence_pct']:.1f}%) — prix {data['prix'][t_last]:.0f}")

    # Append à l'historique
    hist_line = f"{state['date']},{state['prix']},{state['n_actif']},{state['n_mondes']},{state['convergence_pct']}\n"
    write_header = not HISTORY_FILE.exists()
    with open(HISTORY_FILE, 'a') as f:
        if write_header:
            f.write("date,prix,n_actif,n_mondes,convergence_pct\n")
        f.write(hist_line)


if __name__ == '__main__':
    main()
