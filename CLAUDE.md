# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Model Context Protocol (MCP) server that enables natural language interaction with pfSense firewalls through Claude Desktop and other GenAI applications. It uses the pfSense REST API v2 package ([jaredhendrickson13/pfsense-api](https://github.com/jaredhendrickson13/pfsense-api)).

## OpenAPI Spec Workflow

The pfSense API has an OpenAPI spec that defines the correct request/response formats. **Always check the spec before assuming field names or request formats.**

### Fetching the Spec

The spec is fetched from the live pfSense instance and saved locally:

```bash
# Fetch fresh spec (4MB, 258 endpoints)
source /run/secrets/mcp/pfsense.env
curl -sk "$PFSENSE_HOST/api/v2/schema/openapi" -H "X-API-Key: $PFSENSE_API_KEY" -o openapi/pfsense-api-v2.json
```

### Checking Field Names/Types

```bash
python3 << 'EOF'
import json
with open('openapi/pfsense-api-v2.json') as f:
    spec = json.load(f)

# Check a specific schema
schema = spec['components']['schemas']['FirewallRule']
for prop, details in schema['properties'].items():
    print(f"{prop}: {details.get('type', 'ref')}")

# Check required fields for POST
post = spec['paths']['/api/v2/firewall/rule']['post']
for item in post['requestBody']['content']['application/json']['schema'].get('allOf', []):
    if 'required' in item:
        print(f"Required: {item['required']}")
EOF
```

### Validation Tests

Run `tests/test_openapi_validation.py` to validate our implementation matches the spec:

```bash
nix develop --command pytest tests/test_openapi_validation.py -v
```

For programmatic scanning of field mismatches:

```bash
python scripts/validate_against_spec.py
```

These tests/scripts catch:
- Wrong field types (e.g., `interface` should be array not string)
- Wrong field names (e.g., `source` not `src`)
- Missing required fields

### Spec vs Reality

**The spec isn't always accurate.** Document discrepancies:
- Spec says DELETE uses query param `?id=X`, but httpx DELETE with query params returns 400. Body `{"id": X}` works.
- Always test with actual API calls after checking spec.

## Testing

### Quick Test with Nix

```bash
nix develop --command python << 'EOF'
import asyncio, os, sys
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

    # Test create
    rule_data = {
        "interface": ["lan"],  # MUST be array
        "type": "block",
        "ipprotocol": "inet",
        "protocol": "tcp",
        "source": "any",  # NOT "src"
        "destination": "1.1.1.1",  # NOT "dst"
        "destination_port": "12345",  # NOT "dstport"
        "descr": "TEST"
    }
    result = await client.create_firewall_rule(rule_data, ControlParameters(apply=True))
    rule_id = result['data']['id']
    print(f"Created: {rule_id}")

    # Test delete (body, not query param)
    await client.delete_firewall_rule(rule_id)
    print(f"Deleted: {rule_id}")

asyncio.run(test())
EOF
```

### Credentials

Secrets at `/run/secrets/mcp/pfsense.env` (NixOS sops-nix):
```
PFSENSE_HOST=https://192.168.1.1
PFSENSE_API_KEY=<key>
PFSENSE_VERIFY_SSL=false
```

The flake.nix shellHook exports `PFSENSE_URL` from `PFSENSE_HOST`.

## pfSense API v2 Quirks

**Critical - wrong format = 400/404 errors:**

1. **`interface` field differs by schema**:
   - **FirewallRule**: `["lan"]` (array)
   - **PortForward**: `"lan"` (string)
   - Always check OpenAPI spec for the specific schema

2. **Field names** (check OpenAPI spec for others):
   - `source` / `destination` (not `src` / `dst`)
   - `source_port` / `destination_port` (not `srcport` / `dstport`)

3. **DELETE uses body**: `{"id": X}` not URL path `/rule/40`

4. **PATCH for aliases uses body with id**: `{"id": X, "address": [...]}` not URL path

5. **httpx quirk**: Use `.request("DELETE", ...)` not `.delete()` for body support

## Architecture

### Core Components

- **`src/main.py`** - MCP tools (FastMCP `@mcp.tool()` decorators)
- **`src/pfsense_api_enhanced.py`** - HTTP client
  - `_make_request()` ~line 220 - central request handler
  - Check here first for HTTP/format issues
- **`openapi/pfsense-api-v2.json`** - API spec (source of truth for field names)
- **`tests/test_openapi_validation.py`** - Validates implementation vs spec

### Endpoint Patterns

| Operation | Endpoint | Notes |
|-----------|----------|-------|
| List | GET `/firewall/rules` | Plural |
| Create | POST `/firewall/rule` | Singular |
| Update | PATCH `/firewall/rule` | Body: `{"id": X, ...}` |
| Delete | DELETE `/firewall/rule` | Body: `{"id": X}` |

Same pattern for `/firewall/alias`, `/firewall/nat/port_forward`, etc.

## Commands

```bash
# Dev environment
nix develop

# Run tests
nix develop --command pytest tests/ -v

# Run MCP server
MCP_MODE=stdio python -m src.main
```
