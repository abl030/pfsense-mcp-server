"""Auto-generated integration tests. DO NOT EDIT.
Regenerate: python scripts/generate_from_spec.py
"""

import os
import sys
import uuid

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from pfsense_api_enhanced import ControlParameters
from conftest import _find_by_field

pytestmark = pytest.mark.asyncio(loop_scope="session")


class TestNatOneToOneMappingReadOnly:
    """Read-only tests for NAT one-to-one mapping."""

    async def test_get_nat_one_to_one_mappings(self, api_client):
        result = await api_client.get_nat_one_to_one_mappings()
        assert "data" in result


class TestNatOneToOneMappingLifecycle:
    """CRUD lifecycle test for NAT one-to-one mapping."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'interface': 'wan', 'external': '198.51.100.50', 'source': '192.168.1.0/24', 'destination': 'any'}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_nat_one_to_one_mapping(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/firewall/nat/one_to_one/mappings", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_nat_one_to_one_mapping(
                item_id, {'external': '198.51.100.51'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/firewall/nat/one_to_one/mappings", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_nat_one_to_one_mapping(obj["id"])
                except Exception:
                    pass


class TestNatOutboundMappingReadOnly:
    """Read-only tests for NAT outbound mapping."""

    async def test_get_nat_outbound_mappings(self, api_client):
        result = await api_client.get_nat_outbound_mappings()
        assert "data" in result


class TestNatOutboundMappingLifecycle:
    """CRUD lifecycle test for NAT outbound mapping."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'interface': 'wan', 'source': '192.168.1.0/24', 'destination': 'any', 'target': '198.51.100.1', 'protocol': 'any'}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_nat_outbound_mapping(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/firewall/nat/outbound/mappings", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_nat_outbound_mapping(
                item_id, {'target': '198.51.100.2'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/firewall/nat/outbound/mappings", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_nat_outbound_mapping(obj["id"])
                except Exception:
                    pass


class TestNatOutboundModeReadOnly:
    """Read-only tests for NAT outbound mode."""

    async def test_get_nat_outbound_mode(self, api_client):
        result = await api_client.get_nat_outbound_mode()
        assert "data" in result


class TestFirewallScheduleReadOnly:
    """Read-only tests for firewall schedule."""

    async def test_get_firewall_schedules(self, api_client):
        result = await api_client.get_firewall_schedules()
        assert "data" in result


class TestFirewallScheduleLifecycle:
    """CRUD lifecycle test for firewall schedule."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'timerange': [{'month': '1,2,3,4,5,6,7,8,9,10,11,12', 'day': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31', 'hour': '0:00-23:59', 'rangedescr': 'All times'}]}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_firewall_schedule(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/firewall/schedules", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_firewall_schedule(
                item_id, {'descr': 'Updated schedule'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/firewall/schedules", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_firewall_schedule(obj["id"])
                except Exception:
                    pass


class TestFirewallScheduleTimeRangeReadOnly:
    """Read-only tests for firewall schedule time range."""

    async def test_get_firewall_schedule_time_ranges(self, api_client):
        result = await api_client.get_firewall_schedule_time_ranges()
        assert "data" in result


class TestTrafficShaperReadOnly:
    """Read-only tests for traffic shaper."""

    async def test_get_traffic_shapers(self, api_client):
        result = await api_client.get_traffic_shapers()
        assert "data" in result


class TestTrafficShaperLifecycle:
    """CRUD lifecycle test for traffic shaper."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'interface': 'lan', 'scheduler': 'HFSC', 'bandwidthtype': 'Mb', 'bandwidth': 100, 'enabled': True}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_traffic_shaper(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/firewall/traffic_shapers", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_traffic_shaper(
                item_id, {'bandwidth': 200}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/firewall/traffic_shapers", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_traffic_shaper(obj["id"])
                except Exception:
                    pass


class TestTrafficShaperQueueReadOnly:
    """Read-only tests for traffic shaper queue."""

    async def test_get_traffic_shaper_queues(self, api_client):
        result = await api_client.get_traffic_shaper_queues()
        assert "data" in result


class TestTrafficShaperLimiterReadOnly:
    """Read-only tests for traffic shaper limiter."""

    async def test_get_traffic_shaper_limiters(self, api_client):
        result = await api_client.get_traffic_shaper_limiters()
        assert "data" in result


class TestTrafficShaperLimiterLifecycle:
    """CRUD lifecycle test for traffic shaper limiter."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'name': 'testlimiter', 'aqm': 'droptail', 'sched': 'wf2q+', 'enabled': True}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_traffic_shaper_limiter(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/firewall/traffic_shaper/limiters", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_traffic_shaper_limiter(
                item_id, {'description': 'Updated limiter'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/firewall/traffic_shaper/limiters", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_traffic_shaper_limiter(obj["id"])
                except Exception:
                    pass


class TestTrafficShaperLimiterQueueReadOnly:
    """Read-only tests for traffic shaper limiter queue."""

    async def test_get_traffic_shaper_limiter_queues(self, api_client):
        result = await api_client.get_traffic_shaper_limiter_queues()
        assert "data" in result


class TestTrafficShaperLimiterBandwidthReadOnly:
    """Read-only tests for traffic shaper limiter bandwidth."""

    async def test_get_traffic_shaper_limiter_bandwidths(self, api_client):
        result = await api_client.get_traffic_shaper_limiter_bandwidths()
        assert "data" in result


class TestVirtualIpReadOnly:
    """Read-only tests for virtual IP."""

    async def test_get_virtual_ips(self, api_client):
        result = await api_client.get_virtual_ips()
        assert "data" in result


class TestVirtualIpLifecycle:
    """CRUD lifecycle test for virtual IP."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'mode': 'ipalias', 'interface': 'lan', 'subnet': '10.255.255.1', 'subnet_bits': 32, 'descr': '', 'type': 'single'}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_virtual_ip(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/firewall/virtual_ips", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_virtual_ip(
                item_id, {'subnet': '10.255.255.2'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/firewall/virtual_ips", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_virtual_ip(obj["id"])
                except Exception:
                    pass


class TestVirtualIpApplyReadOnly:
    """Read-only tests for virtual IP apply."""

    async def test_get_virtual_ip_apply_status(self, api_client):
        result = await api_client.get_virtual_ip_apply_status()
        assert "data" in result


class TestFirewallStateReadOnly:
    """Read-only tests for firewall state."""

    async def test_get_firewall_states(self, api_client):
        result = await api_client.get_firewall_states()
        assert "data" in result


class TestFirewallStatesSizeReadOnly:
    """Read-only tests for firewall states size."""

    async def test_get_firewall_states_size(self, api_client):
        result = await api_client.get_firewall_states_size()
        assert "data" in result


class TestFirewallAdvancedSettingsReadOnly:
    """Read-only tests for firewall advanced settings."""

    async def test_get_firewall_advanced_settings(self, api_client):
        result = await api_client.get_firewall_advanced_settings()
        assert "data" in result


class TestFirewallApplyReadOnly:
    """Read-only tests for firewall apply."""

    async def test_get_firewall_apply_status(self, api_client):
        result = await api_client.get_firewall_apply_status()
        assert "data" in result


class TestRoutingGatewayReadOnly:
    """Read-only tests for routing gateway."""

    async def test_get_routing_gateways(self, api_client):
        result = await api_client.get_routing_gateways()
        assert "data" in result


class TestRoutingGatewayLifecycle:
    """CRUD lifecycle test for routing gateway."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'name': '', 'ipprotocol': 'inet', 'interface': 'wan', 'gateway': '198.51.100.254'}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_routing_gateway(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/routing/gateways", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_routing_gateway(
                item_id, {'descr': 'Updated gateway'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/routing/gateways", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_routing_gateway(obj["id"])
                except Exception:
                    pass


class TestRoutingGatewayDefaultReadOnly:
    """Read-only tests for default routing gateway."""

    async def test_get_routing_gateway_default(self, api_client):
        result = await api_client.get_routing_gateway_default()
        assert "data" in result


class TestRoutingGatewayGroupReadOnly:
    """Read-only tests for routing gateway group."""

    async def test_get_routing_gateway_groups(self, api_client):
        result = await api_client.get_routing_gateway_groups()
        assert "data" in result


class TestRoutingGatewayGroupLifecycle:
    """CRUD lifecycle test for routing gateway group."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'name': '', 'trigger': 'down', 'descr': '', 'ipprotocol': 'inet', 'priorities': []}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_routing_gateway_group(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/routing/gateway/groups", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_routing_gateway_group(
                item_id, {'descr': 'Updated gateway group'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/routing/gateway/groups", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_routing_gateway_group(obj["id"])
                except Exception:
                    pass


class TestRoutingGatewayGroupPriorityReadOnly:
    """Read-only tests for routing gateway group priority."""

    async def test_get_routing_gateway_group_prioritys(self, api_client):
        result = await api_client.get_routing_gateway_group_prioritys()
        assert "data" in result


class TestRoutingStaticRouteReadOnly:
    """Read-only tests for static route."""

    async def test_get_routing_static_routes(self, api_client):
        result = await api_client.get_routing_static_routes()
        assert "data" in result


class TestRoutingStaticRouteLifecycle:
    """CRUD lifecycle test for static route."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'network': '10.99.99.0/24', 'gateway': 'WAN_DHCP'}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_routing_static_route(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/routing/static_routes", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_routing_static_route(
                item_id, {'descr': 'Updated route'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/routing/static_routes", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_routing_static_route(obj["id"])
                except Exception:
                    pass


class TestRoutingApplyReadOnly:
    """Read-only tests for routing apply."""

    async def test_get_routing_apply_status(self, api_client):
        result = await api_client.get_routing_apply_status()
        assert "data" in result
