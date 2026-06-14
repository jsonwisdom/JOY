# BRENDA HTTP BYTE CHECK CHECKLIST V0.1

```text
STATUS: CHECKLIST_RECORDED
LANE: BOSS_BRENDA
SUBJECT: BRENDA_PERSONALITY_V0_1
TRUTH_STATE: YELLOW_PROTECTED
NO_FAKE_GREEN: TRUE
PUBLIC_GREEN: BLOCKED_UNTIL_HTTP_BYTE_MATCH
HUMAN_APPROVAL_REQUIRED: TRUE
```

## Target Public Route

```text
EXPECTED_ROUTE: https://jsonwisdom.github.io/JOY/joyspace/birthday-brenda-zora-flywheel.html
REPO_SOURCE: joyspace/birthday-brenda-zora-flywheel.html
REQUIRED_MARKERS:
  - BIRTHDAY_BRENDA_ZORA_FLYWHEEL_V0_1
  - BRENDA_PERSONALITY_V0_1
```

## Preconditions

- Repo source exists on `jsonwisdom/JOY@main`.
- Brenda personality leaf is repo-recorded.
- Receipt `FAMILY/receipts/BRENDA_PERSONALITY_LEAF_V0_1.md` exists.
- No private biography, likeness, consent claim, investment claim, or truth-authority claim is promoted.
- GitHub Pages deployment must serve the target route before public green can be considered.

## Byte Check Steps

```bash
set -euo pipefail

cd "${JOY_REPO_DIR:-$HOME/COMPUTERWISDOM/JOY}"

ROUTE="https://jsonwisdom.github.io/JOY/joyspace/birthday-brenda-zora-flywheel.html"
SRC="joyspace/birthday-brenda-zora-flywheel.html"
OUT="_truth/audit/brenda_http_byte_check_$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$OUT"

printf '== REPO SOURCE HASH ==\n' | tee "$OUT/receipt.txt"
sha256sum "$SRC" | tee -a "$OUT/receipt.txt"

printf '\n== HTTP STATUS ==\n' | tee -a "$OUT/receipt.txt"
curl -fsSL -D "$OUT/headers.txt" "$ROUTE" -o "$OUT/public.html"
awk 'NR==1 {print}' "$OUT/headers.txt" | tee -a "$OUT/receipt.txt"

printf '\n== PUBLIC BODY HASH ==\n' | tee -a "$OUT/receipt.txt"
sha256sum "$OUT/public.html" | tee -a "$OUT/receipt.txt"

printf '\n== MARKER CHECK ==\n' | tee -a "$OUT/receipt.txt"
grep -q 'BIRTHDAY_BRENDA_ZORA_FLYWHEEL_V0_1' "$OUT/public.html"
grep -q 'BRENDA_PERSONALITY_V0_1' "$OUT/public.html"
printf 'MARKERS_OK=true\n' | tee -a "$OUT/receipt.txt"

printf '\n== BYTE MATCH CHECK ==\n' | tee -a "$OUT/receipt.txt"
if cmp -s "$SRC" "$OUT/public.html"; then
  printf 'SHA256_REPO_EQUALS_PUBLIC=true\n' | tee -a "$OUT/receipt.txt"
  printf 'PUBLIC_GREEN_CANDIDATE=true\n' | tee -a "$OUT/receipt.txt"
else
  printf 'SHA256_REPO_EQUALS_PUBLIC=false\n' | tee -a "$OUT/receipt.txt"
  printf 'PUBLIC_GREEN_CANDIDATE=false\n' | tee -a "$OUT/receipt.txt"
fi

printf '\n== HUMAN APPROVAL ==\n' | tee -a "$OUT/receipt.txt"
printf 'HUMAN_APPROVAL_REQUIRED=true\n' | tee -a "$OUT/receipt.txt"
printf 'FINAL_GREEN_REQUIRES_MANUAL_RULING=true\n' | tee -a "$OUT/receipt.txt"

cat "$OUT/receipt.txt"
```

## Green Rule

```text
PUBLIC_GREEN = HTTP_200
             + ROUTE_PRESENT
             + REQUIRED_MARKERS_PRESENT
             + SHA256_REPO_SOURCE_EQUALS_SHA256_PUBLIC_BODY
             + CHANGELOG_OR_RECEIPT_UPDATE
             + HUMAN_APPROVAL
```

## Failure Rules

- If HTTP status is not `200`, state remains `YELLOW_PROTECTED`.
- If marker is missing, state remains `YELLOW_PROTECTED`.
- If repo source hash does not equal public body hash, state remains `YELLOW_PROTECTED`.
- If human approval is missing, state remains `YELLOW_PROTECTED`.
- No automatic promotion to GREEN.

## Ruling

Checklist is recorded. Brenda remains repo-recorded and protected. Public green is still blocked until the live route passes HTTP byte match and human approval.
