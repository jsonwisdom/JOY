"""JoySpace synthetic-only deterministic content-addressed receipt verifier.

Offline in-memory R2 simulator. No production writes, child data, deployment,
credentials, external anchors, or authority created.
"""
import hashlib
import json


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False) + '\n').encode('utf-8')


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


class SyntheticStore:
    def __init__(self):
        self.objects = {}

    def create_only(self, key, blob):
        # Simulator only. Real R2 conditional write behavior NOT TESTED here.
        if key in self.objects:
            raise FileExistsError(key)
        self.objects[key] = blob

    def get(self, key):
        return self.objects[key]


def append(store, receipt, previous=None):
    if receipt.get('authority') is not False or receipt.get('synthetic') is not True:
        raise ValueError('synthetic=true and authority=false required')
    if any(k in receipt for k in ('child_data', 'guardian_consent', 'secrets')):
        raise ValueError('prohibited fields')
    seq = read_manifest(store, previous)['sequence'] + 1 if previous else 1
    payload = canonical(receipt)
    h = digest(payload)
    rkey = f'receipts/sha256-{h}.json'
    store.create_only(rkey, payload)
    if store.get(rkey) != payload or digest(store.get(rkey)) != h:
        raise ValueError('receipt readback mismatch')
    manifest = dict(schema='cw-joyspace-synthetic-manifest-v0.1',
                    sequence=seq, previous_manifest_sha256=previous,
                    receipt_key=rkey, receipt_sha256=h,
                    production_write=False, authority_created=False)
    mbytes = canonical(manifest)
    mh = digest(mbytes)
    store.create_only(f'manifests/sha256-{mh}.json', mbytes)
    return mh


def read_manifest(store, manifest_hash):
    data = store.get(f'manifests/sha256-{manifest_hash}.json')
    if digest(data) != manifest_hash:
        raise ValueError('manifest hash mismatch')
    obj = json.loads(data)
    if canonical(obj) != data:
        raise ValueError('noncanonical manifest')
    if obj['authority_created'] is not False or obj['production_write'] is not False:
        raise ValueError('unsafe manifest')
    return obj


def verify(store, tip):
    seen = set()
    expected_seq = None
    while tip is not None:
        if tip in seen:
            raise ValueError('manifest cycle')
        seen.add(tip)
        m = read_manifest(store, tip)
        if expected_seq is not None and m['sequence'] != expected_seq:
            raise ValueError('sequence discontinuity')
        expected_seq = m['sequence'] - 1
        key = m['receipt_key']
        blob = store.get(key)
        h = digest(blob)
        if key != f'receipts/sha256-{h}.json' or h != m['receipt_sha256']:
            raise ValueError('receipt hash mismatch')
        r = json.loads(blob)
        if canonical(r) != blob or r.get('synthetic') is not True or r.get('authority') is not False:
            raise ValueError('receipt noncanonical/unsafe')
        tip = m['previous_manifest_sha256']
    if expected_seq != 0:
        raise ValueError('missing genesis')
    return len(seen)


if __name__ == '__main__':
    import unittest

    class ProtocolTests(unittest.TestCase):
        def fixture(self, n):
            return {'schema': 'cw-joyspace-synthetic-receipt-v0.1',
                    'synthetic': True, 'authority': False, 'event': f'fixture-{n}',
                    'result_state': 'HOLD', 'sources': [], 'dissent_notes': []}

        def test_two_receipts_verify(self):
            s = SyntheticStore()
            first = append(s, self.fixture(1))
            second = append(s, self.fixture(2), first)
            self.assertEqual(verify(s, second), 2)

        def test_duplicate_rejected(self):
            s = SyntheticStore()
            append(s, self.fixture(1))
            with self.assertRaises(FileExistsError):
                append(s, self.fixture(1))

        def test_tamper_detected(self):
            s = SyntheticStore()
            tip = append(s, self.fixture(1))
            k = next(k for k in s.objects if k.startswith('receipts/'))
            s.objects[k] += b'bad'
            with self.assertRaises(ValueError):
                verify(s, tip)

        def test_broken_link_detected(self):
            s = SyntheticStore()
            first = append(s, self.fixture(1))
            second = append(s, self.fixture(2), first)
            del s.objects[f'manifests/sha256-{first}.json']
            with self.assertRaises(KeyError):
                verify(s, second)

        def test_authority_denied(self):
            with self.assertRaises(ValueError):
                append(SyntheticStore(), {'synthetic': True, 'authority': True})

    unittest.main(verbosity=2)
