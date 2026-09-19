"""Apple Blossom AI Naming Audit V0.1.

Deterministic classifier only. It does not fetch the web and does not create authority.
A host agent is expected to resolve SOURCE_QUERIES before classification when public sources
are available.

ASK -> SEARCH -> BIND -> ANSWER -> NEXT_GATE
"""

from collections import Counter
from typing import Any, Dict, Iterable, Mapping


ALLOWED_STATES = {"OBSERVED", "NOT_OBSERVED", "CONFLICT", "HOLD"}


def abbreviation_collision(options: Mapping[str, str]) -> bool:
    counts = Counter(options.values())
    return any(count > 1 for count in counts.values())


def answer_question(receipts: Mapping[str, Any]) -> Dict[str, Any]:
    """Classify current receipt set without converting absence into falsehood."""
    official_ai = bool(receipts.get("white_house_uses_ai") and receipts.get("nist_uses_ai"))
    naming_event = bool(receipts.get("naming_event_observed"))
    asi_mentions = bool(receipts.get("nist_published_asi_mentions"))

    options = receipts.get(
        "proposed_labels",
        {
            "Superior Intelligence": "SI",
            "Extreme Intelligence": "EI",
            "Supreme Intelligence": "SI",
        },
    )

    result: Dict[str, Any] = {
        "object_id": "APPLE_BLOSSOM_AI_NAMING_AUDIT_V0_1",
        "authority_created": False,
        "political_verdict": "NONE",
        "naming_event": "OBSERVED_AS_PROPOSAL" if naming_event else "HOLD",
        "legal_term_changed": "NOT_OBSERVED" if official_ai else "HOLD",
        "technical_standard_changed": "NOT_OBSERVED" if official_ai else "HOLD",
        "taxonomy_collision": "OBSERVED" if abbreviation_collision(options) else "NOT_OBSERVED",
        "model_authority_delta": (
            "OBSERVED" if receipts.get("binding_authority_delta")
            else "NOT_OBSERVED"
        ),
        "girl_specific_operational_edge": (
            "OBSERVED" if receipts.get("girl_specific_operational_edge")
            else "NOT_OBSERVED"
        ),
        "asi_research_term": "OBSERVED" if asi_mentions else "HOLD",
    }

    if result["naming_event"] == "HOLD":
        next_gate = "RESOLVE_NAMING_EVENT_SOURCE"
    elif result["legal_term_changed"] == "HOLD":
        next_gate = "RESOLVE_CURRENT_OPERATIVE_TERM"
    elif result["asi_research_term"] == "HOLD":
        next_gate = "SEARCH_SUPERINTELLIGENCE_TAXONOMY"
    elif result["taxonomy_collision"] == "OBSERVED":
        next_gate = "SUPERINTELLIGENCE_TAXONOMY_COLLISION_V0_1"
    else:
        next_gate = "MODEL_AUTHORITY_AUDIT"

    result["next_gate"] = next_gate
    return result


def validate_states(result: Mapping[str, Any]) -> None:
    state_keys: Iterable[str] = (
        "legal_term_changed",
        "technical_standard_changed",
        "taxonomy_collision",
        "model_authority_delta",
        "girl_specific_operational_edge",
        "asi_research_term",
    )
    for key in state_keys:
        state = result[key]
        if state not in ALLOWED_STATES:
            raise ValueError(f"{key}: invalid state {state!r}")


if __name__ == "__main__":
    seed = {
        "naming_event_observed": True,
        "white_house_uses_ai": True,
        "nist_uses_ai": True,
        "nist_published_asi_mentions": True,
        "binding_authority_delta": False,
        "girl_specific_operational_edge": False,
    }
    out = answer_question(seed)
    validate_states(out)
    print(out)
