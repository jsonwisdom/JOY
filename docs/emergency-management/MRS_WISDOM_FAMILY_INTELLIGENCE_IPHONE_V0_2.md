# Mrs. Wisdom’s Family Intelligence iPhone — Emergency Management Design v0.2

```text
STATE                  = DESIGN_CANDIDATE
RESULT                 = ACCEPTED_WITH_HIERARCHY_CORRECTION
PRIMARY_DOMAIN         = FAMILY_INTELLIGENCE
SECONDARY_DOMAIN       = WORK
PROFILE                = APPLE_ONLY_SIMULATION
AUTHORITY_CREATED      = FALSE
IDENTITY_PROOF         = FALSE
CONSENT_INFERRED       = FALSE
REPOSITORY_EFFECT      = DESIGN_BRANCH_ONLY
PROMOTION              = PROHIBITED
OPERATIONAL_USE        = NOT_AUTHORIZED
```

## Product name

**JOY Guardian — Mrs. Wisdom’s Family Intelligence iPhone**

A calm, feminine, family-first iPhone interface for household awareness, safety, continuity, memory, emergency preparation, and bounded Siri-assisted discovery.

**Work is a secondary, isolated mode.** It never outranks family safety, family continuity, or personal wellbeing.

“Girl Version” describes the welcoming visual voice. It does not assign capability, authority, risk, or responsibility by gender.

## Controlling hierarchy

```text
MRS. WISDOM
→ FAMILY INTELLIGENCE
→ HOME / PEOPLE / SAFETY / CONTINUITY / MEMORY
→ EMERGENCY MANAGEMENT
→ WORK MODE
```

This order is mandatory. A work request cannot displace an active family safety need.

## Meaning of family intelligence

Family intelligence is **consented household awareness** that helps a family remember, prepare, coordinate, and care for one another.

It is not:

- surveillance
- secret profiling
- parental or employer command authority
- inferred consent
- proof of identity
- automatic location tracking
- a substitute for direct family communication

## Core promise

The phone helps answer:

1. Is everyone safe?
2. What does the family need now?
3. What plan or memory helps us respond?
4. What official source supports the information?
5. Who has consented to receive or share this?
6. What must remain private?
7. Only after those checks: what work remains?

The design does not replace 911, local emergency management, first responders, medical professionals, official alerts, or Apple’s built-in Emergency SOS.

## Family-first home screen

### 1. Family Pulse

A low-stress summary showing only consented status:

- **Together:** approved check-ins are current
- **Check:** a family plan, contact, supply, or check-in needs review
- **Act:** an official alert or user-confirmed family safety action exists
- **Unknown:** information is missing, stale, or unverified

Color is paired with text, icon, timestamp, and source. Missing information never becomes a negative judgment about a person.

### 2. Primary family controls

- **Family Check-In:** prepares a consented message before sending
- **Emergency SOS:** opens Apple’s native emergency path; JOY never imitates or intercepts it
- **Need Help:** offers bounded call, text, official-guidance, or offline options
- **People:** approved contacts, accessibility needs, and reunification preferences
- **Home:** shelter, utilities, pets, supplies, medications, transportation, and evacuation notes
- **Family Plan:** meeting places, communication trees, caregiving, and recovery steps
- **Family Memory:** selected stories, instructions, traditions, and continuity records
- **Official Alerts:** pointer-only links to approved public sources
- **Incident Notebook:** observations kept distinct from verified facts

### 3. Secondary Work control

**Work** appears below the family controls and opens an isolated workspace.

Work mode may contain:

- schedule pointers
- task drafts
- approved work contacts
- public workplace emergency guidance
- non-sensitive incident notes

Work mode may not inherit:

- family location
- medical information
- private family messages
- family identity documents
- family contact permissions
- family memory records
- household authority

## Priority invariant

```text
ACTIVE_FAMILY_SAFETY_NEED > WORK_NOTIFICATION
ACTIVE_EMERGENCY_ACTION   > WORK_TASK
FAMILY_CONSENT_BOUNDARY   > WORK_CONVENIENCE
PERSONAL_WELLBEING        > PRODUCTIVITY_PRESSURE
```

The interface may delay or mute work cards during a user-confirmed family emergency. It may not conceal legally required information or fabricate completion.

## Siri AI membrane

Siri is a natural-language discovery layer, never direct execution authority.

```text
NATURAL LANGUAGE
→ PARSE
→ CANONICAL REQUEST
→ DOMAIN CHECK
→ CAPABILITY CHECK
→ CONSENT CHECK
→ PRIORITY CHECK
→ POINTER-ONLY RESPONSE
```

Example:

> “Siri, ask JOY whether my family plan has an approved shelter.”

Canonical request:

```json
{
  "request_type": "DISCOVER_FAMILY_PLAN_SHELTER",
  "domain": "FAMILY_INTELLIGENCE",
  "household_scope": "USER_APPROVED_FAMILY_PLAN",
  "source_policy": "APPROVED_POINTERS_ONLY",
  "side_effects": false,
  "consent_required": true
}
```

Siri may summarize approved public information, prepare a draft, or open an approved pointer. It may not silently call, message, publish, purchase, transfer data, cross family/work boundaries, identify a person, declare an emergency, or infer family consent.

## Domain separation

### Family domain

Contains consented household plans, check-ins, care preferences, emergency contacts, accessibility notes, pet plans, and selected continuity memories.

### Work domain

Contains bounded work pointers and drafts. It is secondary and isolated.

### Cross-domain links

CrissCross AppleSauce links are pointers only. A family record may reference a work record, or a work record may reference public emergency guidance, but the link does not:

- merge identity
- infer consent
- copy protected content
- inherit permissions
- inherit ownership
- inherit priority
- inherit authority

## Data zones

### Public

Official alerts, public maps, public shelter pointers, and preparedness guidance.

### Family-shared

Only information explicitly approved for named family participants.

### Personal

Private preferences, draft check-ins, individual accessibility needs, and personal notes.

### Protected

Medical details, precise location history, credentials, private messages, identity documents, and non-shared family memories.

Protected data is local-first, platform-encrypted, redacted from receipts, and never copied through cross-links.

## Modes

### Family

The default surface: people, home, care, plans, memory, and readiness.

### Prepare

Verify contacts, plans, supplies, accessibility, offline guidance, and reunification steps.

### Watch

Review official pointers and timestamps without treating rumors as verified.

### Respond

Show the smallest approved family safety action set.

### Recover

Record needs, receipts, photos, expenses, and follow-up tasks without claiming eligibility or reimbursement.

### Replay

Reconstruct what was known, when, from which source, under whose consent, and what action was approved.

### Work

A secondary workspace available only after domain, consent, and priority checks. Work is never the root identity of Mrs. Wisdom.

## Girl Math boundary

“Girl Math” remains a playful readiness label only, such as “Two charged phones means one less family worry.”

It is prohibited for accounting, pricing, procurement, resource allocation, benefits, medical dosage, risk scoring, incident severity, eligibility, or ledger decisions.

## Minimum acceptance tests

1. The default launch surface is Family, not Work.
2. An active family safety card is never displaced by a work notification.
3. Work cannot read family-shared, personal, or protected fields without explicit bounded consent.
4. Family membership is never inferred from contacts, surname, device access, or proximity.
5. Natural language cannot directly trigger an external side effect.
6. Missing consent returns `DENIED`.
7. Unknown fields and unsupported domains return `DENIED`.
8. Cross-links cannot inherit private data, permissions, priority, or authority.
9. Official and unverified reports remain visually distinct.
10. Emergency SOS routes to Apple’s native control.
11. Offline cards display source age and last verification time.
12. Denials are visible and locally replayable without exposing secrets.

## Deployment gate

```text
DEFINE_FAMILY_CONSENT_MODEL
→ DEFINE_FAMILY_AND_WORK_SCHEMAS
→ SELECT_EXACT_IOS_VERSION
→ SELECT_EXACT_XCODE_TOOLCHAIN
→ DEFINE_SIGNED_CAPABILITIES
→ BUILD_CANONICAL_REQUEST_SCHEMA
→ TEST_DOMAIN_ISOLATION
→ TEST_PRIORITY_INVARIANTS
→ RUN_ACCESSIBILITY_TESTS
→ RUN_OFFLINE_TESTS
→ RUN_DENIAL_TESTS
→ HUMAN_FAMILY_SAFETY_REVIEW
→ HUMAN_EMERGENCY_MANAGEMENT_REVIEW
→ SECURITY_REVIEW
→ CONSENT_REVIEW
```

Until every gate passes:

```text
STATUS          = DESIGN_CANDIDATE
AUTHORITY       = FALSE
OPERATIONAL     = FALSE
PROMOTION       = PROHIBITED
```
