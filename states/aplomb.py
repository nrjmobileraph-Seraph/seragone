#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aplomb — décideur souverain amont
Produit un état canonique enrichi :
- direction: LONG / SHORT / NEUTRE
- permission: [0.0, 1.0]
"""

from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path("/home/ubuntu/seragone/states")
STATE_FILE = BASE_DIR / "aplomb_state.json"


def load_json(path: Path, default: dict) -> dict:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def load_mondes_state() -> dict:
    return load_json(
        BASE_DIR / "mondes_paralleles_state.json",
        {"n_actif": 0, "n_gp_actif": 0},
    )


def load_m2_state() -> dict:
    return load_json(
        BASE_DIR / "m2_bear_state_v2.json",
        {"nactif": 0, "signalbear20": False, "signalbear40": False},
    )


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def evaluate_aplomb() -> dict:
    bull = load_mondes_state()
    bear = load_m2_state()

    n_actif_long = int(bull.get("n_actif", 0) or 0)
    n_gp_actif = int(bull.get("n_gp_actif", 0) or 0)
    n_actif_short = int(bear.get("nactif", 0) or 0)
    signalbear20 = bool(bear.get("signalbear20", False))
    signalbear40 = bool(bear.get("signalbear40", False))

    total_long = n_actif_long + n_gp_actif
    total_short = n_actif_short

    direction = "NEUTRE"
    base_permission = 0.0
    raison = "Aucune domination nette entre les mondes long et short."

    if total_long > total_short * 1.2:
        direction = "LONG"
        base_permission = 0.6 + 0.2 * (total_long / 305)
        raison = f"Domination LONG: total_long={total_long} > 1.2 * total_short={total_short}."
    elif total_short > total_long * 1.2:
        direction = "SHORT"
        base_permission = 0.5 + 0.2 * (total_short / 278)
        raison = f"Domination SHORT: total_short={total_short} > 1.2 * total_long={total_long}."

        if signalbear20:
            base_permission *= 1.3
            raison += " Renfort signalbear20."
        if signalbear40:
            base_permission *= 1.1
            raison += " Renfort signalbear40."

    permission = clamp01(base_permission)

    state = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "direction": direction,
        "permission": permission,
        "n_actif_long": n_actif_long,
        "n_gp_actif": n_gp_actif,
        "n_actif_short": n_actif_short,
        "signalbear20": signalbear20,
        "signalbear40": signalbear40,
        "raison": raison
    }

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

    print(f"Aplomb: {direction} | permission={permission:.4f}")
    print(f"Raison: {raison}")
    return state


if __name__ == "__main__":
    evaluate_aplomb()
