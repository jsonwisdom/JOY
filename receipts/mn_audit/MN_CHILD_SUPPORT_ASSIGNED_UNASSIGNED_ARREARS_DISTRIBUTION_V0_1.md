# MN_CHILD_SUPPORT_ASSIGNED_UNASSIGNED_ARREARS_DISTRIBUTION_V0_1

```json
{
  "artifact": "MN_CHILD_SUPPORT_ASSIGNED_UNASSIGNED_ARREARS_DISTRIBUTION_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_CHILD_SUPPORT_ASSIGNED_UNASSIGNED_ARREARS_DISTRIBUTION_V0_1.md",
  "parent_artifact": "MN_CHILD_SUPPORT_STATE_REVENUE_RECAPTURE_OFFSET_V0_1",
  "parent_spine": "MN_CHILD_SUPPORT_ENFORCEMENT_INTERCEPT_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "assigned vs unassigned arrears distribution rules",
  "classification": "CHILD_SUPPORT_DISTRIBUTION_AND_ARREARS_CLASSIFICATION_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED_BY_USER",
  "evidence_weight": "HIGH_PROGRAM_LEVEL_PENDING_DIRECT_OFFICIAL_URL_HASH_REPLAY",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

Minnesota child support arrears may be categorized as assigned or unassigned. That classification affects distribution: whether collections reimburse the state for public assistance/foster-care-related support or pass through to the family.

This layer answers:

```text
After IWO, Project Intercept, or Revenue Recapture collects money, who gets paid first: state, family, or both?
```

## Source Packet Submitted

```json
{
  "primary_surfaces": [
    "Minnesota DCYF / MN Child Support glossary and program guidance",
    "Minnesota Child Support Online case-specific distribution history",
    "county child support worker breakdown for assigned/unassigned balances"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "MN_CHILD_SUPPORT_ASSIGNED_UNASSIGNED_DISTRIBUTION_20260613_USER_PACKET",
  "witness_service_or_replay_surface": "User-submitted official-source packet; direct URL/hash replay still required for full four-surface verification",
  "official_source_type": "MN_DCYF_CHILD_SUPPORT_GLOSSARY_PLUS_CASE_PORTAL_CONTEXT"
}
```

## Arrears Types Indexed

```json
{
  "unassigned_arrears": "Arrears not assigned to the state; generally payable to the family/obligee.",
  "permanently_assigned_arrears": "Arrears assigned to the state from public assistance periods; collections may reimburse state/federal assistance up to assistance paid.",
  "conditionally_assigned_arrears": "Arrears assigned in connection with assistance rules that may return family priority after assistance ends, subject to exceptions.",
  "temporarily_assigned_or_pass_through_context": "Current support or pass-through treatment during assistance may be governed by specific program rules."
}
```

## Distribution Rules Indexed

- Current support is generally prioritized before arrears distribution.
- Unassigned arrears generally flow to the family.
- Permanently assigned arrears may reimburse the state/federal government up to assistance provided.
- Conditionally assigned arrears may shift distribution treatment after assistance ends, subject to federal/state rules and intercept-specific exceptions.
- Mixed cases may require pro-rated, oldest-first, or category-specific distribution logic.
- All person-level distribution requires ledger and assignment-status records.

## Tool-Specific Distribution Notes

| Collection Tool | Distribution Note |
|---|---|
| IWO / income withholding | Ongoing collections route through payment center and apply per current support/arrears distribution rules. |
| Project Intercept / federal tax refund offset | Federal intercepts may retain more aggressively for assigned arrears depending on public assistance status and rules. |
| Revenue Recapture / state refund offset | State offset collections may reimburse state-assigned arrears before family distribution, depending on ledger and assignment status. |

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Distribution model separated from individual ledger reality. |
| ERS-002 Wrong Vault | PASS | Collection mechanism and distribution destination are not collapsed. |
| ERS-003 Wrong Certificate | PARTIAL | User supplied official-source packet; direct URL/hash replay still needed for full four-surface verification. |
| ERS-004 Unknown Waters | DOWNGRADED | Program distribution model clear; person-level ledger/assignment history still required. |

## Strict Scope

This artifact does not verify:

- any specific assigned arrears balance;
- any specific unassigned arrears balance;
- any specific public assistance history;
- any specific foster-care reimbursement balance;
- any specific payment center distribution;
- any specific obligee or obligor case;
- any specific Project Intercept or Revenue Recapture distribution;
- any agency error;
- any legal conclusion.

## Remaining Four-Surface Requirements

```json
{
  "Minnesota_DCYF_child_support_glossary_public_url": "REQUIRED_FOR_FULL_REPLAY",
  "Minnesota_distribution_rules_public_url_or_manual": "REQUIRED_FOR_FULL_REPLAY",
  "Minnesota_Child_Support_Online_case_history": "PERSON_LEVEL_ONLY_IF_AUTHORIZED",
  "fetched_at": "REQUIRED_PER_SOURCE",
  "content_hash": "REQUIRED_PER_SOURCE",
  "witness_service_or_replay_surface": "REQUIRED_PER_SOURCE"
}
```

## Person-Level Packet Requirements

```json
{
  "support_order": "REQUIRED_FOR_PERSON_LEVEL",
  "arrears_ledger": "REQUIRED_FOR_PERSON_LEVEL",
  "public_assistance_or_foster_assignment_history": "REQUIRED_IF_ASSIGNED_ARREARS_DISPUTED",
  "payment_center_distribution_history": "REQUIRED_FOR_PERSON_LEVEL",
  "collection_tool_used": "REQUIRED_FOR_PERSON_LEVEL",
  "notice_or_intercept_record": "REQUIRED_FOR_PERSON_LEVEL",
  "review_hearing_or_correction_record": "REQUIRED_IF_CONTESTED"
}
```

## Classification Update

```json
{
  "vector": "assigned vs unassigned arrears distribution rules",
  "classification": "CHILD_SUPPORT_DISTRIBUTION_AND_ARREARS_CLASSIFICATION_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED_BY_USER",
  "evidence_weight": "HIGH_PROGRAM_LEVEL_PENDING_DIRECT_OFFICIAL_URL_HASH_REPLAY",
  "promotion_allowed": "PROGRAM_LEVEL_ONLY_WITH_CAUTION",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Next Lawful Surfaces

1. Attach direct DCYF glossary/distribution rule URLs with hashes.
2. Select county child support notice/review/hearing path.
3. Select arrears compromise, payment agreement, or modification process.
4. Select person-level support order, arrears ledger, assignment history, and distribution packet, if a specific case lane is chosen.

## Closing Receipt

Assigned vs unassigned arrears distribution lane indexed.  
The enforcement tools collect; distribution rules decide who receives funds.  
Program model holds with caution pending direct URL/hash replay.  
Person-level ledger, assignment status, and payment history remain unverified.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
