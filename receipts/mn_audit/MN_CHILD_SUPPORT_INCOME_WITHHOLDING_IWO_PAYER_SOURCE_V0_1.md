# MN_CHILD_SUPPORT_INCOME_WITHHOLDING_IWO_PAYER_SOURCE_V0_1

```json
{
  "artifact": "MN_CHILD_SUPPORT_INCOME_WITHHOLDING_IWO_PAYER_SOURCE_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_CHILD_SUPPORT_INCOME_WITHHOLDING_IWO_PAYER_SOURCE_V0_1.md",
  "parent_artifact": "MN_CHILD_SUPPORT_ENFORCEMENT_INTERCEPT_SPINE_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "income withholding official source / IWO form surface",
  "classification": "CHILD_SUPPORT_PAYER_SOURCE_WITHHOLDING_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED_BY_USER",
  "evidence_weight": "HIGH_PROGRAM_LEVEL_PENDING_DIRECT_OFFICIAL_URL_HASH_REPLAY",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

Minnesota uses the federal OMB-approved Income Withholding for Support form and Minnesota child support employer/payor guidance to direct employers and other income payors to withhold support. This creates a payer-source bridge: the payor executes withholding but does not create the underlying child support debt.

This layer answers:

```text
How does child support enforcement reach wages, UI benefits, or other income sources without confusing the payor with the debt-origin authority?
```

## Source Packet Submitted

```json
{
  "primary_surfaces": [
    "Federal Income Withholding for Support form / OMB 0970-0154 via ACF Office of Child Support Services",
    "Minnesota DCYF income withholding support payments page",
    "Employer's Guide to Minnesota Child Support Laws / DHS-3177-ENG",
    "Minnesota Child Support Online employer/case payment surfaces"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "MN_CHILD_SUPPORT_IWO_PAYER_SOURCE_20260613_USER_PACKET",
  "witness_service_or_replay_surface": "User-submitted official-source packet; direct URL/hash replay still required for full four-surface verification",
  "official_source_type": "FEDERAL_IWO_FORM_PLUS_MN_DCYF_EMPLOYER_GUIDANCE"
}
```

## Indexed Payer-Source Rule

```json
{
  "rule": "The IWO or child support withholding notice directs a payor to withhold. The payor does not create the underlying child support debt.",
  "DEED_UI_role": "payer_source_when_UI_or_paid_leave_benefits_are_subject_to withholding",
  "county_or_child_support_agency_role": "issuer_or_enforcement_actor_for_support_order_or_arrears",
  "payment_center_role": "receives_and_processes_withheld_support_payments"
}
```

## Mechanics Indexed

- Income withholding is a primary ongoing child support collection mechanism.
- County child support agencies or authorized child support actors may send IWO/withholding notices to employers or income payors.
- Employers/payors must implement withholding according to timing and remittance rules.
- Payments route to the Minnesota Child Support Payment Center for full-service cases.
- Child support withholding generally has priority over many other garnishments, subject to legal limits.
- Federal CCPA caps and disposable-earnings rules limit the amount that can be withheld.
- DEED, when acting as UI or benefit payor, withholds as source-of-funds actor, not as creator of the child support order or arrears.
- Disputes about support amount, arrears, or order validity route to child support agency/court/hearing paths; disputes about UI eligibility remain separate.

## Indexed Pipeline

```json
{
  "step_1": "child_support_order_or_arrears_exist",
  "step_2": "county_or_child_support_agency_issues_IWO_or_withholding_notice",
  "step_3": "employer_or_payor_receives_withholding_direction",
  "step_4": "payor_withholds_from_income_source_subject_to_limits",
  "step_5": "payor_remits_to_MN_Child_Support_Payment_Center",
  "step_6": "payment_is_applied_to_current_support_arrears_or_related_obligations",
  "step_7": "disputes_route_to_child_support_review_court_or_hearing_path"
}
```

## DEED/UI Boundary

```json
{
  "DEED_as_payor": true,
  "DEED_creates_child_support_debt": false,
  "DEED_sets_child_support_order": false,
  "DEED_correct_for_UI_eligibility_or_benefit_amount_dispute": true,
  "child_support_agency_correct_for_order_arrears_or_withholding_basis_dispute": true
}
```

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | IWO withholding model is separated from person-level order reality. |
| ERS-002 Wrong Vault | PASS | Payor execution is separated from debt-origin authority. |
| ERS-003 Wrong Certificate | PARTIAL | User supplied official source packet; direct URL/hash replay still needed for full four-surface verification. |
| ERS-004 Unknown Waters | DOWNGRADED | Program payer-source lane clear; individual IWO/order/ledger still required. |

## Strict Scope

This artifact does not verify:

- any specific support order;
- any specific IWO;
- any specific employer/payor notice;
- any specific DEED UI withholding;
- any specific arrears amount;
- any specific CCPA cap calculation;
- any specific payment center transaction;
- any agency or payor error;
- any legal conclusion.

## Remaining Four-Surface Requirements

```json
{
  "federal_IWO_public_url": "REQUIRED_FOR_FULL_REPLAY",
  "Minnesota_DCYF_income_withholding_public_url": "REQUIRED_FOR_FULL_REPLAY",
  "DHS_3177_ENG_or_current_employer_guide_public_url": "REQUIRED_FOR_FULL_REPLAY",
  "fetched_at": "REQUIRED_PER_SOURCE",
  "content_hash": "REQUIRED_PER_SOURCE",
  "witness_service_or_replay_surface": "REQUIRED_PER_SOURCE"
}
```

## Person-Level Packet Requirements

```json
{
  "support_order": "REQUIRED_FOR_PERSON_LEVEL",
  "IWO_or_withholding_notice": "REQUIRED_FOR_PERSON_LEVEL",
  "employer_or_payor_identity": "REQUIRED_FOR_PERSON_LEVEL",
  "income_source": "REQUIRED_FOR_PERSON_LEVEL",
  "withholding_amount": "REQUIRED_FOR_PERSON_LEVEL",
  "CCPA_cap_or_limit_calculation": "REQUIRED_IF_AMOUNT_DISPUTED",
  "payment_center_record": "REQUIRED_FOR_PERSON_LEVEL",
  "review_hearing_or_modification_record": "REQUIRED_IF_CONTESTED"
}
```

## Classification Update

```json
{
  "vector": "income withholding official source / IWO form surface",
  "classification": "CHILD_SUPPORT_PAYER_SOURCE_WITHHOLDING_SPINE",
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

1. Attach direct official ACF IWO URL, Minnesota DCYF income withholding URL, and DHS-3177-ENG URL with hashes.
2. Select federal tax refund offset / Project Intercept lane.
3. Select state Revenue Recapture child support lane.
4. Select person-level IWO/order/ledger packet, if a specific case lane is chosen.

## Closing Receipt

Income withholding / IWO payer-source lane indexed.  
DEED and employers are executor/payor surfaces, not debt-origin authorities.  
Program model holds with caution pending direct URL/hash replay.  
Person-level order, arrears, IWO, and payment records remain unverified.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
