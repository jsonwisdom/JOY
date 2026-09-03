#!/usr/bin/env python3
"""MOVE 013 tests: movement, sidecar routing, receipt chain, no terminal hold."""

from __future__ import annotations

import json
import unittest
from copy import deepcopy

from engine import (
    GAME_DIR,
    GENESIS_RECEIPT,
    InvariantError,
    ReferenceEngine,
    canonical_bytes,
    sha256_hex,
)


def load_vector(name: str) -> dict:
    return json.loads((GAME_DIR / "test-vectors" / name).read_text(encoding="utf-8"))


class OpeningMovementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vector = load_vector("opening-move.json")
        self.engine = ReferenceEngine.opening()

    def test_opening_invariants(self) -> None:
        self.assertIs(self.engine.state["terminal_hold"], False)
        self.assertIs(self.engine.state["authority_created"], False)
        self.assertIs(self.vector["sidecar_activated"], False)

    def test_shield_and_node_match_vector(self) -> None:
        self.assertEqual(
            self.engine.legal_moves("sister_one_shield"),
            self.vector["legal_moves"]["sister_one_shield"],
        )
        self.assertEqual(
            self.engine.legal_moves("sister_three_node"),
            self.vector["legal_moves"]["sister_three_node"],
        )

    def test_spiral_vector_moves_are_legal_prefix_of_full_rays(self) -> None:
        legal = self.engine.legal_moves("sister_two_spiral")
        listed = self.vector["legal_moves"]["sister_two_spiral"]
        for cell in listed:
            self.assertIn(cell, legal)
        self.assertGreater(len(legal), len(listed))
        self.assertEqual(legal[:4], [[1, 30], [1, 32], [2, 29], [2, 33]])


class SidecarRoutingTests(unittest.TestCase):
    def test_blocked_route_vector_selection(self) -> None:
        vector = load_vector("blocked-route.json")
        engine = ReferenceEngine.opening()
        shield = engine.piece("sister_one_shield")
        shield["row"], shield["column"] = vector["position"]
        candidates = engine.sidecar_candidates("sister_one_shield")
        selected = engine.select_sidecar_route("sister_one_shield")
        self.assertEqual(candidates, vector["node_route_candidates"])
        self.assertEqual(selected, vector["selected_safe_route"])
        self.assertEqual(vector["selection_rule"], "row_then_column_ascending")
        self.assertIs(vector["terminal_hold"], False)
        ordinary = engine.legal_moves("sister_one_shield")
        self.assertNotEqual(
            ordinary,
            [],
            "shield at [12,20] still has in-zone orthogonal moves under 3-piece occupancy",
        )

    def test_sidecar_applies_when_ordinary_moves_are_empty(self) -> None:
        engine = ReferenceEngine.opening()
        engine.piece("sister_one_shield")["row"] = 0
        engine.piece("sister_one_shield")["column"] = 0
        engine.piece("sister_two_spiral")["row"] = 0
        engine.piece("sister_two_spiral")["column"] = 1
        engine.piece("sister_three_node")["row"] = 1
        engine.piece("sister_three_node")["column"] = 0
        self.assertEqual(engine.legal_moves("sister_one_shield"), [])
        before = deepcopy(engine.state)
        receipt = engine.apply_sidecar_route("sister_one_shield")
        self.assertEqual(receipt["result"], "ROUTED")
        self.assertEqual(receipt["receipt_class"], "routing")
        self.assertEqual(receipt["destination"], [1, 1])
        self.assertIs(receipt["terminal_hold"], False)
        self.assertIs(engine.state["turn_open"], True)
        self.assertEqual(engine.piece("sister_one_shield")["row"], 0)
        self.assertEqual(engine.piece("sister_one_shield")["column"], 0)
        self.assertEqual(engine.piece("sister_three_node")["row"], 1)
        self.assertEqual(engine.piece("sister_three_node")["column"], 1)
        self.assertEqual(before["pieces"][0], engine.piece("sister_one_shield"))

    def test_route_required_when_lineage_is_broken(self) -> None:
        engine = ReferenceEngine.opening()
        engine.piece("sister_one_shield")["row"] = 0
        engine.piece("sister_one_shield")["column"] = 0
        engine.piece("sister_two_spiral")["row"] = 0
        engine.piece("sister_two_spiral")["column"] = 1
        engine.piece("sister_three_node")["row"] = 1
        engine.piece("sister_three_node")["column"] = 0
        engine.state["lineage_intact"] = False
        receipt = engine.apply_sidecar_route("sister_one_shield")
        self.assertEqual(receipt["result"], "ROUTE_REQUIRED")
        self.assertIs(engine.state["turn_open"], True)
        self.assertIs(engine.state["terminal_hold"], False)
        self.assertEqual(engine.piece("sister_three_node")["row"], 1)
        self.assertEqual(engine.piece("sister_three_node")["column"], 0)


class ReceiptChainTests(unittest.TestCase):
    def test_accepted_move_chains_sha256_over_payload_without_digest(self) -> None:
        engine = ReferenceEngine.opening()
        first = engine.apply_ordinary_move("sister_one_shield", [1, 10])
        self.assertEqual(first["previous_receipt_sha256"], GENESIS_RECEIPT)
        self.assertEqual(first["receipt_class"], "preservation")
        payload = {key: value for key, value in first.items() if key != "receipt_sha256"}
        self.assertEqual(first["receipt_sha256"], sha256_hex(canonical_bytes(payload)))
        self.assertNotIn("receipt_sha256", json.loads(canonical_bytes(payload)))
        second = engine.apply_ordinary_move("sister_two_spiral", [1, 32])
        self.assertEqual(second["previous_receipt_sha256"], first["receipt_sha256"])
        self.assertEqual(second["receipt_class"], "continuity")
        second_payload = {
            key: value for key, value in second.items() if key != "receipt_sha256"
        }
        self.assertEqual(
            second["receipt_sha256"], sha256_hex(canonical_bytes(second_payload))
        )


class InvariantTests(unittest.TestCase):
    def test_hold_attempt_is_type_error(self) -> None:
        engine = ReferenceEngine.opening()
        broken = deepcopy(engine.state)
        broken["terminal_hold"] = True
        with self.assertRaises(InvariantError):
            ReferenceEngine(broken)

    def test_authority_cannot_be_created(self) -> None:
        engine = ReferenceEngine.opening()
        broken = deepcopy(engine.state)
        broken["authority_created"] = True
        with self.assertRaises(InvariantError):
            ReferenceEngine(broken)

    def test_victory_vector(self) -> None:
        vector = load_vector("victory-state.json")
        engine = ReferenceEngine.from_victory_vector()
        self.assertEqual(engine.evaluate(), vector["expected_result"])
        self.assertIs(engine.state["terminal_hold"], False)
        self.assertIs(engine.state["authority_created"], False)


if __name__ == "__main__":
    unittest.main()
