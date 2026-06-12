# PSR Signature Layer Selection — V0.1

**Status:** design note  
**Lane:** GCRE / PSR  
**Authority:** false  
**No fake green:** true  
**Depends on:** `scripts/gcre/psr-kv-simulator.cjs`

---

## Recommendation

Proceed with the Signature Layer before Lattice Mapping.

The simulator is now deterministic, but determinism alone does not stop an adversary with write access from fabricating a new internally consistent chain.

The next security boundary is signer identity and verification.

---

## Selected Signing Scheme

Initial target: **Ed25519**.

Reasons:

- deterministic signatures
- small public keys
- small signatures
- strong ecosystem support
- suitable for receipt envelopes
- easier cross-language implementation than many alternatives

---

## Receipt Signing Boundary

The signature layer should not sign arbitrary JavaScript object memory.

It should sign a canonical receipt envelope:

```json
{
  "psrVersion": "PSRKV-0.1",
  "hash": "<transition_hash>",
  "prevHash": "<previous_hash>",
  "transitionId": "<transition_id>",
  "stateTransitionDigest": "<canonical_digest>",
  "signer": "<public_key_or_key_id>",
  "signatureAlgorithm": "Ed25519"
}
```

The signature verifies that an authorized signer witnessed or produced the receipt hash.

---

## Required Methods

The next implementation should add:

- `generateKeypair()`
- `signReceiptEnvelope(receipt, privateKey)`
- `verifyReceiptSignature(receipt, publicKey)`
- `verifyChain({ requireSignatures: true })`

---

## Fail-Closed Rules

When signature mode is enabled:

- missing signature fails verification
- malformed signature fails verification
- unknown signer fails verification
- receipt hash mismatch fails before signature acceptance
- valid signature over invalid hash still fails

---

## Non-Goals for V0.1

- no key rotation protocol yet
- no threshold signatures yet
- no hardware-backed key storage yet
- no lattice-derived trust weighting yet

Those belong after the single-signer envelope is replay-clean.

---

## Next Gate

```json
{
  "artifact": "PSR_SIGNATURE_LAYER_SELECTION_V0_1",
  "selected_scheme": "Ed25519",
  "next_gate": "IMPLEMENT_PSR_SIG_LAYER_V0_1",
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```
