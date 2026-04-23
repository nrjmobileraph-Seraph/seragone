#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
"""
MONEY MANAGER SÉRAGONE
======================

Applique l'allocation capital synthétisée à partir des 4 réponses IA.
Lit les états des tireurs + V9 + Aplomb + brisance + étincelle.
Calcule la position nette finale du portefeuille (35 000 €).

Mode OBSERVATOIRE uniquement.
"""

from doubletempo import get_tempo_budgets

import json
import logging
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple

BASE = Path("/home/ubuntu/seragone")

STATE_OUT = BASE / "money_manager_state.json"
LOG_PATH = BASE / "logs" / "money_manager.log"
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

CAPITAL_TOTAL = 35000.0

COUCHES = {
    "V9_PREMIUM": 0.35,
    "TIREURS": 0.40,
    "TEMPERANCE": 0.20,
    "RESERVE": 0.05,
}

TIREURS_ALLOCATION = {
    "Presence": 0.22,
    "Tenue": 0.18,
    "Vigie": 0.15,
    "Agilite": 0.13,
    "Precision": 0.11,
    "Fulgurance": 0.08,
    "Etincelle": 0.10,
    "Aplomb": 0.03,
}

BOOK_STRATEGIQUE = ["Presence", "Tenue"]
BOOK_TACTIQUE = ["Vigie", "Agilite", "Precision", "Fulgurance"]

SEUIL_COMPENSATION = 0.30

MULT_APLOMB = {
    "CERTITUDE": {"LONG": 1.50, "SHORT": 0.0},
    "CONVICTION": {"LONG": 1.10, "SHORT": 0.0},
    "AUTORISE": {"LONG": 0.75, "SHORT": 0.0},
    "SURVEILLER": {"LONG": 0.25, "SHORT": 0.0},
    "FULL": {"LONG": 1.10, "SHORT": 1.10},
    "MEDIUM": {"LONG": 0.75, "SHORT": 0.75},
    "LIGHT": {"LONG": 0.25, "SHORT": 0.25},
    "NONE": {"LONG": 0.0, "SHORT": 0.0},
    "SHORT": {"LONG": 0.0, "SHORT": 1.00},
    "INTERDIT": {"LONG": 0.0, "SHORT": 0.0},
    "WAIT": {"LONG": 0.0, "SHORT": 0.0},
    "NEUTRE": {"LONG": 0.0, "SHORT": 0.0},
    "FLAT": {"LONG": 0.0, "SHORT": 0.0},
}

CAP_PROGRESSIF = {
    1: 0.20,
    2: 0.35,
    3: 0.50,
    4: 0.62,
    5: 0.72,
    6: 0.82,
    7: 0.90,
    8: 1.00,
}

DD_INTRADAY_CUT = 0.15
DD_CLOTURE_CASH = 0.25
CORR_TIREURS_MAX = 0.80

TIREURS_STATE_FILES = {
    "Aplomb": BASE / "aplombdailystate.json",
    "Presence": BASE / "presence1hstate.json",
    "Tenue": BASE / "tenue30mstate.json",
    "Vigie": BASE / "vigie15mstate.json",
    "Agilite": BASE / "tireurs_agilite_5m_state.json",
    "Precision": BASE / "tireurs_minute_state.json",
    "Fulgurance": BASE / "fulgurance_state.json",
    "Etincelle": BASE / "etincellestate.json",
}

V9_SIGNAL_FILE = BASE / "signal_baisse_raphael_V9.csv"
BRISANCE_STATE = BASE / "brisance_state.json"
ETINCELLE_STATE = BASE / "etincellestate.json"

log = logging.getLogger("MONEY_MANAGER")
log.setLevel(logging.INFO)
log.propagate = False
if not log.handlers:
    _fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    _fh = logging.FileHandler(LOG_PATH, encoding="utf-8")
    _fh.setFormatter(_fmt)
    _sh = logging.StreamHandler()
    _sh.setFormatter(_fmt)
    log.addHandler(_fh)
    log.addHandler(_sh)


def read_json(path: Path) -> Optional[Dict]:
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        log.warning(f"Lecture {path.name} échouée : {e}")
        return None


def get_aplomb_permission() -> str:
    candidates = [
        BASE / "aplombdailystate.json",
        BASE / "aplombdailystate.json",
        BASE / "aplombstate.json",
    ]

    state = None
    for path in candidates:
        state = read_json(path)
        if state:
            break

    if not state:
        return "NEUTRE"

    permission = str(state.get("permission", "") or "").upper()
    direction = str(state.get("direction", "") or state.get("action", "") or "").upper()
    intensity = float(state.get("intensity", 0.0) or state.get("force", 0.0) or 0.0)

    if permission in MULT_APLOMB:
        return permission

    if direction == "SHORT":
        if intensity >= 0.75:
            return "SHORT"
        return "SHORT"

    if direction == "LONG":
        if intensity >= 0.75:
            return "LONG"
        if intensity >= 0.10:
            return "LONG"
        if intensity > 0.0:
            return "LONG"
        return "NONE"

    return "NEUTRE"


def get_tireur_direction(tireur_name: str) -> Tuple[str, float, bool]:
    path = TIREURS_STATE_FILES.get(tireur_name)
    if not path:
        return "WAIT", 0.0, False

    state = read_json(path)
    if not state:
        return "WAIT", 0.0, False

    if tireur_name == "Aplomb":
        direction = str(
            state.get("direction")
            or state.get("action")
            or state.get("direction_nette")
            or "WAIT"
        ).upper()
        intensity = float(
            state.get("intensity", 0.0)
            or state.get("force", 0.0)
            or 0.0
        )
    else:
        direction = str(
            state.get("direction")
            or state.get("direction_nette")
            or state.get("direction_nette_minute")
            or "WAIT"
        ).upper()
        intensity = float(
            state.get("force", 0.0)
            or state.get("intensite", 0.0)
            or state.get("entry_score", 0.0)
            or state.get("intensity", 0.0)
            or 0.0
        )

    if direction in ("LONG", "ACHAT", "BUY"):
        direction = "LONG"
    elif direction in ("SHORT", "VENTE", "SELL"):
        direction = "SHORT"
    elif direction in ("FLAT", "NONE", "NEUTRE", "NEUTRAL"):
        direction = "WAIT"
    else:
        direction = "WAIT"

    intensity = max(0.0, min(1.0, intensity))
    actif = direction != "WAIT" and intensity > 0.0
    return direction, intensity, actif


def get_etincelle_state() -> Tuple[str, bool]:
    state = read_json(ETINCELLE_STATE)
    if not state:
        return "HABITABLE", False

    engine_state = str(state.get("enginestate", "IDLE")).upper()
    horloge = str(state.get("horloge", "HABITABLE")).upper()

    veto_actif = engine_state in ("FIRE", "VETO", "CUT") or horloge == "CASSE"
    return horloge, veto_actif


def get_brisance_active() -> bool:
    state = read_json(BRISANCE_STATE)
    if not state:
        return False
    val = state.get("brisance", state.get("valeur", 0.0))
    try:
        return float(val) > 0.5
    except (ValueError, TypeError):
        return False


def get_v9_bear() -> bool:
    if not V9_SIGNAL_FILE.exists():
        return False
    try:
        with open(V9_SIGNAL_FILE, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
        if len(lines) < 2:
            return False
        last = lines[-1].split(",")
        for cell in last:
            cell_up = cell.strip().upper()
            if cell_up == "BEAR":
                return True
            if cell_up == "BULL":
                return False
        return False
    except Exception as e:
        log.warning(f"V9 lecture échouée : {e}")
        return False


@dataclass
class TireurPosition:
    nom: str
    direction: str
    intensite: float
    allocation_eur: float
    multiplicateur_aplomb: float
    position_signee: float
    book: str


def calculer_positions_tireurs(
    permission_aplomb: str,
    capital_tireurs: float,
) -> List[TireurPosition]:
    positions = []
    mults = MULT_APLOMB.get(permission_aplomb, MULT_APLOMB["NEUTRE"])
    mult_long = mults["LONG"]
    mult_short = mults["SHORT"]

    for nom, pct_poche in TIREURS_ALLOCATION.items():
        if nom == "Aplomb":
            continue
        direction, intensite, actif = get_tireur_direction(nom)
        allocation = capital_tireurs * pct_poche

        if nom == "Etincelle":
            position_signee = 0.0
            mult = 0.0
        elif not actif:
            position_signee = 0.0
            mult = 0.0
        else:
            if nom == "Aplomb":
                mult = 1.0
            elif direction == "LONG":
                mult = mult_long
            elif direction == "SHORT":
                mult = mult_short
            else:
                mult = 0.0

            signed = 1.0 if direction == "LONG" else (-1.0 if direction == "SHORT" else 0.0)
            position_signee = signed * intensite * mult * (allocation / CAPITAL_TOTAL)

        if nom in BOOK_STRATEGIQUE:
            book = "STRAT"
        elif nom in BOOK_TACTIQUE:
            book = "TACT"
        elif nom == "Etincelle":
            book = "RESERVE"
        else:
            book = "OTHER"

        positions.append(TireurPosition(
            nom=nom,
            direction=direction,
            intensite=intensite,
            allocation_eur=allocation,
            multiplicateur_aplomb=mult,
            position_signee=position_signee,
            book=book,
        ))

    return positions


def sommer_avec_cap_progressif(positions: List[TireurPosition]) -> Tuple[float, int, str]:
    positions_non_nulles = [p for p in positions if p.position_signee != 0.0]

    if not positions_non_nulles:
        return 0.0, 0, "NEUTRAL"

    somme_brute = sum(p.position_signee for p in positions_non_nulles)

    if somme_brute > 0:
        aligned = sum(1 for p in positions_non_nulles if p.position_signee > 0)
        direction_nette = "LONG"
    else:
        aligned = sum(1 for p in positions_non_nulles if p.position_signee < 0)
        direction_nette = "SHORT"

    cap = CAP_PROGRESSIF.get(aligned, 1.0)
    somme_cappee = max(-cap, min(cap, somme_brute))

    return somme_cappee, aligned, direction_nette


def compenser_books(positions: List[TireurPosition]) -> Dict[str, Any]:
    strat = sum(p.position_signee for p in positions if p.book == "STRAT")
    tact = sum(p.position_signee for p in positions if p.book == "TACT")

    compensation_appliquee = False
    if strat != 0.0 and tact != 0.0 and (strat * tact < 0):
        ratio = abs(tact) / abs(strat)
        if ratio < SEUIL_COMPENSATION:
            strat_ajuste = strat + tact
            tact_ajuste = 0.0
            compensation_appliquee = True
        else:
            strat_ajuste = strat
            tact_ajuste = tact
    else:
        strat_ajuste = strat
        tact_ajuste = tact

    return {
        "strat_brut": strat,
        "tact_brut": tact,
        "strat_final": strat_ajuste,
        "tact_final": tact_ajuste,
        "compensation_appliquee": compensation_appliquee,
        "position_nette_final": strat_ajuste + tact_ajuste,
    }


@dataclass
class GardeFoOuActif:
    nom: str
    action: str
    seuil: str
    declenche: bool


def appliquer_gardes_fous(
    position_nette: float,
    permission_aplomb: str,
) -> Tuple[float, List[GardeFoOuActif]]:
    alerts = []
    reduction_factor = 1.0
    force_cash = False

    try:
        ex = json.load(open(BASE / "sentinelle_exchange_state.json", "r", encoding="utf-8"))
        ex_status = str(ex.get("global_status", "OK")).upper()
        ws = str(ex.get("withdraws", {}).get("status", "OK")).upper()
        if ws in ("WARN", "CRIT") or ex_status == "CRIT":
            alerts.append(GardeFoOuActif(
                "Exchange", "CASH — Binance instable ou retraits suspendus",
                f"exchange={ex_status} withdraws={ws}", True
            ))
            force_cash = True
    except Exception:
        pass

    horloge, veto = get_etincelle_state()
    if veto:
        alerts.append(GardeFoOuActif(
            "Etincelle", "CASH immédiat", horloge, True
        ))
        force_cash = True

    if get_brisance_active():
        alerts.append(GardeFoOuActif(
            "Brisance", "CASH tireurs, grid /2", "> 0.5", True
        ))
        force_cash = True

    v9_bear = get_v9_bear()
    if v9_bear and permission_aplomb == "SHORT":
        alerts.append(GardeFoOuActif(
            "V9+SHORT", "SHORT confirmé", "combo", True
        ))

    if v9_bear and position_nette > 0:
        cap_v9 = 0.20
        if position_nette > cap_v9:
            alerts.append(GardeFoOuActif(
                "V9_BEAR_cap", f"LONG cappé à {cap_v9}", "V9 BEAR", True
            ))
            position_nette = cap_v9

    if force_cash:
        return 0.0, alerts

    return position_nette * reduction_factor, alerts


def load_clones_state():
    f = BASE / "clones_v6_state.json"
    if f.exists():
        with open(f, "r", encoding="utf-8") as fp:
            return json.load(fp)
    return {"action": "WAIT", "confiance": 0.0}


def load_m4_state():
    f = BASE / "states" / "ours_v2_state.json"
    if f.exists():
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            return {
                "active": data.get("multiplicateur_final", 0.0) > 0,
                "proposed_multiplier": data.get("multiplicateur_final", 0.0)
            }
    return {"active": False, "proposed_multiplier": 0.0}


def load_m5_state():
    f = BASE / "states" / "grappillage_state.json"
    if f.exists():
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            return {
                "active": data.get("taille_actuelle", 0.0) > 0,
                "proposed_multiplier": data.get("taille_actuelle", 0.0)
            }
    return {"active": False, "proposed_multiplier": 0.0}


def main():
    log.info("=" * 70)
    log.info("MONEY MANAGER SÉRAGONE — démarrage")
    log.info("=" * 70)

    permission = get_aplomb_permission()
    log.info(f"Permission Aplomb : {permission}")

    v9_bear = get_v9_bear()
    log.info(f"V9 BEAR : {v9_bear}")

    horloge, veto = get_etincelle_state()
    log.info(f"Étincelle : horloge={horloge}, veto={veto}")

    brisance = get_brisance_active()

    sous_ma200 = False
    try:
        chef = json.load(open(BASE / "state.json", "r", encoding="utf-8"))
        prix_actuel = chef.get("prix", 0)
        ma200 = chef.get("ailes_ma200", 0)
        if prix_actuel > 0 and ma200 > 0:
            sous_ma200 = prix_actuel < ma200
    except Exception:
        pass

    log.info(f"Sous MA200 : {sous_ma200}")
    log.info(f"Brisance active : {brisance}")

    tempostate, tempo = get_tempo_budgets(CAPITAL_TOTAL)

    capital_v9 = tempo["tempobudgetv9"]
    capital_tireurs = tempo["tempobudgettireurs"]
    capital_temperance = tempo["tempobudgettemperance"]
    capital_reserve = tempo["tempobudgetreserve"]

    log.info(
        f"Couches : V9={capital_v9:.0f}€ | Tireurs={capital_tireurs:.0f}€ | "
        f"Tempérance={capital_temperance:.0f}€ | Réserve={capital_reserve:.0f}€"
    )

    positions = calculer_positions_tireurs(permission, capital_tireurs)

    try:
        _auto = read_json(BASE / "tireurs_state.json")
        if _auto and permission == "SHORT":
            _auto_dir = str(_auto.get("direction_nette", "NEUTRE")).upper()
            if _auto_dir == "SHORT":
                for _nom, _pos in _auto.get("positions", {}).items():
                    _pf = float(_pos) if isinstance(_pos, (int, float)) else 0.0
                    if _pf != 0.0:
                        positions.append(TireurPosition(
                            nom=f"Auto_{_nom}",
                            direction="SHORT",
                            intensite=abs(_pf),
                            allocation_eur=abs(_pf) * CAPITAL_TOTAL,
                            multiplicateur_aplomb=1.0,
                            position_signee=_pf,
                            book="STRAT",
                        ))
                        log.info(f"  Auto_{_nom:10} SHORT pos={_pf:+.4f} = {int(_pf*CAPITAL_TOTAL):+d}€")
    except Exception as e:
        log.warning(f"Autonomes non lus: {e}")

    m4 = load_m4_state()
    m5 = load_m5_state()
    clones = load_clones_state()
    log.info(f"Clones V6 : {clones.get('action', '?')}")

    if m4.get("active") and permission == "SHORT":
        _m4_mult = min(float(m4.get("proposed_multiplier", 0.0) or 0.0), 0.10)
        if _m4_mult > 0:
            positions.append(TireurPosition(
                nom="M4_Short_Tactique",
                direction="SHORT",
                intensite=_m4_mult,
                allocation_eur=_m4_mult * CAPITAL_TOTAL,
                multiplicateur_aplomb=1.0,
                position_signee=-_m4_mult,
                book="TACT",
            ))
            log.info(f"  M4_Short     SHORT mult={_m4_mult:.3f} = {int(_m4_mult*CAPITAL_TOTAL)}€")

    if m5.get("active") and permission == "LONG":
        _m5_mult = min(float(m5.get("proposed_multiplier", 0.0) or 0.0), 0.10)
        if _m5_mult > 0:
            positions.append(TireurPosition(
                nom="M5_Grappillage",
                direction="LONG",
                intensite=_m5_mult,
                allocation_eur=_m5_mult * CAPITAL_TOTAL,
                multiplicateur_aplomb=1.0,
                position_signee=_m5_mult,
                book="TACT",
            ))
            log.info(f"  M5_Grapill   LONG  mult={_m5_mult:.3f} = {int(_m5_mult*CAPITAL_TOTAL)}€")

    log.info(f"Tireurs actifs : {sum(1 for p in positions if p.position_signee != 0)}")
    for p in positions:
        if p.position_signee != 0:
            log.info(
                f"  {p.nom:12} {p.direction:5} int={p.intensite:.3f} "
                f"mult={p.multiplicateur_aplomb:.2f} "
                f"pos={p.position_signee:+.4f} book={p.book}"
            )

    comp = compenser_books(positions)
    log.info(f"Book STRAT brut : {comp['strat_brut']:+.4f}")
    log.info(f"Book TACT brut  : {comp['tact_brut']:+.4f}")
    log.info(f"Compensation appliquée : {comp['compensation_appliquee']}")

    pos_nette_avant_gardes, nb_aligned, dir_nette = sommer_avec_cap_progressif(positions)

    log.info(
        f"Position nette avant gardes-fous : {pos_nette_avant_gardes:+.4f} "
        f"({dir_nette}, {nb_aligned} tireurs alignés)"
    )

    pos_nette_finale, alerts = appliquer_gardes_fous(pos_nette_avant_gardes, permission)
    log.info(f"Position nette FINALE : {pos_nette_finale:+.4f}")
    for a in alerts:
        log.info(f"  [ALERT] {a.nom} → {a.action} (seuil : {a.seuil})")

    exposition_eur = pos_nette_finale * CAPITAL_TOTAL

    state = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "engine": "MONEY_MANAGER",
        "version": "1.1-aplomb-canon",
        "mode": "OBSERVATOIRE",
        "capital_total_eur": CAPITAL_TOTAL,
        "double_tempo": {
            "regime": tempo["temporegime"],
            "reason": tempo["temporeason"],
            "drawdown_from_peak": tempo["tempodrawdownfrompeak"],
        },
        "couches_eur": {
            "V9_PREMIUM": capital_v9,
            "TIREURS": capital_tireurs,
            "TEMPERANCE": capital_temperance,
            "RESERVE": capital_reserve,
        },
        "contexte": {
            "permission_aplomb": permission,
            "v9_bear": v9_bear,
            "etincelle_horloge": horloge,
            "etincelle_veto": veto,
            "brisance_active": brisance,
            "sous_ma200": sous_ma200,
        },
        "positions_tireurs": [
            {
                "nom": p.nom,
                "direction": p.direction,
                "intensite": p.intensite,
                "allocation_eur": p.allocation_eur,
                "multiplicateur_aplomb": p.multiplicateur_aplomb,
                "position_signee": p.position_signee,
                "book": p.book,
            } for p in positions
            if p.nom != "Aplomb"
        ],
        "compensation_books": {
            "strat_brut": comp["strat_brut"],
            "tact_brut": comp["tact_brut"],
            "strat_final": comp["strat_final"],
            "tact_final": comp["tact_final"],
            "compensation_appliquee": comp["compensation_appliquee"],
        },
        "position_nette": {
            "avant_gardes": pos_nette_avant_gardes,
            "finale": pos_nette_finale,
            "direction": "LONG" if pos_nette_finale > 0 else "SHORT" if pos_nette_finale < 0 else "NEUTRAL",
            "tireurs_alignes": nb_aligned,
        },
        "exposition_eur": exposition_eur,
        "gardes_fous_alerts": [asdict(a) for a in alerts],
    }

    try:
        with open(STATE_OUT, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, default=str, ensure_ascii=False)
        log.info(f"État écrit : {STATE_OUT}")
    except Exception as e:
        log.error(f"Écriture state échouée : {e}")

    log.info("MONEY MANAGER — fin")


if __name__ == "__main__":
    main()
