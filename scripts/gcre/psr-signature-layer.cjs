const { generateKeyPairSync, sign, verify } = require('crypto');

const SIGNATURE_ALGORITHM = 'Ed25519';
const PSR_SIG_LAYER_VERSION = 'PSR-SIG-LAYER-V0.1';

function deterministicStringify(obj) {
  if (obj === null || typeof obj !== 'object') return JSON.stringify(obj);
  if (Array.isArray(obj)) return `[${obj.map(deterministicStringify).join(',')}]`;

  const sorted = Object.keys(obj).sort().reduce((acc, key) => {
    acc[key] = obj[key];
    return acc;
  }, {});

  return JSON.stringify(sorted, (_, value) => {
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      return Object.keys(value).sort().reduce((acc, key) => {
        acc[key] = value[key];
        return acc;
      }, {});
    }
    return value;
  });
}

function generateKeypair() {
  const { publicKey, privateKey } = generateKeyPairSync('ed25519');

  return {
    publicKeyPem: publicKey.export({ type: 'spki', format: 'pem' }),
    privateKeyPem: privateKey.export({ type: 'pkcs8', format: 'pem' })
  };
}

function buildReceiptEnvelope(receipt, signer) {
  if (!receipt || !receipt.hash || !receipt.prevHash || !receipt.transitionId || !receipt.data) {
    throw new Error('INVALID_RECEIPT_FOR_SIGNATURE_ENVELOPE');
  }

  return {
    psrSigLayerVersion: PSR_SIG_LAYER_VERSION,
    psrVersion: receipt.data.version,
    hash: receipt.hash,
    prevHash: receipt.prevHash,
    transitionId: receipt.transitionId,
    stateTransitionDigest: receipt.hash,
    signer,
    signatureAlgorithm: SIGNATURE_ALGORITHM
  };
}

function signReceiptEnvelope(receipt, privateKeyPem, signer = 'local-ed25519-signer') {
  const envelope = buildReceiptEnvelope(receipt, signer);
  const payload = Buffer.from(deterministicStringify(envelope));
  const signature = sign(null, payload, privateKeyPem).toString('base64');

  return {
    ...envelope,
    signature
  };
}

function verifyReceiptSignature(receipt, signedEnvelope, publicKeyPem) {
  if (!signedEnvelope || !signedEnvelope.signature) return false;

  const expectedEnvelope = buildReceiptEnvelope(receipt, signedEnvelope.signer);

  for (const key of Object.keys(expectedEnvelope)) {
    if (signedEnvelope[key] !== expectedEnvelope[key]) return false;
  }

  const signature = Buffer.from(signedEnvelope.signature, 'base64');
  const payload = Buffer.from(deterministicStringify(expectedEnvelope));

  return verify(null, payload, publicKeyPem, signature);
}

module.exports = {
  SIGNATURE_ALGORITHM,
  PSR_SIG_LAYER_VERSION,
  deterministicStringify,
  generateKeypair,
  buildReceiptEnvelope,
  signReceiptEnvelope,
  verifyReceiptSignature
};

if (require.main === module) {
  const { PSRKVSimulator } = require('./psr-kv-simulator.cjs');

  const keys = generateKeypair();
  const sim = new PSRKVSimulator();

  const { receipt } = sim.transition('asset:gcre', 'signature-layer-active', {
    lane: 'gcre',
    authority: false,
    no_fake_green: true
  }, {
    timestamp: 1710000002000,
    transitionId: 'gcre-signature-transition-0003'
  });

  const signedEnvelope = signReceiptEnvelope(receipt, keys.privateKeyPem, 'gcre-local-ed25519-v0.1');
  const verified = verifyReceiptSignature(receipt, signedEnvelope, keys.publicKeyPem);

  console.log(JSON.stringify({
    layer: PSR_SIG_LAYER_VERSION,
    algorithm: SIGNATURE_ALGORITHM,
    verified,
    signer: signedEnvelope.signer,
    receiptHash: receipt.hash
  }, null, 2));
}
