#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path("/home/ubuntu/seragone")
LOGS_DIR = BASE_DIR / "logs"
STATES_DIR = BASE_DIR / "states"

LOGS_DIR.mkdir(parents=True, exist_ok=True)
STATES_DIR.mkdir(parents=True, exist_ok=True)

log = logging.getLogger("TIREUR_APLOMB")
log.setLevel(logging.INFO)
log.propagate = False
if not log.handlers:
    _fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    _fh = logging.FileHandler(LOGS_DIR / "tireur_aplomb.log", encoding="utf-8")
    _fh.setFormatter(_fmt)
    _sh = logging.StreamHandler()
    _sh.setFormatter(_fmt)
    log.addHandler(_fh)
    log.addHandler(_sh)

APL_STATE_FILE = BASE_DIR / "aplombstate.json"
APL_DAILY_STATE_FILE = BASE_DIR / "aplombdailystate.json"
POLICY_STATE_FILE = STATES_DIR / "policy_state.json"
SIGNAL_LOG_FILE = LOGS_DIR / "signal_log.jsonl"
POLICY_MONITOR_FILE = BASE_DIR / "policy_monitor.json"

CANDIDATE_BULL_FILES = [
    BASE_DIR / "mondesparallelesstate.json",
    BASE_DIR / "mondes_paralleles_state.json",
    BASE_DIR / "datamondesparallelescache.json",
]

CANDIDATE_BEAR_FILES = [
    BASE_DIR / "m2bearstatev2.json",
    BASE_DIR / "m2_bear_state_v2.json",
    BASE_DIR / "m2bearstate.json",
]


def load_json(path: Path, default=None):
    if default is None:
        default = {}
    try:
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        log.warning("Lecture impossible %s : %s", path, e)
    return default


def load_first(paths, default=None):
    if default is None:
        default = {}
    for path in paths:
        if path.exists():
            data = load_json(path, default)
            log.info("State chargé : %s", path.name)
            return data
    return default


def infer_aplomb_input():
    bull = load_first(CANDIDATE_BULL_FILES, {})
    bear = load_first(CANDIDATE_BEAR_FILES, {})

    n_actif_long = (
        bull.get("n_actif")
        or bull.get("n_gp_actif")
        or bull.get("nactif")
        or bull.get("actifs")
        or 0
    )

    n_gp_actif = bull.get("n_gp_actif", 0)

    n_actif_short = (
        bear.get("nactif")
        or bear.get("n_actif")
        or bear.get("actifs")
        or 0
    )

    signalbear20 = bool(bear.get("signalbear20", False))
    signalbear40 = bool(bear.get("signalbear40", False))

    total_long = float(n_actif_long or 0) + float(n_gp_actif or 0)
    total_short = float(n_actif_short or 0)

    if total_short > total_long * 1.2:
        regime_fond = "bear_trend"
        geste_natif = "OUVRIR" if (signalbear20 or signalbear40) else "MAINTENIR"
    elif total_long > total_short * 1.2:
        regime_fond = "bull_trend"
        geste_natif = "OUVRIR"
    else:
        regime_fond = "range"
        geste_natif = "FERMER"

    return {
        "regime_fond": regime_fond,
        "geste_natif": geste_natif,
        "n_actif_long": n_actif_long,
        "n_gp_actif": n_gp_actif,
        "n_actif_short": n_actif_short,
        "signalbear20": signalbear20,
        "signalbear40": signalbear40,
        "bull_state": bull,
        "bear_state": bear,
    }


def decide_local(geste_natif: str, regime_fond: str):
    if geste_natif == "OUVRIR":
        if regime_fond == "bear_trend":
            return {
                "action": "SHORT",
                "sizing": -1.0,
                "holding_bias": "moyen",
                "override_source": "local_rule",
                "raison": "OUVRIR + bear_trend -> SHORT",
            }
        return {
            "action": "LONG",
            "sizing": 1.0 if regime_fond == "bull_trend" else 0.3,
            "holding_bias": "moyen" if regime_fond == "bull_trend" else "court",
            "override_source": "local_rule",
            "raison": "OUVRIR -> LONG",
        }

    if geste_natif == "MAINTENIR":
        if regime_fond == "bear_trend":
            return {
                "action": "SHORT",
                "sizing": -0.097,
                "holding_bias": "court",
                "override_source": "local_rule",
                "raison": "MAINTENIR + bear_trend -> micro short",
            }
        if regime_fond == "bull_trend":
            return {
                "action": "LONG",
                "sizing": 0.097,
                "holding_bias": "court",
                "override_source": "local_rule",
                "raison": "MAINTENIR + bull_trend -> micro long",
            }
        return {
            "action": "LONG",
            "sizing": 0.05,
            "holding_bias": "court",
            "override_source": "local_rule",
            "raison": "MAINTENIR + range -> micro long",
        }

    if regime_fond == "bear_trend":
        return {
            "action": "SHORT",
            "sizing": -0.075,
            "holding_bias": "court",
            "override_source": "local_rule",
            "raison": "FERMER + bear_trend -> micro short",
        }
    if regime_fond == "bull_trend":
        return {
            "action": "LONG",
            "sizing": 0.075,
            "holding_bias": "court",
            "override_source": "local_rule",
            "raison": "FERMER + bull_trend -> micro long",
        }
    return {
        "action": "LONG",
        "sizing": 0.05,
        "holding_bias": "court",
        "override_source": "local_rule",
        "raison": "FERMER + range -> micro long",
    }


def canonical_permission(action: str, direction: str, sizing: float) -> str:
    amp = abs(float(sizing))
    if action == "FLAT" or direction == "FLAT" or amp <= 0:
        return "NONE"
    if direction == "SHORT":
        return "SHORT"
    if direction == "LONG":
        return "LONG"
    return "NONE"


def save_policy_state_local(payload: dict, date_str: str, regime_fond: str, geste_natif: str):
    state = {
        "date": date_str,
        "action": payload["action"],
        "sizing": payload["sizing"],
        "holding_bias": payload["holding_bias"],
        "override_source": payload["override_source"],
        "raison": payload["raison"],
        "geste_natif": geste_natif,
        "label_nc": None,
        "composite_label": None,
        "confluence_score": None,
        "regime_fond": regime_fond,
        "timestamp_ecriture": datetime.now(timezone.utc).isoformat(),
    }
    with open(POLICY_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def append_signal_log_local(payload: dict, date_str: str, regime_fond: str, geste_natif: str):
    entry = {
        "date": date_str,
        "geste_natif": geste_natif,
        "label_nc": None,
        "regime_fond": regime_fond,
        "action": payload["action"],
        "sizing": payload["sizing"],
        "holding_bias": payload["holding_bias"],
        "override_source": payload["override_source"],
        "raison": payload["raison"],
    }
    with open(SIGNAL_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main():
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")

    log.info("======================================================================")
    log.info("TIREUR APLOMB SERAGONE — démarrage")
    log.info("======================================================================")

    raw = infer_aplomb_input()
    decision = decide_local(raw["geste_natif"], raw["regime_fond"])

    save_policy_state_local(decision, date_str, raw["regime_fond"], raw["geste_natif"])
    append_signal_log_local(decision, date_str, raw["regime_fond"], raw["geste_natif"])

    action = str(decision["action"]).upper()
    sizing = float(decision["sizing"])
    intensity = round(min(1.0, abs(sizing)), 4)

    if action == "LONG":
        direction = "LONG"
        target_position = intensity
    elif action == "SHORT":
        direction = "SHORT"
        target_position = -intensity
    else:
        direction = "FLAT"
        target_position = 0.0

    permission = canonical_permission(action, direction, sizing)

    state = {
        "timestamp": now.isoformat(),
        "module": "aplomb",
        "source": "local_policy_fallback",
        "action": action,
        "direction": direction,
        "permission": permission,
        "intensity": intensity,
        "target_position": round(target_position, 4),
        "sizing_signed": round(sizing, 4),
        "holding_bias": decision["holding_bias"],
        "override_source": decision["override_source"],
        "raison": decision["raison"],
        "inputs": raw,
    }

    for out_file in (APL_STATE_FILE, APL_DAILY_STATE_FILE):
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

    with open(POLICY_MONITOR_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {
                "timestamp": now.isoformat(),
                "action": action,
                "direction": direction,
                "permission": permission,
                "intensity": intensity,
                "target_position": round(target_position, 4),
                "sizing_signed": round(sizing, 4),
                "override_source": decision["override_source"],
                "raison": decision["raison"],
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    log.info("Permission Aplomb : %s", permission)
    log.info("Direction Aplomb : %s", direction)
    log.info("Aplomb %s int=%.3f pos=%+.4f", direction, intensity, target_position)
    log.info("États écrits : %s | %s", APL_STATE_FILE, APL_DAILY_STATE_FILE)
    log.info("TIREUR APLOMB — fin")


if __name__ == "__main__":
    main()
