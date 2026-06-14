import json
from typing import Any, Dict

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sse_starlette.sse import EventSourceResponse

app = FastAPI(title="ALMS MCP V0")

GITHUB_BASE = "https://raw.githubusercontent.com/jsonwisdom/JOY/main/alms/claims"
BASE_SEPOLIA_EAS = "https://base-sepolia.easscan.org/attestation/view"

TOOLS = [
    {
        "name": "alms.lookup_claim",
        "description": "Fetch an ALMS claim from jsonwisdom/JOY and summarize its state.",
        "inputSchema": {
            "type": "object",
            "properties": {"claim": {"type": "string"}},
            "required": ["claim"]
        }
    },
    {
        "name": "alms.lookup_witness",
        "description": "Return witness metadata for an ALMS claim.",
        "inputSchema": {
            "type": "object",
            "properties": {"claim": {"type": "string"}},
            "required": ["claim"]
        }
    },
    {
        "name": "alms.check_green_state",
        "description": "Check whether an ALMS claim is GREEN under the six-proof invariant.",
        "inputSchema": {
            "type": "object",
            "properties": {"claim": {"type": "string"}},
            "required": ["claim"]
        }
    }
]


def claim_filename(claim: str) -> str:
    claim = claim.strip().replace("/", "")
    if claim.endswith(".json"):
        return claim
    if claim.endswith(".claim.v1"):
        return f"{claim}.json"
    return f"{claim}.claim.v1.json"


async def fetch_claim(claim: str) -> Dict[str, Any]:
    url = f"{GITHUB_BASE}/{claim_filename(claim)}"
    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(url)
    if response.status_code != 200:
        raise ValueError(f"claim not found: {claim}")
    return response.json()


def summarize_claim(data: Dict[str, Any]) -> Dict[str, Any]:
    proofs = data.get("proofs", {})
    green = data.get("green_state", {})
    witness = proofs.get("witness", {})
    hash_or_cid = proofs.get("hash_or_cid", {})
    commit = proofs.get("commit_sha", {})
    replay = proofs.get("replay_path", {})
    witness_ref = witness.get("witness_ref")
    return {
        "claim_id": data.get("claim_id"),
        "claim_type": data.get("claim_type"),
        "surface": data.get("scope", {}).get("surface"),
        "green_eligible": green.get("eligible"),
        "green_reason": green.get("reason"),
        "commit_sha": commit.get("value"),
        "hash_algorithm": hash_or_cid.get("algorithm"),
        "hash_value": hash_or_cid.get("value"),
        "replay_status": replay.get("status"),
        "witness_status": witness.get("status"),
        "witness_ref": witness_ref,
        "witness_url": f"{BASE_SEPOLIA_EAS}/{witness_ref}" if isinstance(witness_ref, str) and witness_ref.startswith("0x") else None,
        "no_fake_green": data.get("mirror_status", {}).get("no_fake_green") or data.get("template_status", {}).get("no_fake_green")
    }


def check_green(data: Dict[str, Any]) -> Dict[str, Any]:
    proofs = data.get("proofs", {})
    checks = {
        "source_artifact": proofs.get("source_artifact", {}).get("exists") is True,
        "commit_sha": bool(proofs.get("commit_sha", {}).get("value")),
        "hash_or_cid": bool(proofs.get("hash_or_cid", {}).get("value")),
        "receipt": bool(proofs.get("receipt", {}).get("id")),
        "witness": proofs.get("witness", {}).get("status") == "PRESENT" or proofs.get("witness", {}).get("required") is False,
        "replay_path": proofs.get("replay_path", {}).get("exists") is True and proofs.get("replay_path", {}).get("status") == "PASS"
    }
    green = data.get("green_state", {})
    return {
        "claim_id": data.get("claim_id"),
        "is_green": green.get("eligible") is True and all(checks.values()),
        "green_state": green,
        "six_proof_status": checks,
        "missing": [name for name, ok in checks.items() if not ok]
    }


@app.get("/")
async def root():
    return {"name": "ALMS MCP V0", "sse": "/sse", "message": "/message"}


@app.get("/sse")
async def sse(request: Request):
    async def events():
        yield {"event": "endpoint", "data": "/message"}
        while not await request.is_disconnected():
            yield {"event": "ping", "data": "ALMS MCP V0"}
    return EventSourceResponse(events())


@app.post("/message")
async def message(request: Request):
    body = await request.json()
    method = body.get("method")

    if method == "tools/list":
        return {"tools": TOOLS}

    if method == "tools/call":
        params = body.get("params", {})
        name = params.get("name")
        args = params.get("arguments", {})
        claim = args.get("claim")
        if not claim:
            return JSONResponse({"error": "missing claim"}, status_code=400)
        try:
            data = await fetch_claim(claim)
            if name == "alms.lookup_claim":
                result = summarize_claim(data)
            elif name == "alms.lookup_witness":
                result = {
                    "claim_id": data.get("claim_id"),
                    "witness": data.get("proofs", {}).get("witness", {}),
                    "witness_metadata": data.get("witness_metadata", {})
                }
            elif name == "alms.check_green_state":
                result = check_green(data)
            else:
                return JSONResponse({"error": f"unknown tool: {name}"}, status_code=400)
            return {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}
        except Exception as exc:
            return JSONResponse({"error": str(exc)}, status_code=404)

    return JSONResponse({"error": f"unsupported method: {method}"}, status_code=400)
