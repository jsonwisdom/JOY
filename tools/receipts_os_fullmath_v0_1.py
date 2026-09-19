"""Receipts OS FullMath validator v0.1.

Validation only. Does not establish truth, legal authority, or legal burden.
"""
import hashlib
import json
from typing import Any, Dict, List

VALID_ARTIFACT = {"CANDIDATE","ACQUIRED","PARSED","UNAVAILABLE_AFTER_OBSERVATION"}
VALID_BINDING = {"UNBOUND","BOUND","PARTIAL","CONFLICT"}
VALID_VERIFY = {"UNVERIFIED","SOURCE_POINTER_MATCH","HASH_MATCH","HASH_MISMATCH","HASH_HOLD"}
VALID_CLAIM = {"UNOBSERVED","OBSERVED","HOLD","CONFLICT","REJECTED","ESTABLISHED"}

def canonical_event_bytes(event: Dict[str, Any]) -> bytes:
    body = json.loads(json.dumps(event))
    body.setdefault("replay", {})["event_sha256"] = None
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def event_sha256(event: Dict[str, Any]) -> str:
    return hashlib.sha256(canonical_event_bytes(event)).hexdigest()

def validate_receipt(r: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for key in ("receipt_id","schema_version","receipt_class","claim","source","capture","binding","verification","replay","state"):
        if key not in r:
            errors.append(f"missing:{key}")

    if errors:
        return errors

    if r["schema_version"] != "0.1":
        errors.append("schema_version")

    if not r["claim"].get("claim_id"):
        errors.append("claim.claim_id")
    if not r["claim"].get("exact_claim"):
        errors.append("claim.exact_claim")

    cap = r["capture"]
    if cap.get("exact_bytes_captured") is False and cap.get("source_sha256") not in (None, "HOLD"):
        errors.append("source_hash_without_exact_bytes")

    if r["binding"].get("binding_status") not in VALID_BINDING:
        errors.append("binding_status")
    if r["verification"].get("verification_status") not in VALID_VERIFY:
        errors.append("verification_status")
    if r["state"].get("artifact_status") not in VALID_ARTIFACT:
        errors.append("artifact_status")
    if r["state"].get("claim_status") not in VALID_CLAIM:
        errors.append("claim_status")

    if r["state"].get("authority_created") is not False:
        errors.append("authority_created_must_be_false")
    if r["state"].get("political_verdict") != "NONE":
        errors.append("political_verdict_must_be_NONE")

    replay = r["replay"]
    if replay.get("sequence", -1) < 0:
        errors.append("sequence")

    return errors

def validate_append(prev: Dict[str, Any], nxt: Dict[str, Any]) -> List[str]:
    errors = validate_receipt(nxt)
    if nxt.get("replay", {}).get("sequence") != prev.get("replay", {}).get("sequence", -1) + 1:
        errors.append("sequence_not_append_only")

    prev_hash = prev.get("replay", {}).get("event_sha256")
    if prev_hash and nxt.get("replay", {}).get("prev_event_sha256") != prev_hash:
        errors.append("prev_event_hash_mismatch")

    return errors
