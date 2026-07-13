import hashlib
import hmac
import json
import os
from pathlib import Path

from fastapi import APIRouter, BackgroundTasks, HTTPException, Request

from .dedup import claim_event, release_event
from .queue import enqueue_for_alms

router = APIRouter()
RAW_DIR = Path("mcp/storage/raw")


def process_event(body: bytes, event_id: str) -> None:
    enqueue_for_alms(json.loads(body), event_id)


@router.post("/webhooks/courtlistener/v2/{secret}", status_code=202)
async def courtlistener_webhook(
    secret: str,
    request: Request,
    background_tasks: BackgroundTasks,
):
    configured_secret = os.environ.get("COURTLISTENER_WEBHOOK_SECRET", "")

    if not configured_secret:
        raise HTTPException(503, "Webhook secret not configured")

    if not hmac.compare_digest(secret, configured_secret):
        raise HTTPException(401, "Invalid secret")

    body = await request.body()
    event_id = hashlib.sha256(body).hexdigest()

    if not claim_event(event_id):
        return {"status": "duplicate_ack", "receipt": event_id}

    try:
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        (RAW_DIR / f"{event_id}.json").write_bytes(body)
    except Exception:
        release_event(event_id)
        raise HTTPException(500, "Receipt storage failed")

    background_tasks.add_task(process_event, body, event_id)
    return {"status": "accepted", "receipt": event_id}
