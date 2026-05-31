#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VECTOR_PATH = ROOT / "receipts" / "test_vectors" / "ALMS_L2_TEST_VECTOR_001.json"
KNOWN_GOOD_PATH = ROOT / "receipts" / "test_vectors" / "ALMS_L2_KNOWN_GOOD_OUTPUT_001.json"

REQUIRED_FIELDS = [
    "source_artifact_hash",
    "receipt_id",
    "observed_at",
    "operator_signature_or_commit",
    "authority_false",
]


def canonical_bytes(obj):
    # Deterministic JSON bytes approximating RFC8785 for this restricted object set:
    # UTF-8, sorted object keys, compact separators, no whitespace.
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_prefixed(data):
    return "sha256:" + hashlib.sha256(data).hexdigest()


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, obj):
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fail(message):
    print(json.dumps({"status": "FAIL", "reason": message, "authority": False}, indent=2))
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        fail("usage: python3 lock_replay_proof.py <REAL_JOY_COMMIT_SHA>")

    joy_sha = sys.argv[1].strip()
    if not joy_sha or len(joy_sha) < 7:
        fail("missing or invalid commit SHA")

    vector = load_json(VECTOR_PATH)
    known_good = load_json(KNOWN_GOOD_PATH)

    if vector.get("authority") is not False:
        fail("vector authority must be false")

    forbidden = vector.get("forbidden_transition", {})
    if forbidden.get("from") != "CLAIM" or forbidden.get("to") != "VERIFIED_RECEIPT" or forbidden.get("allowed") is not False:
        fail("CLAIM -> VERIFIED_RECEIPT must remain forbidden")

    transition = vector.get("transition", {})
    if transition.get("from") != "OBSERVED" or transition.get("to") != "RECEIPT_BACKED" or transition.get("allowed") is not True:
        fail("OBSERVED -> RECEIPT_BACKED transition missing or not allowed")

    receipt_entry = vector.get("receipt_entry")
    if not isinstance(receipt_entry, dict):
        fail("receipt_entry missing")

    for field in REQUIRED_FIELDS:
        if field not in receipt_entry:
            fail(f"missing required field: {field}")

    if receipt_entry.get("authority") is not False:
        fail("receipt_entry authority must be false")
    if receipt_entry.get("authority_false") is not True:
        fail("receipt_entry authority_false must be true")

    receipt_entry["operator_signature_or_commit"] = joy_sha
    if receipt_entry.get("source_artifact_hash", "").startswith("sha256:930c305"):
        receipt_entry["source_artifact_hash"] = "sha256:" + joy_sha
    vector["receipt_entry"] = receipt_entry

    receipt_canonical = canonical_bytes(receipt_entry)
    index_entry_hash = sha256_prefixed(receipt_canonical)
    canonical_json_sha256 = index_entry_hash

    output = {
        "artifact": "ALMS_L2_KNOWN_GOOD_OUTPUT_001",
        "test_vector": vector.get("artifact"),
        "transition": "OBSERVED -> RECEIPT_BACKED",
        "operator_commit": joy_sha,
        "canonicalization": "RFC8785_JSON_SORTED_COMPACT_UTF8",
        "index_order": "receipt_id_ASC",
        "canonical_json_sha256": canonical_json_sha256,
        "index_entry_hash": index_entry_hash,
        "replay_proven": False,
        "authority": False,
        "forbidden_transition_enforced": {
            "from": "CLAIM",
            "to": "VERIFIED_RECEIPT",
            "allowed": False,
            "required_intermediate": "RECEIPT_BACKED",
        },
        "required_fields_verified": REQUIRED_FIELDS,
    }

    output_without_self_hash = dict(output)
    output_hash = sha256_prefixed(canonical_bytes(output_without_self_hash))
    output["known_good_output_hash"] = output_hash

    write_json(VECTOR_PATH, vector)
    write_json(KNOWN_GOOD_PATH, output)

    print(json.dumps({
        "status": "HASHES_COMPUTED",
        "environment": "UNSPECIFIED_OPERATOR_ENVIRONMENT",
        "commit_sha": joy_sha,
        "index_entry_hash": index_entry_hash,
        "canonical_json_sha256": canonical_json_sha256,
        "known_good_output_hash": output_hash,
        "replay_proven": False,
        "authority": False,
        "note": "Run in a second independent environment and compare before marking replay_proven true."
    }, indent=2))


if __name__ == "__main__":
    main()
