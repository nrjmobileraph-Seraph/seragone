#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ORCHESTRATEUR_DEMO_V1 — SQUELETTE INERTE

Date : 13 mai 2026, 23h52 CEST
Statut : SQUELETTE CANONIQUE — SYNTAXE VALIDÉE — pas runtime
Dépendance : CONTRAT_ORCHESTRATEUR_DEMO_V1_2026-05-13_2330_VALIDATED.md

Règle fondatrice :
- Tout module V1 est traité comme calculateur.
- Tout write V1 passe par orchestrateur_demo.
- Tout write legacy est interdit.

Ce fichier est volontairement inerte :
- aucun import de module métier legacy au chargement ;
- aucun mkdir ;
- aucun write actif ;
- aucun cron/systemd/process ;
- aucun exchange ;
- aucune exécution automatique de cycle.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Mapping
import json
import os


CONTRACT_ID = "CONTRAT_ORCHESTRATEUR_DEMO_V1_2026-05-13_2330_VALIDATED"
ORCHESTRATOR_ID = "orchestrateur_demo_v1"
V1_STATE_DIR = Path("/home/ubuntu/seragone/states/v1/")

ALLOWED_V1_STATES = {
    "aplomb": V1_STATE_DIR / "aplomb_state_v1.json",
    "policy": V1_STATE_DIR / "policy_state_v1.json",
    "allocation": V1_STATE_DIR / "allocation_state_v1.json",
    "prudence_measure": V1_STATE_DIR / "prudence_measure_v1.json",
    "trace": V1_STATE_DIR / "orchestrateur_trace_v1.jsonl",
}

FORBIDDEN_LEGACY_TARGETS = {
    Path("/home/ubuntu/seragone/state.json"),
    Path("/home/ubuntu/seragone/aplombstate.json"),
    Path("/home/ubuntu/seragone/states/policystate.json"),
    Path("/home/ubuntu/seragone/doubletempostate.json"),
    Path("/home/ubuntu/seragone/state/prudencestate.json"),
    Path("/home/ubuntu/seragone/states/prudencestate.json"),
}


@dataclass(frozen=True)
class CycleInputs:
    capital_eur: float
    market_context: Mapping[str, Any]
    run_id: str
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class CycleOutputs:
    aplomb_state: Mapping[str, Any]
    policy_state: Mapping[str, Any]
    allocation_state: Mapping[str, Any]
    prudence_measure: Mapping[str, Any]
    trace_line: Mapping[str, Any]


class ContractViolation(RuntimeError):
    pass


class InertSkeleton(RuntimeError):
    pass


def _resolve(path: Path) -> Path:
    return Path(os.path.abspath(os.path.expanduser(str(path))))


def assert_v1_write_target(path: Path) -> None:
    resolved = _resolve(path)
    allowed = {_resolve(p) for p in ALLOWED_V1_STATES.values()}
    forbidden = {_resolve(p) for p in FORBIDDEN_LEGACY_TARGETS}

    if resolved in forbidden:
        raise ContractViolation(f"write legacy interdit: {resolved}")
    if resolved not in allowed:
        raise ContractViolation(f"write non déclaré dans le contrat V1: {resolved}")
    if _resolve(V1_STATE_DIR) not in [resolved.parent, *resolved.parents]:
        raise ContractViolation(f"write hors V1_STATE_DIR interdit: {resolved}")


def build_market_context(raw_snapshot: Mapping[str, Any]) -> Dict[str, Any]:
    return dict(raw_snapshot)


def call_aplomb_calculator(inputs: CycleInputs) -> Dict[str, Any]:
    raise InertSkeleton("À brancher après relecture : appel pur de ./aplomb.py, sans write module.")


def call_prudence_measure(inputs: CycleInputs, aplomb_state: Mapping[str, Any]) -> Dict[str, Any]:
    raise InertSkeleton("À brancher après relecture : prudence_module.py en MEASURE_ONLY.")


def call_double_tempo(inputs: CycleInputs, aplomb_state: Mapping[str, Any]) -> Dict[str, Any]:
    raise InertSkeleton("À brancher après relecture : double_tempo.py comme calculateur budgets.")


def call_policy_engine(
    inputs: CycleInputs,
    aplomb_state: Mapping[str, Any],
    prudence_measure: Mapping[str, Any],
    tempo_budgets: Mapping[str, Any],
) -> Dict[str, Any]:
    raise InertSkeleton("À brancher après relecture : policyengine.py par appel decide pur.")


def call_allocation(
    inputs: CycleInputs,
    policy_state: Mapping[str, Any],
    prudence_measure: Mapping[str, Any],
    tempo_budgets: Mapping[str, Any],
) -> Dict[str, Any]:
    raise InertSkeleton("À brancher après relecture : allocation pure/wrapper V1 sans chemin legacy.")


def build_trace_line(inputs: CycleInputs, outputs: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "contract_id": CONTRACT_ID,
        "orchestrator_id": ORCHESTRATOR_ID,
        "run_id": inputs.run_id,
        "inputs": asdict(inputs),
        "outputs_keys": sorted(outputs.keys()),
        "d9_writer": "orchestrateur_demo",
        "d11_scope": "explicit_reads_parameters_returns_writes",
    }


def prepare_cycle_outputs(inputs: CycleInputs) -> CycleOutputs:
    market_context = build_market_context(inputs.market_context)
    normalized_inputs = CycleInputs(
        capital_eur=inputs.capital_eur,
        market_context=market_context,
        run_id=inputs.run_id,
        timestamp_utc=inputs.timestamp_utc,
    )

    aplomb_state = call_aplomb_calculator(normalized_inputs)
    prudence_measure = call_prudence_measure(normalized_inputs, aplomb_state)
    tempo_budgets = call_double_tempo(normalized_inputs, aplomb_state)
    policy_state = call_policy_engine(normalized_inputs, aplomb_state, prudence_measure, tempo_budgets)
    allocation_state = call_allocation(normalized_inputs, policy_state, prudence_measure, tempo_budgets)

    trace_line = build_trace_line(
        normalized_inputs,
        {
            "aplomb_state": aplomb_state,
            "prudence_measure": prudence_measure,
            "tempo_budgets": tempo_budgets,
            "policy_state": policy_state,
            "allocation_state": allocation_state,
        },
    )

    return CycleOutputs(
        aplomb_state=aplomb_state,
        policy_state=policy_state,
        allocation_state=allocation_state,
        prudence_measure=prudence_measure,
        trace_line=trace_line,
    )


def atomic_write_json(path: Path, payload: Mapping[str, Any], *, allow_write: bool = False) -> None:
    assert_v1_write_target(path)
    if not allow_write:
        raise InertSkeleton("Write désactivé : squelette inerte, allow_write=False.")

    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)


def append_trace_jsonl(path: Path, payload: Mapping[str, Any], *, allow_write: bool = False) -> None:
    assert_v1_write_target(path)
    if not allow_write:
        raise InertSkeleton("Trace désactivée : squelette inerte, allow_write=False.")

    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def write_cycle_outputs(outputs: CycleOutputs, *, allow_write: bool = False) -> None:
    atomic_write_json(ALLOWED_V1_STATES["aplomb"], outputs.aplomb_state, allow_write=allow_write)
    atomic_write_json(ALLOWED_V1_STATES["policy"], outputs.policy_state, allow_write=allow_write)
    atomic_write_json(ALLOWED_V1_STATES["allocation"], outputs.allocation_state, allow_write=allow_write)
    atomic_write_json(ALLOWED_V1_STATES["prudence_measure"], outputs.prudence_measure, allow_write=allow_write)
    append_trace_jsonl(ALLOWED_V1_STATES["trace"], outputs.trace_line, allow_write=allow_write)


def run_cycle(inputs: CycleInputs, *, allow_write: bool = False) -> CycleOutputs:
    if allow_write:
        raise InertSkeleton("Activation runtime interdite dans ce squelette : relire/valider avant exécution.")
    outputs = prepare_cycle_outputs(inputs)
    write_cycle_outputs(outputs, allow_write=False)
    return outputs


if __name__ == "__main__":
    raise SystemExit(
        "SQUELETTE INERTE : import/relecture seulement. "
        "Aucun cycle V1 ne doit être lancé depuis ce fichier sans validation ultérieure."
    )
