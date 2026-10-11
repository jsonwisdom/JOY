# Aubrey Plaza Forest Test Path v0.1

**System:** AppleBlossomAwesomeLeahPrimeMerkleForest  
**Replay:** AubreyPlazaChaosAgent  
**Status:** test fixture / public-source only  
**Authority created:** false

## Purpose

Use Aubrey Plaza as a metadata stress test for the first concrete **LEAF → TREE → FOREST** path.

The fixture deliberately contains:

- a genuine same-target public-source conflict (`age_at_stroke = 21` vs `20`);
- a temporal-semantic near-miss that must **not** become a false conflict (`The White Lotus` series year label `2021` vs Plaza participation in Season 2 in `2022`);
- a synthetic LeahPrime creative replay that is discoverable but has `evidence_weight = 0` and cannot resolve factual conflicts.

## Boundary corrections

1. **Public interview ≠ private receipt.** If a public figure says something in a published interview, the access scope remains public.
2. **Series start year ≠ performer participation year.** Different semantics require different `target_id` values.
3. **Creative replay ≠ factual evidence.** LeahPrime can model scenarios without voting on historical truth.
4. **Hash ≠ semantic truth.** Hashes prove byte inclusion/replay, not that the underlying claim is correct.
5. **Forest shared ≠ root shared.** Cross-tree inference remains false.

## Existing-schema compatibility

JOY already has `schemas/joy/epistemic_receipt_v0_1.schema.json` with `additionalProperties: false`.

This test does **not** mutate that canonical schema. Forest metadata lives in a sidecar:

`schemas/forest/forest_leaf_envelope_v0_1.schema.json`

The sidecar references the receipt by `receipt_ref`.

## Fixture sources

- Guardian, 2012: reports July 2005, age 21.
- Guardian, 2016: reports the stroke as occurring at age 20.
- TVLine, 2022: Plaza joins *The White Lotus* Season 2 as Harper Spiller.
- IMDb name page: uses the title-year label *The White Lotus (2021)*; the fixture treats this as a series-label year, not proof Plaza appeared in 2021.
- LeahPrime creative replay: synthetic URN only; no factual weight.

## Run

```bash
python3 tools/forest/aubrey_plaza_receipt_factory_v0_1.py \
  fixtures/forest/aubrey_plaza_seed_v0_1.json \
  -o receipts/forest/AUBREY_PLAZA_FOREST_RECEIPTS_V0_1.json
```

Expected BoxDee behavior:

```text
STROKE_AGE              -> CONFLICT / HOLD
WHITE_LOTUS_YEAR_PAIR   -> NO_CONFLICT (different target semantics)
CREATIVE_REPLAY         -> DISCOVERABLE / ZERO_FACT_WEIGHT
CROSS_TREE_INFERENCE    -> FALSE
AUTHORITY_CREATED       -> FALSE
```

## Next gate

Implement the Replay Collision Matrix against **classes and target semantics**, not merely root names. A collision rule should never merge two claims until their `target_id` semantics are demonstrably equivalent.
