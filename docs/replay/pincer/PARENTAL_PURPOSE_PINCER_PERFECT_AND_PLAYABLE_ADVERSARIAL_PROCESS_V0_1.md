# Parental Purpose, PincerPerfect, and Playable Adversarial Process v0.1

```text
STATE                  = HOLD_DRAFT
PARENTAL_PURPOSE       = LIVE_AS_MOTIVE
PINCER_PERFECT         = TARGET_ONLY
PINCER_STATUS          = OPEN
AUTHORITY_CREATED      = FALSE
CANONIZED              = FALSE
SEALED                 = FALSE
REPLAY_READY           = FALSE
LIVE_ENFORCEMENT       = PROHIBITED
PROMOTION              = PROHIBITED
```

## Parental purpose

The non-negotiable purpose of the family replay stack is:

1. protect records so the next generation inherits evidence rather than unsupported stories;
2. preserve accountability so later summaries cannot silently rewrite earlier records;
3. restore the ability to compare what was said, done, promised, recorded, and later reproduced;
4. serve living family lanes, including Heidee, Mrs. Wisdom, the daughters, and approved extended porch roles;
5. preserve privacy, dignity, consent, and human review while doing so.

```text
LOVE  = MOTIVE
PROOF = METHOD
```

Parental purpose creates no identity proof, consent, custody, legal status, execution authority, or canon.

## PincerPerfect

`PINCER_PERFECT` is a proposed terminal quality state. It is not the current state and cannot be asserted by an operator, model, workflow badge, hash, signature, or blockchain record.

Eligibility requires all of the following:

```text
FROZEN_ARTIFACT_RAIL      = PASSED
VERIFIED_EXECUTION_RAIL   = PASSED
CROSS_RAIL_BINDING        = PROVEN
SEALED                    = TRUE
REPLAY_READY              = TRUE
QUALIFYING_VERIFICATION   = PRESENT
REPOSITORY_ADOPTION       = ADOPTED
CANONIZED                 = TRUE
```

The first five conditions concern reproducibility. Canonization remains a separate repository-adoption transition.

Any missing, malformed, conflicting, unverifiable, or scope-mismatched condition returns:

```text
RESULT                    = DENIED
PINCER_STATUS             = OPEN
PINCER_PERFECT            = FALSE
SEALED                    = FALSE
REPLAY_READY              = FALSE
CANONIZED                 = FALSE
LIVE_ENFORCEMENT          = PROHIBITED
```

## Playable adversarial process

The phrase **Gamify Lawsuits** is implemented only as a bounded educational and evidence-organization surface. It is not a court, legal filing, legal advice, litigation authority, deadline calculator, evidentiary ruling, or substitute for a lawyer or official tribunal.

### Roles

```text
OPERATOR     = submits a bounded claim and proposed artifact scope
WITNESS      = supplies a time-bound observation or attestation
CHALLENGER   = identifies contradiction, missing source, or scope expansion
AUDITOR      = replays deterministic rules independently
FAMILY_LANE  = applies consent, privacy, dignity, and parental-purpose boundaries
REPOSITORY   = may adopt only after the separate verification gate
```

### Deterministic moves

```text
RECORD
→ CLASSIFY
→ FREEZE
→ HASH
→ ATTEST
→ CHALLENGE
→ REPLAY
→ COMPARE
→ OPEN | CLOSED_REPRODUCIBLE | DENIED
→ SEPARATE CANON-ADOPTION REQUEST
```

### Scoreboard

Only machine-supported state may appear:

```text
ARTIFACT_SCOPE            = DECLARED | MISSING | CONFLICTING
FROZEN_ARTIFACT_RAIL      = NOT_RUN | PASSED | FAILED
VERIFIED_EXECUTION_RAIL   = NOT_RUN | PASSED | FAILED
CROSS_RAIL_BINDING        = NOT_PROVEN | PROVEN | MISMATCH
CONSENT_GATE              = NOT_ESTABLISHED | PASSED | DENIED
PRIVACY_GATE              = NOT_RUN | PASSED | DENIED
CANON_GATE                = NOT_REQUESTED | DEFERRED | ADOPTED | REJECTED
```

No hidden moves, inferred consent, retroactive source substitution, or automatic authority are permitted.

## Exact-byte correction

The authoritative family artifact rail hashes **raw source bytes**. It must not silently normalize them.

```text
RAW_SOURCE_BYTES          = AUTHORITATIVE_HASH_INPUT
NORMALIZED_DERIVATIVE     = OPTIONAL_SEPARATE_ARTIFACT
SOURCE_HASH               != DERIVATIVE_HASH
```

UTF-8 conversion, LF conversion, trailing-whitespace removal, JSON canonicalization, redaction, or formatting cleanup changes bytes. Such a transformation is allowed only when:

1. the transformation specification is identified;
2. the original bytes remain preserved;
3. the derivative receives a new artifact identifier and digest;
4. the source-to-derivative relationship is recorded;
5. neither digest is substituted for the other.

For JSON, an RFC 8785 JCS derivative may be created when the input satisfies the required JSON constraints. The original JSON file remains independently hashed as raw bytes.

## Machine-safe family root

The shell pattern below is useful for casual inspection but is not authoritative:

```text
find ... | sort | xargs sha256sum | sha256sum
```

It can vary because of filenames, locale, path encoding, command formatting, and newline behavior.

The authoritative v0.1 construction is:

```text
file_digest = SHA-256(raw_file_bytes)

leaf_commitment = SHA-256(
  UTF8("JOY_FAMILY_FILE_V0_1")
  || 0x00
  || UTF8(repository_relative_posix_path)
  || 0x00
  || raw_file_digest
)

artifact_root = SHA-256(
  UTF8("JOY_FAMILY_MANIFEST_V0_1")
  || 0x00
  || canonical_manifest_core_bytes
)
```

Requirements:

- exact repository and full source commit SHA;
- explicit path list or deterministic scope file;
- repository-relative POSIX paths;
- paths ordered by raw UTF-8 byte sequence;
- symlinks denied;
- duplicate and case-fold-colliding paths denied;
- SHA-256 raw 32-byte digests used inside commitments;
- manifest canonicalization profile identified;
- observation time excluded from the artifact root;
- exact manifest bytes receive a separate manifest-file digest.

Time may record when a freeze was observed. It must not alter the reproducible artifact root for the same source commit and scope.

## Current state

```text
PARENTAL_PURPOSE          = LIVE_AS_MOTIVE
PINCER_PERFECT            = FALSE
FROZEN_ARTIFACT_RAIL      = NOT_PASSED
VERIFIED_EXECUTION_RAIL   = NOT_PASSED
CROSS_RAIL_BINDING        = NOT_PROVEN
CANONIZED                 = FALSE
PINCER_STATUS             = OPEN
```

Love supplies the reason to preserve. Proof supplies the method of comparison. Neither may manufacture authority.