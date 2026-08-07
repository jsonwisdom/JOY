from dataclasses import dataclass
from datetime import datetime, timezone


EEV_THRESHOLD_USD = 15.0
FORMULA_VERSION = "EEV_V0_1"


@dataclass(frozen=True)
class OpportunityInputs:
    opportunity_id: str
    payout_usd: float
    acceptance_probability: float
    estimated_agent_hours: float
    agent_hour_cost_usd: float
    estimated_human_minutes: float
    human_minute_cost_usd: float


def compute_eev_usd(inputs: OpportunityInputs, scored_at: str | None = None) -> dict:
    if not 0 <= inputs.acceptance_probability <= 1:
        raise ValueError("acceptance_probability must be between 0 and 1")

    nonnegative = {
        "payout_usd": inputs.payout_usd,
        "estimated_agent_hours": inputs.estimated_agent_hours,
        "agent_hour_cost_usd": inputs.agent_hour_cost_usd,
        "estimated_human_minutes": inputs.estimated_human_minutes,
        "human_minute_cost_usd": inputs.human_minute_cost_usd,
    }
    for name, value in nonnegative.items():
        if value < 0:
            raise ValueError(f"{name} must be non-negative")

    gross_expected_value = inputs.payout_usd * inputs.acceptance_probability
    agent_cost = inputs.estimated_agent_hours * inputs.agent_hour_cost_usd
    human_cost = inputs.estimated_human_minutes * inputs.human_minute_cost_usd
    eev = gross_expected_value - agent_cost - human_cost

    threshold_pass = eev >= EEV_THRESHOLD_USD
    return {
        "opportunity_id": inputs.opportunity_id,
        "expected_value_usd": round(eev, 2),
        "threshold_usd": EEV_THRESHOLD_USD,
        "threshold_pass": threshold_pass,
        "reason": "OK" if threshold_pass else "LOW_EEV",
        "inputs": {
            "payout_usd": inputs.payout_usd,
            "acceptance_probability": inputs.acceptance_probability,
            "estimated_agent_hours": inputs.estimated_agent_hours,
            "agent_hour_cost_usd": inputs.agent_hour_cost_usd,
            "estimated_human_minutes": inputs.estimated_human_minutes,
            "human_minute_cost_usd": inputs.human_minute_cost_usd,
        },
        "formula_version": FORMULA_VERSION,
        "scored_at": scored_at or datetime.now(timezone.utc).isoformat(),
    }
