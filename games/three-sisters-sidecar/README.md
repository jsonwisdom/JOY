# Three Sisters Sidecar

MOVE 012 materializes a cooperative game specification on a 64 x 64 grid.
The board has 4,096 cells, addressed as `[row, column]` from `[0,0]` through
`[63,63]`.

## Purpose

Three sisters preserve memory, continue joy, and route around obstruction.
Victory belongs to the group: all three active pieces must occupy row 63 in the
same state, with the lineage chain intact and the final route marked safe.

## Zones

- Sister One: columns 0-20, blue, preserve.
- Sister Two: columns 21-42, gold, continue.
- Sister Three: columns 43-63, green, route.

The three zones are contiguous, non-overlapping, and cover all 64 columns.
The sidecar is a rule membrane over the entire board, not a fourth piece.

## Turns and movement

1. Sister One's shield moves one cell orthogonally. It stays in its zone unless
   a sidecar route explicitly authorizes a boundary crossing. It preserves one
   adjacent allied piece for the next turn.
2. Sister Two's spiral moves any unobstructed positive distance diagonally. It
   stays in its zone unless routed. Every traversed cell becomes a joy trail for
   one turn and gives the next landing piece one additional unit of range.
3. Sister Three's node uses a `(2,1)` knight displacement and may cross zones.
   During sidecar activation it may relocate to a safe cell adjacent to the
   blocked piece and open one safe passage.

## Sidecar resolution

When the active piece has no ordinary legal move, the engine must preserve the
current state, keep the same turn open, and choose the lexicographically first
safe executable route proposed by Sister Three. A candidate is safe only when
it remains on-board, is unoccupied, preserves the lineage chain, and does not
set authority or publication state. If no candidate can be demonstrated, the
state is `ROUTE_REQUIRED`; it is not a win, loss, or fabricated move.

`TERMINAL_HOLD=false` is a design invariant. These JSON artifacts define the
invariant and test vectors; an engine test is still required to prove every
reachable runtime state has a safe route.

## Receipts

Each accepted move carries `previous_receipt_sha256` and `receipt_sha256`.
The receipt digest is lowercase SHA-256 over the exact UTF-8 bytes of an
RFC 8785/JCS canonical move payload. The payload excludes its own digest.
The three receipt classes are `preservation`, `continuity`, and `routing`.
No identity, ownership, authority, or publication permission is inferred.

## Files

- `board-schema.json`: board geometry, zones, and state contract.
- `pieces.json`: movement and abilities.
- `sidecar-rules.json`: deterministic blocked-state routing.
- `victory-condition.json`: cooperative victory predicate.
- `test-vectors/`: opening, blocked-route, and victory examples.
- `engine.py`: MOVE 013 stdlib reference engine.
- `test_engine.py`: vector-backed engine tests.

## MOVE 013 engine

Run:

```bash
python3 -m unittest test_engine.py
```

from this directory. The engine checks legal movement, deterministic sidecar
selection, receipt-chain hashing, and `TERMINAL_HOLD=false`. It does **not**
prove that every reachable blocked state has a safe route.

Spiral opening moves in `test-vectors/opening-move.json` are a legal prefix of
the full unobstructed diagonal rays. Shield at `[12, 20]` still has ordinary
in-zone moves under three-piece occupancy; sidecar *selection* matches the
blocked-route vector, while `ordinary_legal_moves: []` requires additional
occupancy.

Canonical receipts use the JOY restricted JCS approximation from
`lock_replay_proof.py` (UTF-8, sorted keys, compact separators). That is not a
full RFC 8785 number serializer.

Status: specification materialized; reference engine tests run on published
vectors. Exhaustive no-stall proof of every reachable state remains open.
Authority created: false.
