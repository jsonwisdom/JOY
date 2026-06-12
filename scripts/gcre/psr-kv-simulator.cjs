const { createHash, sign, verify, generateKeyPairSync } = require('crypto');
const fs = require('fs');
const path = require('path');

class PSRKVSimulator {
  constructor(keyPair = null) {
    this.state = new Map();
    this.receiptChain = [];
    this.currentHash = '0'.repeat(64); // genesis
    this.version = 'PSRKV-0.1';
    this.keyPair = keyPair;
  }

  deterministicStringify(obj) {
    const sorted = Object.keys(obj).sort().reduce((acc, key) => {
      acc[key] = obj[key];
      return acc;
    }, {});
    return JSON.stringify(sorted);
  }

  signReceipt(dataBuffer) {
    if (!this.keyPair?.privateKey) return null;
    return sign(null, dataBuffer, this.keyPair.privateKey).toString('base64');
  }

  verifySignature(dataBuffer, signature) {
    if (!this.keyPair?.publicKey || !signature) return false;
    return verify(null, dataBuffer, this.keyPair.publicKey, Buffer.from(signature, 'base64'));
  }

  transition(key, value, metadata = {}, opts = {}) {
    const timestamp = opts.timestamp ?? Date.now();
    const transitionId = opts.transitionId ??
      (timestamp.toString(36) + Math.random().toString(36).slice(2));

    const data = { key, value, metadata, timestamp, version: this.version };
    const prevHash = this.currentHash;

    const hashInput = this.deterministicStringify({
      prevHash,
      data,
      transitionId,
      version: this.version
    });

    const hash = createHash('sha256').update(hashInput).digest('hex');
    const sigPayload = Buffer.from(hash);
    const signature = this.signReceipt(sigPayload);

    const receipt = {
      hash,
      prevHash,
      data,
      transitionId,
      signature
    };

    this.state.set(key, value);
    this.receiptChain.push(receipt);
    this.currentHash = hash;

    return { receipt, stateSnapshot: Object.fromEntries(this.state) };
  }

  replayFromTransitions(transitions) {
    const sim = new PSRKVSimulator(this.keyPair);
    for (const t of transitions) {
      sim.transition(t.key, t.value, t.metadata || {}, {
        timestamp: t.timestamp,
        transitionId: t.transitionId
      });
    }
    return sim;
  }

  verifyChain(options = { requireSignatures: false }) {
    let expectedHash = '0'.repeat(64);

    for (const receipt of this.receiptChain) {
      const hashInput = this.deterministicStringify({
        prevHash: receipt.prevHash,
        data: receipt.data,
        transitionId: receipt.transitionId,
        version: this.version
      });
      const computedHash = createHash('sha256').update(hashInput).digest('hex');

      if (computedHash !== receipt.hash || receipt.prevHash !== expectedHash) {
        return false;
      }

      if (options.requireSignatures) {
        if (!this.verifySignature(Buffer.from(receipt.hash), receipt.signature)) {
          return false;
        }
      }

      expectedHash = receipt.hash;
    }
    return true;
  }

  exportGoldenFixtures(filePath = 'fixtures/psrkv-test-vectors.json') {
    const fixtureData = {
      genesisHash: '0'.repeat(64),
      transitionLog: this.receiptChain.map(r => ({
        key: r.data.key,
        value: r.data.value,
        metadata: r.data.metadata,
        timestamp: r.data.timestamp,
        transitionId: r.transitionId
      })),
      receiptChain: this.receiptChain,
      finalState: Object.fromEntries(this.state)
    };

    const dir = path.dirname(filePath);
    if (dir && dir !== '.') {
      fs.mkdirSync(dir, { recursive: true });
    }

    fs.writeFileSync(filePath, JSON.stringify(fixtureData, null, 2));
    return filePath;
  }

  toLatticePoint(receipt, index) {
    return {
      coord: index,
      label: receipt.hash.slice(0, 16),
      payloadHash: receipt.hash
    };
  }

  static generateKeyPair() {
    return generateKeyPairSync('ed25519');
  }
}

module.exports = { PSRKVSimulator };

if (require.main === module) {
  const keyPair = PSRKVSimulator.generateKeyPair();
  const sim = new PSRKVSimulator(keyPair);

  sim.transition('asset:gcre', 'protected', {
    lane: 'gcre',
    authority: false,
    no_fake_green: true
  }, {
    timestamp: 1710000000000,
    transitionId: 'gcre-genesis-transition-0001'
  });

  sim.transition('asset:gcre:mode', 'shadow-layer', {
    phase: 1
  }, {
    timestamp: 1710000001000,
    transitionId: 'gcre-shadow-transition-0002'
  });

  const ok = sim.verifyChain({ requireSignatures: true });
  const fixturePath = sim.exportGoldenFixtures('fixtures/gcre/psrkv-test-vectors-v0.1.json');

  console.log(JSON.stringify({
    simulator: sim.version,
    verifyChain: ok,
    requireSignatures: true,
    currentHash: sim.currentHash,
    fixturePath
  }, null, 2));
}
