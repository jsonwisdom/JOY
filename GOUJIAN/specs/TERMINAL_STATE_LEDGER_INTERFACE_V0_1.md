# TERMINAL_STATE_LEDGER_INTERFACE_V0_1

## STATUS: ARCHITECTURE_DRAFT
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE
## DEPLOYED: FALSE

This specification defines the Goujian terminal-state ledger interface for closing claims without deleting lineage.

Core rule:

```text
A tombstone without lineage is deletion.
A tombstone with parent_hash is custody.
```

## 1. Purpose

The terminal state ledger enforces append-only closure for claims that are no longer current, valid, or usable.

It supports three terminal states:

```text
REJECTED
DEPRECATED
SUPERSEDED
```

Terminal records do not mutate the original claim. They attach a closing entry that references the original claim by `parent_hash`.

## 2. Terminal State Object Schema

```json
{
  "$schema": "https://jaywisdom.base.eth/schemas/terminal-v1.json",
  "type": "object",
  "required": [
    "entry_type",
    "terminal_state",
    "parent_hash",
    "reason",
    "actor",
    "timestamp",
    "integrity_proof"
  ],
  "properties": {
    "entry_type": { "const": "TERMINAL_RECORD" },
    "terminal_state": {
      "type": "string",
      "enum": ["REJECTED", "DEPRECATED", "SUPERSEDED"]
    },
    "parent_hash": {
      "type": "string",
      "description": "Hash of the claim being terminated. Cannot be null."
    },
    "reason": {
      "type": "string",
      "description": "Structured human-readable reason, e.g. EVIDENCE_CONTRADICTS, LOGICALLY_INVALID, SUPERSEDED_BY_{hash}, DEPRECATED_DUE_TO_DOMAIN_SHIFT."
    },
    "actor": {
      "type": "string",
      "description": "ENS name, on-chain identity, DAO, JunZi agent, or multisig issuing the terminal record."
    },
    "timestamp": {
      "type": "integer",
      "description": "Unix time in seconds."
    },
    "integrity_proof": {
      "type": "object",
      "description": "Signature or witness proof over the canonical tombstone object."
    },
    "optional_redirect": {
      "type": "string",
      "description": "Required when terminal_state is SUPERSEDED. Points to replacement claim hash."
    }
  }
}
```

## 3. Contract Interface Draft

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface IGoujianTerminalStateLedgerV01 {
    enum TerminalState {
        NONE,
        REJECTED,
        DEPRECATED,
        SUPERSEDED
    }

    struct TerminalRecord {
        bytes32 parentHash;
        TerminalState terminalState;
        bytes32 reasonHash;
        address actor;
        uint64 timestamp;
        bytes32 integrityProofHash;
        bytes32 optionalRedirect;
    }

    event ClaimTerminated(
        bytes32 indexed parentHash,
        TerminalState indexed terminalState,
        address indexed actor,
        bytes32 reasonHash,
        bytes32 integrityProofHash,
        bytes32 optionalRedirect,
        uint64 timestamp
    );

    error ParentHashRequired();
    error InvalidTerminalState();
    error RedirectRequiredForSuperseded();
    error DirectUpdateForbidden();

    function terminateClaim(
        bytes32 parentHash,
        TerminalState terminalState,
        bytes32 reasonHash,
        bytes32 integrityProofHash,
        bytes32 optionalRedirect
    ) external returns (bytes32 terminalRecordHash);

    function latestTerminalRecord(bytes32 parentHash)
        external
        view
        returns (TerminalRecord memory record);

    function isTerminated(bytes32 parentHash)
        external
        view
        returns (bool);
}
```

## 4. Enforcement Rules

```text
parent_hash MUST NOT equal 0x0.
terminal_state MUST be REJECTED, DEPRECATED, or SUPERSEDED.
SUPERSEDED MUST include optional_redirect.
No direct UPDATE is allowed on an existing claim.
Correction path is TERMINATE + CREATE_NEW.
Original claims remain queryable forever unless the storage layer itself fails.
```

## 5. Reference Logic

```text
on terminateClaim(record):
  require parentHash != 0x0
  require terminalState in [REJECTED, DEPRECATED, SUPERSEDED]
  if terminalState == SUPERSEDED:
    require optionalRedirect != 0x0
  canonicalize record
  terminalRecordHash = hash(record)
  append terminalRecordHash to parentHash terminal index
  emit ClaimTerminated
```

## 6. Query Indexer Resolution

```text
resolveClaim(claimHash):
  claim = load claimHash
  tombstones = load terminal records where parentHash == claimHash

  if tombstones is empty:
    return claim.current_state

  latest = newest valid tombstone by timestamp and chain order

  if latest.terminalState == REJECTED:
    return TERMINATED_REJECTED + latest metadata

  if latest.terminalState == DEPRECATED:
    return TERMINATED_DEPRECATED + latest metadata

  if latest.terminalState == SUPERSEDED:
    replacement = load latest.optionalRedirect
    return TERMINATED_SUPERSEDED + replacement pointer + latest metadata
```

## 7. One-Way Ratchet Doctrine

```text
No silent demotion.
No deletion without tombstone.
No overwrite without parent_hash.
No fake green.
No finality without lineage.
```

## 8. Current Custody State

This artifact is a design and interface specification only.

```yaml
contract_deployed: false
runtime_verified: false
formal_audit_complete: false
schema_final: false
highest_defensible_state: ARCHITECTURE_DRAFT
truth_state: YELLOW
```
