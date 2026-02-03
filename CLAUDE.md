# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Model Context Protocol (MCP) server that enables natural language interaction with pfSense firewalls through Claude Desktop and other GenAI applications. It uses the pfSense REST API v2 package ([jaredhendrickson13/pfsense-api](https://github.com/jaredhendrickson13/pfsense-api)).

## Testing

### Quick Test with Nix (Recommended)

Use the flake.nix to get a dev environment with all dependencies:

```bash
nix develop --command python << 'EOF'
import asyncio
import os
import sys
sys.path.insert(0, 'src')

from pfsense_api_enhanced import EnhancedPfSenseAPIClient, AuthMethod, PfSenseVersion, ControlParameters

async def test():
    client = EnhancedPfSenseAPIClient(
        host=os.environ['PFSENSE_URL'],
        auth_method=AuthMethod.API_KEY,
        api_key=os.environ['PFSENSE_API_KEY'],
        verify_ssl=False,
        version=PfSenseVersion.CE_2_8_0
    )

    # Test connection
    status = await client.get_system_status()
    print(f"Connected: {status.get('data', {}).get('system_platform', 'OK')}")

    # Test create rule
    rule_data = {
        "interface": ["lan"],
        "type": "block",
        "ipprotocol": "inet",
        "protocol": "tcp",
        "source": "any",
        "destination": "1.1.1.1",
        "destination_port": "12345",
        "descr": "MCP TEST - DELETE ME"
    }
    result = await client.create_firewall_rule(rule_data, ControlParameters(apply=True))
    rule_id = result['data']['id']
    print(f"Created rule: {rule_id}")

    # Test delete rule
    await client.delete_firewall_rule(rule_id, apply_immediately=True)
    print(f"Deleted rule: {rule_id}")

asyncio.run(test())
EOF
```

The flake.nix shellHook loads credentials from `/run/secrets/mcp/pfsense.env` (NixOS sops-nix).

### Credentials

Secrets are at `/run/secrets/mcp/pfsense.env`:
```
PFSENSE_HOST=https://192.168.1.1
PFSENSE_API_KEY=<key>
PFSENSE_VERIFY_SSL=false
```

The flake exports `PFSENSE_URL` from `PFSENSE_HOST`.

## pfSense API v2 Quirks

**These are critical - the API will return 400/404 if you get them wrong:**

1. **`interface` must be an array**, not a string:
   ```python
   # WRONG
   "interface": "lan"
   # CORRECT
   "interface": ["lan"]
   ```

2. **Field names for firewall rules**:
   - `source` / `destination` (not `src` / `dst`)
   - `source_port` / `destination_port` (not `srcport` / `dstport`)

3. **DELETE uses request body**, not URL path:
   ```python
   # WRONG
   DELETE /api/v2/firewall/rule/40

   # CORRECT
   DELETE /api/v2/firewall/rule
   Body: {"id": 40}
   ```

4. **httpx quirk**: Use `.request("DELETE", ...)` not `.delete(...)` because `.delete()` doesn't support `json=` parameter.

## Commands

### Run the MCP server (stdio mode for Claude Desktop)
```bash
MCP_MODE=stdio python -m src.main
```

### Run as HTTP server (for testing)
```bash
MCP_MODE=http python -m src.main
```

### Run tests
```bash
pytest tests/ -v
python scripts/test_connection.py
```

### Linting
```bash
ruff check .
black .
mypy src/
```

## Architecture

### Core Components

- **`src/main.py`** - FastMCP server entry point. Defines all MCP tools that expose pfSense functionality. Uses a global `EnhancedPfSenseAPIClient` singleton.

- **`src/pfsense_api_enhanced.py`** - HTTP client for pfSense REST API v2:
  - `EnhancedPfSenseAPIClient` - async HTTP client with auth (API key, Basic, JWT)
  - `_make_request()` at ~line 220 - central request handler (check here for HTTP issues)
  - Data classes: `QueryFilter`, `SortOptions`, `PaginationOptions`, `ControlParameters`

### Key Patterns

**MCP Tool Registration**:
```python
@mcp.tool()
async def create_firewall_rule_advanced(...) -> Dict:
    client = get_api_client()
    # ...
```

**Control Parameters**: Operations support `ControlParameters(apply=True)` to apply changes immediately.

## API Endpoints

Read operations use plural, write operations use singular:
- GET `/api/v2/firewall/rules` (list)
- POST `/api/v2/firewall/rule` (create)
- PATCH `/api/v2/firewall/rule/{id}` (update)
- DELETE `/api/v2/firewall/rule` with `{"id": X}` body (delete)

Same pattern for aliases, NAT port forwards, etc.
