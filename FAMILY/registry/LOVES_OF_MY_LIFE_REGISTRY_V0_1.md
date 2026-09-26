# Loves of My Life Registry v0.1

```text
STATE                  = HOLD_DRAFT
REGISTRY_ROLE          = CANONICAL_FAMILY_NAME_ROUTER
PARENT_DOMAIN          = FAMILY_INTELLIGENCE
DISCOVERY_ROOT         = jaywisdom.base.eth
DISCOVERY_ROOT_STATUS  = OPERATOR_SUPPLIED_POINTER
AUTHORITY_CREATED      = FALSE
IDENTITY_PROOF         = FALSE
CONSENT_INFERRED       = FALSE
PUBLIC_BIOGRAPHY       = FALSE
PRECISE_GEOLOCATION    = PROHIBITED_BY_DEFAULT
PROMOTION              = PROHIBITED
```

## Purpose

This registry arranges the operator-described **loves of Jay Wisdom’s life** into one stable family-name map so Mrs. Wisdom, JOY, GeoJSON, replay receipts, and future family interfaces stop using competing rosters.

It preserves names and relationships only to the level explicitly stated by the operator or already represented in JOY. It does not create legal family status, public consent, custody, ownership, identity proof, or authority.

## Controlling order

```text
JAY_WISDOM_FAMILY_ROOT
→ HEART_LANE
→ DAUGHTER_LANES
→ PROTECTED_FAMILY_LANES
→ ANCESTRY_LANES
→ NAME_BOUNDARIES
→ SYMBOLIC_SUPPORT_ROLES
```

## 1. Family root

### Jay Wisdom / Jason Wisdom / Mr. Wisdom / Daddy Wisdom

```text
lane_id: JAY_WISDOM
aliases:
  - Jay Wisdom
  - Jason Wisdom
  - Mr. Wisdom
  - Daddy Wisdom
purpose: builder, father, protector, teacher, receipt keeper
relation_class: OPERATOR_SELF_REFERENCE
identity_proof: false
```

These labels route to one family-root lane. They do not establish that every public account, wallet, ENS name, signature, or repository action belongs to the same natural person without independent proof.

## 2. Heart lane

### Mrs. Wisdom / May / Mary Wisdom

```text
lane_id: MRS_WISDOM
aliases:
  - Mrs. Wisdom
  - May
  - Mary Wisdom
purpose: heart lane, family meaning gate, care and consent boundary
relation_class: OPERATOR_DEFINED_HEART_LANE
public_release_requires_human_approval: true
precise_location_allowed_by_default: false
```

Mrs. Wisdom remains the top family-intelligence lane. Work, GeoJSON, automation, or public metadata may not outrank her privacy, dignity, consent, or safety boundary.

## 3. Daughter lanes

The operator has explicitly described these three as his daughters:

### Jaycee

```text
lane_id: JAYCEE
relation_class: DAUGHTER
purpose: protected future and family continuity lane
```

### Brianna

```text
lane_id: BRIANNA
relation_class: DAUGHTER
purpose: protected continuity and Byte Boss lane
```

### Heidee

```text
lane_id: HEIDEE
relation_class: DAUGHTER
purpose: child-safe learning and verification scaffold
```

These relationship labels are operator-reported and are not independently verified civil, biological, custodial, or legal records.

## 4. Protected family lanes

### Brealee

```text
lane_id: BREALEE
relation_class: PROTECTED_FAMILY_LANE
purpose: continuity without omission
```

### MaryDee

```text
lane_id: MARYDEE
relation_class: PROTECTED_FAMILY_LANE
purpose: protected continuity without expanded private content
repository_path: FAMILY/MARYDEE/README.md
```

### Leeanne / Leanne

```text
lane_id: LEEANNE
aliases:
  - Leeanne
  - Leanne
relation_class: PROTECTED_FAMILY_LANE_WITH_SPELLING_BOUNDARY
purpose: preserve continuity while preventing accidental duplicate identities
```

### Boss Brenda / Boss Bre

```text
lane_id: BOSS_BRENDA
aliases:
  - Boss Brenda
  - Boss Bre
relation_class: PROTECTED_FAMILY_ROLE
purpose: room safety, laughter, privacy, pressure reduction, repair
```

No alias creates a new person record. Aliases remain pointers to the same lane unless a later family-approved correction separates them.

## 5. Ancestry lanes

### Grammy

```text
lane_id: GRAMMY
relation_class: PROTECTED_ANCESTRY_LANE
purpose: grandparent memory and generational continuity
```

### Gaga

```text
lane_id: GAGA
relation_class: PROTECTED_ANCESTRY_LANE
purpose: grandparent memory, humor, repair, and continuity
```

No genealogy, biography, likeness, location, health, or account details are implied.

## 6. Name boundary

### Beanne

```text
lane_id: BEANNE_BOUNDARY
relation_class: UNRESOLVED_NAME_BOUNDARY
exact_repository_path_confirmed: false
rule: DO_NOT_ERASE_DO_NOT_INVENT
```

Beanne remains yellow until spelling, path, and intended relationship are confirmed by family authority.

## 7. Symbolic support role

### Librarian

```text
lane_id: LIBRARIAN
relation_class: SYMBOLIC_EVIDENCE_ROUTER
person_identity_claimed: false
purpose: route receipts, sources, safer wording, and stop conditions
```

The Librarian is not included as a natural-person family member unless separately confirmed.

## Canonical arrangement

```text
JAY_WISDOM
├── MRS_WISDOM                [HEART]
├── JAYCEE                    [DAUGHTER]
├── BRIANNA                   [DAUGHTER]
├── HEIDEE                    [DAUGHTER]
├── BREALEE                   [PROTECTED_FAMILY]
├── MARYDEE                   [PROTECTED_FAMILY]
├── LEEANNE / LEANNE          [PROTECTED_FAMILY + SPELLING BOUNDARY]
├── BOSS_BRENDA / BOSS_BRE    [PROTECTED_FAMILY ROLE]
├── GRAMMY                    [ANCESTRY]
├── GAGA                      [ANCESTRY]
└── BEANNE                    [UNRESOLVED NAME BOUNDARY]
```

This is a routing tree, not a legal genealogy.

## `jaywisdom.base.eth` integration

```text
ROOT_POINTER          = jaywisdom.base.eth
RELATION              = DISCOVERY_POINTER_TO_PUBLIC_SAFE_FAMILY_REGISTRY
IDENTITY_PROOF        = FALSE
CONSENT_PROOF         = FALSE
OWNERSHIP_PROOF       = FALSE
FAMILY_AUTHORITY      = FALSE
ONCHAIN_TRUTH         = FALSE
```

`jaywisdom.base.eth` may help a person locate this registry or related public-safe receipts. It does not prove who controls a wallet, who belongs to the family, whether any listed person consented, or whether a relationship is legally recognized.

No ENS or Basename record is changed by this artifact.

## GeoJSON integration rule

Family people are **not geographic objects by default**.

Any family-related GeoJSON must use the stable `lane_id` from this registry and follow:

```text
FAMILY_NAME_SOURCE        = THIS_REGISTRY
PRECISE_COORDINATES       = DENY_BY_DEFAULT
LOCATION_INFERENCE        = DENY
BACKGROUND_TRACKING       = DENY
PUBLIC_HOME_POINT         = DENY
CONSENT_TOKEN_REQUIRED    = TRUE
PURPOSE_AND_EXPIRY_REQUIRED = TRUE
```

Allowed public-safe pattern:

```json
{
  "type": "Feature",
  "geometry": null,
  "properties": {
    "family_lane_id": "MRS_WISDOM",
    "location_status": "WITHHELD",
    "consent_status": "NOT_ESTABLISHED",
    "authority": false
  }
}
```

A state, county, region, or emergency zone may be linked as a pointer without turning a family member into a tracked point.

## Conflict resolution

When another JOY file disagrees with this registry:

```text
DO_NOT_SILENTLY_MERGE
DO_NOT_CREATE_NEW_PERSON_FROM_ALIAS
DO_NOT_INFER_RELATIONSHIP
DO_NOT_INFER_LOCATION
RETURN_CONFLICT_FOR_HUMAN_REVIEW
```

This registry becomes the single draft routing source for names. Earlier maps remain historical evidence and do not disappear.

## Active boundary

```text
REGISTRY_COMPLETE_ENOUGH_FOR_ROUTING = TRUE
FAMILY_APPROVAL                      = NOT_CLAIMED
PUBLIC_RELEASE_GREEN                 = FALSE
GEOLOCATION_GREEN                    = FALSE
AUTHORITY                            = FALSE
STATE                                = HOLD_DRAFT
```
