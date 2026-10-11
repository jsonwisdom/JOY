#!/usr/bin/env python3
"""Print MOVE 013 verification status. Does not claim exhaustive no-stall proof."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from engine import ReferenceEngine

HERE = Path(__file__).resolve().parent


def main() -> int:
    suite = unittest.defaultTestLoader.discover(str(HERE), pattern="test_engine.py")
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    engine = ReferenceEngine.opening()
    first = engine.apply_ordinary_move("sister_one_shield", [1, 10])
    second = engine.apply_ordinary_move("sister_two_spiral", [1, 32])
    report = {
        "move": "013",
        "action": "REFERENCE_ENGINE_IMPLEMENTATION",
        "tests_run": result.testsRun,
        "tests_ok": result.wasSuccessful(),
        "legal_movement": "PASS" if result.wasSuccessful() else "FAIL",
        "deterministic_sidecar_routing": "PASS" if result.wasSuccessful() else "FAIL",
        "receipt_chain_hashing": "PASS" if result.wasSuccessful() else "FAIL",
        "terminal_hold_invariant": "PASS" if result.wasSuccessful() else "FAIL",
        "runtime_no_stall_proof": "NOT_PROVEN_ALL_REACHABLE_STATES",
        "observed_opening_chain": {
            "shield_move_1_10_receipt_sha256": first["receipt_sha256"],
            "spiral_move_1_32_receipt_sha256": second["receipt_sha256"],
        },
        "terminal_hold_design": False,
        "authority_created": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
