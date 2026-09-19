# AI_FORCE_AUTHORITY_BINDING_V0_1 — Primary-source replay — 2026-09-19

AUTHORITY_CREATED = FALSE
POLITICAL_VERDICT = NONE
MAIN_MUTATED = FALSE
PRIMARY_SOURCES_ONLY = TRUE

## Trigger
TRIGGER = NAMED_AI_CZAR_IN_PRIMARY_SOURCE
SUPPORTED_DIMENSION = NAMED_AI_CZAR

White House press briefing, January 29, 2025: Press Secretary Karoline Leavitt states that President Trump appointed David Sacks as the first White House AI and crypto czar and that his team was working at the White House.
Source: https://www.whitehouse.gov/briefings-statements/2025/01/press-briefing-by-press-secretary-karoline-leavitt/

Corroborating White House primary sources:
- January 23, 2025 PCAST fact sheet: White House A.I. and Crypto Czar co-chairs PCAST. https://www.whitehouse.gov/fact-sheets/2025/01/fact-sheet-president-donald-j-trump-launches-pcast-to-restore-american-leadership-in-science-and-technology/
- July 23, 2025 AI Action Plan release identifies David Sacks as AI and Crypto Czar. https://www.whitehouse.gov/releases/2025/07/white-house-unveils-americas-ai-action-plan/

## Dimension binding
NAMED_AI_CZAR = OBSERVED / DAVID_SACKS
AI_CZAR_TITLE_IN_WHITE_HOUSE_PRIMARY_SOURCE = OBSERVED
AI_CZAR_TEAM_AT_WHITE_HOUSE = OBSERVED_AS_PRESS_BRIEFING_STATEMENT
AI_CZAR_STATUTORY_OFFICE = HOLD
AI_CZAR_PERSONNEL_AUTHORITY = HOLD
AI_CZAR_INVESTIGATIVE_AUTHORITY = HOLD
AI_CZAR_ENFORCEMENT_AUTHORITY = HOLD
AI_CZAR_DEDICATED_APPROPRIATION = HOLD
AI_CZAR_IS_ANNOUNCED_AI_FORCE = HOLD / NOT_ESTABLISHED

## Existing task-force separation
DOJ Attorney General memorandum, January 9, 2026, formally establishes the Artificial Intelligence Litigation Task Force and states its sole responsibility is to challenge state AI laws inconsistent with stated federal policy.
Source: https://www.justice.gov/ag/media/1422986/dl?inline=

EXISTING_AI_LITIGATION_TASK_FORCE = OBSERVED / FORMALLY_ESTABLISHED
ANNOUNCED_AI_FORCE = OBSERVED_AS_ANNOUNCEMENT
ANNOUNCED_AI_FORCE_IS_SAME_OBJECT = HOLD / NOT_ESTABLISHED

## AI_FORCE_DUPLICATION_TEST_V0_1
OBJECT_A = DOJ_ARTIFICIAL_INTELLIGENCE_LITIGATION_TASK_FORCE
OBJECT_B = ANNOUNCED_AI_FORCE
EXPLICIT_PRIMARY_LINK_A_TO_B = NOT_FOUND_IN_THIS_REPLAY
SAME_OBJECT = HOLD / NOT_ESTABLISHED
DO_NOT_COLLAPSE = TRUE

## AI_FORCE_GIRL_IMPACT_AUDIT_V0_1
model = HOLD
data = HOLD
agency = HOLD
legal_authority = HOLD
human_review = HOLD
action = HOLD
notice = HOLD
appeal = HOLD
audit_log = HOLD
remedy = HOLD

EXISTING_FEDERAL_AI_CHILD_SAFETY_LANGUAGE = OBSERVED
ANNOUNCED_AI_FORCE_INHERITS_THAT_LANGUAGE = NOT_ESTABLISHED
HUMAN_CHAIR = HER_WORDS_ONLY
AFFECTED_PERSON != BURDEN_DUMP

## FullMath close
NAMED_AI_CZAR dimension closes only.
No primary receipt found in this replay that closes announced-AI-Force identity, org chart/office designation for that announced object, budget/appropriation, personnel authority, investigative/enforcement authority, or DOJ/OMB/OSTP implementation memorandum for that announced object.

COVERAGE_BLOCK != NEGATIVE
NOT_FOUND != FALSE
ONE_DIMENSION_BOUND != WHOLE_OBJECT_BOUND
