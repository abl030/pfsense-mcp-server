# TODO: Live API Integration Testing

## Problem

Current validation only does static analysis:
- `tests/test_openapi_validation.py` - validates code patterns against OpenAPI spec
- `scripts/validate_against_spec.py` - scans for field name mismatches

Neither confirms requests actually succeed against the live pfSense API.

## Proposed Solution

Create `tests/test_integration.py` that:

1. **Creates resources** (firewall rule, NAT port forward, alias)
2. **Verifies creation** via GET
3. **Modifies resources** (PATCH)
4. **Deletes resources**
5. **Verifies deletion**

Requirements:
- Needs live pfSense instance with API v2
- Should clean up after itself (delete test resources)
- Skip if credentials not available
- Use unique descriptions/names to avoid conflicts

## Example Structure

```python
@pytest.fixture
def api_client():
    """Skip if no credentials available."""
    if not os.environ.get('PFSENSE_URL'):
        pytest.skip("No PFSENSE_URL configured")
    return EnhancedPfSenseAPIClient(...)

class TestFirewallRuleIntegration:
    async def test_create_read_delete_rule(self, api_client):
        # Create
        rule = await api_client.create_firewall_rule({...})
        rule_id = rule['data']['id']

        # Verify exists
        rules = await api_client.get_firewall_rules()
        assert any(r['id'] == rule_id for r in rules['data'])

        # Delete
        await api_client.delete_firewall_rule(rule_id)

        # Verify gone
        rules = await api_client.get_firewall_rules()
        assert not any(r['id'] == rule_id for r in rules['data'])
```

## Run Command

```bash
# With credentials configured
nix develop --command pytest tests/test_integration.py -v

# Or with explicit env vars
PFSENSE_URL=https://... PFSENSE_API_KEY=... pytest tests/test_integration.py -v
```
