# JOYSPACE Librarian × HEIDEE — Family Role Repair v0.2

21 November 2026 | CI-FIRST | JOY FIRST | REVIEW ONLY | authority=false

## Finding
JOY already specifies the Librarian as an advisory source-routing and clarification role. The role-membrane record is documentation, not proof of live service. HEIDEE remains independently governed. The JOY Family Security OODA v0.1 tests did not exercise an authenticated cross-repo Librarian adapter.

## Repair
- A NEW offline candidate module at tools/joyspace_librarian_gate_v0_2.py pins four original JOY source blobs and two HEIDEE source blobs by exact Git blob SHA1.
- Missing, corrupted, or drifted source bytes fail closed. No file paths from user input, no external lookups or family identifiers.
- Only the existing six synthetic JOY OODA scenario IDs are accepted. Each maps to a fixed suggestion shelf, never a free-text instruction.
- The Librarian suggests; Boss Bre may pause; ALMS provides a public-source replay; JOY provides education; HEIDEE makes independent decisions.
- REJECT > CONFLICT > HOLD > PASS; every mechanical PASS produces EFFECTIVE_DECISION=HOLD.
- JSON receipts are deterministic and contain only public source hashes, scenario hashes, and explicit false permissions.
- No real person's relationship, consent, identity, custody, enrollment, publication, contract, or deployment can be inferred from software state.

## Exact source pins
JOY main: a9d9bf1678cbc97703df7582ec5879b6ea5a0bd7
JOy Librarian Git blob: 95f216f6e23e5edf72937f03e7d0d7f579983f99
JOY role membrane: de6c243360ba289d71906421ff7b80342f6ca0c2
JOY authority boundary: afe19d59a507fa47522280249e0d1645a8a039d4
JOY Boss Bre safety: 2c66e091177c37b6156dae27ab8970be36caec7e
HEIDEE master: 8e61fc2ce623b59feca2a3b231390bd5c968dbe7
HEIDEE family legacy blob: 79e66f3281f8cb6272a7ea03058d4f12026ddb36
HEIDEE learning rail blob: d05fb243d44b05fef6be502cbaaf0ee4dded8285

## Verification
Earlier JOY v0.1 review CI run 44921628465: SUCCESS, 32 original Python tests.
Wolfram independently verified 4^4 = 256 decision combinations. A synthetic all-PASS combination does not grant permission.
New branch CI must confirm current v0.2 tests and positive/negative runner receipts before promotion.

## Windows PowerShell reproduction from JOY review checkout
Install no extra packages; use Python 3. Clone the pinned HEIDEE snapshot into a separate sibling folder.

    py -3 -m unittest discover -s tests -p 'test_joyspace_librarian_gate_v0_2.py' -v
    py -3 tools/joyspace_librarian_gate_v0_2.py --request drills/FAMILY_SECURITY_OODA_EXAMPLE_V0_1.json --joy-root . --heidee-root ..\HEIDEE --receipt librarian-proof.json

Expected: SIMULATION_VERDICT=PASS, EFFECTIVE_DECISION=HOLD, AUTHORITY=false.
Bad fixture: drills/FAMILY_SECURITY_OODA_NEGATIVE_V0_1.json must return REJECT exit 2.

No GitHub merge, default branch retarget, actual family enrollment, private family-data disclosure, Cloudflare deployment, contact, account change, wallet, or spending.

FAMILY FIRST · LIBRARIAN SUGGESTS · HEIDEE INDEPENDENT · NO FAKE GREEN.
