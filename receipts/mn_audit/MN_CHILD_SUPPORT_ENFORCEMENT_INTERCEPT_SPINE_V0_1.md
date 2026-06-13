# MN_CHILD_SUPPORT_ENFORCEMENT_INTERCEPT_SPINE_V0_1

```json
{
  "artifact": "MN_CHILD_SUPPORT_ENFORCEMENT_INTERCEPT_SPINE_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_CHILD_SUPPORT_ENFORCEMENT_INTERCEPT_SPINE_V0_1.md",
  "parent_artifact": "DCYF_CHILD_SUPPORT_IMPLEMENTATION_CONTRAST_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "Minnesota child support enforcement / tax intercept / income withholding source packet",
  "classification": "CHILD_SUPPORT_ENFORCEMENT_AND_INTERCEPT_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED_BY_USER",
  "evidence_weight": "HIGH_PROGRAM_LEVEL_PENDING_DIRECT_OFFICIAL_URL_HASH_REPLAY",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

Minnesota child support enforcement operates through a statewide child support framework involving DCYF, county agencies, Tribal agencies, courts, payment processing, income withholding, tax refund intercepts, arrears handling, and review/hearing pathways.

This source packet turns the prior DCYF contrast into a Minnesota-specific enforcement spine while preserving the boundary between program mechanics and person-level proof.

## Indexed Minnesota Spine

```json
{
  "program_supervision": "Minnesota DCYF Child Support Division / statewide child support program",
  "implementation_partners": ["counties", "Tribal agencies", "courts", "employers/payors", "payment center"],
  "collection_tools": [
    "income withholding",
    "state tax refund offset / Revenue Recapture",
    "federal tax refund offset / Treasury intercept",
    "license suspension",
    "credit reporting",
    "passport denial",
    "bank levies / FIDM",
    "contempt or court enforcement where applicable"
  ],
  "program_boundary": "program-level only; no person-level arrears verified"
}
```

## Federal Tax Refund Offset / Project Intercept Layer

Indexed mechanics from submitted packet:

- arrears thresholds can determine federal tax refund offset eligibility;
- notices and review rights are part of the process;
- joint refund/injured spouse handling may affect release timing;
- public-assistance/state-assigned arrears and family-owed arrears may route differently;
- person-level eligibility requires an arrears ledger, order, assignment status, and notice packet.

## State Tax Refund Offset / Revenue Recapture Layer

Indexed mechanics from submitted packet:

- child support arrears can connect to Minnesota Revenue Recapture;
- state income tax refunds, property tax refunds, renter credits, lottery winnings, and other qualifying streams may be implicated by the broader MNDOR spine;
- child support sits high in the MNDOR priority order already indexed in `MNDOR_DEBT_PRIORITY_QUALIFYING_PAYMENTS_V0_1`;
- the Revenue Recapture notice/hearing path remains part of the administrative spine.

## Income Withholding Layer

Indexed mechanics from submitted packet:

- income withholding is a primary ongoing collection tool;
- employers and payors may receive income withholding orders;
- wages, UI benefits, and other payment sources may be affected depending on order and source rules;
- funds route through the Minnesota Child Support Payment Center for full-service cases;
- disputes about the support order, arrears, or withholding basis route through child support review/hearing/modification paths, not by assuming the payor agency created the debt.

## DEED Contrast

```json
{
  "DEED_role": "payer/source agency for UI withholding and claimant agency for UI overpayments, depending on lane",
  "child_support_role": "DCYF/county/Tribal/court framework creates or enforces support obligations and arrears",
  "boundary": "DEED may withhold from UI under support orders but does not create the underlying child support arrears"
}
```

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Minnesota child-support enforcement model is separated from Washington comparison and person-level reality. |
| ERS-002 Wrong Vault | PASS | DCYF/county/Tribal enforcement, DEED payor role, and MNDOR offset mechanics are separated. |
| ERS-003 Wrong Certificate | PARTIAL | Source packet submitted; direct official URLs/hashes/replay surfaces still should be attached for full four-surface verification. |
| ERS-004 Unknown Waters | DOWNGRADED | Program spine clear; individual order, arrears, notice, and payment records remain person-level. |

## Strict Scope

This artifact does not verify:

- any specific child support order;
- any specific arrears ledger;
- any specific foster-care or public-assistance assignment;
- any specific state or federal tax intercept;
- any specific income withholding order;
- any specific DEED UI withholding;
- any specific county, Tribal, court, or DCYF action;
- any agency error;
- any legal conclusion.

## Remaining Source Packet Requirements

```json
{
  "Minnesota_DCYF_child_support_public_url": "STILL_REQUIRED_FOR_FULL_REPLAY",
  "Minnesota_child_support_enforcement_public_url": "STILL_REQUIRED_FOR_FULL_REPLAY",
  "federal_offset_or_Project_Intercept_public_url": "STILL_REQUIRED_FOR_FULL_REPLAY",
  "income_withholding_public_url_or_form": "STILL_REQUIRED_FOR_FULL_REPLAY",
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
  "assigned_or_unassigned_arrears_status": "REQUIRED_FOR_PERSON_LEVEL",
  "notice_of_intercept_or_income_withholding": "REQUIRED_FOR_PERSON_LEVEL",
  "payment_center_record": "REQUIRED_FOR_PERSON_LEVEL",
  "hearing_review_or_modification_record": "REQUIRED_FOR_PERSON_LEVEL"
}
```

## Classification Update

```json
{
  "vector": "Minnesota child support enforcement / tax intercept / income withholding source packet",
  "classification": "CHILD_SUPPORT_ENFORCEMENT_AND_INTERCEPT_SPINE",
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

1. Attach direct official Minnesota DCYF Child Support program URLs and hashes.
2. Attach Project Intercept / federal tax refund offset official source surface.
3. Attach income withholding official source or IWO form surface.
4. Select a narrower lane: state tax offset, federal tax offset, income withholding, or foster/public assistance arrears.
5. Person-level order, arrears ledger, and notice packet, if a specific case lane is selected.

## Closing Receipt

Minnesota child support enforcement spine indexed.  
DCYF contrast now has a Minnesota framework.  
Direct official URL/hash replay packet still needed for full four-surface verification.  
Person-level arrears and intercept records remain unverified.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
