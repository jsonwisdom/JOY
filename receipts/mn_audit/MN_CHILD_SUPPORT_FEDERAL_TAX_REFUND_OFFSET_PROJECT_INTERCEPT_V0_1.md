# MN_CHILD_SUPPORT_FEDERAL_TAX_REFUND_OFFSET_PROJECT_INTERCEPT_V0_1

```json
{
  "artifact": "MN_CHILD_SUPPORT_FEDERAL_TAX_REFUND_OFFSET_PROJECT_INTERCEPT_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_CHILD_SUPPORT_FEDERAL_TAX_REFUND_OFFSET_PROJECT_INTERCEPT_V0_1.md",
  "parent_artifact": "MN_CHILD_SUPPORT_INCOME_WITHHOLDING_IWO_PAYER_SOURCE_V0_1",
  "parent_spine": "MN_CHILD_SUPPORT_ENFORCEMENT_INTERCEPT_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "federal tax refund offset / Project Intercept lane",
  "classification": "CHILD_SUPPORT_FEDERAL_REFUND_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED_BY_USER",
  "evidence_weight": "HIGH_PROGRAM_LEVEL_PENDING_DIRECT_OFFICIAL_URL_HASH_REPLAY",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

Minnesota's Federal Tax Refund Offset / Project Intercept lane is a lump-sum child support enforcement tool that complements ongoing income withholding. It targets eligible federal tax refunds through federal offset matching rather than recurring paycheck or benefit deductions.

This layer answers:

```text
How does child support enforcement reach annual federal refunds, and how is that different from IWO withholding?
```

## Source Packet Submitted

```json
{
  "primary_surface": "Minnesota DCYF federal tax refund offset / Project Intercept page",
  "public_url_submitted": "https://dcyf.mn.gov/federal-tax-refund-offset",
  "fetched_at": "2026-06-13",
  "content_hash": "MN_CHILD_SUPPORT_PROJECT_INTERCEPT_20260613_USER_PACKET",
  "witness_service_or_replay_surface": "User-submitted official-source packet; direct URL/hash replay still required for full four-surface verification",
  "official_source_type": "MN_DCYF_PAGE_PLUS_FEDERAL_TOP_CONTEXT"
}
```

## Indexed Federal Offset Rule

```json
{
  "rule": "Project Intercept targets federal tax refunds for eligible child support arrears. It is not the same mechanism as ongoing income withholding.",
  "IWO_lane": "ongoing deductions from wages, UI benefits, or other payor income streams",
  "Project_Intercept_lane": "lump-sum federal refund offset through Treasury matching",
  "DEED_boundary": "DEED may be a payor source for IWO/UI withholding but does not create the child support debt and is not the federal refund offset authority"
}
```

## Mechanics Indexed

- Eligible Minnesota child support arrears may be certified for federal tax refund offset.
- Pre-offset notice and review rights are part of the process.
- Federal refund matching and offset happen through the Treasury Offset Program / federal pipeline.
- Treasury may send a Notice of Offset after a refund is offset.
- Joint return situations may involve injured spouse allocation handling.
- Public assistance/state-assigned arrears and family-owed arrears may have different thresholds or distribution rules.
- Person-level eligibility requires order, arrears ledger, assignment status, notice, and offset records.

## Indexed Pipeline

```json
{
  "step_1": "child_support_order_and_arrears_exist",
  "step_2": "county_or_child_support_program_identifies_eligible_arrears",
  "step_3": "pre_offset_notice_or_administrative_offset_notice_sent",
  "step_4": "eligible_arrears_certified_or_reported_for_federal_offset",
  "step_5": "Treasury_refund_match_and_offset_if_refund_exists",
  "step_6": "Notice_of_Offset_and_funds_forwarding_or_hold_period",
  "step_7": "application_to_arrears_with_assignment_distribution_rules",
  "step_8": "review_correction_or_injured_spouse_path_if_applicable"
}
```

## IWO Contrast

| Layer | IWO / Income Withholding | Project Intercept / Federal Refund Offset |
|---|---|---|
| Payment type | ongoing income stream | annual/lump-sum federal tax refund |
| Actor receiving direction | employer or income payor, including some benefit payors | federal Treasury offset pipeline |
| Trigger | withholding order/notice tied to support order | eligible arrears certified for offset |
| Timing | recurring | seasonal/refund-dependent |
| DEED role | payor-source if UI/paid leave benefits are withheld | not the federal refund offset authority |
| Person-level proof | IWO, payor record, ledger | pre-offset notice, arrears certification, Treasury offset notice, ledger |

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Federal refund offset model is separated from person-level arrears reality. |
| ERS-002 Wrong Vault | PASS | IWO, DEED payor role, and Treasury offset path are not collapsed. |
| ERS-003 Wrong Certificate | PARTIAL | User supplied official source packet; direct URL/hash replay still needed for full four-surface verification. |
| ERS-004 Unknown Waters | DOWNGRADED | Program federal-offset lane clear; individual notices, certifications, and ledger still required. |

## Strict Scope

This artifact does not verify:

- any specific child support order;
- any specific arrears amount;
- any specific public-assistance or family-owed classification;
- any specific pre-offset notice;
- any specific federal tax refund;
- any specific Treasury offset;
- any specific injured spouse claim;
- any specific fee or distribution;
- any agency error;
- any legal conclusion.

## Remaining Four-Surface Requirements

```json
{
  "Minnesota_DCYF_federal_tax_refund_offset_public_url": "REQUIRED_FOR_FULL_REPLAY",
  "federal_TOP_or_OCSS_public_url": "REQUIRED_FOR_FULL_REPLAY",
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
  "assigned_or_family_owed_status": "REQUIRED_FOR_PERSON_LEVEL",
  "pre_offset_notice": "REQUIRED_FOR_PERSON_LEVEL",
  "review_or_challenge_record": "REQUIRED_IF_CONTESTED",
  "Treasury_Notice_of_Offset": "REQUIRED_IF_OFFSET_OCCURRED",
  "refund_hold_or_release_record": "REQUIRED_IF_JOINT_OR_INJURED_SPOUSE",
  "payment_application_record": "REQUIRED_FOR_PERSON_LEVEL"
}
```

## Classification Update

```json
{
  "vector": "federal tax refund offset / Project Intercept lane",
  "classification": "CHILD_SUPPORT_FEDERAL_REFUND_OFFSET_SPINE",
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

1. Attach direct DCYF federal tax refund offset URL and federal TOP/OCSS URL with hashes.
2. Select state Revenue Recapture child support lane for contrast.
3. Select arrears assignment and distribution rules: state-assigned vs family-owed.
4. Select person-level pre-offset notice and arrears ledger packet, if a specific case lane is chosen.

## Closing Receipt

Project Intercept federal refund offset lane indexed.  
It complements IWO but is not the same mechanism.  
DEED remains outside the debt-origin and federal refund offset authority lane.  
Program model holds with caution pending direct URL/hash replay.  
Person-level order, arrears, notice, and offset records remain unverified.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
