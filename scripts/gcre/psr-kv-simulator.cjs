const { createHash } = require('crypto');
const fs = require('fs');
const path = require('path');

class PSRKVSimulator {
  constructor() {
    this.state = new Map();
    this.receiptChain = [];
    this.currentHash = '0'.repeat(64); // genesis
    this.version = 'PSRKV-0.1';
  }

  // Helper for stable serialization.
  deterministicStringify(obj) {
    const sorted = Object.keys(obj).sort().reduce((acc, key) => {
      acc[key] = obj[key];
      return acc;
    }, {});
    return JSON.stringify(sorted);
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

    const receipt = {
      hash,
      prevHash,
      data,
      transitionId,
      signature: this.signReceipt({ hash, prevHash, data, transitionId })
    };

    this.state.set(key, value);
    this.receiptChain.push(receipt);
    this.currentHash = hash;

    return { receipt, stateSnapshot: Object.fromEntries(this.state) };
  }

  replayFromTransitions(transitions) {
    const sim = new PSRKVSimulator();
    for (const t of transitions) {
      sim.transition(t.key, t.value, t.metadata || {}, {
        timestamp: t.timestamp,
        transitionId: t.transitionId
      });
    }
    return sim;
  }

  verifyChain() {
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

  signReceipt(receipt) {
    // Stub: PSR-SIG-LAYER-V0.1
    // Implementation target: Ed25519 signing of the canonical receipt hash envelope.
    return null;
  }

  toLatticePoint(receipt, index) {
    // Stub: Maps hash to coordinate space for resilience modeling.
    return {
      coord: index,
      label: receipt.hash.slice(0, 16),
      payloadHash: receipt.hash
    };
  }
}

module.exports = { PSRKVSimulator };

if (require.main === module) {
  const sim = new PSRKVSimulator();
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

  const ok = sim.verifyChain();
  const fixturePath = sim.exportGoldenFixtures('fixtures/gcre/psrkv-test-vectors-v0.1.json');

  console.log(JSON.stringify({
    simulator: sim.version,
    verifyChain: ok,
    currentHash: sim.currentHash,
    fixturePath
  }, null, 2));
}
