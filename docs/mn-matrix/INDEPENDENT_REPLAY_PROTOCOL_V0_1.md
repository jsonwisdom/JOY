# INDEPENDENT_REPLAY_PROTOCOL_V0_1

Classification: REPLAY_CONFIRMATION_GATE  
Jurisdiction: Minnesota  
Cluster: CENTRAL_MN_01  
Authority: false  
Verified: false  
No Fake Green: true

---

## Purpose

Define the minimum conditions under which a third party can replay a preserved county surface and report whether their output matches the preserved surface.

Independent replay tests reproducibility of the preserved surface. It does not prove truth of the underlying claim, agency fault, systemic cause, or legal authority.

---

## Core Rule

```text
INDEPENDENT_REPLAY
=
REPRODUCIBILITY_SIGNAL_ONLY
```

---

## Anti-Inference Lock

```text
INDEPENDENT_REPLAY != TRUTH
MATCH != MERITS_PROVEN
MISMATCH != FRAUD
UNABLE_TO_REPLAY != WRONGDOING
REPLAY_CONFIRMATION = REPRODUCIBILITY_SIGNAL_ONLY
```

---

## Replay Object

```json
{
  "replay_id": "REPLAY_<COUNTY>_<YYYYMMDD>_<NNN>",
  "county": null,
  "source_surface_id": null,
  "replayer": {
    "name_or_handle": null,
    "affiliation": null,
    "independence_claimed": true,
    "relationship_to_originator": "none | known | unknown"
  },
  "input_materials": {
    "surface_manifest": null,
    "receipt_objects": [],
    "preservation_hashes": [],
    "public_urls": [],
    "instructions_used": null
  },
  "replay_run": {
    "started_at": null,
    "completed_at": null,
    "environment": null,
    "method": "manual | scripted | hybrid",
    "tooling": [],
    "steps_performed": []
  },
  "output": {
    "output_hash": null,
    "match_status": "MATCH | PARTIAL_MATCH | MISMATCH | UNABLE_TO_REPLAY",
    "differences": [],
    "notes": null
  },
  "limits": {
    "truth_claimed": false,
    "agency_fault_claimed": false,
    "systemic_pattern_claimed": false,
    "authority_claimed": false
  }
}
```

---

## Match States

```json
{
  "MATCH": "Independent replayer produced the same preserved output from the same declared inputs.",
  "PARTIAL_MATCH": "Some outputs matched, but differences or missing steps remain.",
  "MISMATCH": "Replay produced a different output from declared inputs.",
  "UNABLE_TO_REPLAY": "Inputs, links, instructions, permissions, or records were insufficient for replay."
}
```

---

## Promotion Rule

A county surface may move from PRESERVED to REPLAYABLE only when all required replay fields are present and match_status is MATCH.

```json
{
  "preserved_surface_exists": true,
  "surface_hash_present": true,
  "replay_inputs_complete": true,
  "independent_replayer_present": true,
  "match_status": "MATCH",
  "limits_acknowledged": true,
  "no_fake_green": true
}
```

---

## CENTRAL_MN_01 Cluster Gate

```json
{
  "cluster_id": "CENTRAL_MN_01",
  "members": ["Stearns", "Sherburne", "Benton", "Wright", "Morrison"],
  "entry_state": "PRESERVED_MULTI_COUNTY_SURFACES",
  "exit_requires": {
    "preserved_county_surfaces": 5,
    "independent_replay_confirmations_minimum": 1,
    "verified_findings": 0,
    "authority": false,
    "no_fake_green": true
  },
  "unlocks_next": "METRO_MAJOR_02"
}
```

---

## Goblin Ruling

Template is not evidence. Evidence is not truth. Replay is not authority. Replayable means independently reproducible from declared inputs.
