import copy
from tools.receipts_os_fullmath_v0_1 import validate_receipt, validate_append, event_sha256

def fixture():
    return {
        "receipt_id":"R0",
        "schema_version":"0.1",
        "receipt_class":"OBSERVATION_RECEIPT",
        "claim":{"claim_id":"C0","claimant":None,"claimant_role":None,"exact_claim":"test","claim_type":None,"jurisdiction":None,"procedural_posture":None},
        "burden":{"burden_bearer":None,"standard_of_proof":None,"standard_authority":None,"burden_scope":None},
        "source":{"source_id":"S0","source_domain":None,"source_url":None,"source_type":"TEST","custodian":None,"publication_or_record_date":None,"observed_at":"TEST_CLOCK"},
        "capture":{"exact_bytes_captured":False,"source_sha256":"HOLD","parsed_text_captured":True,"parser_or_method":"fixture","extraction_scope":"fixture"},
        "binding":{"supported_dimensions":["TEST"],"unsupported_dimensions":[],"binding_status":"BOUND"},
        "verification":{"verification_status":"HASH_HOLD","verification_method":None,"verification_notes":None},
        "population":{},
        "procedure":{},
        "replay":{"sequence":0,"prev_event_sha256":None,"event_sha256":None,"supersedes":[],"superseded_by":[],"counter_receipts":[],"conflicts":[],"unresolved_edges":[]},
        "mirrors":{},
        "state":{"artifact_status":"PARSED","claim_status":"OBSERVED","authority_created":False,"political_verdict":"NONE"}
    }

def test_no_source_hash_without_exact_bytes():
    r = fixture()
    r["capture"]["source_sha256"] = "abc"
    assert "source_hash_without_exact_bytes" in validate_receipt(r)

def test_authority_must_remain_false():
    r = fixture()
    r["state"]["authority_created"] = True
    assert "authority_created_must_be_false" in validate_receipt(r)

def test_append_requires_sequence_and_prev_hash():
    a = fixture()
    a["replay"]["event_sha256"] = event_sha256(a)
    b = copy.deepcopy(a)
    b["receipt_id"] = "R1"
    b["replay"]["sequence"] = 1
    b["replay"]["prev_event_sha256"] = a["replay"]["event_sha256"]
    b["replay"]["event_sha256"] = event_sha256(b)
    assert validate_append(a, b) == []

def test_one_edge_does_not_promote_claim():
    r = fixture()
    r["binding"]["supported_dimensions"] = ["ONE_EDGE"]
    r["state"]["claim_status"] = "HOLD"
    assert validate_receipt(r) == []
