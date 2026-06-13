# DEED_UI_OVERPAYMENT_NOTICE_APPEAL_CORRECTION_V0_1

```json
{
  "artifact": "DEED_UI_OVERPAYMENT_NOTICE_APPEAL_CORRECTION_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/DEED_UI_OVERPAYMENT_NOTICE_APPEAL_CORRECTION_V0_1.md",
  "parent_artifact": "DEED_UI_OVERPAYMENTS_RECAPTURE_IMPLEMENTATION_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "DEED-specific notice sample or overpayment appeal/correction process",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "agency": "Minnesota DEED / Unemployment Insurance",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

DEED issues unemployment-insurance overpayment determinations or related notices that describe the overpayment amount, affected period, reason, repayment responsibility, and appeal or correction path. Timely appeal can trigger a hearing before an Unemployment Law Judge. Successful appeal or correction may reduce, reverse, or otherwise change the debt before or alongside later collection activity.

This layer answers:

```text
What is the DEED paper trail between overpayment determination and possible MNDOR recapture?
```

## Source Packet

```json
{
  "public_urls": [
    "https://www.uimn.org/applicants/needtoknow/fraud/benefit-overpayments.jsp",
    "https://www.uimn.org/applicants/howappeal/index.jsp",
    "https://www.uimn.org/applicants/howappeal/appeal/instructions-for-filing.jsp"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "DEED_UI_OVERPAYMENT_NOTICE_APPEAL_20260613",
  "witness_service_or_replay_surface": "Official DEED/UI Minnesota websites (uimn.org)",
  "official_source_type": "DEED_PAGE"
}
```

## Mechanics Indexed

- DEED overpayment determinations may state amount, reason, affected weeks or period, repayment responsibility, and appeal instructions.
- Appeal deadline is controlled by the notice and official appeal process; this packet indexes the public process, not a specific deadline for any person.
- A timely appeal can trigger a hearing before an Unemployment Law Judge, commonly handled by phone.
- Fraud or misrepresentation classifications must remain separate from non-fraud overpayment classification.
- Billing, repayment, benefit deductions, and potential MNDOR recapture are collection layers that do not themselves prove the underlying debt is correct.
- Correction requires person-level records, evidence, appeal materials, or agency communication.

## Indexed Pipeline

```json
{
  "step_1": "DEED_overpayment_determination_or_notice",
  "step_2": "notice_describes_amount_reason_period_and_appeal_rights",
  "step_3": "claimant_files_appeal_or_correction_materials_if_disputed",
  "step_4": "Unemployment_Law_Judge_hearing_or_agency_review_path",
  "step_5": "determination_affirmed_reversed_modified_or_corrected",
  "step_6": "repayment_benefit_deduction_or_recapture_path_continues_if_debt_remains",
  "step_7": "MNDOR_revenue_recapture_possible_if_certified_or_referred"
}
```

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | DEED paper-trail model is separated from individual case reality. |
| ERS-002 Wrong Vault | PASS | Determination, appeal, collection, and MNDOR recapture are not collapsed. |
| ERS-003 Wrong Certificate | PASS | DEED source packet belongs to the UI notice/appeal/correction lane. |
| ERS-004 Unknown Waters | DOWNGRADED | Public flow clear; individual determination and correction packet still required. |

## Strict Scope

This artifact verifies a program-level DEED notice, appeal, and correction process.

It does not verify:

- any specific person's overpayment;
- any specific determination letter;
- any specific appeal deadline;
- any specific fraud or non-fraud classification;
- any specific hearing result;
- any specific MNDOR certification;
- any specific offset;
- any agency error;
- any legal conclusion.

## Remaining Person-Level Unknowns

```json
{
  "specific_DEED_determination": "NOT_PROVIDED",
  "specific_mail_or_send_date": "NOT_PROVIDED",
  "specific_appeal_deadline": "NOT_PROVIDED",
  "affected_weeks_or_period": "NOT_PROVIDED",
  "debt_amount": "NOT_PROVIDED",
  "reason_for_overpayment": "NOT_PROVIDED",
  "fraud_or_nonfraud_classification": "NOT_PROVIDED",
  "appeal_filing_record": "NOT_PROVIDED",
  "ULJ_hearing_record": "NOT_PROVIDED",
  "corrected_determination": "NOT_PROVIDED",
  "MNDOR_certification_or_offset_record": "NOT_PROVIDED"
}
```

## Classification Update

```json
{
  "vector": "DEED-specific notice sample or overpayment appeal/correction process",
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

1. DCYF child support implementation details for contrast.
2. DEED waiver or repayment plan options.
3. Bankruptcy or statute-of-limitations interplay with UI overpayments.
4. Person-level DEED determination, appeal, correction, and MNDOR offset packet, if a specific case lane is selected.

## Closing Receipt

DEED notice to appeal/correction lane indexed with official source packet.  
Program paper trail holds.  
Person-level overpayment, appeal, correction, and certification remain unverified.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
