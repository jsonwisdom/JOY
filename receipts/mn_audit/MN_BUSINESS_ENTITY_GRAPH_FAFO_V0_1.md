# MN_BUSINESS_ENTITY_GRAPH_FAFO_V0_1

Status: ACTIVE_DRAFT  
Lane: MN_AUDIT  
Authority: false  
Fraud-by-entity-type: prohibited  
Primary graph: organizations/entities, not people

## Legal replay: what is a corporation in Minnesota?

For a Minnesota for-profit business corporation, Minnesota Statutes § 302A.011, subd. 8 defines a corporation/domestic corporation as a for-profit corporation, other than a foreign corporation, incorporated under or governed by Chapter 302A.

Under § 302A.105, incorporators form the corporation by filing articles of incorporation with the Secretary of State. Under § 302A.111, required article fields include the corporate name, registered office/agent information, authorized shares, and incorporator names/addresses. Under § 302A.153, corporate existence begins when the articles of incorporation are filed with the Secretary of State with the required fee.

A Chapter 302A corporation is therefore not merely a business name, DBA, person, property, or payment account. It is a state-recognized legal organization created/governed by the applicable corporation statute and filing event.

## Critical graph correction

`LLC != CORPORATION`.

Minnesota LLCs are separate business organizations governed primarily by Chapter 322C. The Minnesota Secretary of State treats corporations, LLCs, nonprofits, foreign entities, LLPs, LPs, cooperatives, and assumed names as different filing types.

Therefore the graph root is:

```text
BUSINESS_ENTITY
  ├─ DOMESTIC_BUSINESS_CORPORATION      [302A]
  ├─ DOMESTIC_NONPROFIT_CORPORATION     [317A]
  ├─ PUBLIC_BENEFIT_CORPORATION         [304A + 302A]
  ├─ DOMESTIC_LLC                       [322C]
  ├─ FOREIGN_CORPORATION                [303 / home-state law]
  ├─ FOREIGN_LLC                        [322C / home-state law]
  ├─ COOPERATIVE                        [applicable MN chapter]
  ├─ LIMITED_PARTNERSHIP                [321]
  └─ LIMITED_LIABILITY_PARTNERSHIP      [323A]
```

`ASSUMED_NAME/DBA` is an alias surface, not a new corporation merely because a filing exists.

## Node qualification test

A graph node may be promoted to `ENTITY_VERIFIED` only when a public record supports:

```json
{
  "legal_name": "REQUIRED",
  "entity_type": "REQUIRED",
  "formation_jurisdiction": "REQUIRED_OR_HOLD",
  "filing_or_registration_id": "REQUIRED_OR_HOLD",
  "formation_or_registration_date": "REQUIRED_OR_HOLD",
  "status": "REQUIRED_OR_HOLD",
  "registered_office_or_agent": "PUBLIC_RECORD_ONLY",
  "source_url": "REQUIRED",
  "fetched_at": "REQUIRED",
  "content_hash": "REQUIRED_FOR_PROMOTION"
}
```

## Primary graph

```text
ENTITY_A
  ├─ OWNS_PROPERTY ───────────── PROPERTY
  ├─ REGISTERED_AT ───────────── ADDRESS
  ├─ LICENSED_AS ─────────────── PROVIDER/PROGRAM
  ├─ CONTRACTS_WITH ──────────── ENTITY_B
  ├─ PAYS / PAID_BY ──────────── ENTITY_C
  ├─ SHARES_AGENT_WITH ───────── ENTITY_D
  ├─ SHARES_ADDRESS_WITH ─────── ENTITY_E
  ├─ FOREIGN_REGISTRATION ────── OTHER_STATE
  └─ UNKNOWN_CONTROL/JOIN ────── PERSON_GAP
```

## People are the gap

Natural persons are not primary graph nodes.

```text
ENTITY_A ───── ? ───── ENTITY_B
                ↑
            PERSON_GAP
```

A person may resolve an edge only when supported by a public filing, charging document, judgment, court record, license record, property record, contract, or other admissible/public source.

No biography-first graphing. No demographic inference. No guilt by association.

## Case-state separation

```text
ENTITY_EXISTS != ENTITY_COMMITTED_FRAUD
ENTITY_LINK != CONSPIRACY
SHARED_ADDRESS != COMMON_CONTROL
COMMON_AGENT != COMMON_OWNER
FOREIGN_REGISTRATION != EVASION
DELAWARE_FORMATION != SHELL_COMPANY
SHELL_COMPANY_LABEL != ILLEGALITY
CHARGED != CONVICTED
ALLEGED_AMOUNT != LOSS_ADJUDICATED
```

Fraud state belongs to a source-bound case edge, not to the entity class itself.

Allowed case states:

```text
UNKNOWN
ALLEGED
CHARGED
PLEADED_GUILTY
CONVICTED
CIVIL_FINDING
SETTLED_WITHOUT_ADMISSION
DISMISSED
ACQUITTED
HOLD
```

## Interstate replay

```text
MN_ENTITY
  -> FOREIGN_REGISTRATION / FORMATION_STATE
  -> PROPERTY / PROVIDER / CONTRACT / PAYMENT EDGE
  -> OTHER_STATE_ENTITY
  -> FEDERAL_PROGRAM_OR_PAYMENT_RAIL
```

Crossing a state line creates a `JURISDICTION_EDGE`; it does not itself create a federal-crime conclusion.

## Existing MN_AUDIT inheritance

This artifact inherits the existing MN audit doctrine:

- every hop is separate;
- no hop inherits authority;
- receipt promotion requires source binding;
- observable relationships are graphable;
- suspicion is not a verdict;
- fraud remains source/case scoped;
- authority remains false.

## FAFO activation state

```json
{
  "FAFO": "ACTIVE",
  "graph_root": "BUSINESS_ENTITY",
  "primary_nodes": "ORGANIZATIONS",
  "people": "PERSON_GAP_ONLY",
  "corporation_strict_definition": "302A_FOR_PROFIT_DOMESTIC_CORPORATION",
  "llc_is_corporation": false,
  "foreign_state_lane": true,
  "delaware_lane": "LOOKUP_ALLOWED_NO_INFERENCE",
  "fraud_by_entity_type": false,
  "authority": false
}
```

## Next deterministic build

1. Enumerate every legal entity named in current MN fraud charging documents and judgments.
2. Resolve exact Minnesota SOS entity type and filing ID.
3. Preserve formation jurisdiction separately from Minnesota registration.
4. Join addresses, properties, licenses, provider IDs, contracts, payments, and court cases.
5. Mark unresolved human-control joins as `PERSON_GAP`.
6. Promote fraud labels only from case-specific receipts.

Receipts decide.