#!/usr/bin/env python3
"""MOVE 013 reference engine for Three Sisters Sidecar.

Deterministic, stdlib-only. Authority is never created. TERMINAL_HOLD is never
true. Exhaustive proof that every reachable blocked state has a safe route is
intentionally not claimed; this engine proves legal movement, sidecar
selection, receipt chaining, and the hold invariant on the published vectors.
"""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from pathlib import Path

GAME_DIR = Path(__file__).resolve().parent
GENESIS_RECEIPT = "0" * 64
BOARD_MAX = 63
ORTHOGONAL = ((-1, 0), (1, 0), (0, -1), (0, 1))
DIAGONAL = ((-1, -1), (-1, 1), (1, -1), (1, 1))
ADJACENT_8 = ORTHOGONAL + DIAGONAL
KNIGHT_DELTA = (
    (1, 2),
    (2, 1),
    (-1, 2),
    (-2, 1),
    (1, -2),
    (2, -1),
    (-1, -2),
    (-2, -1),
)
ZONES = {
    "sister_one_shield": (0, 20),
    "sister_two_spiral": (21, 42),
    "sister_three_node": (43, 63),
}
RECEIPT_CLASS = {
    "sister_one_shield": "preservation",
    "sister_two_spiral": "continuity",
    "sister_three_node": "routing",
}
TURN_ORDER = ("sister_one_shield", "sister_two_spiral", "sister_three_node")


class InvariantError(ValueError):
    """Raised when a sidecar invariant would be broken."""


def canonical_bytes(obj: object) -> bytes:
    """JOY restricted JCS: UTF-8, sorted keys, compact separators.

    Same approximation used by lock_replay_proof.py. Not a full RFC 8785
    number serializer. Receipts in this engine contain only int/str/bool/null
    and nested objects/arrays.
    """
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def on_board(row: int, column: int) -> bool:
    return 0 <= row <= BOARD_MAX and 0 <= column <= BOARD_MAX


def in_home_zone(piece_id: str, column: int) -> bool:
    lo, hi = ZONES[piece_id]
    return lo <= column <= hi


def load_json(name: str) -> object:
    return json.loads((GAME_DIR / name).read_text(encoding="utf-8"))


class ReferenceEngine:
    def __init__(self, state: dict) -> None:
        self.state = state
        self._assert_invariants(self.state)

    @classmethod
    def opening(cls) -> "ReferenceEngine":
        vector = load_json("test-vectors/opening-move.json")
        initial = vector["initial"]
        pieces = [
            {
                "id": "sister_one_shield",
                "owner": "sister_one",
                "type": "shield",
                "row": initial["sister_one_shield"][0],
                "column": initial["sister_one_shield"][1],
            },
            {
                "id": "sister_two_spiral",
                "owner": "sister_two",
                "type": "spiral",
                "row": initial["sister_two_spiral"][0],
                "column": initial["sister_two_spiral"][1],
            },
            {
                "id": "sister_three_node",
                "owner": "sister_three",
                "type": "node",
                "row": initial["sister_three_node"][0],
                "column": initial["sister_three_node"][1],
            },
        ]
        return cls(
            {
                "game": "three-sisters-sidecar-v0.1",
                "move": 0,
                "pieces": pieces,
                "active_piece": "sister_one_shield",
                "lineage_intact": True,
                "joy_intact": True,
                "safe_path_confirmed": False,
                "terminal_hold": False,
                "authority_created": False,
                "publication": None,
                "previous_receipt_sha256": GENESIS_RECEIPT,
                "joy_trails": [],
                "range_bonus": 0,
                "turn_open": True,
            }
        )

    @classmethod
    def from_victory_vector(cls) -> "ReferenceEngine":
        vector = load_json("test-vectors/victory-state.json")
        return cls(
            {
                "game": vector["game"],
                "move": vector["move"],
                "pieces": deepcopy(vector["pieces"]),
                "active_piece": "sister_one_shield",
                "lineage_intact": vector["lineage_intact"],
                "joy_intact": vector["joy_intact"],
                "safe_path_confirmed": vector["safe_path_confirmed"],
                "terminal_hold": vector["terminal_hold"],
                "authority_created": vector["authority_created"],
                "publication": None,
                "previous_receipt_sha256": GENESIS_RECEIPT,
                "joy_trails": [],
                "range_bonus": 0,
                "turn_open": True,
            }
        )

    def piece(self, piece_id: str) -> dict:
        for item in self.state["pieces"]:
            if item["id"] == piece_id:
                return item
        raise KeyError(piece_id)

    def occupied(self) -> set[tuple[int, int]]:
        return {(item["row"], item["column"]) for item in self.state["pieces"]}

    def _assert_invariants(self, state: dict) -> None:
        if state.get("terminal_hold") is not False:
            raise InvariantError("object is no longer a sidecar if it holds")
        if state.get("authority_created") is not False:
            raise InvariantError("authority_created must remain false")

    def legal_moves(self, piece_id: str) -> list[list[int]]:
        piece = self.piece(piece_id)
        occupied = self.occupied() - {(piece["row"], piece["column"])}
        bonus = int(self.state.get("range_bonus") or 0)
        if piece["type"] == "shield":
            moves = self._orthogonal_moves(piece, occupied, 1 + bonus)
        elif piece["type"] == "spiral":
            moves = self._diagonal_rays(piece, occupied)
        elif piece["type"] == "node":
            moves = self._knight_moves(piece, occupied)
        else:
            raise InvariantError(f"unknown piece type: {piece['type']}")
        return sorted(moves)

    def _allows_zone_exit(self, piece_id: str) -> bool:
        return piece_id == "sister_three_node"

    def _orthogonal_moves(
        self, piece: dict, occupied: set[tuple[int, int]], distance: int
    ) -> list[list[int]]:
        moves: list[list[int]] = []
        for dr, dc in ORTHOGONAL:
            for step in range(1, distance + 1):
                row = piece["row"] + dr * step
                column = piece["column"] + dc * step
                if not on_board(row, column) or (row, column) in occupied:
                    break
                if not self._allows_zone_exit(piece["id"]) and not in_home_zone(
                    piece["id"], column
                ):
                    break
                moves.append([row, column])
        return moves

    def _diagonal_rays(
        self, piece: dict, occupied: set[tuple[int, int]]
    ) -> list[list[int]]:
        moves: list[list[int]] = []
        for dr, dc in DIAGONAL:
            step = 1
            while True:
                row = piece["row"] + dr * step
                column = piece["column"] + dc * step
                if not on_board(row, column) or (row, column) in occupied:
                    break
                if not in_home_zone(piece["id"], column):
                    break
                moves.append([row, column])
                step += 1
        return moves

    def _knight_moves(
        self, piece: dict, occupied: set[tuple[int, int]]
    ) -> list[list[int]]:
        moves: list[list[int]] = []
        for dr, dc in KNIGHT_DELTA:
            row = piece["row"] + dr
            column = piece["column"] + dc
            if not on_board(row, column) or (row, column) in occupied:
                continue
            moves.append([row, column])
        return moves

    def sidecar_candidates(self, blocked_piece_id: str) -> list[list[int]]:
        blocked = self.piece(blocked_piece_id)
        occupied = self.occupied()
        publication = self.state.get("publication")
        candidates: list[list[int]] = []
        for dr, dc in ADJACENT_8:
            row = blocked["row"] + dr
            column = blocked["column"] + dc
            if not on_board(row, column):
                continue
            if (row, column) in occupied:
                continue
            if not in_home_zone(blocked_piece_id, column):
                continue
            if self.state["lineage_intact"] is not True:
                continue
            if self.state["authority_created"] is not False:
                continue
            if self.state.get("publication") != publication:
                continue
            candidates.append([row, column])
        return sorted(candidates)

    def select_sidecar_route(self, blocked_piece_id: str) -> list[int] | None:
        candidates = self.sidecar_candidates(blocked_piece_id)
        if not candidates:
            return None
        return candidates[0]

    def evaluate(self) -> str:
        self._assert_invariants(self.state)
        rows = {item["row"] for item in self.state["pieces"]}
        if (
            rows == {63}
            and self.state["lineage_intact"] is True
            and self.state["joy_intact"] is True
            and self.state["safe_path_confirmed"] is True
            and self.state["terminal_hold"] is False
            and self.state["authority_created"] is False
        ):
            return "VICTORY"
        return "CONTINUE_OR_ROUTE"

    def apply_ordinary_move(self, piece_id: str, destination: list[int]) -> dict:
        if piece_id != self.state["active_piece"]:
            raise InvariantError("move is not this piece's turn")
        legal = self.legal_moves(piece_id)
        if destination not in legal:
            raise InvariantError("destination is not an ordinary legal move")
        before = deepcopy(self.state)
        piece = self.piece(piece_id)
        origin = [piece["row"], piece["column"]]
        traversed = self._traversed_cells(origin, destination)
        piece["row"], piece["column"] = destination[0], destination[1]
        self.state["joy_trails"] = traversed
        self.state["range_bonus"] = 1 if piece["type"] == "spiral" else 0
        self.state["move"] = int(self.state["move"]) + 1
        self.state["turn_open"] = False
        self.state["active_piece"] = self._next_turn(piece_id)
        self.state["safe_path_confirmed"] = False
        receipt = self._emit_receipt(
            piece_id=piece_id,
            receipt_class=RECEIPT_CLASS[piece_id],
            origin=origin,
            destination=destination,
            result="MOVED",
            sidecar_activated=False,
            before=before,
        )
        self._assert_invariants(self.state)
        return receipt

    def apply_sidecar_route(self, blocked_piece_id: str) -> dict:
        if self.legal_moves(blocked_piece_id):
            raise InvariantError("sidecar activates only when ordinary moves are empty")
        before = deepcopy(self.state)
        selected = self.select_sidecar_route(blocked_piece_id)
        if selected is None:
            receipt = self._emit_receipt(
                piece_id=blocked_piece_id,
                receipt_class="routing",
                origin=[
                    self.piece(blocked_piece_id)["row"],
                    self.piece(blocked_piece_id)["column"],
                ],
                destination=None,
                result="ROUTE_REQUIRED",
                sidecar_activated=True,
                before=before,
            )
            self.state["turn_open"] = True
            self._assert_invariants(self.state)
            return receipt
        node = self.piece("sister_three_node")
        origin = [node["row"], node["column"]]
        node["row"], node["column"] = selected[0], selected[1]
        self.state["move"] = int(self.state["move"]) + 1
        self.state["turn_open"] = True
        self.state["safe_path_confirmed"] = True
        receipt = self._emit_receipt(
            piece_id=blocked_piece_id,
            receipt_class="routing",
            origin=origin,
            destination=selected,
            result="ROUTED",
            sidecar_activated=True,
            before=before,
        )
        self._assert_invariants(self.state)
        return receipt

    def _next_turn(self, piece_id: str) -> str:
        index = TURN_ORDER.index(piece_id)
        return TURN_ORDER[(index + 1) % len(TURN_ORDER)]

    def _traversed_cells(
        self, origin: list[int], destination: list[int]
    ) -> list[list[int]]:
        dr = destination[0] - origin[0]
        dc = destination[1] - origin[1]
        steps = max(abs(dr), abs(dc))
        if steps == 0:
            return []
        if dr % steps != 0 or dc % steps != 0:
            return [destination]
        step_r = dr // steps
        step_c = dc // steps
        return [
            [origin[0] + step_r * step, origin[1] + step_c * step]
            for step in range(1, steps + 1)
        ]

    def _emit_receipt(
        self,
        piece_id: str,
        receipt_class: str,
        origin: list[int],
        destination: list[int] | None,
        result: str,
        sidecar_activated: bool,
        before: dict,
    ) -> dict:
        payload = {
            "authority_created": False,
            "destination": destination,
            "game": self.state["game"],
            "lineage_intact": self.state["lineage_intact"],
            "move": self.state["move"],
            "origin": origin,
            "piece_id": piece_id,
            "previous_receipt_sha256": before["previous_receipt_sha256"],
            "publication": self.state.get("publication"),
            "receipt_class": receipt_class,
            "result": result,
            "sidecar_activated": sidecar_activated,
            "terminal_hold": False,
            "turn_open": self.state["turn_open"],
        }
        digest = sha256_hex(canonical_bytes(payload))
        receipt = dict(payload)
        receipt["receipt_sha256"] = digest
        self.state["previous_receipt_sha256"] = digest
        self.state["last_receipt"] = receipt
        return receipt
