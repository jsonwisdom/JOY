# MN_SCHOOL_PAYMENT_INFRASTRUCTURE_VENDOR_CHAIN_AUDIT_V0_1

```json
{
  "artifact": "MN_SCHOOL_PAYMENT_INFRASTRUCTURE_VENDOR_CHAIN_AUDIT_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_SCHOOL_PAYMENT_INFRASTRUCTURE_VENDOR_CHAIN_AUDIT_V0_1.md",
  "parent_context": "MN_SCHOOL_DEVICE_MDM_CHILD_SAFETY_VENDOR_AUDIT_V0_1",
  "lane": "MN_AUDIT",
  "vector": "Minnesota school payment infrastructure / cafeteria terminals / online lunch pre-pay / activity fees",
  "classification": "SCHOOL_PAYMENT_INFRASTRUCTURE_VENDOR_CHAIN_AUDIT",
  "state": "CLAIM_INDEXED_SOURCE_PACKET_PENDING",
  "kid_protective": true,
  "fraud_claim": false,
  "foreign_claim_verified": false,
  "security_incident_claim": false,
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

Minnesota school payment infrastructure may include cafeteria point-of-sale terminals, online meal pre-payment portals, activity-fee portals, card terminals, ACH/payment processors, gateways, acquirers, convenience-fee structures, and subcontractor/vendor chains.

This audit asks:

```text
Who processes school-related payments, what data path is used, what fees apply, and whether any vendor-chain or foreign-exposure issues exist.
```

This is not a fraud finding.  
This is not a foreign-control finding.  
This is not a child-safety incident finding.

## Kid-Protective Boundary

Any audit must avoid disrupting:

- meal access;
- free or reduced-price meal access;
- student dignity;
- parent/student privacy;
- school operations needed to feed kids.

The audit target is vendor-chain transparency, not stigma or disruption.

## Submitted Framework Summary

The user-submitted packet claims:

- school payment systems commonly use hosted or redirected payment models;
- PCI compliance and minimizing district-held card data are key controls;
- PaySchools, MySchoolBucks, LINQ Connect, SchoolCafe, or similar platforms may appear in Minnesota school contexts;
- U.S. Bank / Elavon or similar acquirers may sit in backend payment-processing lanes;
- schools should preserve fee-free payment options for school meals where applicable;
- specific district contracts and receipts are required before vendor-specific conclusions.

This packet is indexed as source-packet pending until direct official URLs, contracts, hashes, and replay surfaces are attached.

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | HOLD | Seeing a cafeteria terminal or online portal does not prove foreign control, fraud, or data exposure. |
| ERS-002 Wrong Vault | HOLD | Processor/gateway/vendor role is separate from school district, meal program, and public-funding authority. |
| ERS-003 Wrong Certificate | ACTIVE | Need receipt, portal terms, district contract, terminal label, procurement record, PCI artifact, or data-flow document. |
| ERS-004 Unknown Waters | ACTIVE | Vendor ownership, data routing, acquirer, telecom, fees, subsidies, and subcontractors remain unmapped. |

## One-School Observation Template

```json
{
  "school_building": "Full name and address",
  "counter_or_office": "Cafeteria POS | Activities Office | Online Portal | Other",
  "receipt_merchant_name": "Exact merchant name or DBA from receipt or portal",
  "terminal_brand_model": "Visible brand/model only if lawful to observe",
  "processor_or_acquirer": "Shown on receipt, portal, or posted notice if visible",
  "connection_type": "Ethernet | Cellular | Dial-up | WiFi | Hosted redirect | Unknown",
  "fee_line": "Convenience/service/merchant fee amount or percent; note if district subsidized",
  "date_time": "Observation timestamp",
  "payment_context": "Lunch pre-pay | activity fee | exam fee | device fee | other",
  "notes": "Powered-by marks, terms, routing clues, posted fee-free options",
  "photo_or_receipt": "Yes/No; lawful public capture only"
}
```

## Vendor Chain to Map

```json
{
  "district_or_school": "UNKNOWN",
  "payment_portal": "UNKNOWN",
  "cafeteria_POS_vendor": "UNKNOWN",
  "merchant_of_record": "UNKNOWN",
  "processor": "UNKNOWN",
  "acquirer_or_bank": "UNKNOWN",
  "gateway": "UNKNOWN",
  "terminal_vendor": "UNKNOWN",
  "terminal_maintenance_vendor": "UNKNOWN",
  "telecom_or_network_carrier": "UNKNOWN",
  "fee_structure": "UNKNOWN",
  "district_fee_subsidy": "UNKNOWN",
  "PCI_attestation": "UNKNOWN",
  "foreign_ownership_or_control_disclosure": "UNKNOWN",
  "subcontractor_chain": "UNKNOWN"
}
```

## Formal Records Request Targets

1. Merchant services and payment-processing contracts for school meals, fees, and activity payments.
2. Payment processor, gateway, acquirer, merchant of record, and fee schedule.
3. Cafeteria POS vendor, online meal-payment vendor, terminal vendor, supplier, and maintenance contractor.
4. Telecom/network carrier for in-person terminals, if applicable.
5. Latest PCI-DSS compliance attestation, SAQ/ROC, or equivalent vendor security statement.
6. Payment data-flow diagram or routing description, including hosted/redirected model details.
7. Convenience-fee policy and district subsidy/fee-free payment option policy.
8. Foreign ownership/control disclosures, subcontractor lists, and data-processing addenda.
9. Procurement bid, award, RFP, contract number, board approval, and amendments.

## Required Source Packet for Promotion

```json
{
  "district_payment_portal_public_url": "REQUIRED",
  "district_or_school_contract_record": "REQUIRED",
  "vendor_terms_or_service_document": "REQUIRED",
  "receipt_or_portal_screenshot": "REQUIRED_FOR_ONE_PAYMENT_TRACE",
  "PCI_or_security_artifact": "REQUIRED_FOR_DATA_RISK_CLAIM",
  "foreign_ownership_disclosure": "REQUIRED_FOR_FOREIGN_EXPOSURE_CLAIM",
  "fee_free_option_policy": "REQUIRED_FOR_MEAL_ACCESS_CLAIM",
  "fetched_at": "REQUIRED_PER_SOURCE",
  "content_hash": "REQUIRED_PER_SOURCE",
  "witness_service_or_replay_surface": "REQUIRED_PER_SOURCE"
}
```

## Classification Update

```json
{
  "vector": "Minnesota school payment infrastructure vendor-chain audit",
  "classification": "SCHOOL_PAYMENT_INFRASTRUCTURE_VENDOR_CHAIN_AUDIT",
  "state": "CLAIM_INDEXED_SOURCE_PACKET_PENDING",
  "evidence_weight": "MEDIUM_FRAMEWORK_LOW_DISTRICT_SPECIFIC_TRACE",
  "promotion_allowed": false,
  "kid_protective": true,
  "fraud_claim": false,
  "foreign_claim_verified": false,
  "security_incident_claim": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Next Lawful Surfaces

1. Specific school/district payment portal URL.
2. PaySchools / MSBA source packet or district contract, if selected.
3. MySchoolBucks, LINQ Connect, SchoolCafe, or other portal source packet, if selected.
4. One receipt or payment screen showing merchant name, fee, and processor clues.
5. District public-records request for contracts, PCI, data flow, fee policy, and subcontractors.

## Closing Receipt

School payment infrastructure vector indexed.  
Foreign exposure is not proven.  
Fraud is not claimed.  
Vendor chain must be mapped by district, contract, receipt, and data-flow evidence.  
Audit remains kid-protective, evidence-driven, and cold.

Not fraud until proven.  
Not foreign until traced.  
Not a student-risk finding without evidence.  
Do not disrupt meals.
