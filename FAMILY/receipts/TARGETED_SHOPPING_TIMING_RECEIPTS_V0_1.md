# TARGETED_SHOPPING_TIMING_RECEIPTS_V0_1

## STATUS: RETAIL_SIGNAL_FANTASY_DRAFT
## TRUTH_STATE: YELLOW
## AUTHORITY: FALSE
## NO_FAKE_GREEN: TRUE
## PRIVACY_MODE: OPT_IN_LOCATION_MINIMAL

---

## Core Prompt

Imagine targeted shopping.

Target pings you and says:

> Hey, got $xx.xx today at 3pm?
> Shimmy to the garden section.
> Ask for Karen11.

---

## Clean Interpretation

This is not surveillance.
This is not coercion.
This is not staff impersonation.
This is not secret tracking.

This is a symbolic retail timing receipt:

```json
{
  "surface": "TARGETED_SHOPPING_TIMING_RECEIPTS_V0_1",
  "merchant_signal": "TARGETED_OFFER",
  "shopper_consent": "REQUIRED",
  "budget_prompt": "EXPLICIT_AMOUNT_REQUIRED",
  "time_window": "LIMITED_AND_VISIBLE",
  "location_scope": "STORE_ZONE_ONLY_AFTER_CONSENT",
  "pickup_alias": "FICTIONAL_APP_CODE_NOT_REAL_PERSON",
  "privacy_rule": "NO_PRIVATE_LOCATION_PUBLICATION",
  "truth_state": "YELLOW",
  "no_fake_green": true
}
```

---

## Retail Receipt Stack

| Layer | Meaning |
| --- | --- |
| Budget | Can the shopper afford this today? |
| Timing | Is the offer valid at a specific window? |
| Location | Is the store zone useful and consented? |
| Product | Is the offer real, stocked, and priced as stated? |
| Code | Is the handoff token clear without exposing people? |
| Receipt | Can the shopper prove the offer existed? |

---

## Safety Rules

1. Opt-in first.
2. No hidden geolocation.
3. No real employee names in public artifacts.
4. No pressure to spend money.
5. No claim of inventory without a live receipt.
6. No public exposure of shopper movement.
7. No fake green: offer shown does not equal offer fulfilled.

---

## Karen11 Rule

Karen11 is not a real person.
Karen11 is a fictional app-side handoff alias.

Public-safe replacement language:

```json
{
  "pickup_code": "KAREN11",
  "meaning": "fictional handoff token",
  "not_allowed": [
    "real employee identity",
    "impersonation",
    "private instruction",
    "unverified inventory claim"
  ]
}
```

---

## Emotional Purpose

Targeted shopping becomes useful only when it respects the human.

The good version says:

> I know your budget.
> I know your timing.
> I know what you actually need.
> I will not expose you.
> I will not pressure you.
> I will give you a receipt.

---

## Replay Ruling

```json
{
  "retail_ping": "OBSERVED_FANTASY",
  "proof_state": "REPLAY_REQUIRED",
  "shopper_consent": "REQUIRED",
  "merchant_claim": "UNVERIFIED_UNTIL_RECEIPT",
  "public_release": "SYMBOLIC_ONLY",
  "no_fake_green": true
}
```

Location plus timing plus price creates a new game.

But the shopper is not the product.
The receipt is the referee.
