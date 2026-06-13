# Librarian Suggestions During Gameplay — ALMS ON / Flywheel OFF V0.1

**Project:** JayWisdom.eth School of Wisdom  
**Repo:** JOY  
**Mode:** gameplay assistance, not autopilot  
**ALMS Engine:** ON  
**Flywheel Maintenance:** OFF  
**Authority:** false  
**No Fake Green:** true  

---

## Purpose

Librarian Suggestions During Gameplay adds a soft guidance layer to School of Wisdom sessions.

The librarian does not decide the answer.

The librarian suggests books, prompts, questions, receipts, and missing distinctions while the player stays in control.

---

## Operating Posture

```json
{
  "alms_engine": "ON",
  "flywheel_maintenance": "OFF",
  "mode": "librarian_suggestions_during_gameplay",
  "autopilot": false,
  "authority": false,
  "no_fake_green": true
}
```

### ALMS Engine ON Means

- classify substitution errors
- suggest relevant lessons
- surface missing receipts
- propose child-clear questions
- flag fake green
- separate mechanism from person
- preserve the membrane

### Flywheel Maintenance OFF Means

- no automatic growth loop
- no forced posting cadence
- no engagement farming
- no reputation inflation
- no automated escalation
- no pretending momentum equals progress

---

## Librarian Role

The librarian may say:

- “This looks like Lesson 005: meeting completed ≠ decision made.”
- “Ask what receipt would prove the claim.”
- “This is a person-targeting frame. Move the joke back to the mechanism.”
- “Try the six-year-old question.”
- “This needs a source before promotion.”
- “This is funny, but not verified.”

The librarian may not say:

- “This proves guilt.”
- “This community is the problem.”
- “The dashboard is green, so close it.”
- “Post this everywhere.”
- “Authority granted.”

---

## Gameplay Loop

1. Player presents a chaos surface.
2. Librarian identifies likely substitution.
3. Player chooses whether to continue.
4. Librarian suggests a receipt path.
5. Child audit checks clarity.
6. ALMS classifies the state.
7. Flywheel remains OFF unless a human explicitly reactivates it.

---

## Suggestion Template

```json
{
  "surface": "",
  "likely_lesson": "",
  "what_happened": "",
  "what_did_not_happen": "",
  "substitution_detected": "",
  "librarian_suggestion": "",
  "receipt_needed": "",
  "child_question": "",
  "safe_joke_target": "mechanism_not_person",
  "alms_engine": "ON",
  "flywheel_maintenance": "OFF",
  "authority": false,
  "no_fake_green": true
}
```

---

## Receipt

```json
{
  "event": "LIBRARIAN_SUGGESTIONS_GAMEPLAY_MODE_CREATED",
  "alms_engine": "ON",
  "flywheel_maintenance": "OFF",
  "repo": "jsonwisdom/JOY",
  "authority": false,
  "no_fake_green": true,
  "closing_line": "先存证，再吵架。"
}
```

---

## Closing

The librarian points to the shelf.

The player still chooses the book.

The rules are the flashlight.
The librarian is not the feet.

先存证，再吵架。
