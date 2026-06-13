# MNDOR_MEDICAL_DEBT_EXEMPTION_MECHANICS_V0_1

```json
{
  "artifact": "MNDOR_MEDICAL_DEBT_EXEMPTION_MECHANICS_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MNDOR_MEDICAL_DEBT_EXEMPTION_MECHANICS_V0_1.md",
  "parent_artifact": "MNDOR_NONLIABLE_SPOUSE_JOINT_REFUND_MECHANICS_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "medical debt exemption mechanics",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

Hospital and ambulance medical-service debts can enter the MNDOR Revenue Recapture program, but an income-based exemption path exists when the debtor's income at the time of service was at or below the Poverty / Medical Income Guidelines.

This layer answers:

```text
Can medical debt enter the recapture engine?
What protection gate limits it?
What proof remains person-specific?
```

## Source Packet

```json
{
  "public_urls": [
    "https://www.revenue.state.mn.us/debts-medical-services",
    "https://www.revenue.state.mn.us/revenue-recapture-related-information"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "MNDOR_MEDICAL_DEBT_EXEMPTION_PRIORITY_20260613",
  "witness_service_or_replay_surface": "Minnesota Department of Revenue official public website",
  "official_source_type": "MNDOR_PAGE",
  "cross_references": [
    "Minnesota Statutes section 270A.03",
    "Minnesota Rules part 8165.0300",
    "MNDOR debt priority table"
  ]
}
```

## Mechanics Indexed

- Medical-service debts may be submitted through the Revenue Recapture framework by qualifying medical-service claimant agencies.
- Hospital or ambulance debts sit in the priority structure as a distinct debt category.
- Medical-service debts may be exempt from recapture if the debtor's income at the time of service was at or below the applicable Poverty / Medical Income Guidelines.
- Notices for medical-service debts must include exemption-path language.
- Debtor-side exemption review may require tax returns and income-source documentation for the service year.
- Claimant agency review, not vibe, determines the exemption application at the person level.

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Medical-debt model is tied to official program surfaces and rules references. |
| ERS-002 Wrong Vault | PASS | Entry into recapture and exemption qualification are separated. |
| ERS-003 Wrong Certificate | PASS | Medical debt notice/exemption language belongs to the medical-service recapture lane. |
| ERS-004 Unknown Waters | DOWNGRADED | Public exemption path is clear; person-level income qualification requires documents. |

## Strict Scope

This artifact verifies the program-level medical-debt entry and exemption mechanics.

It does not verify:

- any specific hospital or ambulance debt;
- any specific debtor's income;
- any specific service date;
- any specific Poverty / Medical Income Guideline calculation;
- any specific exemption approval or denial;
- any specific agency error;
- any legal conclusion.

## Remaining Person-Level Unknowns

```json
{
  "specific_medical_service_debt": "NOT_PROVIDED",
  "specific_claimant_agency": "NOT_SELECTED",
  "service_date_or_range": "NOT_PROVIDED",
  "debtor_income_at_time_of_service": "NOT_PROVIDED",
  "tax_return_or_income_docs": "NOT_PROVIDED",
  "guideline_table_applied": "NOT_PROVIDED",
  "agency_exemption_determination": "NOT_PROVIDED",
  "recapture_notice_copy": "NOT_PROVIDED"
}
```

## Classification Update

```json
{
  "vector": "medical debt exemption mechanics",
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

1. Specific agency implementation details: DCYF child support, DEED UI overpayments, court/county debts, hospital/ambulance.
2. Healthcare Recapture claim type or sample medical-debt notice/form.
3. Bankruptcy interplay or statute of limitations refinements.
4. Person-level medical-debt notice packet, if a specific case lane is selected.

## Closing Receipt

Medical debt lane indexed with official exemption and priority packet.  
Program entry is allowed at the mechanics layer.  
Income shield exists and requires person-level documentation.  
No person-level promotion.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
