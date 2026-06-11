/**
 * MINTING_OPTIONS_GOBLIN_GATE_V0_1
 *
 * Homepage Integration Module
 * Case: 0012
 * Archive: ALMS
 * Role: Goblin Frost Archivist
 *
 * Rule:
 * State Intake -> Gate Translation -> Friction Enforcement
 *
 * No drift.
 * No magic.
 * No fake green.
 */

export type TimeBox = "PAST" | "PRESENT" | "FUTURE";

export type EvidenceStamp = "VERIFIED" | "LOCAL" | "RECON" | "UNKNOWN";

export type MintingDoor =
  | "CLAIM_A_MINT"
  | "INSPECT_COIN"
  | "GATE_FUTURE_MINT";

export type GateStatus = "OPEN" | "FRICTION" | "BLOCKED";

export type WisdomWorkSubject =
  | "GOBLIN"
  | "SOPHIA"
  | "JOY"
  | "FROST"
  | "ALMS"
  | "ZORA"
  | "UNKNOWN";

export type WisdomWorkCourt =
  | "GOBLIN_COURT"
  | "SOPHIA_COURT"
  | "JOY_SPACE"
  | "FROST_ARCHIVE"
  | "ALMS_ARCHIVE"
  | "ZORA_GATE"
  | "UNKNOWN_COURT";

export interface EvidencePlaceholder {
  commit?: string;
  pullRequest?: string;
  receipt?: string;
  uid?: string;
  transaction?: string;
  artifactPath?: string;
  publicUrl?: string;
  replayLog?: string;
}

export interface GateClaim {
  case: "0012";
  archive: "ALMS";
  module: "MINTING_OPTIONS_GOBLIN_GATE_V0_1";
  door: MintingDoor;
  title: string;
  description: string;
  evidence: EvidencePlaceholder;
}

export interface ReplayObject {
  case: "0012";
  archive: "ALMS";
  role: "frost_archivist";
  homepage_function: "question_every_claim";
  past: "replay";
  present: "build";
  future: "gate";
  authority: false;
  no_fake_green: true;
}

export interface GateTranslation {
  box: TimeBox;
  stamp: EvidenceStamp;
  reason: string;
  requiredNextEvidence: string[];
}

export interface GateDecision {
  claim: GateClaim;
  replay: ReplayObject;
  translation: GateTranslation;
  status: GateStatus;
  visitorMessage: string;
}

export interface WisdomArtifactInput {
  repo: string;
  path: string;
  title?: string;
  subject?: WisdomWorkSubject;
  court?: WisdomWorkCourt;
  evidence: EvidencePlaceholder;
}

export interface WisdomArtifactNode {
  repo: string;
  path: string;
  title: string;
  subject: WisdomWorkSubject;
  court: WisdomWorkCourt;
  box: TimeBox;
  stamp: EvidenceStamp;
  homepageHref?: string;
  evidence: EvidencePlaceholder;
}

export interface WisdomConstellationIndex {
  module: "WISDOM_WORKS_CONSTELLATION_INDEX_V0_1";
  primarySubject: WisdomWorkSubject;
  primaryCourt: WisdomWorkCourt;
  artifactCount: number;
  subjects: WisdomWorkSubject[];
  courts: WisdomWorkCourt[];
  artifacts: WisdomArtifactNode[];
  authority: false;
  no_fake_green: true;
}

export const GOBLIN_REPLAY_OBJECT: ReplayObject = {
  case: "0012",
  archive: "ALMS",
  role: "frost_archivist",
  homepage_function: "question_every_claim",
  past: "replay",
  present: "build",
  future: "gate",
  authority: false,
  no_fake_green: true
};

/**
 * LAYER ONE - STATE INTAKE
 *
 * Accepts a homepage minting claim.
 * Does not verify.
 * Does not upgrade.
 * Does not mutate evidence.
 */
export function intakeMintingClaim(input: GateClaim): GateClaim {
  return {
    case: "0012",
    archive: "ALMS",
    module: "MINTING_OPTIONS_GOBLIN_GATE_V0_1",
    door: input.door,
    title: input.title,
    description: input.description,
    evidence: {
      commit: input.evidence.commit,
      pullRequest: input.evidence.pullRequest,
      receipt: input.evidence.receipt,
      uid: input.evidence.uid,
      transaction: input.evidence.transaction,
      artifactPath: input.evidence.artifactPath,
      publicUrl: input.evidence.publicUrl,
      replayLog: input.evidence.replayLog
    }
  };
}

/**
 * LAYER TWO - GATE TRANSLATION
 *
 * Converts claim state into:
 * PAST / PRESENT / FUTURE
 * VERIFIED / LOCAL / RECON / UNKNOWN
 */
export function translateGate(claim: GateClaim): GateTranslation {
  const evidence = claim.evidence;

  const hasReplayEvidence =
    Boolean(evidence.commit) ||
    Boolean(evidence.pullRequest) ||
    Boolean(evidence.receipt) ||
    Boolean(evidence.uid) ||
    Boolean(evidence.transaction) ||
    Boolean(evidence.replayLog);

  const hasLocalArtifact = Boolean(evidence.artifactPath) && !Boolean(evidence.publicUrl);
  const hasPublicSurface = Boolean(evidence.publicUrl);

  if (hasReplayEvidence && hasPublicSurface) {
    return {
      box: "PAST",
      stamp: "VERIFIED",
      reason: "Claim has replay evidence and a public surface. It may enter Past as evidence.",
      requiredNextEvidence: []
    };
  }

  if (hasLocalArtifact) {
    return {
      box: "PRESENT",
      stamp: "LOCAL",
      reason: "Claim has a local artifact path, but public replay is not yet available.",
      requiredNextEvidence: ["publicUrl", "commit or pullRequest", "replayLog or receipt"]
    };
  }

  if (claim.door === "GATE_FUTURE_MINT") {
    return {
      box: "FUTURE",
      stamp: "UNKNOWN",
      reason: "Future mint requires written conditions before it can become active build.",
      requiredNextEvidence: ["mint conditions", "approval rule", "evidence requirement", "replay path"]
    };
  }

  return {
    box: "PRESENT",
    stamp: "RECON",
    reason: "Claim has shape, but no replayable artifact trail has been provided.",
    requiredNextEvidence: ["artifactPath", "publicUrl", "commit or pullRequest", "receipt or replayLog"]
  };
}

/**
 * LAYER THREE - FRICTION ENFORCEMENT
 *
 * Determines what the homepage may show.
 * VERIFIED may open.
 * LOCAL / RECON create friction.
 * UNKNOWN blocks promotion.
 */
export function enforceFriction(
  claim: GateClaim,
  translation: GateTranslation
): GateDecision {
  if (translation.stamp === "VERIFIED") {
    return {
      claim,
      replay: GOBLIN_REPLAY_OBJECT,
      translation,
      status: "OPEN",
      visitorMessage: "Goblin allows entry. This claim has public replay evidence."
    };
  }

  if (translation.stamp === "UNKNOWN") {
    return {
      claim,
      replay: GOBLIN_REPLAY_OBJECT,
      translation,
      status: "BLOCKED",
      visitorMessage: "Goblin blocks promotion. Conditions are missing or audit is required."
    };
  }

  return {
    claim,
    replay: GOBLIN_REPLAY_OBJECT,
    translation,
    status: "FRICTION",
    visitorMessage: "Goblin pauses the visitor. This claim needs stronger evidence before opening fully."
  };
}

/**
 * BOUND HOMEPAGE FUNCTION
 *
 * Ready for use under:
 * Minting Options
 */
export function bindMintingOptionsGoblinGate(input: GateClaim): GateDecision {
  const claim = intakeMintingClaim(input);
  const translation = translateGate(claim);
  return enforceFriction(claim, translation);
}

/**
 * Minimal hook-style alias for homepage components.
 * This is intentionally not React-dependent.
 */
export function useMintingOptionsGoblinGate(input: GateClaim): GateDecision {
  return bindMintingOptionsGoblinGate(input);
}

function inferSubject(input: WisdomArtifactInput): WisdomWorkSubject {
  const text = `${input.title ?? ""} ${input.repo} ${input.path}`.toLowerCase();

  if (text.includes("goblin")) return "GOBLIN";
  if (text.includes("sophia")) return "SOPHIA";
  if (text.includes("joy")) return "JOY";
  if (text.includes("frost")) return "FROST";
  if (text.includes("alms")) return "ALMS";
  if (text.includes("zora")) return "ZORA";

  return "UNKNOWN";
}

function inferCourt(subject: WisdomWorkSubject): WisdomWorkCourt {
  if (subject === "GOBLIN") return "GOBLIN_COURT";
  if (subject === "SOPHIA") return "SOPHIA_COURT";
  if (subject === "JOY") return "JOY_SPACE";
  if (subject === "FROST") return "FROST_ARCHIVE";
  if (subject === "ALMS") return "ALMS_ARCHIVE";
  if (subject === "ZORA") return "ZORA_GATE";

  return "UNKNOWN_COURT";
}

function classifyArtifactEvidence(evidence: EvidencePlaceholder): Pick<WisdomArtifactNode, "box" | "stamp"> {
  const hasReplayEvidence =
    Boolean(evidence.commit) ||
    Boolean(evidence.pullRequest) ||
    Boolean(evidence.receipt) ||
    Boolean(evidence.uid) ||
    Boolean(evidence.transaction) ||
    Boolean(evidence.replayLog);

  const hasPublicSurface = Boolean(evidence.publicUrl);
  const hasArtifactPath = Boolean(evidence.artifactPath);

  if (hasReplayEvidence && hasPublicSurface) {
    return { box: "PAST", stamp: "VERIFIED" };
  }

  if (hasArtifactPath) {
    return { box: "PRESENT", stamp: "LOCAL" };
  }

  if (hasPublicSurface) {
    return { box: "PRESENT", stamp: "RECON" };
  }

  return { box: "FUTURE", stamp: "UNKNOWN" };
}

function toHomepageHref(node: WisdomArtifactNode): string | undefined {
  if (node.evidence.publicUrl) return node.evidence.publicUrl;

  if (node.repo && node.path) {
    return `https://github.com/${node.repo}/blob/main/${node.path}`;
  }

  return undefined;
}

/**
 * CONSTELLATION MAPPER - ARTIFACT GRAPH
 *
 * Goblin is one word, one subject, one court system.
 * This mapper also supports other Wisdom works of art and ideas by collapsing
 * each artifact into a subject and court for homepage navigation.
 *
 * This function maps. It does not verify external truth.
 */
export function mapWisdomArtifacts(
  artifacts: WisdomArtifactInput[],
  primarySubject: WisdomWorkSubject = "GOBLIN"
): WisdomConstellationIndex {
  const nodes: WisdomArtifactNode[] = artifacts.map((artifact) => {
    const subject = artifact.subject ?? inferSubject(artifact);
    const court = artifact.court ?? inferCourt(subject);
    const classification = classifyArtifactEvidence(artifact.evidence);

    const node: WisdomArtifactNode = {
      repo: artifact.repo,
      path: artifact.path,
      title: artifact.title ?? artifact.path.split("/").pop() ?? artifact.path,
      subject,
      court,
      box: classification.box,
      stamp: classification.stamp,
      evidence: artifact.evidence
    };

    return {
      ...node,
      homepageHref: toHomepageHref(node)
    };
  });

  const subjects = Array.from(new Set(nodes.map((node) => node.subject)));
  const courts = Array.from(new Set(nodes.map((node) => node.court)));

  return {
    module: "WISDOM_WORKS_CONSTELLATION_INDEX_V0_1",
    primarySubject,
    primaryCourt: inferCourt(primarySubject),
    artifactCount: nodes.length,
    subjects,
    courts,
    artifacts: nodes,
    authority: false,
    no_fake_green: true
  };
}

/**
 * BOUND GOBLIN CONSTELLATION
 *
 * The discovered Goblin-class artifacts across JOY, AL, and COMPUTERWISDOM.
 * Evidence links are public file surfaces discovered through GitHub search.
 * Commit fields remain placeholders unless independently pinned.
 */
export function bindGoblinRepoConstellation(): WisdomConstellationIndex {
  return mapWisdomArtifacts(
    [
      {
        repo: "jsonwisdom/JOY",
        path: "components/goblin-gate/index.ts",
        title: "Goblin Gate Homepage Module",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          commit: "8e3c056fb29aca9a51f5e0012f1d2ec5b9c51697",
          artifactPath: "components/goblin-gate/index.ts",
          publicUrl: "https://github.com/jsonwisdom/JOY/blob/main/components/goblin-gate/index.ts"
        }
      },
      {
        repo: "jsonwisdom/AL",
        path: "verify_goblin_stack.py",
        title: "Goblin Stack Verifier",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          artifactPath: "verify_goblin_stack.py",
          publicUrl: "https://github.com/jsonwisdom/AL/blob/7cc757114e6ae1d4c51a3c283a0829f8fc0e973c/verify_goblin_stack.py"
        }
      },
      {
        repo: "jsonwisdom/AL",
        path: "docs/goblin_gap_map_batch_007.md",
        title: "Goblin Gap Map Batch 007",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          artifactPath: "docs/goblin_gap_map_batch_007.md",
          publicUrl: "https://github.com/jsonwisdom/AL/blob/7cc757114e6ae1d4c51a3c283a0829f8fc0e973c/docs/goblin_gap_map_batch_007.md"
        }
      },
      {
        repo: "jsonwisdom/AL",
        path: "_truth/constitution/goblin_full_stack_report.json",
        title: "Goblin Full Stack Report",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          artifactPath: "_truth/constitution/goblin_full_stack_report.json",
          publicUrl: "https://github.com/jsonwisdom/AL/blob/7cc757114e6ae1d4c51a3c283a0829f8fc0e973c/_truth/constitution/goblin_full_stack_report.json"
        }
      },
      {
        repo: "jsonwisdom/COMPUTERWISDOM",
        path: "docs/goblin_verifier_v0_1.md",
        title: "Goblin Verifier V0.1",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          artifactPath: "docs/goblin_verifier_v0_1.md",
          publicUrl: "https://github.com/jsonwisdom/COMPUTERWISDOM/blob/c5849e2118241f2802be0e326e97ef19dd7a9faa/docs/goblin_verifier_v0_1.md"
        }
      },
      {
        repo: "jsonwisdom/COMPUTERWISDOM",
        path: "docket/GOBLIN_DOCKET_V0_1.md",
        title: "Goblin Docket V0.1",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          artifactPath: "docket/GOBLIN_DOCKET_V0_1.md",
          publicUrl: "https://github.com/jsonwisdom/COMPUTERWISDOM/blob/c5849e2118241f2802be0e326e97ef19dd7a9faa/docket/GOBLIN_DOCKET_V0_1.md"
        }
      },
      {
        repo: "jsonwisdom/COMPUTERWISDOM",
        path: "docs/GOBLIN_PRECEDENT_INDEX_V0_1.md",
        title: "Goblin Precedent Index V0.1",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          artifactPath: "docs/GOBLIN_PRECEDENT_INDEX_V0_1.md",
          publicUrl: "https://github.com/jsonwisdom/COMPUTERWISDOM/blob/c5849e2118241f2802be0e326e97ef19dd7a9faa/docs/GOBLIN_PRECEDENT_INDEX_V0_1.md"
        }
      },
      {
        repo: "jsonwisdom/COMPUTERWISDOM",
        path: "schemas/goblin_court_v0_1.schema.json",
        title: "Goblin Court Schema V0.1",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          artifactPath: "schemas/goblin_court_v0_1.schema.json",
          publicUrl: "https://github.com/jsonwisdom/COMPUTERWISDOM/blob/c5849e2118241f2802be0e326e97ef19dd7a9faa/schemas/goblin_court_v0_1.schema.json"
        }
      },
      {
        repo: "jsonwisdom/COMPUTERWISDOM",
        path: "court/goblin_precedent_engine_anchor_packet_v0_1.json",
        title: "Goblin Precedent Engine Anchor Packet V0.1",
        subject: "GOBLIN",
        court: "GOBLIN_COURT",
        evidence: {
          artifactPath: "court/goblin_precedent_engine_anchor_packet_v0_1.json",
          publicUrl: "https://github.com/jsonwisdom/COMPUTERWISDOM/blob/c5849e2118241f2802be0e326e97ef19dd7a9faa/court/goblin_precedent_engine_anchor_packet_v0_1.json"
        }
      }
    ],
    "GOBLIN"
  );
}

export function useGoblinRepoConstellation(): WisdomConstellationIndex {
  return bindGoblinRepoConstellation();
}
