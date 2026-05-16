# -*- coding: utf-8 -*-
"""
Wrapper PRUDENCE_MEASURE V1 inert.
Module documentaire pur.
Aucun effet au chargement.
"""

SCHEMA = "wrapper_prudence_measure_v1_inert"
ROLE = "PRUDENCE_MEASURE"
MODE = "DEMO_PAPER_INERT"


def wrapper_prudence_measure_v1_inert(
    marketcontext,
    policydecision=None,
    allocationcandidate=None,
):
    if policydecision is None:
        policydecision = {}
    if allocationcandidate is None:
        allocationcandidate = {}
    if not isinstance(marketcontext, dict):
        raise TypeError("marketcontext must be a dict")
    if not isinstance(policydecision, dict):
        raise TypeError("policydecision must be a dict")
    if not isinstance(allocationcandidate, dict):
        raise TypeError("allocationcandidate must be a dict")

    return {
        "schema": SCHEMA,
        "role": ROLE,
        "mode": MODE,
        "prudencemeasure": {
            "veto": False,
            "score": 0.0,
            "reason": "inert_v1_measure_only_no_final_forcing",
            "final_decision_forced": False,
            "marketcontext_keys": sorted(str(k) for k in marketcontext.keys()),
            "policydecision_keys": sorted(str(k) for k in policydecision.keys()),
            "allocationcandidate_keys": sorted(str(k) for k in allocationcandidate.keys()),
        },
        "realfinanceallowed": False,
        "branching_allowed": False,
        "final_decision": None,
    }


measure_prudence = wrapper_prudence_measure_v1_inert

__all__ = [
    "wrapper_prudence_measure_v1_inert",
    "measure_prudence",
]
