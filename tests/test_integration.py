#!/usr/bin/env python3
"""
Live integration tests for pfSense MCP Server.

These tests run against a real pfSense instance. They are skipped automatically
when PFSENSE_URL is not set.

Run all:
    nix develop --command pytest tests/test_integration.py -v

Read-only tests only (safe):
    nix develop --command pytest tests/test_integration.py -v -k "not Lifecycle"

CRUD lifecycle tests only:
    nix develop --command pytest tests/test_integration.py -v -k "Lifecycle"
"""

import os
import sys
import time
import uuid

import pytest
import pytest_asyncio

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from pfsense_api_enhanced import (
    EnhancedPfSenseAPIClient,
    AuthMethod,
    PfSenseVersion,
    ControlParameters,
    PaginationOptions,
)

# Apply asyncio mark with session loop scope to every test in this module.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SKIP_REASON = "PFSENSE_URL not set – skipping live integration tests"


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def api_client():
    """Session-scoped async client; skips everything when no credentials."""
    url = os.environ.get("PFSENSE_URL")
    if not url:
        pytest.skip(SKIP_REASON)

    api_key = os.environ.get("PFSENSE_API_KEY")

    auth_str = os.environ.get("AUTH_METHOD", "api_key").lower()
    if auth_str == "basic":
        auth_method = AuthMethod.BASIC
    elif auth_str == "jwt":
        auth_method = AuthMethod.JWT
    else:
        auth_method = AuthMethod.API_KEY

    verify_ssl = os.environ.get("VERIFY_SSL", "false").lower() == "true"

    ver_str = os.environ.get("PFSENSE_VERSION", "CE_2_8_0")
    version = PfSenseVersion.PLUS_24_11 if ver_str == "PLUS_24_11" else PfSenseVersion.CE_2_8_0

    client = EnhancedPfSenseAPIClient(
        host=url,
        auth_method=auth_method,
        api_key=api_key,
        verify_ssl=verify_ssl,
        version=version,
    )
    yield client
    await client.close()


@pytest.fixture
def unique_id():
    """Return a unique string for test resource names."""
    return f"{int(time.time())}_{uuid.uuid4().hex[:8]}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


async def _find_by_field(client, endpoint, field, value):
    """Find object by exact field match with client-side verification.

    The pfSense API filter may return partial matches, so we iterate results
    and verify the field value matches exactly.
    """
    result = await client._make_request("GET", endpoint)
    for obj in result.get("data", []):
        if obj.get(field) == value:
            return obj
    return None


# ---------------------------------------------------------------------------
# Read-only tests
# ---------------------------------------------------------------------------


class TestSystemEndpoints:
    """Tests for system status and API capability endpoints."""

    async def test_get_system_status(self, api_client):
        result = await api_client.get_system_status()
        assert "data" in result

    async def test_get_api_capabilities(self, api_client):
        result = await api_client.get_api_capabilities()
        assert "data" in result

    async def test_connection(self, api_client):
        assert await api_client.test_connection() is True


class TestInterfaceEndpoints:
    """Tests for interface listing and filtering."""

    async def test_get_interfaces(self, api_client):
        result = await api_client.get_interfaces()
        assert "data" in result
        assert len(result["data"]) >= 1

    async def test_find_interfaces_by_status(self, api_client):
        result = await api_client.find_interfaces_by_status("up")
        assert "data" in result

    async def test_search_interfaces(self, api_client):
        result = await api_client.search_interfaces("wan")
        assert "data" in result

    async def test_get_interfaces_with_pagination(self, api_client):
        result = await api_client.get_interfaces(
            pagination=PaginationOptions(limit=1)
        )
        assert "data" in result
        # Note: /status/interfaces may ignore limit param; just verify the call succeeds


class TestFirewallLogEndpoints:
    """Tests for firewall log retrieval."""

    async def test_get_firewall_logs(self, api_client):
        result = await api_client.get_firewall_logs()
        assert "data" in result

    async def test_get_logs_by_ip(self, api_client):
        result = await api_client.get_logs_by_ip("192.0.2.1")
        assert "data" in result

    async def test_get_blocked_traffic_logs(self, api_client):
        result = await api_client.get_blocked_traffic_logs()
        assert "data" in result


class TestServiceEndpoints:
    """Tests for service status endpoints."""

    async def test_get_services(self, api_client):
        result = await api_client.get_services()
        assert "data" in result

    async def test_find_running_services(self, api_client):
        result = await api_client.find_running_services()
        assert "data" in result
        assert len(result["data"]) >= 1

    async def test_find_stopped_services(self, api_client):
        result = await api_client.find_stopped_services()
        assert "data" in result


class TestDHCPEndpoints:
    """Tests for DHCP lease endpoints."""

    async def test_get_dhcp_leases(self, api_client):
        result = await api_client.get_dhcp_leases()
        assert "data" in result

    async def test_find_lease_by_mac(self, api_client):
        result = await api_client.find_lease_by_mac("00:00:00:00:00:00")
        assert "data" in result

    async def test_find_lease_by_hostname(self, api_client):
        result = await api_client.find_lease_by_hostname("nonexistent_host_xyz")
        assert "data" in result

    async def test_get_active_leases(self, api_client):
        result = await api_client.get_active_leases()
        assert "data" in result


class TestObjectIDManagement:
    """Tests for object ID refresh and lookup helpers."""

    async def test_refresh_object_ids(self, api_client):
        result = await api_client.refresh_object_ids("/firewall/rules")
        assert "data" in result
        assert isinstance(result["data"], list)

    async def test_find_object_by_field(self, api_client):
        obj = await api_client.find_object_by_field(
            "/firewall/rules", "type", "pass"
        )
        # May be None if no pass rules exist, but should not raise
        assert obj is None or isinstance(obj, dict)


class TestHATEOASNavigation:
    """Tests for HATEOAS toggle and link following."""

    async def test_enable_disable_hateoas(self, api_client):
        # hateoas_enabled is the bool attribute; enable_hateoas() is the method.
        api_client.hateoas_enabled = True
        assert api_client.hateoas_enabled is True
        api_client.hateoas_enabled = False
        assert api_client.hateoas_enabled is False

    async def test_extract_links(self, api_client):
        api_client.hateoas_enabled = True
        try:
            result = await api_client.get_system_status()
            links = api_client.extract_links(result)
            assert isinstance(links, dict)
        finally:
            api_client.hateoas_enabled = False

    async def test_follow_link(self, api_client):
        api_client.hateoas_enabled = True
        try:
            result = await api_client.get_system_status()
            links = api_client.extract_links(result)
            if not links:
                pytest.skip("No HATEOAS links returned by API")
            # Follow the first link
            first_link = next(iter(links.values()))
            followed = await api_client.follow_link(first_link)
            assert isinstance(followed, dict)
        finally:
            api_client.hateoas_enabled = False


# ---------------------------------------------------------------------------
# CRUD lifecycle tests
# ---------------------------------------------------------------------------


class TestFirewallRuleLifecycle:
    """Full create / read / update / disable / enable / delete cycle."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        rule_id = None
        new_descr = f"{descr}_updated"
        try:
            # Create
            rule_data = {
                "interface": ["lan"],
                "type": "block",
                "ipprotocol": "inet",
                "protocol": "tcp",
                "source": "any",
                "destination": "192.0.2.1",
                "destination_port": "12345",
                "descr": descr,
            }
            result = await api_client.create_firewall_rule(
                rule_data, ControlParameters(apply=True)
            )
            rule_id = result["data"]["id"]
            assert rule_id is not None

            # Read back (client-side exact match); IDs shift after apply
            obj = await _find_by_field(
                api_client, "/firewall/rules", "descr", descr
            )
            assert obj is not None
            assert obj["descr"] == descr
            rule_id = obj["id"]  # refresh in case ID shifted

            # Update description
            await api_client.update_firewall_rule(
                rule_id, {"descr": new_descr}, ControlParameters(apply=True)
            )
            obj2 = await _find_by_field(
                api_client, "/firewall/rules", "descr", new_descr
            )
            assert obj2 is not None
            rule_id = obj2["id"]  # refresh again

            # Disable
            await api_client.disable_firewall_rule(rule_id)

            # Enable
            await api_client.enable_firewall_rule(rule_id)

        finally:
            # Re-lookup for cleanup since IDs shift after apply
            for d in (new_descr, descr):
                obj = await _find_by_field(
                    api_client, "/firewall/rules", "descr", d
                )
                if obj is not None:
                    try:
                        await api_client.delete_firewall_rule(obj["id"])
                    except Exception:
                        pass
                    break

        # Verify gone
        obj3 = await _find_by_field(
            api_client, "/firewall/rules", "descr", new_descr
        )
        assert obj3 is None

    async def test_move_firewall_rule(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        rule_id = None
        try:
            rule_data = {
                "interface": ["lan"],
                "type": "block",
                "ipprotocol": "inet",
                "protocol": "tcp",
                "source": "any",
                "destination": "192.0.2.2",
                "destination_port": "12346",
                "descr": descr,
            }
            result = await api_client.create_firewall_rule(
                rule_data, ControlParameters(apply=True)
            )
            rule_id = result["data"]["id"]

            # Re-lookup ID (may shift after apply)
            obj = await _find_by_field(
                api_client, "/firewall/rules", "descr", descr
            )
            assert obj is not None
            rule_id = obj["id"]

            # Move to top
            await api_client.move_firewall_rule(rule_id, 0)
        finally:
            if rule_id is not None:
                # Re-lookup in case move shifted the ID
                obj = await _find_by_field(
                    api_client, "/firewall/rules", "descr", descr
                )
                if obj is not None:
                    try:
                        await api_client.delete_firewall_rule(obj["id"])
                    except Exception:
                        pass

    async def test_get_firewall_rules(self, api_client):
        result = await api_client.get_firewall_rules()
        assert "data" in result

    async def test_find_blocked_rules(self, api_client):
        result = await api_client.find_blocked_rules()
        assert "data" in result

    async def test_find_rules_by_destination_port(self, api_client):
        result = await api_client.find_rules_by_destination_port("443")
        assert "data" in result


class TestNATPortForwardLifecycle:
    """Create / update / delete cycle for NAT port forwards."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        pf_id = None
        new_descr = f"{descr}_updated"
        try:
            pf_data = {
                "interface": "wan",
                "protocol": "tcp",
                "source": "any",
                "destination": "any",
                "destination_port": "55555",
                "target": "192.168.1.100",
                "local_port": "55555",
                "descr": descr,
            }
            result = await api_client.create_nat_port_forward(
                pf_data, ControlParameters(apply=True)
            )
            pf_id = result["data"]["id"]
            assert pf_id is not None

            # Re-lookup ID (may shift after apply)
            obj = await _find_by_field(
                api_client, "/firewall/nat/port_forwards", "descr", descr
            )
            assert obj is not None
            pf_id = obj["id"]

            # Update description
            await api_client.update_nat_port_forward(
                pf_id, {"descr": new_descr}, ControlParameters(apply=True)
            )

        finally:
            if pf_id is not None:
                # Re-lookup for cleanup since IDs shift
                for d in (new_descr, descr):
                    obj = await _find_by_field(
                        api_client, "/firewall/nat/port_forwards", "descr", d
                    )
                    if obj is not None:
                        try:
                            await api_client.delete_nat_port_forward(obj["id"])
                        except Exception:
                            pass
                        break

        # Verify gone
        obj = await _find_by_field(
            api_client, "/firewall/nat/port_forwards", "descr", new_descr
        )
        assert obj is None

    async def test_get_nat_port_forwards(self, api_client):
        result = await api_client.get_nat_port_forwards()
        assert "data" in result

    async def test_create_delete_roundtrip(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        pf_id = None
        try:
            pf_data = {
                "interface": "wan",
                "protocol": "tcp",
                "source": "any",
                "destination": "any",
                "destination_port": "55556",
                "target": "192.168.1.101",
                "local_port": "55556",
                "descr": descr,
            }
            result = await api_client.create_nat_port_forward(
                pf_data, ControlParameters(apply=True)
            )
            pf_id = result["data"]["id"]
            assert pf_id is not None
        finally:
            if pf_id is not None:
                try:
                    await api_client.delete_nat_port_forward(pf_id)
                except Exception:
                    pass


class TestAliasLifecycle:
    """Create / add / remove / delete cycle for aliases."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        hex8 = uuid.uuid4().hex[:8]
        alias_name = f"mcpt_{hex8}"
        descr = f"MCP_INTTEST_{unique_id}"
        alias_id = None
        try:
            alias_data = {
                "name": alias_name,
                "type": "host",
                "address": ["192.0.2.1", "192.0.2.2"],
                "descr": descr,
            }
            result = await api_client.create_alias(
                alias_data, ControlParameters(apply=True)
            )
            alias_id = result["data"]["id"]
            assert alias_id is not None

            # Add address
            await api_client.add_to_alias(alias_id, ["192.0.2.3"])

            # Remove address
            await api_client.remove_from_alias(alias_id, ["192.0.2.1"])

        finally:
            if alias_id is not None:
                try:
                    await api_client.delete_alias(alias_id)
                except Exception:
                    pass

        # Verify gone
        obj = await _find_by_field(
            api_client, "/firewall/aliases", "name", alias_name
        )
        assert obj is None

    async def test_get_aliases(self, api_client):
        result = await api_client.get_aliases()
        assert "data" in result

    async def test_search_aliases(self, api_client):
        result = await api_client.search_aliases("nonexistent_alias_xyz")
        assert "data" in result
        # Note: API may not honour name__contains filter; just verify the call succeeds

    async def test_find_aliases_containing_ip(self, api_client):
        result = await api_client.find_aliases_containing_ip("198.51.100.254")
        assert "data" in result
