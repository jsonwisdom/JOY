#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PARENT = ROOT / 'receipts' / 'composition' / 'composite_proof_001.json'
OUT = ROOT / 'receipts' / 'recursive' / 'composite_proof_002.json'

parent = json.loads(PARENT.read_text())
expected = 'sha256:3a9f683aaac459ddfebdfdc56ff5c449414d5c1de4abede46795db3ebb7be42b'
assert parent['canonical_json_sha256'] == expected
assert parent['authority'] is False

child = {
 'artifact':'composite_proof_002',
 'parent_artifact':'composite_proof_001',
 'parent_hash': expected,
 'inheritance_depth': 2,
 'L4_recursive_inheritance':'PROVED',
 'authority': False
}

OUT.write_text(json.dumps(child,sort_keys=True,indent=2)+'\n')
print('wrote', OUT)
print(hashlib.sha256(OUT.read_bytes()).hexdigest())
