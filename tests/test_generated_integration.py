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


class TestInterfaceReadOnly:
    """Read-only tests for network interface."""

    async def test_get_interfaces(self, api_client):
        result = await api_client.get_interfaces()
        assert "data" in result


class TestInterfaceLifecycle:
    """CRUD lifecycle test for network interface."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'if': 'lo0', 'descr': '', 'typev4': 'none', 'ipaddr': '', 'subnet': ''}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_interface(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/interfaces", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_interface(
                item_id, {'descr': 'Updated iface'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/interfaces", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_interface(obj["id"])
                except Exception:
                    pass


class TestInterfaceApplyReadOnly:
    """Read-only tests for interface apply."""

    async def test_get_interface_apply_status(self, api_client):
        result = await api_client.get_interface_apply_status()
        assert "data" in result


class TestAvailableInterfacesReadOnly:
    """Read-only tests for available interfaces."""

    async def test_get_available_interfaces(self, api_client):
        result = await api_client.get_available_interfaces()
        assert "data" in result


class TestInterfaceBridgeReadOnly:
    """Read-only tests for interface bridge."""

    async def test_get_interface_bridges(self, api_client):
        result = await api_client.get_interface_bridges()
        assert "data" in result


class TestInterfaceBridgeLifecycle:
    """CRUD lifecycle test for interface bridge."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'members': ['lan']}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_interface_bridge(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/interface/bridges", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_interface_bridge(
                item_id, {'descr': 'Updated bridge'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/interface/bridges", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_interface_bridge(obj["id"])
                except Exception:
                    pass


class TestInterfaceGroupReadOnly:
    """Read-only tests for interface group."""

    async def test_get_interface_groups(self, api_client):
        result = await api_client.get_interface_groups()
        assert "data" in result


class TestInterfaceGroupLifecycle:
    """CRUD lifecycle test for interface group."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'ifname': '', 'members': [], 'descr': ''}
        create_data["ifname"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_interface_group(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/interface/groups", "ifname", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_interface_group(
                item_id, {'descr': 'Updated group'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/interface/groups", "ifname", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_interface_group(obj["id"])
                except Exception:
                    pass


class TestInterfaceVlanReadOnly:
    """Read-only tests for interface VLAN."""

    async def test_get_interface_vlans(self, api_client):
        result = await api_client.get_interface_vlans()
        assert "data" in result


class TestInterfaceVlanLifecycle:
    """CRUD lifecycle test for interface VLAN."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'if': 'lan', 'tag': 4000, 'descr': ''}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_interface_vlan(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/interface/vlans", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_interface_vlan(
                item_id, {'descr': 'Updated VLAN'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/interface/vlans", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_interface_vlan(obj["id"])
                except Exception:
                    pass


class TestInterfaceGreReadOnly:
    """Read-only tests for interface GRE tunnel."""

    async def test_get_interface_gres(self, api_client):
        result = await api_client.get_interface_gres()
        assert "data" in result


class TestInterfaceGreLifecycle:
    """CRUD lifecycle test for interface GRE tunnel."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'if': 'wan', 'remote_addr': '198.51.100.1', 'tunnel_remote_addr': '10.0.0.2', 'tunnel_remote_addr6': '::1'}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_interface_gre(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/interface/gres", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_interface_gre(
                item_id, {'descr': 'Updated GRE'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/interface/gres", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_interface_gre(obj["id"])
                except Exception:
                    pass


class TestInterfaceLaggReadOnly:
    """Read-only tests for interface LAGG."""

    async def test_get_interface_laggs(self, api_client):
        result = await api_client.get_interface_laggs()
        assert "data" in result


class TestInterfaceLaggLifecycle:
    """CRUD lifecycle test for interface LAGG."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'members': ['lan'], 'proto': 'none'}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_interface_lagg(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/interface/laggs", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_interface_lagg(
                item_id, {'descr': 'Updated LAGG'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/interface/laggs", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_interface_lagg(obj["id"])
                except Exception:
                    pass


class TestDhcpServerReadOnly:
    """Read-only tests for DHCP server."""

    async def test_get_dhcp_servers(self, api_client):
        result = await api_client.get_dhcp_servers()
        assert "data" in result


class TestDhcpServerLifecycle:
    """CRUD lifecycle test for DHCP server."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'interface': 'lan'}
        create_data["interface"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_dhcp_server(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/services/dhcp_servers", "interface", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_dhcp_server(
                item_id, {'domain': 'test.local'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/services/dhcp_servers", "interface", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_dhcp_server(obj["id"])
                except Exception:
                    pass


class TestDhcpServerStaticMappingReadOnly:
    """Read-only tests for DHCP static mapping."""

    async def test_get_dhcp_server_static_mappings(self, api_client):
        result = await api_client.get_dhcp_server_static_mappings()
        assert "data" in result


class TestDhcpServerAddressPoolReadOnly:
    """Read-only tests for DHCP address pool."""

    async def test_get_dhcp_server_address_pools(self, api_client):
        result = await api_client.get_dhcp_server_address_pools()
        assert "data" in result


class TestDhcpServerCustomOptionReadOnly:
    """Read-only tests for DHCP custom option."""

    async def test_get_dhcp_server_custom_options(self, api_client):
        result = await api_client.get_dhcp_server_custom_options()
        assert "data" in result


class TestDhcpServerApplyReadOnly:
    """Read-only tests for DHCP server apply."""

    async def test_get_dhcp_server_apply_status(self, api_client):
        result = await api_client.get_dhcp_server_apply_status()
        assert "data" in result


class TestDhcpRelayReadOnly:
    """Read-only tests for DHCP relay."""

    async def test_get_dhcp_relay(self, api_client):
        result = await api_client.get_dhcp_relay()
        assert "data" in result


class TestDnsResolverHostOverrideReadOnly:
    """Read-only tests for DNS resolver host override."""

    async def test_get_dns_resolver_host_overrides(self, api_client):
        result = await api_client.get_dns_resolver_host_overrides()
        assert "data" in result


class TestDnsResolverHostOverrideLifecycle:
    """CRUD lifecycle test for DNS resolver host override."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'host': 'mcptest', 'domain': 'test.local', 'ip': '192.168.1.250'}
        create_data["host"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_dns_resolver_host_override(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/services/dns_resolver/host_overrides", "host", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_dns_resolver_host_override(
                item_id, {'descr': 'Updated override'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/services/dns_resolver/host_overrides", "host", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_dns_resolver_host_override(obj["id"])
                except Exception:
                    pass


class TestDnsResolverHostOverrideAliasReadOnly:
    """Read-only tests for DNS resolver host override alias."""

    async def test_get_dns_resolver_host_override_aliass(self, api_client):
        result = await api_client.get_dns_resolver_host_override_aliass()
        assert "data" in result


class TestDnsResolverDomainOverrideReadOnly:
    """Read-only tests for DNS resolver domain override."""

    async def test_get_dns_resolver_domain_overrides(self, api_client):
        result = await api_client.get_dns_resolver_domain_overrides()
        assert "data" in result


class TestDnsResolverDomainOverrideLifecycle:
    """CRUD lifecycle test for DNS resolver domain override."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'domain': 'mcptest.local', 'ip': '10.0.0.53'}
        create_data["domain"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_dns_resolver_domain_override(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/services/dns_resolver/domain_overrides", "domain", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_dns_resolver_domain_override(
                item_id, {'descr': 'Updated domain override'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/services/dns_resolver/domain_overrides", "domain", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_dns_resolver_domain_override(obj["id"])
                except Exception:
                    pass


class TestDnsResolverAccessListReadOnly:
    """Read-only tests for DNS resolver access list."""

    async def test_get_dns_resolver_access_lists(self, api_client):
        result = await api_client.get_dns_resolver_access_lists()
        assert "data" in result


class TestDnsResolverAccessListLifecycle:
    """CRUD lifecycle test for DNS resolver access list."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'name': '', 'action': 'allow', 'networks': ['192.168.1.0/24']}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_dns_resolver_access_list(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/services/dns_resolver/access_lists", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_dns_resolver_access_list(
                item_id, {'description': 'Updated ACL'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/services/dns_resolver/access_lists", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_dns_resolver_access_list(obj["id"])
                except Exception:
                    pass


class TestDnsResolverAccessListNetworkReadOnly:
    """Read-only tests for DNS resolver access list network."""

    async def test_get_dns_resolver_access_list_networks(self, api_client):
        result = await api_client.get_dns_resolver_access_list_networks()
        assert "data" in result


class TestDnsResolverApplyReadOnly:
    """Read-only tests for DNS resolver apply."""

    async def test_get_dns_resolver_apply_status(self, api_client):
        result = await api_client.get_dns_resolver_apply_status()
        assert "data" in result


class TestDnsResolverSettingsReadOnly:
    """Read-only tests for DNS resolver settings."""

    async def test_get_dns_resolver_settings(self, api_client):
        result = await api_client.get_dns_resolver_settings()
        assert "data" in result


class TestDnsForwarderHostOverrideReadOnly:
    """Read-only tests for DNS forwarder host override."""

    async def test_get_dns_forwarder_host_overrides(self, api_client):
        result = await api_client.get_dns_forwarder_host_overrides()
        assert "data" in result


class TestDnsForwarderHostOverrideLifecycle:
    """CRUD lifecycle test for DNS forwarder host override."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'host': 'mcpfwdtest', 'domain': 'test.local', 'ip': '192.168.1.251'}
        create_data["host"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_dns_forwarder_host_override(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/services/dns_forwarder/host_overrides", "host", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_dns_forwarder_host_override(
                item_id, {'descr': 'Updated forwarder override'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/services/dns_forwarder/host_overrides", "host", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_dns_forwarder_host_override(obj["id"])
                except Exception:
                    pass


class TestDnsForwarderHostOverrideAliasReadOnly:
    """Read-only tests for DNS forwarder host override alias."""

    async def test_get_dns_forwarder_host_override_aliass(self, api_client):
        result = await api_client.get_dns_forwarder_host_override_aliass()
        assert "data" in result


class TestDnsForwarderApplyReadOnly:
    """Read-only tests for DNS forwarder apply."""

    async def test_get_dns_forwarder_apply_status(self, api_client):
        result = await api_client.get_dns_forwarder_apply_status()
        assert "data" in result


class TestCronJobReadOnly:
    """Read-only tests for cron job."""

    async def test_get_cron_jobs(self, api_client):
        result = await api_client.get_cron_jobs()
        assert "data" in result


class TestCronJobLifecycle:
    """CRUD lifecycle test for cron job."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'minute': '0', 'hour': '0', 'mday': '*', 'month': '*', 'wday': '*', 'who': 'root', 'command': '/usr/bin/true # MCP_INTTEST'}
        create_data["command"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_cron_job(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/services/cron/jobs", "command", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_cron_job(
                item_id, {'minute': '30'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/services/cron/jobs", "command", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_cron_job(obj["id"])
                except Exception:
                    pass


class TestNtpTimeServerReadOnly:
    """Read-only tests for NTP time server."""

    async def test_get_ntp_time_servers(self, api_client):
        result = await api_client.get_ntp_time_servers()
        assert "data" in result


class TestNtpTimeServerLifecycle:
    """CRUD lifecycle test for NTP time server."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'timeserver': 'time.mcptest.invalid', 'type': 'server'}
        create_data["timeserver"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_ntp_time_server(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/services/ntp/time_servers", "timeserver", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_ntp_time_server(
                item_id, {'prefer': True}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/services/ntp/time_servers", "timeserver", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_ntp_time_server(obj["id"])
                except Exception:
                    pass


class TestNtpSettingsReadOnly:
    """Read-only tests for NTP settings."""

    async def test_get_ntp_settings(self, api_client):
        result = await api_client.get_ntp_settings()
        assert "data" in result


class TestServiceWatchdogReadOnly:
    """Read-only tests for service watchdog."""

    async def test_get_service_watchdogs(self, api_client):
        result = await api_client.get_service_watchdogs()
        assert "data" in result


class TestServiceWatchdogLifecycle:
    """CRUD lifecycle test for service watchdog."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'name': 'sshd'}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_service_watchdog(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/services/service_watchdogs", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_service_watchdog(
                item_id, {'description': 'Updated watchdog'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/services/service_watchdogs", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_service_watchdog(obj["id"])
                except Exception:
                    pass


class TestSshSettingsReadOnly:
    """Read-only tests for SSH settings."""

    async def test_get_ssh_settings(self, api_client):
        result = await api_client.get_ssh_settings()
        assert "data" in result


class TestWakeOnLanReadOnly:
    """Read-only tests for Wake on LAN."""

    @pytest.mark.skip(reason="POST-only action endpoint — no safe read test")
    async def test_wake_on_lan_placeholder(self, api_client):
        pass


class TestSystemCertificateReadOnly:
    """Read-only tests for system certificate."""

    async def test_get_system_certificates(self, api_client):
        result = await api_client.get_system_certificates()
        assert "data" in result


class TestSystemCertificateLifecycle:
    """CRUD lifecycle test for system certificate."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'descr': '', 'crt': '', 'prv': ''}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_system_certificate(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/system/certificates", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_system_certificate(
                item_id, {'descr': 'Updated cert'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/system/certificates", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_system_certificate(obj["id"])
                except Exception:
                    pass


class TestSystemCaReadOnly:
    """Read-only tests for certificate authority."""

    async def test_get_system_cas(self, api_client):
        result = await api_client.get_system_cas()
        assert "data" in result


class TestSystemCaLifecycle:
    """CRUD lifecycle test for certificate authority."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'descr': '', 'crt': ''}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_system_ca(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/system/certificate_authorities", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_system_ca(
                item_id, {'descr': 'Updated CA'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/system/certificate_authorities", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_system_ca(obj["id"])
                except Exception:
                    pass


class TestSystemCrlReadOnly:
    """Read-only tests for certificate revocation list."""

    async def test_get_system_crls(self, api_client):
        result = await api_client.get_system_crls()
        assert "data" in result


class TestSystemCrlLifecycle:
    """CRUD lifecycle test for certificate revocation list."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'caref': '', 'descr': '', 'method': 'internal', 'text': ''}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_system_crl(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/system/crls", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_system_crl(
                item_id, {'descr': 'Updated CRL'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/system/crls", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_system_crl(obj["id"])
                except Exception:
                    pass


class TestSystemTunableReadOnly:
    """Read-only tests for system tunable."""

    async def test_get_system_tunables(self, api_client):
        result = await api_client.get_system_tunables()
        assert "data" in result


class TestSystemTunableLifecycle:
    """CRUD lifecycle test for system tunable."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'tunable': 'kern.ipc.maxsockbuf', 'value': '16777216'}
        create_data["tunable"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_system_tunable(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/system/tunables", "tunable", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_system_tunable(
                item_id, {'descr': 'Updated tunable'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/system/tunables", "tunable", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_system_tunable(obj["id"])
                except Exception:
                    pass


class TestRestapiAccessListEntryReadOnly:
    """Read-only tests for REST API access list entry."""

    async def test_get_restapi_access_list_entrys(self, api_client):
        result = await api_client.get_restapi_access_list_entrys()
        assert "data" in result


class TestRestapiAccessListEntryLifecycle:
    """CRUD lifecycle test for REST API access list entry."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'network': '10.0.0.0/8'}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_restapi_access_list_entry(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/system/restapi/access_list", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_restapi_access_list_entry(
                item_id, {'descr': 'Updated ACL entry'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/system/restapi/access_list", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_restapi_access_list_entry(obj["id"])
                except Exception:
                    pass


class TestSystemConsoleReadOnly:
    """Read-only tests for system console settings."""

    async def test_get_system_console(self, api_client):
        result = await api_client.get_system_console()
        assert "data" in result


class TestSystemDnsReadOnly:
    """Read-only tests for system DNS settings."""

    async def test_get_system_dns(self, api_client):
        result = await api_client.get_system_dns()
        assert "data" in result


class TestSystemHostnameReadOnly:
    """Read-only tests for system hostname."""

    async def test_get_system_hostname(self, api_client):
        result = await api_client.get_system_hostname()
        assert "data" in result


class TestSystemTimezoneReadOnly:
    """Read-only tests for system timezone."""

    async def test_get_system_timezone(self, api_client):
        result = await api_client.get_system_timezone()
        assert "data" in result


class TestSystemVersionReadOnly:
    """Read-only tests for system version."""

    async def test_get_system_version(self, api_client):
        result = await api_client.get_system_version()
        assert "data" in result


class TestWebguiSettingsReadOnly:
    """Read-only tests for WebGUI settings."""

    async def test_get_webgui_settings(self, api_client):
        result = await api_client.get_webgui_settings()
        assert "data" in result


class TestEmailNotificationSettingsReadOnly:
    """Read-only tests for email notification settings."""

    async def test_get_email_notification_settings(self, api_client):
        result = await api_client.get_email_notification_settings()
        assert "data" in result


class TestRestapiSettingsReadOnly:
    """Read-only tests for REST API settings."""

    async def test_get_restapi_settings(self, api_client):
        result = await api_client.get_restapi_settings()
        assert "data" in result


class TestRestapiVersionReadOnly:
    """Read-only tests for REST API version."""

    async def test_get_restapi_version(self, api_client):
        result = await api_client.get_restapi_version()
        assert "data" in result


class TestSystemPackageReadOnly:
    """Read-only tests for system package."""

    async def test_get_system_packages(self, api_client):
        result = await api_client.get_system_packages()
        assert "data" in result


class TestSystemPackageLifecycle:
    """CRUD lifecycle test for system package."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'name': ''}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_system_package(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/system/packages", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_system_package(
                item_id, {}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/system/packages", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_system_package(obj["id"])
                except Exception:
                    pass


class TestUserReadOnly:
    """Read-only tests for user."""

    async def test_get_users(self, api_client):
        result = await api_client.get_users()
        assert "data" in result


class TestUserLifecycle:
    """CRUD lifecycle test for user."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'name': '', 'password': 'McpT3st!Pass#9876'}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_user(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/users", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_user(
                item_id, {'descr': 'Updated user'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/users", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_user(obj["id"])
                except Exception:
                    pass


class TestUserGroupReadOnly:
    """Read-only tests for user group."""

    async def test_get_user_groups(self, api_client):
        result = await api_client.get_user_groups()
        assert "data" in result


class TestUserGroupLifecycle:
    """CRUD lifecycle test for user group."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'name': ''}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_user_group(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/user/groups", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_user_group(
                item_id, {'description': 'Updated group'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/user/groups", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_user_group(obj["id"])
                except Exception:
                    pass


class TestUserAuthServerReadOnly:
    """Read-only tests for authentication server."""

    async def test_get_user_auth_servers(self, api_client):
        result = await api_client.get_user_auth_servers()
        assert "data" in result


class TestUserAuthServerLifecycle:
    """CRUD lifecycle test for authentication server."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'type': 'ldap', 'name': '', 'host': 'ldap.mcptest.invalid', 'ldap_port': 389, 'ldap_urltype': 'TCP - Standard', 'ldap_scope': 'one', 'ldap_bindpw': 'pass', 'radius_secret': '', 'radius_nasip_attribute': 'wan'}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_user_auth_server(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/user/auth_servers", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_user_auth_server(
                item_id, {'host': 'ldap2.mcptest.invalid'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/user/auth_servers", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_user_auth_server(obj["id"])
                except Exception:
                    pass


class TestIpsecApplyReadOnly:
    """Read-only tests for IPsec apply."""

    async def test_get_ipsec_apply_status(self, api_client):
        result = await api_client.get_ipsec_apply_status()
        assert "data" in result


class TestIpsecPhase1ReadOnly:
    """Read-only tests for IPsec Phase 1."""

    async def test_get_ipsec_phase1s(self, api_client):
        result = await api_client.get_ipsec_phase1s()
        assert "data" in result


class TestIpsecPhase1Lifecycle:
    """CRUD lifecycle test for IPsec Phase 1."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'iketype': 'ikev2', 'mode': 'tunnel', 'protocol': 'inet', 'interface': 'wan', 'remote_gateway': '198.51.100.99', 'authentication_method': 'pre_shared_key', 'myid_type': 'myaddress', 'myid_data': '', 'peerid_type': 'peeraddress', 'peerid_data': '', 'pre_shared_key': 'McpTestKey123!', 'certref': '', 'caref': '', 'encryption': []}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_ipsec_phase1(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/vpn/ipsec/phase1s", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_ipsec_phase1(
                item_id, {'descr': 'Updated phase1'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/vpn/ipsec/phase1s", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_ipsec_phase1(obj["id"])
                except Exception:
                    pass


class TestIpsecPhase1EncryptionReadOnly:
    """Read-only tests for IPsec Phase 1 encryption."""

    async def test_get_ipsec_phase1_encryptions(self, api_client):
        result = await api_client.get_ipsec_phase1_encryptions()
        assert "data" in result


class TestIpsecPhase2ReadOnly:
    """Read-only tests for IPsec Phase 2."""

    async def test_get_ipsec_phase2s(self, api_client):
        result = await api_client.get_ipsec_phase2s()
        assert "data" in result


class TestIpsecPhase2Lifecycle:
    """CRUD lifecycle test for IPsec Phase 2."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'ikeid': 0, 'mode': 'tunnel', 'localid_type': 'lan', 'localid_address': '', 'localid_netbits': 24, 'natlocalid_address': '', 'natlocalid_netbits': 0, 'remoteid_type': 'network', 'remoteid_address': '10.0.0.0', 'remoteid_netbits': 24, 'encryption_algorithm_option': [{'name': 'aes', 'keylen': 256}], 'hash_algorithm_option': ['hmac_sha256']}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_ipsec_phase2(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/vpn/ipsec/phase2s", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_ipsec_phase2(
                item_id, {'descr': 'Updated phase2'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/vpn/ipsec/phase2s", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_ipsec_phase2(obj["id"])
                except Exception:
                    pass


class TestIpsecPhase2EncryptionReadOnly:
    """Read-only tests for IPsec Phase 2 encryption."""

    async def test_get_ipsec_phase2_encryptions(self, api_client):
        result = await api_client.get_ipsec_phase2_encryptions()
        assert "data" in result


class TestOpenvpnServerReadOnly:
    """Read-only tests for OpenVPN server."""

    async def test_get_openvpn_servers(self, api_client):
        result = await api_client.get_openvpn_servers()
        assert "data" in result


class TestOpenvpnServerLifecycle:
    """CRUD lifecycle test for OpenVPN server."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'mode': 'server_tls', 'dev_mode': 'tun', 'protocol': 'UDP4', 'interface': 'wan', 'tls_type': 'auth', 'caref': '', 'certref': '', 'dh_length': 2048, 'ecdh_curve': 'none', 'data_ciphers': ['AES-256-GCM'], 'data_ciphers_fallback': 'AES-256-CBC', 'digest': 'SHA256', 'serverbridge_interface': '', 'serverbridge_dhcp_start': '', 'serverbridge_dhcp_end': ''}
        create_data["description"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_openvpn_server(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/vpn/openvpn/servers", "description", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_openvpn_server(
                item_id, {'description': 'Updated OVPN server'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/vpn/openvpn/servers", "description", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_openvpn_server(obj["id"])
                except Exception:
                    pass


class TestOpenvpnClientReadOnly:
    """Read-only tests for OpenVPN client."""

    async def test_get_openvpn_clients(self, api_client):
        result = await api_client.get_openvpn_clients()
        assert "data" in result


class TestOpenvpnClientLifecycle:
    """CRUD lifecycle test for OpenVPN client."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'mode': 'p2p_shared_key', 'dev_mode': 'tun', 'protocol': 'UDP4', 'interface': 'wan', 'server_addr': '198.51.100.99', 'server_port': 1194, 'proxy_user': '', 'proxy_passwd': '', 'tls_type': 'auth', 'caref': '', 'data_ciphers': ['AES-256-GCM'], 'data_ciphers_fallback': 'AES-256-CBC', 'digest': 'SHA256'}
        create_data["description"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_openvpn_client(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/vpn/openvpn/clients", "description", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_openvpn_client(
                item_id, {'description': 'Updated OVPN client'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/vpn/openvpn/clients", "description", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_openvpn_client(obj["id"])
                except Exception:
                    pass


class TestOpenvpnCsoReadOnly:
    """Read-only tests for OpenVPN client-specific override."""

    async def test_get_openvpn_csos(self, api_client):
        result = await api_client.get_openvpn_csos()
        assert "data" in result


class TestOpenvpnCsoLifecycle:
    """CRUD lifecycle test for OpenVPN client-specific override."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'common_name': 'mcptest_cso'}
        create_data["common_name"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_openvpn_cso(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/vpn/openvpn/csos", "common_name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_openvpn_cso(
                item_id, {'description': 'Updated CSO'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/vpn/openvpn/csos", "common_name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_openvpn_cso(obj["id"])
                except Exception:
                    pass


class TestWireguardTunnelReadOnly:
    """Read-only tests for WireGuard tunnel."""

    async def test_get_wireguard_tunnels(self, api_client):
        result = await api_client.get_wireguard_tunnels()
        assert "data" in result


class TestWireguardTunnelLifecycle:
    """CRUD lifecycle test for WireGuard tunnel."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'privatekey': ''}
        hex8 = uuid.uuid4().hex[:8]
        create_data["name"] = f"mcpt_{hex8}"
        lookup_val = create_data["name"]
        item_id = None
        try:
            result = await api_client.create_wireguard_tunnel(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/vpn/wireguard/tunnels", "name", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_wireguard_tunnel(
                item_id, {'descr': 'Updated tunnel'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/vpn/wireguard/tunnels", "name", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_wireguard_tunnel(obj["id"])
                except Exception:
                    pass


class TestWireguardTunnelAddressReadOnly:
    """Read-only tests for WireGuard tunnel address."""

    async def test_get_wireguard_tunnel_addresss(self, api_client):
        result = await api_client.get_wireguard_tunnel_addresss()
        assert "data" in result


class TestWireguardPeerReadOnly:
    """Read-only tests for WireGuard peer."""

    async def test_get_wireguard_peers(self, api_client):
        result = await api_client.get_wireguard_peers()
        assert "data" in result


class TestWireguardPeerLifecycle:
    """CRUD lifecycle test for WireGuard peer."""

    async def test_crud_lifecycle(self, api_client, unique_id):
        descr = f"MCP_INTTEST_{unique_id}"
        create_data = {'publickey': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='}
        create_data["descr"] = descr
        lookup_val = descr
        item_id = None
        try:
            result = await api_client.create_wireguard_peer(
                create_data, ControlParameters(apply=True),
            )
            item_id = result["data"]["id"]
            assert item_id is not None

            # Re-lookup (IDs may shift after apply)
            obj = await _find_by_field(
                api_client, "/vpn/wireguard/peers", "descr", lookup_val,
            )
            assert obj is not None
            item_id = obj["id"]

            # Update
            await api_client.update_wireguard_peer(
                item_id, {'descr': 'Updated peer'}, ControlParameters(apply=True),
            )

        finally:
            # Cleanup — re-lookup since IDs shift
            obj = await _find_by_field(
                api_client, "/vpn/wireguard/peers", "descr", lookup_val,
            )
            if obj is not None:
                try:
                    await api_client.delete_wireguard_peer(obj["id"])
                except Exception:
                    pass


class TestWireguardPeerAllowedIpReadOnly:
    """Read-only tests for WireGuard peer allowed IP."""

    async def test_get_wireguard_peer_allowed_ips(self, api_client):
        result = await api_client.get_wireguard_peer_allowed_ips()
        assert "data" in result


class TestWireguardApplyReadOnly:
    """Read-only tests for WireGuard apply."""

    async def test_get_wireguard_apply_status(self, api_client):
        result = await api_client.get_wireguard_apply_status()
        assert "data" in result


class TestWireguardSettingsReadOnly:
    """Read-only tests for WireGuard settings."""

    async def test_get_wireguard_settings(self, api_client):
        result = await api_client.get_wireguard_settings()
        assert "data" in result


class TestArpTableEntryReadOnly:
    """Read-only tests for ARP table entry."""

    async def test_get_arp_table_entrys(self, api_client):
        result = await api_client.get_arp_table_entrys()
        assert "data" in result


class TestConfigHistoryRevisionReadOnly:
    """Read-only tests for config history revision."""

    async def test_get_config_history_revisions(self, api_client):
        result = await api_client.get_config_history_revisions()
        assert "data" in result


class TestPfTableReadOnly:
    """Read-only tests for pf table."""

    async def test_get_pf_tables(self, api_client):
        result = await api_client.get_pf_tables()
        assert "data" in result


class TestCarpStatusReadOnly:
    """Read-only tests for CARP status."""

    async def test_get_carp_status(self, api_client):
        result = await api_client.get_carp_status()
        assert "data" in result


class TestGatewayStatusReadOnly:
    """Read-only tests for gateway status."""

    async def test_get_gateway_status(self, api_client):
        result = await api_client.get_gateway_status()
        assert "data" in result


class TestLogSettingsReadOnly:
    """Read-only tests for log settings."""

    async def test_get_log_settings(self, api_client):
        result = await api_client.get_log_settings()
        assert "data" in result


class TestOpenvpnServerStatusReadOnly:
    """Read-only tests for OpenVPN server status."""

    async def test_get_openvpn_server_status(self, api_client):
        result = await api_client.get_openvpn_server_status()
        assert "data" in result


class TestIpsecSaStatusReadOnly:
    """Read-only tests for IPsec SA status."""

    async def test_get_ipsec_sa_status(self, api_client):
        result = await api_client.get_ipsec_sa_status()
        assert "data" in result
