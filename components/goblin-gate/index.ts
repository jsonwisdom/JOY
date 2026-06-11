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
