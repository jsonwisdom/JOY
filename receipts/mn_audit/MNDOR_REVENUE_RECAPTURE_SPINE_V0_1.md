# MNDOR_REVENUE_RECAPTURE_SPINE_V0_1

```json
{
  "artifact": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MNDOR_REVENUE_RECAPTURE_SPINE_V0_1.md",
  "parent_vector": "MN_PAYMENT_SYSTEMS_FRAUD_OFFSET_VECTOR_V0_1",
  "source_packet": "MNDOR_REVENUE_RECAPTURE_SOURCE_PACKET_V0_1",
  "lane": "MN_AUDIT",
  "vector": "MNDOR Revenue Recapture claimant-agency certification",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL_MEDIUM_GRANULAR",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

MNDOR acts as a central administrative offset engine under Minnesota's revenue recapture framework. Claimant agencies submit certified debts. MNDOR performs matching and offset/recapture functions, while the underlying debt authority remains with the claimant agency.

This creates a pipeline:

```text
Claimant agency certification -> MNDOR match -> offset/recapture -> notice -> contest/hearing path
```

## Attached Source Packet

```json
{
  "source_packet_artifact": "MNDOR_REVENUE_RECAPTURE_SOURCE_PACKET_V0_1",
  "public_url": "https://www.revenue.state.mn.us/revenue-recapture",
  "fetched_at": "2026-06-13",
  "content_hash": "MNDOR_PRIMARY_RECAPTURE_PAGE_20260613",
  "witness_service_or_replay_surface": "Minnesota Department of Revenue official public website (revenue.state.mn.us)",
  "official_source_type": "MNDOR_PAGE",
  "supporting_statute_url": "https://www.revisor.mn.gov/statutes/cite/270A",
  "supporting_source_type": "REVISOR_STATUTE"
}
```

## Strict Scope

This artifact indexes the statutory/program-level spine.

It does not verify:

- any specific person's debt;
- any specific agency certification packet;
- any specific offset notice;
- any specific fraud flag;
- any agency wrongdoing;
- any judicial or legal conclusion.

## ERS Replay

| ERS Check | Classification | Result |
|---|---|---|
| ERS-001 Wrong Fridge | Model vs. reality | PASS at program-model level; HOLD at person-level reality |
| ERS-002 Wrong Vault | Proof vs. deployment | PASS for administrative spine; HOLD for individual deployment packet |
| ERS-003 Wrong Certificate | Document vs. thing | PASS at program/statute level; HOLD for person-level certificate |
| ERS-004 Unknown Waters | Unknown mapping | DOWNGRADED; claimant-agency and person-level evidence still separate |

## Indexed Pipeline

```json
{
  "step_1": "claimant_agency_certifies_debt",
  "step_2": "MNDOR_or_revenue_recapture_program_receives_claim",
  "step_3": "matching_or_offset_process_runs",
  "step_4": "payment_or_refund_is_intercepted_or_recaptured_if_eligible",
  "step_5": "notice_or_contest_window_is_triggered",
  "step_6": "hearing_or_correction_path_runs_through_claimant_agency_or_designated_forum"
}
```

## Remaining Unknowns

```json
{
  "sample_certification_language": "NOT_YET_ATTACHED",
  "specific_claimant_agency": "NOT_SELECTED",
  "specific_notice_language": "NOT_ATTACHED",
  "specific_debt_priority_rule": "NOT_ATTACHED",
  "person_level_record": "NOT_PROVIDED"
}
```

## Evidence Weight

```json
{
  "program_level": "HIGH_WITH_OFFICIAL_SOURCE_PACKET_ATTACHED",
  "statute_level": "HIGH_WITH_REVISOR_SOURCE_ATTACHED",
  "granular_claimant_agency_packet": "MEDIUM_TO_LOW_UNTIL_REQUESTED_OR_RECEIVED",
  "person_level_verification": "ABSENT",
  "promotion_allowed": "PROGRAM_LEVEL_ONLY"
}
```

## Next Gate Options

1. Extract specific claimant-agency certification requirements.
2. Index the 45-day contest/hearing mechanics.
3. Index debt priority order and qualifying payments list.
4. Attach a sample notice or claimant-agency claim form.
5. File or draft a records request for agency-specific certification records.

## Closing Receipt

The administrative spine is indexed.  
The source packet is attached.  
The program-level model holds.  
No person-level claim is verified.  
Authority remains false.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
