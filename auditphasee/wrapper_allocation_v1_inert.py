# -*- coding: utf-8 -*-
"""
Wrapper ALLOCATION V1 inert.
Module documentaire pur.
Aucun effet au chargement.
"""

SCHEMA = "wrapper_allocation_v1_inert"
ROLE = "ALLOCATION"
MODE = "DEMO_PAPER_INERT"


def wrapper_allocation_v1_inert(
    capital,
    policydecision,
    tempobudgets,
    prudencemeasure,
):
    if not isinstance(capital, (int, float)):
        raise TypeError("capital must be a scalar number")
    if not isinstance(policydecision, dict):
        raise TypeError("policydecision must be a dict")
    if not isinstance(tempobudgets, dict):
        raise TypeError("tempobudgets must be a dict")
    if not isinstance(prudencemeasure, dict):
        raise TypeError("prudencemeasure must be a dict")

    return {
        "schema": SCHEMA,
        "role": ROLE,
        "mode": MODE,
        "allocationstate": {
            "capital_observed": float(capital),
            "paper_only": True,
            "allocated_capital": 0.0,
            "target_exposure": 0.0,
            "order_required": False,
            "order_payload": None,
            "reason": "inert_v1_no_allocation_effect",
            "policydecision_keys": sorted(str(k) for k in policydecision.keys()),
            "tempobudgets_keys": sorted(str(k) for k in tempobudgets.keys()),
            "prudencemeasure_keys": sorted(str(k) for k in prudencemeasure.keys()),
        },
        "realfinanceallowed": False,
        "branching_allowed": False,
        "final_decision": None,
    }


build_allocation_state = wrapper_allocation_v1_inert

__all__ = [
    "wrapper_allocation_v1_inert",
    "build_allocation_state",
]
