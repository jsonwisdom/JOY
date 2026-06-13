# DCYF_CHILD_SUPPORT_IMPLEMENTATION_CONTRAST_V0_1

```json
{
  "artifact": "DCYF_CHILD_SUPPORT_IMPLEMENTATION_CONTRAST_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/DCYF_CHILD_SUPPORT_IMPLEMENTATION_CONTRAST_V0_1.md",
  "parent_artifact": "DEED_UI_OVERPAYMENT_NOTICE_APPEAL_CORRECTION_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "DCYF child support implementation contrast",
  "classification": "CHILD_SUPPORT_AND_WELFARE_LINKED_ENFORCEMENT_CONTRAST",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_PENDING",
  "evidence_weight": "MEDIUM_PENDING_OFFICIAL_MN_PACKET",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

DCYF-style child welfare and child support implementation differs from DEED UI overpayment implementation. DEED is a benefits and economic agency with unemployment-insurance overpayment and benefit-deduction mechanics. DCYF-style involvement often sits closer to child welfare, foster care, public assistance assignment, family support, and coordination with child support enforcement systems.

This artifact indexes the contrast while avoiding overclaim.

## Jurisdiction Boundary

This artifact separates:

```json
{
  "Minnesota_DCYF_or_child_support_program": "PRIMARY_TARGET_BUT_SOURCE_PACKET_PENDING",
  "Washington_DCYF_examples": "COMPARISON_ONLY_NOT_MINNESOTA_PROOF",
  "DEED_UI_comparison": "PREVIOUSLY_INDEXED_MN_DEED_LANE"
}
```

Washington DCYF policy examples may help compare policy direction, but they do not prove Minnesota implementation.

## Indexed Contrast

| Surface | DEED UI Overpayments | DCYF / Child Support / Welfare-Linked Cases |
|---|---|---|
| Primary posture | UI benefit/debt administration | child support, child welfare, foster care/public assistance intersections |
| Main money path | benefit deductions, repayment plans, Revenue Recapture | support arrears, assigned arrears, public assistance/foster reimbursement, IV-D tools |
| Agency role | claimant agency for UI overpayment debts; payer/source for certain deductions | supervisory/referral/coordination role depending on state structure; counties/tribes/IV-D actors may implement |
| Recapture link | UI overpayments can connect to MNDOR Revenue Recapture | support arrears and state-assigned debts can connect to intercept/recapture systems |
| Person-level proof | overpayment determination, appeal, correction, certification | support order, arrears ledger, assignment status, notice, hearing/modification path |

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | HOLD | Cross-state DCYF examples cannot be treated as Minnesota proof. |
| ERS-002 Wrong Vault | PASS | DEED benefit mechanics and child-support enforcement mechanics are not collapsed. |
| ERS-003 Wrong Certificate | PARTIAL | Comparison document belongs to contrast layer; Minnesota packet still needed. |
| ERS-004 Unknown Waters | ACTIVE | MN-specific DCYF/child support official packet remains pending. |

## Strict Scope

This artifact does not verify:

- Minnesota DCYF's exact current legal authority;
- any specific child support arrears case;
- any specific foster reimbursement policy;
- any specific assignment of arrears;
- any specific tax intercept or recapture;
- any specific DEED withholding from UI for child support;
- any agency error;
- any legal conclusion.

## Remaining Source Packet Requirements

```json
{
  "Minnesota_DCYF_child_support_public_url": "REQUIRED",
  "Minnesota_child_support_enforcement_public_url": "REQUIRED",
  "MNDOR_or_revenue_recapture_child_support_cross_reference": "REQUIRED",
  "fetched_at": "REQUIRED",
  "content_hash": "REQUIRED",
  "witness_service_or_replay_surface": "REQUIRED",
  "official_source_type": "MN_DCYF_PAGE | MN_CHILD_SUPPORT_PAGE | MNDOR_PAGE | REVISOR_STATUTE"
}
```

## Person-Level Packet Requirements

```json
{
  "support_order": "REQUIRED_FOR_PERSON_LEVEL",
  "arrears_ledger": "REQUIRED_FOR_PERSON_LEVEL",
  "assigned_or_unassigned_arrears_status": "REQUIRED_FOR_PERSON_LEVEL",
  "notice_of_action_or_intercept": "REQUIRED_FOR_PERSON_LEVEL",
  "hearing_or_review_path": "REQUIRED_FOR_PERSON_LEVEL",
  "payment_source_or_offset_record": "REQUIRED_FOR_PERSON_LEVEL"
}
```

## Classification Update

```json
{
  "vector": "DCYF child support implementation contrast",
  "classification": "CHILD_SUPPORT_AND_WELFARE_LINKED_ENFORCEMENT_CONTRAST",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_PENDING",
  "evidence_weight": "MEDIUM_PENDING_OFFICIAL_MN_PACKET",
  "promotion_allowed": false,
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Next Lawful Surfaces

1. Minnesota DCYF official child support / program supervision source packet.
2. Minnesota child support enforcement / tax intercept / income withholding source packet.
3. MNDOR child support priority and recapture cross-reference.
4. DEED UI income withholding for child support, if separating payer-source mechanics from claimant-agency mechanics.

## Closing Receipt

DCYF contrast indexed.  
Cross-jurisdiction examples separated.  
Minnesota source packet still required.  
No person-level promotion.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
