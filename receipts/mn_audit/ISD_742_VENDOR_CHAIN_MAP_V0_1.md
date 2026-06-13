# ISD_742_VENDOR_CHAIN_MAP_V0_1

```json
{
  "artifact": "ISD_742_VENDOR_CHAIN_MAP_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/ISD_742_VENDOR_CHAIN_MAP_V0_1.md",
  "parent_artifact": "MN_MEAL_FINANCE_CHAIN_V0_1",
  "district_packet": "MN_DISTRICT_PACKET_ISD_742_V0_1",
  "gate": "PROTECT_CHILDREN_FROM_AI_SYSTEMS_JAYWISDOM_GATE_V0_1",
  "lane": "MN_AUDIT",
  "operator": "Jay Wisdom",
  "identity_surface": "jaywisdom.base.eth",
  "district": "St. Cloud Area Schools / ISD 742",
  "classification": "MINNESOTA_SCHOOL_MEAL_VENDOR_CHAIN",
  "state": "DISTRICT_VENDOR_CHAIN_MAP_INDEXED_SOURCE_PACKET_PENDING",
  "authority": false,
  "green_implied": false,
  "no_fake_green": true,
  "kid_protective": true,
  "vendor_chain_verified": false,
  "portal_verified": false,
  "POS_verified": false,
  "processor_verified": false,
  "gateway_verified": false,
  "acquirer_verified": false,
  "subprocessor_verified": false,
  "data_retention_verified": false,
  "fraud_claim": false,
  "foreign_exposure_verified": false
}
```

## Core Rule

```text
District -> Portal -> POS -> Processor -> Gateway -> Acquirer -> Subprocessors -> Data Retention.
Each hop is separate.
No hop inherits authority.
No hop can deny meals.
Only receipts, contracts, and data-flow maps promote claims.
```

## 0. District: ISD 742

Lane: Meal Rights + Vendor Chains

The district is the public governance surface for:

- meal access;
- procurement;
- student-data obligations;
- policy enforcement;
- vendor oversight.

The district does not automatically own or control:

- card processing;
- card networks;
- hosted payment infrastructure;
- cloud hosting;
- subprocessor chains;
- vendor retention policies.

District artifacts to request:

- payment platform contract;
- vendor list;
- data-sharing agreements;
- third-party delivery or outside-food policy;
- procurement records;
- board approval or renewal records.

## 1. Portal: Payment Convenience Layer

Lane: Payment Systems + Data & Privacy

Target portal claim:

```json
{
  "portal_candidate": "PaySchools Central or actual ISD 742-listed provider",
  "status": "UNVERIFIED_UNTIL_DISTRICT_PORTAL_SOURCE_OR_RECEIPT_ATTACHED"
}
```

Portal may support:

- parent/guardian login;
- student lookup;
- account balance view;
- a la carte deposits;
- activity fees;
- lunch account prepay where applicable;
- recurring payments.

Portal may collect:

- parent email;
- student ID;
- device/browser metadata;
- transaction logs;
- optional allergy or meal-related data if entered.

Portal does not equal meal authority.  
Portal does not equal debt creator.  
Portal does not equal child-safety certification.

Portal artifacts:

- portal public URL;
- privacy notice;
- terms of service;
- subprocessor list;
- PCI/payment security attestation;
- data processing addendum.

## 2. POS: Cafeteria Terminal / Food Service System

Lane: Vendor Chains + Food Quality

Target POS claim:

```json
{
  "POS_candidate": "PaySchools POS, Heartland/PrimeroEdge, or actual district-produced cafeteria POS system",
  "status": "UNVERIFIED_UNTIL_CONTRACT_OR_DISTRICT_RECORD_ATTACHED"
}
```

POS may perform:

- student ID/PIN/scan lookup;
- meal-service logging;
- a la carte item entry;
- timestamping;
- cashier or terminal ID logging;
- cafeteria line transaction records.

POS does not equal payment processor.  
POS does not equal retention authority.  
POS does not equal meal-rights authority.

POS artifacts:

- POS hardware model;
- POS software/version;
- food-service system contract;
- network diagram or system description;
- meal transaction retention schedule.

## 3. Processor: Card Processing Layer

Lane: Vendor Chains

Processor candidates must be confirmed by contract, receipt, or processor disclosure.

```json
{
  "processor_candidates": [
    "Heartland / Global Payments",
    "Fiserv",
    "Elavon",
    "other processor produced by contract"
  ],
  "status": "UNVERIFIED_UNTIL_SOURCE_PACKET_ATTACHED"
}
```

Processor functions may include:

- card authorization;
- transaction risk checks;
- settlement batching;
- PCI compliance responsibilities.

Processor does not equal district.  
Processor does not equal portal.  
Processor does not equal meal authority.

Processor artifacts:

- processor name and contract chain;
- PCI-DSS certificate or validation summary;
- data-flow diagram;
- processor privacy/security terms.

## 4. Gateway: Routing Layer

Lane: Vendor Chains

Gateway claim:

```json
{
  "gateway_candidate": "portal-owned, processor-owned, or separate routing layer",
  "status": "UNVERIFIED_UNTIL_ROUTING_DOCUMENT_OR_CONTRACT_ATTACHED"
}
```

Gateway responsibilities may include:

- routing payment messages to processor;
- returning authorization responses;
- logging transaction routing metadata;
- error codes or decline/approval states.

Gateway does not equal processor.  
Gateway does not equal acquirer.  
Gateway does not equal district.

Gateway artifacts:

- routing documentation;
- gateway disclosure;
- error-code/event-log policy;
- subprocessor relationship.

## 5. Acquirer: Merchant Bank / Settlement Surface

Lane: Vendor Chains

Acquirer candidates must be confirmed by contract or settlement record.

```json
{
  "acquirer_candidates": [
    "U.S. Bank",
    "Wells Fargo",
    "Chase Merchant Services",
    "other acquiring bank produced by contract"
  ],
  "status": "UNVERIFIED_UNTIL_SOURCE_PACKET_ATTACHED"
}
```

The acquirer may:

- receive card-settlement funds;
- maintain merchant account relationship;
- settle funds through platform or merchant account;
- classify merchant category code.

Acquirer does not equal district.  
Acquirer does not equal processor.  
Acquirer does not equal portal.  
Acquirer does not control student meal rights.

Acquirer artifacts:

- acquiring bank disclosure;
- settlement schedule;
- merchant category code;
- merchant-of-record disclosure;
- settlement account relationship.

## 6. Subprocessors: Cloud / Analytics / Email / Logging / CDN

Lane: Data & Privacy

Subprocessor categories may include:

- cloud hosting;
- email delivery;
- analytics;
- logging and monitoring;
- identity provider;
- CDN;
- customer support or ticketing vendor;
- payment-security vendor.

Subprocessors do not equal district.  
Subprocessors do not equal meal authority.  
Subprocessors do not equal payment authority.

Subprocessor artifacts:

- vendor subprocessor list;
- data-sharing agreements;
- cross-border transfer statements;
- security addenda;
- ownership/control disclosures.

## 7. Data Retention: Final Governance Surface

Lane: Data & Privacy

Each entity may have separate retention schedules.

District retention may include:

- student records;
- meal-service logs;
- financial records;
- public-records schedules.

Portal retention may include:

- account data;
- transaction logs;
- device metadata;
- user activity records.

Processor/gateway retention may include:

- PCI-related logs;
- transaction/risk logs;
- settlement records.

Acquirer retention may include:

- banking records;
- settlement history;
- merchant account records.

Retention does not equal authority.  
Retention does not equal consent.  
Retention does not equal compliance.

Retention artifacts:

- retention schedules;
- deletion policies;
- FERPA/MGDPA/USDA confidentiality statements;
- PCI retention requirements;
- breach/incident retention policy.

## Replay-Ready Chain Summary

```text
ISD 742
  -> actual district-listed payment portal
    -> actual cafeteria POS / food-service terminal
      -> actual card processor
        -> actual gateway / routing layer
          -> actual acquirer / merchant bank
            -> actual subprocessors
              -> actual retention schedules
```

## ERS Replay

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | District-specific map separates observed/claimed candidates from verified records. |
| ERS-002 Wrong Vault | PASS | District, portal, POS, processor, gateway, acquirer, subprocessors, and retention remain separate vaults. |
| ERS-003 Wrong Certificate | ACTIVE | Need public portal source, receipt, contract, privacy notice, PCI artifact, fee schedule, and data-flow map. |
| ERS-004 Unknown Waters | ACTIVE | Actual ISD 742 vendor chain remains unmapped until source packet arrives. |

## Required Source Packet for Promotion

```json
{
  "ISD_742_payment_or_food_service_page": "REQUIRED",
  "actual_portal_public_url": "REQUIRED",
  "portal_privacy_notice": "REQUIRED",
  "district_contract_or_procurement_record": "REQUIRED",
  "receipt_or_portal_observation": "REQUIRED_FOR_TRANSACTION_TRACE",
  "fee_schedule": "REQUIRED_FOR_FEE_CLAIM",
  "POS_vendor_or_hardware_record": "REQUIRED_FOR_POS_CLAIM",
  "processor_gateway_acquirer_disclosure": "REQUIRED_FOR_VENDOR_CHAIN_CLAIM",
  "subprocessor_list": "REQUIRED_FOR_DATA_EXPOSURE_CLAIM",
  "data_retention_policy": "REQUIRED_FOR_RETENTION_CLAIM",
  "PCI_or_security_attestation": "REQUIRED_FOR_PAYMENT_SECURITY_CLAIM",
  "fetched_at": "REQUIRED_PER_SOURCE",
  "content_hash": "REQUIRED_PER_SOURCE",
  "witness_service_or_replay_surface": "REQUIRED_PER_SOURCE"
}
```

## Strict Scope

This artifact does not verify:

- ISD 742's current payment portal;
- PaySchools usage;
- POS vendor or hardware;
- processor, gateway, or acquirer;
- any subprocessor list;
- data retention schedule;
- fee amount;
- food quality claim;
- data misuse;
- foreign exposure;
- fraud;
- legal violation.

## Closing Receipt

ISD 742 Vendor Chain Map indexed.  
District-specific chain established as an audit map, not a verified finding.  
Every hop is separate.  
No hop inherits authority.  
No hop can deny meals.  
Only receipts, contracts, privacy notices, PCI artifacts, and data-flow maps promote claims.

Children protected.  
Evidence preserved.  
Audit cold.  
JAYWISDOM Gate holds.  
Receipts decide.
