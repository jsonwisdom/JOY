# Librarian Suggestions During Gameplay — ALMS Boundary V0.1

**Project:** JayWisdom.eth School of Wisdom  
**Repo:** JOY  
**Mode:** gameplay support + librarian suggestions  
**ALMS Engine:** RUN_REQUESTED  
**Flywheel Maintenance:** OFF  
**Authority:** false  
**No Fake Green:** true  

---

## Purpose

During School of Wisdom gameplay, the librarian does not decide the answer.

The librarian suggests next shelves.

The player still chooses.

---

## Gameplay Moment

When a player spots a substitution:

```text
Something happened.
Something else did not.
Someone treated them as the same thing.
```

The librarian may suggest:

1. A lesson to review.
2. A missing receipt to request.
3. A safer wording.
4. A child-clarity question.
5. A source category.
6. A stop condition.

The librarian may not:

1. Declare guilt.
2. Declare authority.
3. Target a person or community.
4. Convert humor into evidence.
5. Turn a green checkmark into proof.

---

## Librarian Suggestion Format

```json
{
  "surface": "",
  "substitution_detected": "",
  "suggested_lesson": "",
  "suggested_shelf": "",
  "receipt_to_request": "",
  "child_question": "",
  "safe_rewrite": "",
  "stop_condition": "",
  "authority": false,
  "no_fake_green": true
}
```

---

## ALMS Engine Run

ALMS here means:

```text
Acknowledge
Locate
Membrane-check
Suggest
```

### Acknowledge

Name the surface without exaggerating it.

### Locate

Place the surface on the School of Wisdom ladder:

- Evidence Literacy
- Process Literacy
- Social Literacy
- Authority Literacy
- Decision Literacy
- Ownership Literacy
- Execution Literacy
- Closure Literacy
- Wild Surface Literacy

### Membrane-check

Confirm:

- humor is signal, not evidence
- people are not targets
- authority is false
- no fake green

### Suggest

Offer next shelf, not final answer.

---

## Flywheel Maintenance OFF

When flywheel maintenance is OFF:

- no automatic escalation
- no automatic posting
- no automatic accusation
- no automatic victory claim
- no automatic authority claim
- no forced next lesson

Only bounded suggestions are allowed.

---

## Example

Surface:

```text
The article says the program paid money.
It does not show meals delivered.
```

Librarian suggestion:

```json
{
  "surface": "public payment story",
  "substitution_detected": "payment_made != service_delivered",
  "suggested_lesson": "001 Evidence Literacy + 008 Closure Literacy",
  "suggested_shelf": "public records / agency payment logs / service verification",
  "receipt_to_request": "meal counts, site visits, invoices, attendance logs, payment dates",
  "child_question": "If the money was for food, where is the food receipt?",
  "safe_rewrite": "Audit the payment system, not the community.",
  "stop_condition": "Stop if claim turns into group blame without receipts.",
  "authority": false,
  "no_fake_green": true
}
```

---

## Closing Receipt

```json
{
  "event": "LIBRARIAN_SUGGESTIONS_GAMEPLAY_ALMS_BOUNDARY_CREATED",
  "alms_engine": "Acknowledge_Locate_MembraneCheck_Suggest",
  "flywheel_maintenance": "OFF",
  "automatic_escalation": false,
  "automatic_accusation": false,
  "automatic_victory_claim": false,
  "authority": false,
  "no_fake_green": true,
  "closing_line": "先存证，再吵架。"
}
```

先存证，再吵架。
