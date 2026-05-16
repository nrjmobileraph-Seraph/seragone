# -*- coding: utf-8 -*-
"""
Wrapper DOUBLE_TEMPO V1 inert.
Module documentaire pur.
Aucun effet au chargement.
"""

SCHEMA = "wrapper_double_tempo_v1_inert"
ROLE = "DOUBLE_TEMPO"
MODE = "DEMO_PAPER_INERT"


def wrapper_double_tempo_v1_inert(marketcontext, policydecision=None):
    if policydecision is None:
        policydecision = {}
    if not isinstance(marketcontext, dict):
        raise TypeError("marketcontext must be a dict")
    if not isinstance(policydecision, dict):
        raise TypeError("policydecision must be a dict")

    return {
        "schema": SCHEMA,
        "role": ROLE,
        "mode": MODE,
        "tempobudgets": {
            "fast_budget_ratio": 0.0,
            "slow_budget_ratio": 0.0,
            "reserve_budget_ratio": 1.0,
            "directional_final_decision": None,
            "reason": "inert_v1_no_directional_decision",
            "marketcontext_keys": sorted(str(k) for k in marketcontext.keys()),
            "policydecision_keys": sorted(str(k) for k in policydecision.keys()),
        },
        "realfinanceallowed": False,
        "branching_allowed": False,
        "final_decision": None,
    }


build_tempo_budgets = wrapper_double_tempo_v1_inert

__all__ = [
    "wrapper_double_tempo_v1_inert",
    "build_tempo_budgets",
]
