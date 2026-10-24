#!/usr/bin/env python3
"""Verify JSONWisdom Layer 3 Atomic Record chain v0.1.

Locked profile:
- RFC 8785 JCS data model
- ASCII object keys only
- integers only; floats rejected
- duplicate object keys rejected
- UTF-8, sorted keys, no insignificant whitespace
- entry = SHA-256(raw previous digest || raw payload digest)

The verifier checks deterministic hashes and no-fake-green invariants. It does
not claim legal, tax, identity, or global authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ZERO_DIGEST = "00" * 32
ALLOWED_OFFICIAL_SOURCES = {
    "OFFICIAL_STATE_SOURCE",
    "OFFICIAL_FEDERAL_SOURCE",
    "FILED_RETURN",
    "OFFICIAL_NOTICE",
    "AGENCY_ACCOUNT_RECORD",
}


class DuplicateKeyError(ValueError):
    pass


def no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicates)


def enforce_jcs_safe(value: Any, path: str = "$") -> None:
    if isinstance(value, float):
        raise ValueError(f"{path}: floats are outside JSONWISDOM_JCS_SAFE_V0_1")
    if isinstance(value, dict):
        for key, child in value.items():
            if not isinstance(key, str):
                raise ValueError(f"{path}: non-string object key")
            if not key.isascii():
                raise ValueError(f"{path}: non-ASCII key outside locked profile: {key!r}")
            enforce_jcs_safe(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            enforce_jcs_safe(child, f"{path}[{index}]")
    elif value is None or isinstance(value, (str, int, bool)):
        return
    else:
        raise ValueError(f"{path}: unsupported JSON type {type(value).__name__}")


def jcs_bytes(value: Any) -> bytes:
    enforce_jcs_safe(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_no_fake_green(record: dict[str, Any]) -> None:
    outcome = record["replay_outcome"]
    surface = record["authority_surface"]
    scope = record["claim_scope"]
    entrance = record["authority_entrance"]
    evidence = record["evidence_refs"]

    if record["legal_effect_claimed"] or record["tax_effect_claimed"]:
        if outcome != "MATCH":
            raise ValueError(f"{record['record_id']}: effect claimed without MATCH")
        if surface not in {"STATE", "FEDERAL"}:
            raise ValueError(f"{record['record_id']}: effect claimed outside government lane")
        if not entrance["present"]:
            raise ValueError(f"{record['record_id']}: effect claimed without authority entrance")
        if entrance["source_type"] not in ALLOWED_OFFICIAL_SOURCES:
            raise ValueError(f"{record['record_id']}: effect claimed without official source")

    if scope == "PHYSICAL_LOCATION" and (
        record["legal_effect_claimed"] or record["tax_effect_claimed"]
    ):
        raise ValueError(f"{record['record_id']}: geometry promoted into legal or tax effect")

    if scope == "WALLET_IDENTITY" and outcome == "MATCH":
        if not any(item["artifact_type"] == "PERSON_CONTROL_PROOF" for item in evidence):
            raise ValueError(f"{record['record_id']}: wallet identity MATCH without control proof")

    if surface == "FEDERAL" and outcome == "MATCH":
        if not entrance["present"] or entrance["source_type"] not in {
            "OFFICIAL_FEDERAL_SOURCE",
            "FILED_RETURN",
            "OFFICIAL_NOTICE",
            "AGENCY_ACCOUNT_RECORD",
        }:
            raise ValueError(f"{record['record_id']}: federal MATCH without federal entrance")


def verify(ledger_path: Path, repo_root: Path) -> None:
    document = load_json(ledger_path)
    entries = document["entries"]

    if document["authority"] is not False or document["verification"] is not False:
        raise ValueError("ledger must preserve authority=false and verification=false")
    if document["no_fake_green"] is not True:
        raise ValueError("no_fake_green must be true")
    if document["chain_length"] != len(entries):
        raise ValueError("chain_length mismatch")

    for binding_name, binding in document["bindings"].items():
        path = repo_root / binding["path"]
        if not path.is_file():
            raise ValueError(f"missing bound {binding_name} artifact: {path}")
        actual = sha256_file(path)
        if actual != binding["sha256"]:
            raise ValueError(
                f"{binding_name} hash mismatch: expected {binding['sha256']} got {actual}"
            )

    previous = ZERO_DIGEST
    for expected_sequence, entry in enumerate(entries):
        path = repo_root / entry["record_path"]
        envelope = load_json(path)
        record = envelope["record"]
        embedded = envelope["ledger"]

        if entry["sequence"] != expected_sequence:
            raise ValueError(f"{entry['record_id']}: manifest sequence mismatch")
        if record["record_id"] != entry["record_id"]:
            raise ValueError(f"{entry['record_id']}: record identifier mismatch")
        if embedded["sequence"] != entry["sequence"]:
            raise ValueError(f"{entry['record_id']}: embedded sequence mismatch")
        if entry["previous_entry_digest"] != previous:
            raise ValueError(f"{entry['record_id']}: manifest previous digest mismatch")
        if embedded["previous_entry_digest"] != previous:
            raise ValueError(f"{entry['record_id']}: embedded previous digest mismatch")
        if embedded["canonicalization"] != "RFC8785-JCS":
            raise ValueError(f"{entry['record_id']}: canonicalization drift")
        if embedded["canonicalization_profile"] != "JSONWISDOM_JCS_SAFE_V0_1":
            raise ValueError(f"{entry['record_id']}: profile drift")
        if embedded["hash_input_rule"] != "ENTRY=SHA256(raw_previous_digest||raw_payload_digest)":
            raise ValueError(f"{entry['record_id']}: hash-input drift")
        if embedded["authority"] is not False or embedded["verification_claimed"] is not False:
            raise ValueError(f"{entry['record_id']}: authority or verification elevation")

        payload_digest = sha256_bytes(jcs_bytes(record))
        if payload_digest != entry["payload_digest"] or payload_digest != embedded["payload_digest"]:
            raise ValueError(f"{entry['record_id']}: payload digest mismatch")

        entry_digest = sha256_bytes(bytes.fromhex(previous) + bytes.fromhex(payload_digest))
        if entry_digest != entry["entry_digest"] or entry_digest != embedded["entry_digest"]:
            raise ValueError(f"{entry['record_id']}: entry digest mismatch")

        for evidence in record["evidence_refs"]:
            expected_hash = evidence["sha256"]
            source_uri = evidence["source_uri"].split("#", 1)[0]
            if expected_hash is None:
                continue
            source_path = repo_root / source_uri
            if not source_path.is_file():
                raise ValueError(f"{entry['record_id']}: missing evidence {source_uri}")
            if sha256_file(source_path) != expected_hash:
                raise ValueError(f"{entry['record_id']}: evidence hash mismatch for {source_uri}")

        check_no_fake_green(record)
        previous = entry_digest

    if previous != document["chain_head"]:
        raise ValueError("chain_head mismatch")

    print(json.dumps({
        "artifact": str(ledger_path),
        "chain_id": document["chain_id"],
        "chain_length": len(entries),
        "chain_head": previous,
        "deterministic_chain_match": True,
        "bound_artifacts_match": True,
        "no_fake_green_checks": "PASS",
        "authority": False,
        "verification_claimed": False,
        "receiptos_status": "PENDING"
    }, indent=2, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ledger",
        default="ledger/replay/SELLER_TWO_STATE_CRYPTO_ATOMIC_LEDGER_V0_1.json",
    )
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    verify(Path(args.ledger), Path(args.repo_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
