# MN_DISTRICT_PACKET_ISD_742_V0_1

```json
{
  "artifact": "MN_DISTRICT_PACKET_ISD_742_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_DISTRICT_PACKET_ISD_742_V0_1.md",
  "parent_artifact": "MN_DATA_AND_PRIVACY_LANE_V0_1",
  "gate": "PROTECT_CHILDREN_FROM_AI_SYSTEMS_JAYWISDOM_GATE_V0_1",
  "lane": "MN_AUDIT",
  "operator": "Jay Wisdom",
  "identity_surface": "jaywisdom.base.eth",
  "district_focus": "St. Cloud Area Schools / ISD 742",
  "classification": "MINNESOTA_SCHOOL_MEAL_GOVERNANCE_SURFACE",
  "state": "DISTRICT_PACKET_DRAFT_SOURCE_PACKET_PENDING",
  "authority": false,
  "green_implied": false,
  "no_fake_green": true,
  "kid_protective": true,
  "vendor_chain_verified": false,
  "privacy_notice_verified": false,
  "contract_verified": false,
  "fee_data_flow_verified": false,
  "fraud_claim": false,
  "foreign_exposure_verified": false
}
```

## Purpose

This artifact creates a district-specific packet template for St. Cloud Area Schools / ISD 742.

It is a lawful public-records target and replay surface, not a verified finding.

## Clean Boundary

```text
Specific district selected.
Specific claims not promoted.
Vendor chain not verified until source packet attached.
Privacy notice not verified until source packet attached.
Contract not verified until produced or cited.
Fee/data-flow trail not verified until receipt or portal observation exists.
```

## District Identity Surface

```json
{
  "district": "St. Cloud Area Schools / ISD 742",
  "region": "St. Cloud area, Minnesota",
  "meal_governance_context": "Minnesota school meal governance frame",
  "state": "PUBLIC_TARGET_SELECTED_SOURCE_PACKET_PENDING"
}
```

## Five-Lane Mapping

```json
{
  "lane_1_meal_rights": {
    "question": "Does the district preserve universal meal access and fee-free meal access?",
    "source_needed": "district meal program page, MDE program source, student meal access policy"
  },
  "lane_2_payment_systems": {
    "question": "What payment portal or POS systems are used for optional prepay, a la carte, or fees?",
    "source_needed": "district payment portal page, receipt, contract, fee schedule"
  },
  "lane_3_vendor_chains": {
    "question": "Who are the platform, processor, gateway, acquirer, POS, and subcontractors?",
    "source_needed": "contract, procurement record, subprocessor list, PCI/security document"
  },
  "lane_4_food_quality": {
    "question": "What menu, service, complaint, nutrition, and vendor records document meal quality?",
    "source_needed": "menus, nutrition compliance records, food service contract, complaint process"
  },
  "lane_5_data_privacy": {
    "question": "What student, parent, payment, meal, allergy, portal, and metadata are collected and retained?",
    "source_needed": "privacy notices, data processing addendum, retention schedule, data-flow map"
  }
}
```

## Four Anchors

### A. One Real Portal

Target surface:

```json
{
  "portal_target": "district meal/payment portal",
  "platform_claim": "PaySchools Central or actual district-listed provider",
  "status": "UNVERIFIED_UNTIL_DISTRICT_PORTAL_SOURCE_ATTACHED",
  "audit_targets": [
    "merchant DBA on receipt",
    "fee schedule",
    "data retention policy",
    "subprocessor list",
    "PCI attestation"
  ]
}
```

### B. One Privacy Notice

Target surfaces:

```json
{
  "district_privacy_notice": "REQUIRED",
  "vendor_privacy_notice": "REQUIRED_IF_PORTAL_VENDOR_IDENTIFIED",
  "topics": [
    "FERPA",
    "directory information",
    "student data handling",
    "third-party vendors",
    "parent rights to inspect records",
    "payment data",
    "device/browser metadata",
    "cookies or analytics",
    "retention and deletion",
    "PCI/payment security"
  ]
}
```

### C. One Contract Target

Records request target:

```json
{
  "recipient": "ISD 742 Business Services / Food Service Director / Data Practices Officer",
  "requested_records": [
    "meal payment platform contract",
    "fee split or fee schedule",
    "PCI attestation or payment security validation",
    "data-flow diagram",
    "foreign ownership or control disclosures",
    "third-party delivery policy",
    "data processing addendum",
    "subprocessor list",
    "retention and deletion schedule"
  ]
}
```

### D. One Fee / Data-Flow Trail

```json
{
  "district": "St. Cloud Area Schools ISD 742",
  "school": "Specific building observed",
  "portal": "Actual district-listed portal",
  "merchant_dba": "Exact printed DBA from receipt or screen",
  "fee": {
    "amount": "Exact dollar or percent",
    "type": "convenience | merchant | card surcharge | none | unknown",
    "fee_free_option": "cash/check/other if visible or documented"
  },
  "processor_chain": "platform -> processor -> gateway -> acquirer, if visible or produced",
  "data_flow": {
    "student_id": "true/false/unknown",
    "parent_email": "true/false/unknown",
    "transaction_logs": "true/false/unknown",
    "device_metadata": "true/false/unknown",
    "allergy_info": "true/false/unknown",
    "retention": "from privacy notice or contract"
  },
  "timestamp": "ISO8601",
  "evidence": "receipt | screenshot | contract | none"
}
```

## ERS Replay

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | HOLD | Selecting ISD 742 does not verify portal, vendor, fee, food quality, or privacy facts. |
| ERS-002 Wrong Vault | PASS | Meal rights, payment convenience, vendor chain, food quality, and data/privacy remain separate lanes. |
| ERS-003 Wrong Certificate | ACTIVE | Need portal source, privacy notice, contract, receipt, fee schedule, or data-flow map. |
| ERS-004 Unknown Waters | ACTIVE | Actual vendor chain, processor, retention, subprocessors, and fee trail remain unmapped. |

## Public Records Draft Skeleton

```text
To: ISD 742 Data Practices Officer / Business Services / Food Service Director

I request public data regarding the district's school meal payment, cafeteria POS, online payment, and related student data systems.

Please provide:
1. current meal payment platform contract and amendments;
2. fee schedule, fee split, and district subsidy policy for card or online payments;
3. payment processor, gateway, acquirer, merchant-of-record, and POS vendor names;
4. PCI-DSS validation, SAQ/ROC summary, or vendor security attestation;
5. privacy notices, data processing addenda, and subprocessor lists;
6. data-flow diagram or written routing description for parent portal -> processor -> district/POS/SIS;
7. data retention and deletion schedules for meal account, transaction, balance, allergy, and portal data;
8. student meal access policy and fee-free payment options;
9. third-party delivery or outside-food policy, if any;
10. procurement records, board approval, RFP, bid, award, or renewal records for the payment platform and cafeteria POS system.

Please provide records electronically if available.
```

## Strict Scope

This artifact does not verify:

- ISD 742's actual current payment vendor;
- PaySchools usage;
- any fee amount;
- any food quality claim;
- any data misuse;
- any foreign exposure;
- any vendor misconduct;
- any child-safety incident;
- any legal conclusion.

## Classification Update

```json
{
  "artifact": "MN_DISTRICT_PACKET_ISD_742_V0_1",
  "classification": "MINNESOTA_SCHOOL_MEAL_GOVERNANCE_SURFACE",
  "state": "DISTRICT_PACKET_DRAFT_SOURCE_PACKET_PENDING",
  "promotion_allowed": false,
  "kid_protective": true,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Closing Receipt

ISD 742 district packet drafted.  
One district selected.  
Four anchors defined: portal, privacy notice, contract target, fee/data-flow trail.  
No claims promoted until source packet arrives.

Children protected.  
Evidence preserved.  
Audit cold.  
JAYWISDOM Gate holds.  
Receipts decide.
