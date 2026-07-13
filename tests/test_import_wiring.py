from mcp.alms_mcp_server import app


def test_router_integration():
    paths = [route.path for route in app.routes]
    assert "/webhooks/courtlistener/v2/{secret}" in paths
