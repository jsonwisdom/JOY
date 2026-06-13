# ANCIENT_WISDOM_COLLECTION_V0_1

## STATUS: COLLECTION_SPEC_DRAFT
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE
## ANCHORED_TO: jaywisdom.eth
## ENGINE: jaywisdom.base.eth
## L1_ANCHOR_EXECUTED: FALSE

---

## 1. Purpose

The Ancient Wisdom Collection preserves old teachings, quotes, fragments, proverbs, philosophical claims, martial lessons, civic lessons, and cultural memory without falsely upgrading them into verified authority.

This collection is a custody lane, not a truth oracle.

```text
Ancient wisdom enters as PRESERVED.
Attribution enters as UNVERIFIED unless sourced.
Interpretation enters as PENDING or PARTIAL unless witnessed.
Surface green requires ALMS receipt custody.
```

---

## 2. Stack Placement

```text
MCP -> CAV -> ALMSL+ -> ALMS -> Ancient Wisdom Collection -> Surface
```

- MCP captures the fragment.
- CAV verifies any CSV / Excel row representation.
- ALMSL+ maps the item to JSONL line custody.
- ALMS archives receipt-bound entries.
- Ancient Wisdom Collection groups archived entries into thematic memory lanes.
- Surface displays only state-labeled entries.

---

## 3. Core Law

```text
Old does not mean true.
Famous does not mean sourced.
Useful does not mean verified.
Beautiful does not mean authoritative.
Unknown is not false.
Unverified is not bad.
Pending is not rejected.
```

---

## 4. Collection Lanes

```text
lane_aw_00_fragment_capture
lane_aw_01_source_attribution
lane_aw_02_translation_or_interpretation
lane_aw_03_civic_application
lane_aw_04_family_or_local_memory
lane_aw_05_receipt_binding
lane_aw_06_tombstone_or_correction
lane_aw_07_surface_card
```

---

## 5. Required State Labels

Every item must carry one state.

```text
PRESERVED     = captured, not verified
UNVERIFIED    = attribution or source not proven
PENDING       = waiting for human or source judgment
PARTIAL       = some evidence attached
VERIFIED      = source + custody + receipt pass
REJECTED      = contradicted or invalid
SUPERSEDED    = replaced by stronger item
DEPRECATED    = retained but no longer recommended
```

---

## 6. Attribution Rules

No item may claim final attribution without source evidence.

Allowed attribution states:

```text
ATTRIBUTED_VERIFIED
ATTRIBUTED_TRADITIONAL
ATTRIBUTED_DISPUTED
ATTRIBUTED_UNKNOWN
ATTRIBUTED_PARAPHRASE
```

If a quote is useful but attribution is weak, preserve it as wisdom fragment, not as verified quotation.

---

## 7. No Fake Green Rules

```text
No green quote without source.
No green author without attribution proof.
No green translation without translator/source note.
No green civic claim without evidence path.
No green family memory without human approval if required.
No L1 anchor claim without transaction hash and read-back proof.
```

---

## 8. Example Collection Entry

```json
{
  "collection": "ANCIENT_WISDOM_COLLECTION_V0_1",
  "item_id": "AWC-000001",
  "lane": "lane_aw_00_fragment_capture",
  "title": "Sword Kept Sharp by Custody",
  "fragment": "A blade kept in silence still remembers the hand that forged it.",
  "attribution_state": "ATTRIBUTED_UNKNOWN",
  "truth_state": "YELLOW",
  "claim_state": "PRESERVED",
  "alms_entry_ref": null,
  "source_ref": null,
  "render_green": false,
  "no_fake_green": true
}
```

---

## 9. Final Ruling

```text
Ancient Wisdom Collection = CREATED AS CUSTODY LANE
STATUS = DRAFT
TRUTH_STATE = YELLOW
L1_ANCHOR_EXECUTED = FALSE
NO_FAKE_GREEN = ACTIVE
```
