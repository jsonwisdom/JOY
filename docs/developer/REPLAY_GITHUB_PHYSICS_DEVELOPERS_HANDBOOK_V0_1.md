# Replay GitHub Physics — Developer's Handbook V0.1

Status: DRAFT_REPLAYABLE
Authority: false
Repo: jsonwisdom/JOY
Branch lane: family-fusion-fissics-v0-1
No Fake Green: true
Append Only: true

## 0. Purpose

This handbook translates the existing JSONWisdom / JOY replay architecture into a developer-facing math-and-physics teaching layer.

It is built from repository-observed parents:

~~~text
WISDOM/wisdom_family_game_night_dice_game_v0_1.md
WISDOM/family_fusion_fissics_fission_physics_applied_wisdom_game_of_dice_v0_1.md
docs/school-of-wisdom/lessons/MATH_CLASS_BRENDA_SPLIT_PHYSICS_GIRL_MATH_20260614.md
docs/constitution/SPEED_IS_NOT_CERTAINTY_V0_1.md
docs/constitution/GENERATE_FAST_PROMOTE_SLOW_REPLAY_ALWAYS_V0_1.md
docs/goblin-courts/JASONS_MINNESOTA_EXPLORER_GAMBIT_TIMESTAMP_ACCOUNTABILITY_V0_1.md
~~~

Cross-repo developer references:

~~~text
jsonwisdom/COMPUTERWISDOM/docs/discovery_path_v1.md
jsonwisdom/COMPUTERWISDOM/docs/statement-to-html-computation-layer-v0-1.md
jsonwisdom/COMPUTERWISDOM/workflows/deepseek-zora-ingestion-v1/programmable_change_mechanics_repo_automation_v1.md
jsonwisdom/COMPUTERWISDOM/agentic-game/DESIGN.md
jsonwisdom/COMPUTERWISDOM/RECEIPT_STACK_2026-06-08.md
jsonwisdom/COMPUTERWISDOM/SUPREME_SEYMOUR/game/README.md
~~~

The exact title "Replay GitHub Physics Developer's Handbook" did not pre-exist in the searched repositories. This file is a new V0.1 synthesis.

## 1. Developer boundary

~~~text
PHYSICS_METAPHOR != PHYSICAL_FINDING
MATH_MODEL != WORLD_STATE
GAME_EVENT != VERIFIER_RESULT
PASS != VERIFIED
COMMIT != EXTERNAL_TRUTH
HASH != MEANING
REPLAY != ADJUDICATION
AUTHORITY = false
~~~

The repository already distinguishes classroom physics metaphor from real physics claims.

Developer rule:

> Use physics words to describe constraints only when the type is explicit.

## 2. Typed symbol table

Every symbol must say what kind of thing it is.

~~~text
x_t       = system state at typed tick t
u_t       = proposed change / input at tick t
r_t       = receipt set available at tick t
C(x,r)    = checker over state and receipts
S         = admissible state set
Delta_t   = declared time-step width or event-step unit
H(X)      = Shannon information entropy of random variable X
P(E)      = probability of event E under stated assumptions
hash(a)   = declared digest of artifact a
~~~

Forbidden collapse:

~~~text
t_game != t_github != t_drive != t_event
P(E) != E
H_information != H_thermodynamic
hash(a) != truth(a)
state_transition != authority_transition
~~~

## 3. American Tick — discrete replay math

A replay system can model ordered events with a discrete tick:

~~~text
t_n = t_0 + n*Delta_t
~~~

But Delta_t must be typed.

Examples:

~~~text
GAME_TICK      = one dice round
REPLAY_TICK    = one deterministic replay step
GITHUB_TICK    = one observed commit transition
RECEIPT_TICK   = one appended receipt event
~~~

Never silently substitute one clock for another.

Repo-backed clock law:

~~~text
CHATGPT_MEMORY_TIMESTAMP
!= GITHUB_COMMIT_TIMESTAMP
!= DRIVE_CREATED_TIME
!= CLAIMED_EVENT_TIME
!= REAL_WORLD_EVENT_TIME
~~~

Developer test:

~~~text
assert(clock_a.type == clock_b.type)
OR
explicitly_normalize_and_record_conversion()
~~~

Ordering remains weaker than causation:

~~~text
A BEFORE B
does not imply
A CAUSED B
~~~

## 4. State-transition mechanics

Use the repo transition equation:

~~~text
PREVIOUS_STATE + CHANGE_EVENT + RECEIPT = NEXT_STATE
~~~

Formalized:

~~~text
x_(t+1) = F(x_t, u_t, r_t)
~~~

Promotion is admissible only when the transition predicate passes:

~~~text
C(x_t, u_t, r_t) = PASS
~~~

Otherwise:

~~~text
missing receipt      -> HOLD
contradiction        -> CONFLICT
invalid transition   -> REJECT
~~~

No state promotion may be inferred merely from the existence of a commit.

## 5. Fission operator

Fission decomposes a compound claim into independently testable atoms.

~~~text
FISSION(C)
= {a_1, a_2, ..., a_n}
~~~

Example:

~~~text
C = "The red die rolled six twice."

a_1 = a red die was used
a_2 = roll 1 was six
a_3 = roll 2 was six
a_4 = both rolls belong to the same recorded round
~~~

Locality law:

~~~text
PASS(a_i) does not imply PASS(a_j), i != j
~~~

Implementation sketch:

~~~text
for atom in fission(claim):
    receipt = resolve(atom)
    status  = check(atom, receipt)
    append(atom, receipt, status)
~~~

## 6. Fusion operator

Fusion is not "put the sentence back together because it sounds right."

~~~text
FUSION({a_i}, B)
~~~

requires:

~~~text
all required atoms admissible
AND
all logical bridges B admissible
~~~

If any required bridge is missing:

~~~text
FUSION_STATUS = HOLD
~~~

Evidence conservation:

~~~text
FUSION DOES NOT CREATE NEW EVIDENCE.
~~~

The output certainty cannot exceed what the input receipts and valid bridges support.

## 7. Collision mathematics

The existing family dice module uses pair counting.

For n observations:

~~~text
pairs(n) = n(n-1)/2
~~~

For a fair D6 and n <= 6 independent rolls:

~~~text
P(no collision)
= product(k=0 to n-1) ((6-k)/6)

P(collision)
= 1 - P(no collision)
~~~

Checkpoints:

~~~text
n=2 -> 1 pair  -> 16.67% collision
n=3 -> 3 pairs -> 44.44% collision
n=4 -> 6 pairs -> 72.22% collision
~~~

Developer lesson:

~~~text
COLLISION != IDENTITY
MATCH != SAME_OBJECT
SHARED_KEY != SHARED_ACTOR
SHARED_LABEL != SHARED_AUTHORITY
~~~

## 8. Certainly Entropy Demon

"Certainly Entropy Demon" is a fictional training character for uncertainty discipline.

For a fair D6:

~~~text
H(D6)
= -sum_i p_i log2 p_i
= log2(6)
~= 2.585 bits
~~~

For two independent fair D6 rolls:

~~~text
H(D6,D6)
= H(D6) + H(D6)
= log2(36)
~= 5.170 bits
~~~

After the result X=x is observed:

~~~text
H(X | X=x) = 0
~~~

Interpretation:

~~~text
uncertainty_about_recorded_roll = 0
~~~

Not:

~~~text
physical_entropy_of_room = 0
future_uncertainty = 0
system_truth = complete
~~~

Character lock line:

> You learned the roll. You did not learn the universe.

## 9. Deterministic replay

The existing receipt-stack doctrine defines deterministic replay as:

~~~text
same declared inputs
+ same manifest
+ same digest procedure
+ same lineage map
-> same digests and checker outcome
~~~

For developer code:

~~~text
replay(input_bundle) = output_bundle
~~~

A valid deterministic replay expects:

~~~text
replay(B) == replay(B)
~~~

for identical canonical bytes B and identical declared rules.

Random game outputs are different:

~~~text
same_game_method != same_random_roll
~~~

Therefore:

~~~text
DETERMINISTIC_CHECKER
can validate
NONDETERMINISTIC_INPUT
if the random draw itself is recorded as input.
~~~

## 10. Commit / reveal / verify dice

The existing dice protocol uses:

~~~text
COMMIT
→ ROLL
→ REVEAL
→ VERIFY
→ NO REROLLS
→ AUDIT THE ROLL
→ REPLAY
~~~

Developer interpretation:

~~~text
commitment = pre-result binding
reveal     = disclose committed input / seed / choice
verify     = test reveal against commitment
replay     = rerun validation from preserved inputs
~~~

Hard laws:

~~~text
ROLL != TRUTH
RANDOM_SELECTION != AUTHORITY
NO_REROLL_WITHOUT_RECEIPT
GAME_OUTPUT != SUBSTANTIVE_TRUTH
~~~

## 11. Brenda mechanics

The existing Brenda lesson maps classroom physics to system behavior:

~~~text
FORCE       -> pressure behind a claim
FRICTION    -> boundary slowing unsafe action
VELOCITY    -> rate of change
INERTIA     -> repeated old behavior
EQUILIBRIUM -> bounded state with categories separated
FEEDBACK    -> replay correction
~~~

For developers:

~~~text
velocity_of_change
= commits / declared interval

friction
= required gates before promotion

feedback
= checker output appended into next iteration
~~~

These are engineering metaphors unless a real physical model is explicitly supplied.

## 12. Speed is not certainty

Repository doctrine:

~~~text
GENERATE FAST
PROMOTE SLOW
REPLAY ALWAYS
~~~

Developer translation:

~~~text
candidate_generation_speed
!= validation_strength
~~~

A fast model may increase hypothesis throughput.

It does not increase the evidentiary weight of any particular hypothesis.

## 13. Physics-to-code pipeline

Use:

~~~text
human statement
→ transcript / source capture
→ domain typing
→ claim fission
→ receipt resolution
→ checker
→ state object
→ code / HTML / game artifact
→ commit
→ replay
→ append receipt
~~~

Never:

~~~text
emotion -> truth
math -> authority
physics -> inevitability
logic -> institutional decision
HTML -> proof
commit -> world truth
~~~

## 14. Game-to-developer bridge

Family game layer:

~~~text
DICE
→ lesson selection
→ prediction
→ observation
→ receipt
→ replay
→ reflection
~~~

Developer layer:

~~~text
EVENT
→ typed input
→ transition candidate
→ checker
→ receipt
→ deterministic replay
→ state classification
~~~

Bridge:

~~~text
GAME_TEACHES_PATTERN
DEVELOPER_SYSTEM_ENFORCES_PATTERN
GAME != VERIFIER
~~~

## 15. Test vectors

### V1 — Missing receipt

~~~text
claim_atom = A
receipt(A) = ABSENT

expected = HOLD
~~~

### V2 — Collision without identity proof

~~~text
label_1 = "X"
label_2 = "X"
identity_receipt = ABSENT

expected:
LABEL_COLLISION = OBSERVED
IDENTITY_BIND = HOLD
~~~

### V3 — Cross-clock comparison

~~~text
clock_A = GITHUB_COMMIT
clock_B = DRIVE_MODIFIED

expected:
DIRECT_SUBTRACTION_WITHOUT_NORMALIZATION = REJECT
TYPED_NORMALIZED_COMPARISON = ALLOWED
CAUSATION = NOT_ESTABLISHED
~~~

### V4 — Fission then fusion

~~~text
C -> {A,B,C}
PASS(A)
PASS(B)
HOLD(C)

expected:
FUSION(CLAIM) = HOLD
~~~

### V5 — Random result replay

~~~text
recorded_roll = 4
method_replay_produces_new_roll = 2

expected:
RANDOM_OUTCOME_DIFFERENCE != METHOD_FAILURE
ORIGINAL_RECEIPT remains 4
NEW_ROUND receipt records 2
~~~

### V6 — Entropy category error

~~~text
H(D6) = 2.585 bits
claim = "room thermodynamic entropy is 2.585 bits"

expected = REJECT_CATEGORY_ERROR
~~~

## 16. Developer checklist

Before promotion:

- type every clock
- type every random variable
- state model assumptions
- fission compound claims
- resolve receipts locally
- preserve HOLD
- validate bridges before fusion
- distinguish information entropy from thermodynamic entropy
- distinguish random result from deterministic replay
- preserve append-only history
- rerun from declared inputs
- keep authority false unless an external authority receipt independently establishes otherwise

## 17. Jason's Story / family-story boundary

The existing family-story command rail remains:

~~~text
MANUSCRIPT = UNBOUND
STORY_BIND = HOLD
REPLAY_RECEIPT = NOT_CREATED
AUTHORITY_CREATED = FALSE
FACTS_PROMOTED = 0
~~~

Therefore this handbook expands the public developer / teaching story only.

~~~text
HANDBOOK_CREATED
!= FAMILY_STORY_BOUND

NEW_GAME_SPEC
!= MANUSCRIPT_REPLAY_RECEIPT

JASON_STORY_LABEL
!= JAY_IDENTITY_BIND
~~~

No private family claim is promoted by this handbook.

## 18. Canonical developer equation

~~~text
UNDERSTANDING
= FISSION
+ TYPED_STATE
+ RECEIPTS
+ VALID_BRIDGES
+ REPLAY
- FAKE_CERTAINTY
~~~

Not literal dimensional physics. It is the teaching equation for this developer lane.

## 19. Lock line

~~~text
Type the symbol.
Split the claim.
Count the collisions.
Name the clock.
Measure uncertainty under stated assumptions.
Bind the receipt.
Fuse only what survives.
Replay the method.
Never let the dice choose truth.
Never let the metaphor become authority.
~~~

AUTHORITY_CREATED = FALSE
NO_FAKE_GREEN = TRUE
