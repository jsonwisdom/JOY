# MNDOR_REVENUE_RECAPTURE_SOURCE_PACKET_V0_1

```json
{
  "artifact": "MNDOR_REVENUE_RECAPTURE_SOURCE_PACKET_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MNDOR_REVENUE_RECAPTURE_SOURCE_PACKET_V0_1.md",
  "parent_artifact": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "MNDOR Revenue Recapture claimant-agency certification",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Official Source Packet

```json
{
  "public_url": "https://www.revenue.state.mn.us/revenue-recapture",
  "fetched_at": "2026-06-13",
  "content_hash": "MNDOR_PRIMARY_RECAPTURE_PAGE_20260613",
  "witness_service_or_replay_surface": "Minnesota Department of Revenue official public website (revenue.state.mn.us)",
  "official_source_type": "MNDOR_PAGE"
}
```

## Supporting Statute Surface

```json
{
  "public_url": "https://www.revisor.mn.gov/statutes/cite/270A",
  "official_source_type": "REVISOR_STATUTE",
  "scope": "Revenue Recapture Act / setoff procedure / notice and hearing / priority of claims"
}
```

## Key Extracted Claims From Source Surface

- The Revenue Recapture program allows the Minnesota Department of Revenue to recapture individual tax refunds or other payments and apply them to debts collected for other agencies or the federal government.
- The program links to Minn. Stat. § 270A.03 and § 270C.41.
- Claimant agencies submit certified claims.
- Debtor notice and contest/hearing mechanics are tied to the claimant agency pathway.
- Only qualifying agencies and authorized agency employees participate; third-party collectors are not treated as direct claimant-agency submitters in this packet.

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Program model is now tied to official MNDOR and statute surfaces. |
| ERS-002 Wrong Vault | PASS | Deployment spine is confirmed at program level; individual deployment packet remains separate. |
| ERS-003 Wrong Certificate | PASS | Statutory authority and claimant-certification flow are linked at program level. |
| ERS-004 Unknown Waters | DOWNGRADED | Granular person-level proof still requires an individual notice, claim packet, or agency records. |

## Classification Update

```json
{
  "vector": "MNDOR Revenue Recapture claimant-agency certification",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Remaining Unknowns

```json
{
  "specific_person_case": "NOT_PROVIDED",
  "specific_claimant_agency_certification": "NOT_PROVIDED",
  "specific_notice": "NOT_PROVIDED",
  "specific_debt_priority_application": "NOT_PROVIDED",
  "specific_45_day_hearing_timeline": "NOT_PROVIDED"
}
```

## Closing Receipt

Spine indexed and source packet attached.  
Model holds at program/statutory level.  
No person-level promotion.  
No authority asserted.  
No fake green.
