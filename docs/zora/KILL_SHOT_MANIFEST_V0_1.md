# KILL SHOT MANIFEST V0.1

**Identity:** `jaywisdom.base.eth`  
**Purpose:** One-shot launch discipline for Zora / Art Auctions / Proof Assets  
**Doctrine:** No signal without execution. No execution claim without receipt.

---

## 1. State Machine

This protocol prevents premature narrative signaling. Transitions are strictly gated by proof of execution.

| Phase | State | Truth State | Required Verification |
| :--- | :--- | :--- | :--- |
| **PREP** | `PREP` | `YELLOW` | `final_asset`, `metadata_json`, `ipfs_cid`, `calldata` |
| **AUDIT** | `AUDIT` | `YELLOW` | `simulation_pass`, `no_revert`, `target_contract_match` |
| **STRIKE** | `STRIKE` | `TRANSITION` | `broadcast_tx_hash` |
| **CONFIRM** | `CONFIRM` | `GREEN_FOR_TX_ONLY` | `tx_receipt`, `status_0x1`, `block_number`, `logs` |
| **NARRATIVE** | `NARRATIVE` | `LIVE` | `receipt_link`, `tx_hash`, `asset_cid` |

---

## 2. Hard Rule

**No public narrative before receipt confirmation.**

Signals emitted prior to receipt confirmation are unauthorized and violate protocol hygiene.

---

## 3. Salt Generation Policy

To ensure replayability and avoid cross-asset collision, all salts must be unique per asset. Do not use global salts.

**Format:**

```text
JAYWISDOM|BASE|ZORA|AUCTION|<ASSET_ID>|V0_1
```

**Example Generation:**

```bash
cast keccak "JAYWISDOM|BASE|ZORA|AUCTION|VISUAL_CONSTITUTION_COVER|V0_1"
```

---

## 4. Execution Flow

1. **Prepare:** Assemble assets and generate calldata via `c3_zora_factory_calldata_draft.sh`.
2. **Simulate:** Audit against the `AUDIT` state requirements.
3. **Broadcast:** Execute Strike. Halt narrative.
4. **Receipt:** Poll for transaction receipt (`status_0x1`).
5. **Live:** Only upon receipt confirmation, push narrative vector.

---

## 5. Boundary

Broadcast is not proof. A transaction hash alone is not green. The first admissible green surface is a confirmed transaction receipt with success status and block inclusion.

```text
BROADCAST_TX_HASH != RECEIPT_CONFIRMED
RECEIPT_CONFIRMED != FULL_SEMANTIC_AUTHORITY
GREEN_FOR_TX_ONLY != GLOBAL_GREEN
NO_FAKE_GREEN_ACTIVE
```
