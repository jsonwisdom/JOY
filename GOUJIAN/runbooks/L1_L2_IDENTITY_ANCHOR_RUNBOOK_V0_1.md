# L1_L2_IDENTITY_ANCHOR_RUNBOOK_V0_1

## STATUS: ANCHOR_RUNBOOK_PREPARED
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE
## ONCHAIN_ANCHOR_EXECUTED: FALSE

Purpose: anchor the mutable L2 identity engine state for `jaywisdom.base.eth` into the immutable L1 seal `jaywisdom.eth` through ENS text records.

Core mapping:

- `jaywisdom.eth` = immutable Seal / L1 non-repudiation surface
- `jaywisdom.base.eth` = mutable Engine / L2 operating custody surface

Guardrail:

> Prepared commands are not proof. Only confirmed L1 transaction hashes are proof.

## Required local tools

- `git`
- `jq`
- `sha256sum`
- Foundry `cast`
- Ethereum mainnet RPC URL in `ETH_RPC_URL`
- signing account controlled by the manager of `jaywisdom.eth`

## Recommended challenge period

```text
CHALLENGE_PERIOD_SECONDS=604800
```

This creates a 7-day review window between the L2 engine commitment and L1 finality interpretation.

## Copy-paste execution block

Run from the repository root.

```bash
set -euo pipefail

ENS_NAME="jaywisdom.eth"
ENGINE_NAME="jaywisdom.base.eth"
REGISTRY="0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e"
CHALLENGE_PERIOD_SECONDS="604800"
L2_STATE_FILE="${L2_STATE_FILE:-GOUJIAN/registry/identity_sync_v0.1.json}"

: "${ETH_RPC_URL:?Set ETH_RPC_URL first}"
: "${FOUNDRY_ACCOUNT:?Set FOUNDRY_ACCOUNT to your Foundry keystore account name}"

test -f "$L2_STATE_FILE"
mkdir -p GOUJIAN/anchors GOUJIAN/receipts

ANCHOR_TS="$(date +%s)"
CHALLENGE_ENDS="$((ANCHOR_TS + CHALLENGE_PERIOD_SECONDS))"
ANCHOR_COMMIT="$(git rev-parse HEAD)"

jq -S . "$L2_STATE_FILE" > GOUJIAN/anchors/l2_identity_anchor_payload_v0_1.canonical.json
ANCHOR_HASH="0x$(sha256sum GOUJIAN/anchors/l2_identity_anchor_payload_v0_1.canonical.json | awk '{print $1}')"
NODE="$(cast namehash "$ENS_NAME")"
RESOLVER="$(cast call "$REGISTRY" 'resolver(bytes32)(address)' "$NODE" --rpc-url "$ETH_RPC_URL")"

echo "ENS_NAME=$ENS_NAME"
echo "ENGINE_NAME=$ENGINE_NAME"
echo "NODE=$NODE"
echo "RESOLVER=$RESOLVER"
echo "ANCHOR_HASH=$ANCHOR_HASH"
echo "ANCHOR_TS=$ANCHOR_TS"
echo "CHALLENGE_ENDS=$CHALLENGE_ENDS"
echo "ANCHOR_COMMIT=$ANCHOR_COMMIT"

echo "== CURRENT TEXT RECORDS BEFORE WRITE =="
cast call "$RESOLVER" 'text(bytes32,string)(string)' "$NODE" 'operational_anchor' --rpc-url "$ETH_RPC_URL" || true
cast call "$RESOLVER" 'text(bytes32,string)(string)' "$NODE" 'anchor_timestamp' --rpc-url "$ETH_RPC_URL" || true
cast call "$RESOLVER" 'text(bytes32,string)(string)' "$NODE" 'anchor_commit' --rpc-url "$ETH_RPC_URL" || true
cast call "$RESOLVER" 'text(bytes32,string)(string)' "$NODE" 'anchor_challenge_ends' --rpc-url "$ETH_RPC_URL" || true

echo "== WRITE ENS TEXT RECORDS: HUMAN SIGNING REQUIRED =="
TX_OPERATIONAL_ANCHOR="$(cast send "$RESOLVER" 'setText(bytes32,string,string)' "$NODE" 'operational_anchor' "$ANCHOR_HASH" --rpc-url "$ETH_RPC_URL" --account "$FOUNDRY_ACCOUNT" --json | jq -r '.transactionHash')"
TX_ANCHOR_TIMESTAMP="$(cast send "$RESOLVER" 'setText(bytes32,string,string)' "$NODE" 'anchor_timestamp' "$ANCHOR_TS" --rpc-url "$ETH_RPC_URL" --account "$FOUNDRY_ACCOUNT" --json | jq -r '.transactionHash')"
TX_ANCHOR_COMMIT="$(cast send "$RESOLVER" 'setText(bytes32,string,string)' "$NODE" 'anchor_commit' "$ANCHOR_COMMIT" --rpc-url "$ETH_RPC_URL" --account "$FOUNDRY_ACCOUNT" --json | jq -r '.transactionHash')"
TX_ANCHOR_ENGINE="$(cast send "$RESOLVER" 'setText(bytes32,string,string)' "$NODE" 'anchor_engine' "$ENGINE_NAME" --rpc-url "$ETH_RPC_URL" --account "$FOUNDRY_ACCOUNT" --json | jq -r '.transactionHash')"
TX_CHALLENGE_ENDS="$(cast send "$RESOLVER" 'setText(bytes32,string,string)' "$NODE" 'anchor_challenge_ends' "$CHALLENGE_ENDS" --rpc-url "$ETH_RPC_URL" --account "$FOUNDRY_ACCOUNT" --json | jq -r '.transactionHash')"

cat > GOUJIAN/receipts/L1_L2_IDENTITY_ANCHOR_RECEIPT_V0_1.md <<EOF
# L1_L2_IDENTITY_ANCHOR_RECEIPT_V0_1

## STATUS: L1_ANCHOR_SUBMITTED
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE

ENS seal: $ENS_NAME
L2 engine: $ENGINE_NAME
State file: $L2_STATE_FILE
Canonical payload: GOUJIAN/anchors/l2_identity_anchor_payload_v0_1.canonical.json
Anchor hash: $ANCHOR_HASH
Anchor timestamp: $ANCHOR_TS
Challenge ends: $CHALLENGE_ENDS
Anchor commit: $ANCHOR_COMMIT
Resolver: $RESOLVER

Transactions:
- operational_anchor: $TX_OPERATIONAL_ANCHOR
- anchor_timestamp: $TX_ANCHOR_TIMESTAMP
- anchor_commit: $TX_ANCHOR_COMMIT
- anchor_engine: $TX_ANCHOR_ENGINE
- anchor_challenge_ends: $TX_CHALLENGE_ENDS

Verification state: PENDING_READBACK
EOF

git add GOUJIAN/anchors/l2_identity_anchor_payload_v0_1.canonical.json GOUJIAN/receipts/L1_L2_IDENTITY_ANCHOR_RECEIPT_V0_1.md
git commit -m "receipt(goujian): record L1 L2 identity anchor submission"

echo "== NEXT READBACK =="
echo "cast call $RESOLVER 'text(bytes32,string)(string)' $NODE operational_anchor --rpc-url \$ETH_RPC_URL"
echo "git push origin $(git branch --show-current)"
```

## State interpretation

- Before the `cast send` transactions confirm: `ANCHOR_PREPARED`
- After transaction hashes exist but before read-back: `L1_ANCHOR_SUBMITTED`
- After ENS read-back matches the local hash: `L1_ANCHOR_READBACK_MATCH`
- After challenge period expires without dispute: `L1_ANCHOR_FINALIZED_BY_POLICY`
- If read-back mismatches: `MISMATCH_TERMINAL_REQUIRED`

## Failure rule

No dashboard may mark the L1 anchor green until:

1. ENS text read-back equals the canonical local anchor hash.
2. The receipt includes confirmed transaction hashes.
3. The challenge window has either not expired and is labeled pending, or has expired and is labeled finalized-by-policy.
