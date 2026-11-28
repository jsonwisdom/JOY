'use strict';
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
// Restricted deterministic JSON serialization; supports strings, booleans,
// safe integers, null, arrays, and plain records. Not full RFC 8785.
function canon(v) {
  if (v === null) return 'null';
  if (typeof v === 'string') return JSON.stringify(v);
  if (typeof v === 'boolean') return v ? 'true' : 'false';
  if (Number.isSafeInteger(v)) return String(v);
  if (Array.isArray(v)) return '[' + v.map(canon).join(',') + ']';
  if (v && typeof v === 'object' && Object.getPrototypeOf(v) === Object.prototype)
    return '{' + Object.keys(v).sort().map(k => JSON.stringify(k) + ':' + canon(v[k])).join(',') + '}';
  throw new TypeError('unsupported canonical JSON value');
}
function encode(v) { return Buffer.from(canon(v) + '\n', 'utf8'); }
function object(v, kind) {
  const bytes = encode(v), hash = sha(bytes);
  return { key: kind + '/sha256-' + hash + '.json', bytes, hash };
}
function manifest(sequence, prev, receipt) {
  return object({schema:'cw-joyspace-manifest-v0.1',sequence,
    previous_manifest_sha256:prev,receipt_key:receipt.key,
    receipt_sha256:receipt.hash,synthetic:true},'manifests');
}
function verifyChain(items) {
  let previous=null;
  for(let i=0;i<items.length;i++) {
    const m=items[i], x=JSON.parse(m.bytes.toString());
    assert.equal(sha(m.bytes),m.hash);
    assert.equal(m.key,'manifests/sha256-'+m.hash+'.json');
    assert.equal(x.sequence,i+1);
    assert.equal(x.previous_manifest_sha256,previous);
    previous=m.hash;
  }
  return previous;
}
class MockR2 {
  constructor(){this.data=new Map();}
  put(key,bytes,ifNoneMatch){
    if(ifNoneMatch!=='*')throw Error('412 REQUIRED: If-None-Match');
    if(this.data.has(key))return 412;
    this.data.set(key,Buffer.from(bytes));return 200;
  }
  get(key){return this.data.get(key);}
}
function test(){
  const store=new MockR2();
  const r=object({schema:'cw-joyspace-receipt-v0.1',synthetic:true,
    contains_child_data:false,payload:'SYNTHETIC ONLY'},'receipts');
  assert.equal(store.put(r.key,r.bytes,'*'),200);
  assert.equal(store.put(r.key,r.bytes,'*'),412);
  assert.equal(sha(store.get(r.key)),r.hash);
  const m1=manifest(1,null,r);
  assert.equal(store.put(m1.key,m1.bytes,'*'),200);
  const m2=manifest(2,m1.hash,r);
  assert.equal(store.put(m2.key,m2.bytes,'*'),200);
  assert.equal(verifyChain([m1,m2]),m2.hash);
  assert.throws(()=>verifyChain([m2,m1]));
  assert.throws(()=>canon({bad:1.5}));
  return {receipt_key:r.key,manifest_1:m1.key,manifest_2:m2.key,
    head_hash:m2.hash,tests:'PASS',scope:'LOCAL_SYNTHETIC_ONLY'};
}
if(require.main===module)console.log(JSON.stringify(test(),null,2));
module.exports={canon,encode,object,manifest,verifyChain,MockR2,test};
