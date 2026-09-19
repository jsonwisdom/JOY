# AI_FORCE_FORMAL_INSTRUMENT_SEARCH_V0_1

```text
CLASS = PRIMARY_SOURCE_SEARCH_RECEIPT
PARENT = REUTERS_TRUMP_AI_FORCE_ANNOUNCEMENT_RECEIPT_V0_1
AUTHORITY_CREATED = FALSE
POLITICAL_VERDICT = NONE
```

## Question

Has a formal federal instrument creating or defining the announced "AI Force" been observed in the current primary-source search?

## Current answer

```text
FORMAL_AI_FORCE_INSTRUMENT = NOT_OBSERVED_IN_CURRENT_SEARCH_SCOPE
STATUTORY_CREATION = NOT_OBSERVED_IN_CURRENT_SEARCH_SCOPE
BUDGET_LINE = NOT_OBSERVED_IN_CURRENT_SEARCH_SCOPE
ORG_CHART = NOT_OBSERVED_IN_CURRENT_SEARCH_SCOPE
AI_CZAR_IDENTITY = NOT_OBSERVED_IN_CURRENT_SEARCH_SCOPE
```

This is a bounded search result, not a claim that no instrument exists anywhere.

## Search scope

Current checks covered:
- White House presidential-actions and AI-related official pages
- Executive-order / memorandum surfaces
- Federal-government search results surfaced through govinfo/Federal Register queries
- Department of Justice AI-related material

No current primary-source result located in this pass used the exact announced "AI Force" label as a new formally constituted organ.

## Existing formal AI authority objects found

### Executive Order 14365 — AI Litigation Task Force

Executive Order 14365, signed December 11, 2025, directed the Attorney General to establish an AI Litigation Task Force within 30 days whose sole responsibility is to challenge State AI laws inconsistent with the order's national policy.

Primary source:
https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/

### DOJ establishment memorandum

A January 9, 2026 Attorney General memorandum states that the Attorney General was establishing the Artificial Intelligence Litigation Task Force, with the Attorney General or designee as Chair and the Associate Attorney General as Vice Chair.

Primary source:
https://www.justice.gov/ag/media/1422986/dl

### Executive Order 14409

Executive Order 14409 coordinates AI cybersecurity and directs enforcement of existing criminal laws against certain AI-enabled cyber activity. It also states that implementation is subject to available appropriations and does not create mandatory AI-model licensing.

Primary source:
https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/

### NSPM-11

NSPM-11 establishes a national-security AI framework across named departments and agencies and includes an AI National Security Strategic Reserve of non-governmental experts.

Primary source:
https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/

## Boundary

```text
ANNOUNCEMENT ≠ FORMAL_INSTRUMENT
FORMAL_INSTRUMENT_SEARCH_MISS ≠ NONEXISTENCE_IN_WORLD
AI_LITIGATION_TASK_FORCE ≠ ANNOUNCED_AI_FORCE
EO_14409 ≠ ANNOUNCED_AI_FORCE
NSPM_11 ≠ ANNOUNCED_AI_FORCE
```

## Output

```text
NEXT_GATE = AI_FORCE_DUPLICATION_TEST_V0_1
```
