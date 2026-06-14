# ALMS MCP V0

**STATUS:** PROTOTYPE  
**NO_FAKE_GREEN:** ACTIVE  
**Purpose:** Expose ALMS claim state from `jsonwisdom/JOY/alms/claims/*.json` through a minimal MCP-style SSE endpoint.

## Tools

- `alms.lookup_claim`
- `alms.lookup_witness`
- `alms.check_green_state`

## Endpoints

```text
GET  /
GET  /sse
POST /message
```

## Deploy on Render

Use `mcp/render.yaml` or create a Render Web Service manually.

Build command:

```bash
pip install -r mcp/requirements.txt
```

Start command:

```bash
uvicorn mcp.alms_mcp_server:app --host 0.0.0.0 --port $PORT
```

After deploy, the Grok connector URL should be:

```text
https://<your-render-app>.onrender.com/sse
```

## Example message call

```json
{
  "method": "tools/call",
  "params": {
    "name": "alms.check_green_state",
    "arguments": {
      "claim": "MN_CIVIC_PACKET_V1"
    }
  }
}
```

## Source of Truth

GitHub remains storage.

EAS remains witness.

MCP is only the query layer.
