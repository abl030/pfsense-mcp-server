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

- **`src/main.py`** - Hand-written MCP tools (FastMCP `@mcp.tool()` decorators) + imports generated tools
- **`src/pfsense_api_enhanced.py`** - HTTP client (inherits `GeneratedFirewallMixin`)
  - `_make_request()` ~line 220 - central request handler
  - Check here first for HTTP/format issues
- **`src/generated_client.py`** - **Generated** — 288 async client methods (mixin class). Do not hand-edit.
- **`src/generated_tools.py`** - **Generated** — 288 MCP tool registrations. Do not hand-edit.
- **`scripts/generate_from_spec.py`** - Code generator. Fix this, then re-run, to change generated output.
- **`openapi/pfsense-api-v2.json`** - API spec (source of truth for field names)
- **`tests/test_integration.py`** - Hand-written integration tests
- **`tests/test_generated_integration.py`** - **Generated** — 131 test classes. Do not hand-edit.
- **`tests/conftest.py`** - Shared fixtures (`api_client`, `unique_id`, `_find_by_field`)

### Generated Code Workflow

Generated files (`src/generated_client.py`, `src/generated_tools.py`, `tests/test_generated_integration.py`) are build artifacts. **Never hand-edit them.** To fix bugs or add endpoints:

```bash
# 1. Edit the generator
vim scripts/generate_from_spec.py

# 2. Re-run it
nix develop --command python scripts/generate_from_spec.py

# 3. Test
nix develop --command pytest tests/test_generated_integration.py -v -k "not Lifecycle"
```

### Endpoint Patterns

| Operation | Endpoint | Notes |
|-----------|----------|-------|
| List | GET `/firewall/rules` | Plural |
| Create | POST `/firewall/rule` | Singular |
| Update | PATCH `/firewall/rule` | Body: `{"id": X, ...}` |
| Delete | DELETE `/firewall/rule` | Body: `{"id": X}` |

Same pattern for `/firewall/alias`, `/firewall/nat/port_forward`, etc.

## pfSense API v2 Learnings

Beyond the quirks listed above, these were discovered during code generation:

1. **Nested resources sometimes require parent_id even for GET listing** — `/system/crl/revoked_certificate` returns 400 without a `parent_id`. Most other nested resources (schedule/time_range, limiter/queue) don't require it for listing.

2. **IDs shift after apply** — Creating a rule with `apply=True` may change the IDs of other rules. Always re-lookup by description/name field after create before doing updates or deletes.

3. **POST-only action endpoints exist** — `/services/wake_on_lan/send` has POST but no GET. The generator skips read-only tests for these.

4. **Some plural paths don't follow the convention** — Most endpoints use `singular` + `s` for plural, but some (like settings endpoints) use the same path for both GET-list and GET-single.

5. **`interface` field type varies per schema** — FirewallRule uses array `["lan"]`, PortForward uses string `"lan"`, some schemas use neither. Always check the OpenAPI spec for each specific schema.

## Commands

```bash
# Dev environment
nix develop

# Run all tests (excluding stale enhanced features tests)
nix develop --command pytest tests/ -v --ignore=tests/test_enhanced_features.py

# Run only hand-written integration tests
nix develop --command pytest tests/test_integration.py -v

# Run generated read-only tests (safe)
nix develop --command pytest tests/test_generated_integration.py -v -k "not Lifecycle"

# Regenerate from spec
nix develop --command python scripts/generate_from_spec.py

# Run MCP server
MCP_MODE=stdio python -m src.main
```
