# MNDOR_45_DAY_CONTEST_HEARING_MECHANICS_V0_1

```json
{
  "artifact": "MNDOR_45_DAY_CONTEST_HEARING_MECHANICS_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MNDOR_45_DAY_CONTEST_HEARING_MECHANICS_V0_1.md",
  "parent_artifact": "MNDOR_REVENUE_RECAPTURE_SOURCE_PACKET_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "45-day contest/hearing mechanics",
  "classification": "ADMINISTRATIVE_DUE_PROCESS_GATE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

After MNDOR applies or initiates a revenue recapture offset, the claimant agency notice and hearing path is the main public-facing contest mechanism.

Indexed public-rights path:

```text
Offset/recapture action -> claimant agency written notice -> 45-day written hearing request window -> claimant agency/OAH hearing path -> determination/correction path
```

## Strict Scope

This artifact indexes the program/statutory due-process gate.

It does not verify:

- any specific person's offset;
- any specific mailed notice;
- the exact date a specific person received notice;
- any specific hearing request;
- any agency error;
- any legal conclusion.

## Source Packet

```json
{
  "primary_source": "MNDOR Revenue Recapture official page",
  "primary_url": "https://www.revenue.state.mn.us/revenue-recapture",
  "supporting_statute": "Minnesota Revenue Recapture Act",
  "supporting_url": "https://www.revisor.mn.gov/statutes/cite/270A",
  "source_packet_artifact": "MNDOR_REVENUE_RECAPTURE_SOURCE_PACKET_V0_1",
  "fetched_at": "2026-06-13"
}
```

## Key Mechanics Indexed

- Claimant agency must send written notice after filing or triggering the claim path.
- Debtor may contest the validity of the claim by sending a written hearing request to the claimant agency.
- The contest/hearing route is through the claimant agency or designated forum, not by treating MNDOR as the sole debt authority.
- Hearing mechanics sit inside the administrative offset spine and are separate from person-level proof.

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Rights mechanic is tied to program/statute surfaces, not vibes. |
| ERS-002 Wrong Vault | PASS | MNDOR offset function and claimant-agency contest path are separated. |
| ERS-003 Wrong Certificate | PASS | Source packet links the rights mechanism to the administrative spine. |
| ERS-004 Unknown Waters | DOWNGRADED | Public path is clear; individual deployment still requires personal notice packet. |

## Remaining Person-Level Unknowns

```json
{
  "specific_offset_notice": "NOT_PROVIDED",
  "mailing_or_receipt_date": "NOT_PROVIDED",
  "claimant_agency_name": "NOT_SELECTED",
  "certified_debt_basis": "NOT_PROVIDED",
  "written_hearing_request": "NOT_PROVIDED",
  "hearing_scheduling_record": "NOT_PROVIDED",
  "final_determination": "NOT_PROVIDED"
}
```

## Classification Update

```json
{
  "vector": "45-day contest/hearing mechanics",
  "classification": "ADMINISTRATIVE_DUE_PROCESS_GATE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "promotion_allowed": "PROGRAM_LEVEL_ONLY",
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Next Lawful Surfaces

1. Sample claimant-agency notice language or form.
2. Debt priority order and qualifying payments.
3. Specific claimant agency process: DCYF, DEED, county, court, or hospital.
4. Nonliable spouse or exemption rules.
5. Person-level notice packet, if the auditor chooses a specific case lane.

## Closing Receipt

The 45-day contest/hearing gate is indexed.  
The public rights path is strong at program level.  
Individual deployment remains unverified until a specific notice packet exists.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
