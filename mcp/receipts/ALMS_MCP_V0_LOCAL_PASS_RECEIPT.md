# ALMS_MCP_V0_LOCAL_PASS_RECEIPT

STATUS: LOCAL_PASS
TRUTH_STATE: GREEN_LOCAL
NO_FAKE_GREEN: TRUE
NO_PRIVATE_KEY_ACCESS: TRUE
READ_ONLY_ONLY: TRUE

## Scope

This receipt records local Cloud Shell validation of ALMS_MCP_V0.

## Endpoints Tested

- GET `/`
- GET `/sse`
- POST `/message`
- tool: `alms.check_green_state`

## SSE Result

```text
event: endpoint
data: /message

event: ping
data: ALMS MCP V0
