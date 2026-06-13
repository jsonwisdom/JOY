# DEED_UI_OVERPAYMENTS_RECAPTURE_IMPLEMENTATION_V0_1

```json
{
  "artifact": "DEED_UI_OVERPAYMENTS_RECAPTURE_IMPLEMENTATION_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/DEED_UI_OVERPAYMENTS_RECAPTURE_IMPLEMENTATION_V0_1.md",
  "parent_artifact": "MNDOR_MEDICAL_DEBT_EXEMPTION_MECHANICS_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "DEED UI overpayments implementation details",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "agency": "Minnesota Department of Employment and Economic Development / Unemployment Insurance",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

DEED UI overpayments can operate as a claimant-agency implementation layer inside the MNDOR Revenue Recapture spine. The operational sequence can include overpayment determination, notice/repayment process, benefit deductions, certification or referral for recapture, MNDOR offset of qualifying payments, and correction or appeal records.

This layer answers:

```text
How does the MNDOR offset spine connect to a specific claimant agency: DEED UI?
```

## Source Packet

```json
{
  "public_urls": [
    "https://www.uimn.org/applicants/needtoknow/fraud/benefit-overpayments.jsp",
    "https://www.revenue.state.mn.us/revenue-recapture"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "DEED_UI_OVERPAYMENT_MNDOR_RECAPTURE_20260613",
  "witness_service_or_replay_surface": "DEED UI official site plus MNDOR official site",
  "official_source_type": "DEED_PAGE_PLUS_MNDOR_PAGE"
}
```

## Mechanics Indexed

- DEED UI overpayments may arise from eligibility issues, earnings reporting issues, audits, appeals, or related unemployment-insurance determinations.
- Non-fraud and fraud/misrepresentation overpayments should remain separated as classifications.
- Repayment tools may include repayment plans, future benefit deductions, and Revenue Recapture offsets where applicable.
- The MNDOR recapture spine remains a collection/offset mechanism; DEED remains the claimant-agency source for UI debt basis and correction records.
- Individual correction/audit packets remain person-level and are not verified by program pages alone.

## Indexed Pipeline

```json
{
  "step_1": "DEED_UI_overpayment_determination",
  "step_2": "notice_of_overpayment_or_debt_and_repayment_options",
  "step_3": "benefit_deduction_or_collection_path",
  "step_4": "claimant_agency_certification_or_referral_to_revenue_recapture_if_applicable",
  "step_5": "MNDOR_match_and_offset_of_qualifying_refunds_or_payments",
  "step_6": "standard_notice_contest_or_correction_path",
  "step_7": "DEED_records_needed_for_person_level_replay"
}
```

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | DEED UI program mechanics are separated from individual case reality. |
| ERS-002 Wrong Vault | PASS | DEED debt basis and MNDOR collection mechanism are not collapsed. |
| ERS-003 Wrong Certificate | PASS | DEED/MNDOR source packet belongs to the UI overpayment recapture lane. |
| ERS-004 Unknown Waters | DOWNGRADED | Public flow is clear; person-level correction/audit packet still required. |

## Strict Scope

This artifact verifies a program-level DEED UI implementation layer.

It does not verify:

- any specific person's UI overpayment;
- any specific fraud or misrepresentation finding;
- any specific debt amount;
- any specific DEED notice;
- any specific certification to MNDOR;
- any specific offset;
- any specific correction request or appeal;
- any agency error;
- any legal conclusion.

## Remaining Person-Level Unknowns

```json
{
  "specific_overpayment_determination": "NOT_PROVIDED",
  "specific_notice_date": "NOT_PROVIDED",
  "specific_debt_amount": "NOT_PROVIDED",
  "fraud_or_nonfraud_classification": "NOT_PROVIDED",
  "benefit_deduction_rate": "NOT_PROVIDED",
  "MNDOR_certification_or_referral_record": "NOT_PROVIDED",
  "specific_offset_notice": "NOT_PROVIDED",
  "appeal_or_correction_record": "NOT_PROVIDED"
}
```

## Classification Update

```json
{
  "vector": "DEED UI overpayments implementation details",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "promotion_allowed": "PROGRAM_LEVEL_ONLY",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Next Lawful Surfaces

1. DEED-specific notice sample or overpayment appeal/correction process.
2. DCYF child support implementation details for contrast.
3. Bankruptcy or statute-of-limitations interplay with UI recapture.
4. Person-level DEED overpayment and MNDOR offset packet, if a specific case lane is selected.

## Closing Receipt

DEED UI lane indexed with official source packet.  
Program implementation bridge holds.  
Specific overpayment, fraud label, certification, and correction records remain person-level.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
