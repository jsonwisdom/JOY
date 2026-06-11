/**
 * GOBLIN_LEVEL_4_HOMEPAGE_BINDING_V0_1
 *
 * Anchored spec:
 * docs/goblin/GOBLIN_HOMEPAGE_INTEGRATION_MAP_V0_1.md
 * commit: 803859cc67cfd9f90e4958199004d9e4e458a524
 *
 * Rule:
 * State Intake -> Gate Translation -> Friction Enforcement
 *
 * This module is a deterministic UI binding.
 * It is not a verifier, court, crawler, classifier, or semantic engine.
 */

export type GoblinRepoKey = "JOY" | "AL" | "COMPUTERWISDOM";

export type GoblinGateLabel =
  | "GREEN"
  | "GREEN_SEEDED"
  | "PUBLIC_ROUTE_MAP_SEEDED"
  | "SPEC_SEEDED_CANDIDATE"
  | "HOLD"
  | "UNKNOWN";

export interface GoblinConstellationNodeInput {
  repoKey: GoblinRepoKey;
  repo: string;
  title: string;
  path: string;
  status: GoblinGateLabel;
  commit?: string;
  href?: string;
}

export interface GoblinConstellationInput {
  sourcePath: "artifacts/goblin_constellation_v0_1.json";
  routeMapPath: "docs/goblin/GOBLIN_PUBLIC_ROUTE_MAP_V0_1.md";
  routeMapCommit: "094949beb259b1796539c7f337c9a36a5e4d6eae";
  integrationMapPath: "docs/goblin/GOBLIN_HOMEPAGE_INTEGRATION_MAP_V0_1.md";
  integrationMapCommit: "803859cc67cfd9f90e4958199004d9e4e458a524";
  homepageArea: "Minting Options";
  componentTarget: "Goblin Gate";
  authority: false;
  noFakeGreen: true;
  nodes: GoblinConstellationNodeInput[];
}

export interface GoblinCard {
  title: string;
  repo: string;
  path: string;
  status: GoblinGateLabel;
  link?: string;
  mintEnabled: false;
  warning: string;
}

export interface GoblinReplayObject {
  route_map_path: "docs/goblin/GOBLIN_PUBLIC_ROUTE_MAP_V0_1.md";
  route_map_commit: "094949beb259b1796539c7f337c9a36a5e4d6eae";
  integration_map_path: "docs/goblin/GOBLIN_HOMEPAGE_INTEGRATION_MAP_V0_1.md";
  integration_map_commit: "803859cc67cfd9f90e4958199004d9e4e458a524";
  homepage_area: "Minting Options";
  component_target: "Goblin Gate";
  authority: false;
  no_fake_green: true;
  fallback_state: "HOLD_OR_UNKNOWN";
  cards: GoblinCard[];
}

const ALLOWED_REPOS: GoblinRepoKey[] = ["JOY", "AL", "COMPUTERWISDOM"];

const ALLOWED_LABELS: GoblinGateLabel[] = [
  "GREEN",
  "GREEN_SEEDED",
  "PUBLIC_ROUTE_MAP_SEEDED",
  "SPEC_SEEDED_CANDIDATE",
  "HOLD",
  "UNKNOWN"
];

const HOLD_CARD_WARNING =
  "Goblin Gate is navigation only. Minting remains disabled unless separate public evidence exists.";

function isAllowedRepo(repoKey: GoblinRepoKey): boolean {
  return ALLOWED_REPOS.includes(repoKey);
}

function isAllowedLabel(status: GoblinGateLabel): boolean {
  return ALLOWED_LABELS.includes(status);
}

function hasAnchor(node: GoblinConstellationNodeInput): boolean {
  return Boolean(node.path) && Boolean(node.commit || node.href);
}

/**
 * LAYER ONE - STATE INTAKE
 *
 * Accepts an explicit constellation object.
 * Does not read files.
 * Does not infer repo nodes.
 * Does not mutate the constellation map.
 */
export function intakeGoblinConstellation(
  input: GoblinConstellationInput
): GoblinConstellationInput {
  return {
    sourcePath: input.sourcePath,
    routeMapPath: input.routeMapPath,
    routeMapCommit: input.routeMapCommit,
    integrationMapPath: input.integrationMapPath,
    integrationMapCommit: input.integrationMapCommit,
    homepageArea: input.homepageArea,
    componentTarget: input.componentTarget,
    authority: false,
    noFakeGreen: true,
    nodes: input.nodes.map((node) => ({
      repoKey: node.repoKey,
      repo: node.repo,
      title: node.title,
      path: node.path,
      status: node.status,
      commit: node.commit,
      href: node.href
    }))
  };
}

/**
 * LAYER TWO - GATE TRANSLATION
 *
 * Converts explicit node state into homepage cards.
 * Does not promote status.
 * Missing anchors collapse to HOLD.
 */
export function translateGoblinCards(
  input: GoblinConstellationInput
): GoblinCard[] {
  return input.nodes.map((node) => {
    const allowed = isAllowedRepo(node.repoKey) && isAllowedLabel(node.status);
    const anchored = hasAnchor(node);
    const status: GoblinGateLabel = allowed && anchored ? node.status : "HOLD";

    return {
      title: node.title,
      repo: node.repo,
      path: node.path,
      status,
      link: anchored ? node.href : undefined,
      mintEnabled: false,
      warning: HOLD_CARD_WARNING
    };
  });
}

/**
 * LAYER THREE - FRICTION ENFORCEMENT
 *
 * Produces the replay object for homepage rendering.
 * Minting is always disabled in this binding.
 * Unknown or invalid cards remain visible as HOLD/UNKNOWN surfaces.
 */
export function enforceGoblinFriction(
  input: GoblinConstellationInput,
  cards: GoblinCard[]
): GoblinReplayObject {
  return {
    route_map_path: input.routeMapPath,
    route_map_commit: input.routeMapCommit,
    integration_map_path: input.integrationMapPath,
    integration_map_commit: input.integrationMapCommit,
    homepage_area: input.homepageArea,
    component_target: input.componentTarget,
    authority: false,
    no_fake_green: true,
    fallback_state: "HOLD_OR_UNKNOWN",
    cards: cards.map((card) => ({
      title: card.title,
      repo: card.repo,
      path: card.path,
      status: card.status,
      link: card.link,
      mintEnabled: false,
      warning: card.warning
    }))
  };
}

/**
 * BOUND HOMEPAGE FUNCTION
 *
 * Ready for JOY homepage placement under Minting Options / Goblin Gate.
 */
export function bindGoblinRepoConstellation(
  input: GoblinConstellationInput
): GoblinReplayObject {
  const state = intakeGoblinConstellation(input);
  const cards = translateGoblinCards(state);
  return enforceGoblinFriction(state, cards);
}

/**
 * Hook-style alias.
 * This is intentionally not React-dependent.
 */
export function useGoblinRepoConstellation(
  input: GoblinConstellationInput
): GoblinReplayObject {
  return bindGoblinRepoConstellation(input);
}
