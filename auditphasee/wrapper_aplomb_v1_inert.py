# -*- coding: utf-8 -*-
"""
Wrapper APLOMB V1 inert.
Module documentaire pur.
Aucun effet au chargement.
"""

SCHEMA = "wrapper_aplomb_v1_inert"
ROLE = "APLOMB"
MODE = "DEMO_PAPER_INERT"


def wrapper_aplomb_v1_inert(marketcontext, parameters=None):
    if parameters is None:
        parameters = {}
    if not isinstance(marketcontext, dict):
        raise TypeError("marketcontext must be a dict")
    if not isinstance(parameters, dict):
        raise TypeError("parameters must be a dict")

    return {
        "schema": SCHEMA,
        "role": ROLE,
        "mode": MODE,
        "aplom bcontext".replace(" ", ""): {
            "score": 0.0,
            "direction_hint": None,
            "confidence": 0.0,
            "reason": "inert_v1_no_runtime_effect",
            "marketcontext_keys": sorted(str(k) for k in marketcontext.keys()),
            "parameters_keys": sorted(str(k) for k in parameters.keys()),
        },
        "realfinanceallowed": False,
        "branching_allowed": False,
        "final_decision": None,
    }


build_aplomb_context = wrapper_aplomb_v1_inert

__all__ = [
    "wrapper_aplomb_v1_inert",
    "build_aplomb_context",
]
