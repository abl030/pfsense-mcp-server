"""Auto-generated firewall client methods. DO NOT EDIT.
Regenerate: python scripts/generate_from_spec.py
"""

from typing import Dict, List, Optional


class GeneratedFirewallMixin:
    """Mixin providing generated client methods for firewall endpoints."""

    async def get_nat_one_to_one_mappings(self, filters=None, sort=None, pagination=None):
        """List NAT one-to-one mappings."""
        return await self._make_request(
            "GET", "/firewall/nat/one_to_one/mappings",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_nat_one_to_one_mapping(self, data, control=None):
        """Create a NAT one-to-one mapping."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/nat/one_to_one/mapping",
            data=data, control=control,
        )

    async def update_nat_one_to_one_mapping(self, item_id, updates, control=None):
        """Update a NAT one-to-one mapping."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/nat/one_to_one/mapping",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_nat_one_to_one_mapping(self, item_id, apply_immediately=True):
        """Delete a NAT one-to-one mapping."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/nat/one_to_one/mapping",
            data={"id": item_id}, control=control,
        )
    async def get_nat_outbound_mappings(self, filters=None, sort=None, pagination=None):
        """List NAT outbound mappings."""
        return await self._make_request(
            "GET", "/firewall/nat/outbound/mappings",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_nat_outbound_mapping(self, data, control=None):
        """Create a NAT outbound mapping."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/nat/outbound/mapping",
            data=data, control=control,
        )

    async def update_nat_outbound_mapping(self, item_id, updates, control=None):
        """Update a NAT outbound mapping."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/nat/outbound/mapping",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_nat_outbound_mapping(self, item_id, apply_immediately=True):
        """Delete a NAT outbound mapping."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/nat/outbound/mapping",
            data={"id": item_id}, control=control,
        )
    async def get_nat_outbound_mode(self):
        """Get NAT outbound mode."""
        return await self._make_request("GET", "/firewall/nat/outbound/mode")

    async def update_nat_outbound_mode(self, updates):
        """Update NAT outbound mode."""
        return await self._make_request(
            "PATCH", "/firewall/nat/outbound/mode",
            data=updates,
        )
    async def get_firewall_schedules(self, filters=None, sort=None, pagination=None):
        """List firewall schedules."""
        return await self._make_request(
            "GET", "/firewall/schedules",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_firewall_schedule(self, data, control=None):
        """Create a firewall schedule."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/schedule",
            data=data, control=control,
        )

    async def update_firewall_schedule(self, item_id, updates, control=None):
        """Update a firewall schedule."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/schedule",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_firewall_schedule(self, item_id, apply_immediately=True):
        """Delete a firewall schedule."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/schedule",
            data={"id": item_id}, control=control,
        )
    async def get_firewall_schedule_time_ranges(self, filters=None, sort=None, pagination=None):
        """List firewall schedule time ranges."""
        return await self._make_request(
            "GET", "/firewall/schedule/time_ranges",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_firewall_schedule_time_range(self, data, control=None):
        """Create a firewall schedule time range. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/schedule/time_range",
            data=data, control=control,
        )

    async def update_firewall_schedule_time_range(self, item_id, updates, control=None):
        """Update a firewall schedule time range."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/schedule/time_range",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_firewall_schedule_time_range(self, item_id, apply_immediately=True):
        """Delete a firewall schedule time range."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/schedule/time_range",
            data={"id": item_id}, control=control,
        )
    async def get_traffic_shapers(self, filters=None, sort=None, pagination=None):
        """List traffic shapers."""
        return await self._make_request(
            "GET", "/firewall/traffic_shapers",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_traffic_shaper(self, data, control=None):
        """Create a traffic shaper."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/traffic_shaper",
            data=data, control=control,
        )

    async def update_traffic_shaper(self, item_id, updates, control=None):
        """Update a traffic shaper."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/traffic_shaper",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_traffic_shaper(self, item_id, apply_immediately=True):
        """Delete a traffic shaper."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/traffic_shaper",
            data={"id": item_id}, control=control,
        )
    async def get_traffic_shaper_queues(self, filters=None, sort=None, pagination=None):
        """List traffic shaper queues."""
        return await self._make_request(
            "GET", "/firewall/traffic_shaper/queues",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_traffic_shaper_queue(self, data, control=None):
        """Create a traffic shaper queue. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/traffic_shaper/queue",
            data=data, control=control,
        )

    async def update_traffic_shaper_queue(self, item_id, updates, control=None):
        """Update a traffic shaper queue."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/traffic_shaper/queue",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_traffic_shaper_queue(self, item_id, apply_immediately=True):
        """Delete a traffic shaper queue."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/traffic_shaper/queue",
            data={"id": item_id}, control=control,
        )
    async def get_traffic_shaper_limiters(self, filters=None, sort=None, pagination=None):
        """List traffic shaper limiters."""
        return await self._make_request(
            "GET", "/firewall/traffic_shaper/limiters",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_traffic_shaper_limiter(self, data, control=None):
        """Create a traffic shaper limiter."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/traffic_shaper/limiter",
            data=data, control=control,
        )

    async def update_traffic_shaper_limiter(self, item_id, updates, control=None):
        """Update a traffic shaper limiter."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/traffic_shaper/limiter",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_traffic_shaper_limiter(self, item_id, apply_immediately=True):
        """Delete a traffic shaper limiter."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/traffic_shaper/limiter",
            data={"id": item_id}, control=control,
        )
    async def get_traffic_shaper_limiter_queues(self, filters=None, sort=None, pagination=None):
        """List traffic shaper limiter queues."""
        return await self._make_request(
            "GET", "/firewall/traffic_shaper/limiter/queues",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_traffic_shaper_limiter_queue(self, data, control=None):
        """Create a traffic shaper limiter queue. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/traffic_shaper/limiter/queue",
            data=data, control=control,
        )

    async def update_traffic_shaper_limiter_queue(self, item_id, updates, control=None):
        """Update a traffic shaper limiter queue."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/traffic_shaper/limiter/queue",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_traffic_shaper_limiter_queue(self, item_id, apply_immediately=True):
        """Delete a traffic shaper limiter queue."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/traffic_shaper/limiter/queue",
            data={"id": item_id}, control=control,
        )
    async def get_traffic_shaper_limiter_bandwidths(self, filters=None, sort=None, pagination=None):
        """List traffic shaper limiter bandwidths."""
        return await self._make_request(
            "GET", "/firewall/traffic_shaper/limiter/bandwidths",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_traffic_shaper_limiter_bandwidth(self, data, control=None):
        """Create a traffic shaper limiter bandwidth. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/traffic_shaper/limiter/bandwidth",
            data=data, control=control,
        )

    async def update_traffic_shaper_limiter_bandwidth(self, item_id, updates, control=None):
        """Update a traffic shaper limiter bandwidth."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/traffic_shaper/limiter/bandwidth",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_traffic_shaper_limiter_bandwidth(self, item_id, apply_immediately=True):
        """Delete a traffic shaper limiter bandwidth."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/traffic_shaper/limiter/bandwidth",
            data={"id": item_id}, control=control,
        )
    async def get_virtual_ips(self, filters=None, sort=None, pagination=None):
        """List virtual IPs."""
        return await self._make_request(
            "GET", "/firewall/virtual_ips",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_virtual_ip(self, data, control=None):
        """Create a virtual IP."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/firewall/virtual_ip",
            data=data, control=control,
        )

    async def update_virtual_ip(self, item_id, updates, control=None):
        """Update a virtual IP."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/firewall/virtual_ip",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_virtual_ip(self, item_id, apply_immediately=True):
        """Delete a virtual IP."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/firewall/virtual_ip",
            data={"id": item_id}, control=control,
        )
    async def get_virtual_ip_apply_status(self):
        """Get virtual IP apply status."""
        return await self._make_request("GET", "/firewall/virtual_ip/apply")

    async def apply_virtual_ip_apply(self):
        """Trigger virtual IP apply."""
        return await self._make_request("POST", "/firewall/virtual_ip/apply")
    async def get_firewall_states(self, filters=None, sort=None, pagination=None):
        """List firewall states."""
        return await self._make_request(
            "GET", "/firewall/states",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def delete_firewall_states(self):
        """Delete all firewall states."""
        return await self._make_request("DELETE", "/firewall/states")
    async def get_firewall_states_size(self):
        """Get firewall states size."""
        return await self._make_request("GET", "/firewall/states/size")

    async def update_firewall_states_size(self, updates):
        """Update firewall states size."""
        return await self._make_request(
            "PATCH", "/firewall/states/size",
            data=updates,
        )
    async def get_firewall_advanced_settings(self):
        """Get firewall advanced settings."""
        return await self._make_request("GET", "/firewall/advanced_settings")

    async def update_firewall_advanced_settings(self, updates):
        """Update firewall advanced settings."""
        return await self._make_request(
            "PATCH", "/firewall/advanced_settings",
            data=updates,
        )
    async def get_firewall_apply_status(self):
        """Get firewall apply status."""
        return await self._make_request("GET", "/firewall/apply")

    async def apply_firewall_apply(self):
        """Trigger firewall apply."""
        return await self._make_request("POST", "/firewall/apply")
    async def get_routing_gateways(self, filters=None, sort=None, pagination=None):
        """List routing gateways."""
        return await self._make_request(
            "GET", "/routing/gateways",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_routing_gateway(self, data, control=None):
        """Create a routing gateway."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/routing/gateway",
            data=data, control=control,
        )

    async def update_routing_gateway(self, item_id, updates, control=None):
        """Update a routing gateway."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/routing/gateway",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_routing_gateway(self, item_id, apply_immediately=True):
        """Delete a routing gateway."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/routing/gateway",
            data={"id": item_id}, control=control,
        )
    async def get_routing_gateway_default(self):
        """Get default routing gateway."""
        return await self._make_request("GET", "/routing/gateway/default")

    async def update_routing_gateway_default(self, updates):
        """Update default routing gateway."""
        return await self._make_request(
            "PATCH", "/routing/gateway/default",
            data=updates,
        )
    async def get_routing_gateway_groups(self, filters=None, sort=None, pagination=None):
        """List routing gateway groups."""
        return await self._make_request(
            "GET", "/routing/gateway/groups",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_routing_gateway_group(self, data, control=None):
        """Create a routing gateway group."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/routing/gateway/group",
            data=data, control=control,
        )

    async def update_routing_gateway_group(self, item_id, updates, control=None):
        """Update a routing gateway group."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/routing/gateway/group",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_routing_gateway_group(self, item_id, apply_immediately=True):
        """Delete a routing gateway group."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/routing/gateway/group",
            data={"id": item_id}, control=control,
        )
    async def get_routing_gateway_group_prioritys(self, filters=None, sort=None, pagination=None):
        """List routing gateway group prioritys."""
        return await self._make_request(
            "GET", "/routing/gateway/group/priorities",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_routing_gateway_group_priority(self, data, control=None):
        """Create a routing gateway group priority. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/routing/gateway/group/priority",
            data=data, control=control,
        )

    async def update_routing_gateway_group_priority(self, item_id, updates, control=None):
        """Update a routing gateway group priority."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/routing/gateway/group/priority",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_routing_gateway_group_priority(self, item_id, apply_immediately=True):
        """Delete a routing gateway group priority."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/routing/gateway/group/priority",
            data={"id": item_id}, control=control,
        )
    async def get_routing_static_routes(self, filters=None, sort=None, pagination=None):
        """List static routes."""
        return await self._make_request(
            "GET", "/routing/static_routes",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_routing_static_route(self, data, control=None):
        """Create a static route."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/routing/static_route",
            data=data, control=control,
        )

    async def update_routing_static_route(self, item_id, updates, control=None):
        """Update a static route."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/routing/static_route",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_routing_static_route(self, item_id, apply_immediately=True):
        """Delete a static route."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/routing/static_route",
            data={"id": item_id}, control=control,
        )
    async def get_routing_apply_status(self):
        """Get routing apply status."""
        return await self._make_request("GET", "/routing/apply")

    async def apply_routing_apply(self):
        """Trigger routing apply."""
        return await self._make_request("POST", "/routing/apply")
    async def get_interfaces(self, filters=None, sort=None, pagination=None):
        """List network interfaces."""
        return await self._make_request(
            "GET", "/interfaces",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_interface(self, data, control=None):
        """Create a network interface."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/interface",
            data=data, control=control,
        )

    async def update_interface(self, item_id, updates, control=None):
        """Update a network interface."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/interface",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_interface(self, item_id, apply_immediately=True):
        """Delete a network interface."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/interface",
            data={"id": item_id}, control=control,
        )
    async def get_interface_apply_status(self):
        """Get interface apply status."""
        return await self._make_request("GET", "/interface/apply")

    async def apply_interface_apply(self):
        """Trigger interface apply."""
        return await self._make_request("POST", "/interface/apply")
    async def get_available_interfaces(self):
        """Get available interfaces."""
        return await self._make_request("GET", "/interface/available_interfaces")
    async def get_interface_bridges(self, filters=None, sort=None, pagination=None):
        """List interface bridges."""
        return await self._make_request(
            "GET", "/interface/bridges",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_interface_bridge(self, data, control=None):
        """Create a interface bridge."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/interface/bridge",
            data=data, control=control,
        )

    async def update_interface_bridge(self, item_id, updates, control=None):
        """Update a interface bridge."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/interface/bridge",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_interface_bridge(self, item_id, apply_immediately=True):
        """Delete a interface bridge."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/interface/bridge",
            data={"id": item_id}, control=control,
        )
    async def get_interface_groups(self, filters=None, sort=None, pagination=None):
        """List interface groups."""
        return await self._make_request(
            "GET", "/interface/groups",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_interface_group(self, data, control=None):
        """Create a interface group."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/interface/group",
            data=data, control=control,
        )

    async def update_interface_group(self, item_id, updates, control=None):
        """Update a interface group."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/interface/group",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_interface_group(self, item_id, apply_immediately=True):
        """Delete a interface group."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/interface/group",
            data={"id": item_id}, control=control,
        )
    async def get_interface_vlans(self, filters=None, sort=None, pagination=None):
        """List interface VLANs."""
        return await self._make_request(
            "GET", "/interface/vlans",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_interface_vlan(self, data, control=None):
        """Create a interface VLAN."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/interface/vlan",
            data=data, control=control,
        )

    async def update_interface_vlan(self, item_id, updates, control=None):
        """Update a interface VLAN."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/interface/vlan",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_interface_vlan(self, item_id, apply_immediately=True):
        """Delete a interface VLAN."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/interface/vlan",
            data={"id": item_id}, control=control,
        )
    async def get_interface_gres(self, filters=None, sort=None, pagination=None):
        """List interface GRE tunnels."""
        return await self._make_request(
            "GET", "/interface/gres",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_interface_gre(self, data, control=None):
        """Create a interface GRE tunnel."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/interface/gre",
            data=data, control=control,
        )

    async def update_interface_gre(self, item_id, updates, control=None):
        """Update a interface GRE tunnel."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/interface/gre",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_interface_gre(self, item_id, apply_immediately=True):
        """Delete a interface GRE tunnel."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/interface/gre",
            data={"id": item_id}, control=control,
        )
    async def get_interface_laggs(self, filters=None, sort=None, pagination=None):
        """List interface LAGGs."""
        return await self._make_request(
            "GET", "/interface/laggs",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_interface_lagg(self, data, control=None):
        """Create a interface LAGG."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/interface/lagg",
            data=data, control=control,
        )

    async def update_interface_lagg(self, item_id, updates, control=None):
        """Update a interface LAGG."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/interface/lagg",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_interface_lagg(self, item_id, apply_immediately=True):
        """Delete a interface LAGG."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/interface/lagg",
            data={"id": item_id}, control=control,
        )
    async def get_dhcp_servers(self, filters=None, sort=None, pagination=None):
        """List DHCP servers."""
        return await self._make_request(
            "GET", "/services/dhcp_servers",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dhcp_server(self, data, control=None):
        """Create a DHCP server."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dhcp_server",
            data=data, control=control,
        )

    async def update_dhcp_server(self, item_id, updates, control=None):
        """Update a DHCP server."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dhcp_server",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dhcp_server(self, item_id, apply_immediately=True):
        """Delete a DHCP server."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dhcp_server",
            data={"id": item_id}, control=control,
        )
    async def get_dhcp_server_static_mappings(self, filters=None, sort=None, pagination=None):
        """List DHCP static mappings."""
        return await self._make_request(
            "GET", "/services/dhcp_server/static_mappings",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dhcp_server_static_mapping(self, data, control=None):
        """Create a DHCP static mapping. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dhcp_server/static_mapping",
            data=data, control=control,
        )

    async def update_dhcp_server_static_mapping(self, item_id, updates, control=None):
        """Update a DHCP static mapping."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dhcp_server/static_mapping",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dhcp_server_static_mapping(self, item_id, apply_immediately=True):
        """Delete a DHCP static mapping."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dhcp_server/static_mapping",
            data={"id": item_id}, control=control,
        )
    async def get_dhcp_server_address_pools(self, filters=None, sort=None, pagination=None):
        """List DHCP address pools."""
        return await self._make_request(
            "GET", "/services/dhcp_server/address_pools",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dhcp_server_address_pool(self, data, control=None):
        """Create a DHCP address pool. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dhcp_server/address_pool",
            data=data, control=control,
        )

    async def update_dhcp_server_address_pool(self, item_id, updates, control=None):
        """Update a DHCP address pool."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dhcp_server/address_pool",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dhcp_server_address_pool(self, item_id, apply_immediately=True):
        """Delete a DHCP address pool."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dhcp_server/address_pool",
            data={"id": item_id}, control=control,
        )
    async def get_dhcp_server_custom_options(self, filters=None, sort=None, pagination=None):
        """List DHCP custom options."""
        return await self._make_request(
            "GET", "/services/dhcp_server/custom_options",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dhcp_server_custom_option(self, data, control=None):
        """Create a DHCP custom option. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dhcp_server/custom_option",
            data=data, control=control,
        )

    async def update_dhcp_server_custom_option(self, item_id, updates, control=None):
        """Update a DHCP custom option."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dhcp_server/custom_option",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dhcp_server_custom_option(self, item_id, apply_immediately=True):
        """Delete a DHCP custom option."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dhcp_server/custom_option",
            data={"id": item_id}, control=control,
        )
    async def get_dhcp_server_apply_status(self):
        """Get DHCP server apply status."""
        return await self._make_request("GET", "/services/dhcp_server/apply")

    async def apply_dhcp_server_apply(self):
        """Trigger DHCP server apply."""
        return await self._make_request("POST", "/services/dhcp_server/apply")
    async def get_dhcp_relay(self):
        """Get DHCP relay."""
        return await self._make_request("GET", "/services/dhcp_relay")

    async def update_dhcp_relay(self, updates):
        """Update DHCP relay."""
        return await self._make_request(
            "PATCH", "/services/dhcp_relay",
            data=updates,
        )
    async def get_dns_resolver_host_overrides(self, filters=None, sort=None, pagination=None):
        """List DNS resolver host overrides."""
        return await self._make_request(
            "GET", "/services/dns_resolver/host_overrides",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dns_resolver_host_override(self, data, control=None):
        """Create a DNS resolver host override."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dns_resolver/host_override",
            data=data, control=control,
        )

    async def update_dns_resolver_host_override(self, item_id, updates, control=None):
        """Update a DNS resolver host override."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dns_resolver/host_override",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dns_resolver_host_override(self, item_id, apply_immediately=True):
        """Delete a DNS resolver host override."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dns_resolver/host_override",
            data={"id": item_id}, control=control,
        )
    async def get_dns_resolver_host_override_aliass(self, filters=None, sort=None, pagination=None):
        """List DNS resolver host override aliass."""
        return await self._make_request(
            "GET", "/services/dns_resolver/host_override/aliases",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dns_resolver_host_override_alias(self, data, control=None):
        """Create a DNS resolver host override alias. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dns_resolver/host_override/alias",
            data=data, control=control,
        )

    async def update_dns_resolver_host_override_alias(self, item_id, updates, control=None):
        """Update a DNS resolver host override alias."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dns_resolver/host_override/alias",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dns_resolver_host_override_alias(self, item_id, apply_immediately=True):
        """Delete a DNS resolver host override alias."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dns_resolver/host_override/alias",
            data={"id": item_id}, control=control,
        )
    async def get_dns_resolver_domain_overrides(self, filters=None, sort=None, pagination=None):
        """List DNS resolver domain overrides."""
        return await self._make_request(
            "GET", "/services/dns_resolver/domain_overrides",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dns_resolver_domain_override(self, data, control=None):
        """Create a DNS resolver domain override."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dns_resolver/domain_override",
            data=data, control=control,
        )

    async def update_dns_resolver_domain_override(self, item_id, updates, control=None):
        """Update a DNS resolver domain override."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dns_resolver/domain_override",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dns_resolver_domain_override(self, item_id, apply_immediately=True):
        """Delete a DNS resolver domain override."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dns_resolver/domain_override",
            data={"id": item_id}, control=control,
        )
    async def get_dns_resolver_access_lists(self, filters=None, sort=None, pagination=None):
        """List DNS resolver access lists."""
        return await self._make_request(
            "GET", "/services/dns_resolver/access_lists",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dns_resolver_access_list(self, data, control=None):
        """Create a DNS resolver access list."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dns_resolver/access_list",
            data=data, control=control,
        )

    async def update_dns_resolver_access_list(self, item_id, updates, control=None):
        """Update a DNS resolver access list."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dns_resolver/access_list",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dns_resolver_access_list(self, item_id, apply_immediately=True):
        """Delete a DNS resolver access list."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dns_resolver/access_list",
            data={"id": item_id}, control=control,
        )
    async def get_dns_resolver_access_list_networks(self, filters=None, sort=None, pagination=None):
        """List DNS resolver access list networks."""
        return await self._make_request(
            "GET", "/services/dns_resolver/access_list/networks",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dns_resolver_access_list_network(self, data, control=None):
        """Create a DNS resolver access list network. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dns_resolver/access_list/network",
            data=data, control=control,
        )

    async def update_dns_resolver_access_list_network(self, item_id, updates, control=None):
        """Update a DNS resolver access list network."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dns_resolver/access_list/network",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dns_resolver_access_list_network(self, item_id, apply_immediately=True):
        """Delete a DNS resolver access list network."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dns_resolver/access_list/network",
            data={"id": item_id}, control=control,
        )
    async def get_dns_resolver_apply_status(self):
        """Get DNS resolver apply status."""
        return await self._make_request("GET", "/services/dns_resolver/apply")

    async def apply_dns_resolver_apply(self):
        """Trigger DNS resolver apply."""
        return await self._make_request("POST", "/services/dns_resolver/apply")
    async def get_dns_resolver_settings(self):
        """Get DNS resolver settings."""
        return await self._make_request("GET", "/services/dns_resolver/settings")

    async def update_dns_resolver_settings(self, updates):
        """Update DNS resolver settings."""
        return await self._make_request(
            "PATCH", "/services/dns_resolver/settings",
            data=updates,
        )
    async def get_dns_forwarder_host_overrides(self, filters=None, sort=None, pagination=None):
        """List DNS forwarder host overrides."""
        return await self._make_request(
            "GET", "/services/dns_forwarder/host_overrides",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dns_forwarder_host_override(self, data, control=None):
        """Create a DNS forwarder host override."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dns_forwarder/host_override",
            data=data, control=control,
        )

    async def update_dns_forwarder_host_override(self, item_id, updates, control=None):
        """Update a DNS forwarder host override."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dns_forwarder/host_override",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dns_forwarder_host_override(self, item_id, apply_immediately=True):
        """Delete a DNS forwarder host override."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dns_forwarder/host_override",
            data={"id": item_id}, control=control,
        )
    async def get_dns_forwarder_host_override_aliass(self, filters=None, sort=None, pagination=None):
        """List DNS forwarder host override aliass."""
        return await self._make_request(
            "GET", "/services/dns_forwarder/host_override/aliases",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_dns_forwarder_host_override_alias(self, data, control=None):
        """Create a DNS forwarder host override alias. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/dns_forwarder/host_override/alias",
            data=data, control=control,
        )

    async def update_dns_forwarder_host_override_alias(self, item_id, updates, control=None):
        """Update a DNS forwarder host override alias."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/dns_forwarder/host_override/alias",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_dns_forwarder_host_override_alias(self, item_id, apply_immediately=True):
        """Delete a DNS forwarder host override alias."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/dns_forwarder/host_override/alias",
            data={"id": item_id}, control=control,
        )
    async def get_dns_forwarder_apply_status(self):
        """Get DNS forwarder apply status."""
        return await self._make_request("GET", "/services/dns_forwarder/apply")

    async def apply_dns_forwarder_apply(self):
        """Trigger DNS forwarder apply."""
        return await self._make_request("POST", "/services/dns_forwarder/apply")
    async def get_cron_jobs(self, filters=None, sort=None, pagination=None):
        """List cron jobs."""
        return await self._make_request(
            "GET", "/services/cron/jobs",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_cron_job(self, data, control=None):
        """Create a cron job."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/cron/job",
            data=data, control=control,
        )

    async def update_cron_job(self, item_id, updates, control=None):
        """Update a cron job."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/cron/job",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_cron_job(self, item_id, apply_immediately=True):
        """Delete a cron job."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/cron/job",
            data={"id": item_id}, control=control,
        )
    async def get_ntp_time_servers(self, filters=None, sort=None, pagination=None):
        """List NTP time servers."""
        return await self._make_request(
            "GET", "/services/ntp/time_servers",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_ntp_time_server(self, data, control=None):
        """Create a NTP time server."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/ntp/time_server",
            data=data, control=control,
        )

    async def update_ntp_time_server(self, item_id, updates, control=None):
        """Update a NTP time server."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/ntp/time_server",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_ntp_time_server(self, item_id, apply_immediately=True):
        """Delete a NTP time server."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/ntp/time_server",
            data={"id": item_id}, control=control,
        )
    async def get_ntp_settings(self):
        """Get NTP settings."""
        return await self._make_request("GET", "/services/ntp/settings")

    async def update_ntp_settings(self, updates):
        """Update NTP settings."""
        return await self._make_request(
            "PATCH", "/services/ntp/settings",
            data=updates,
        )
    async def get_service_watchdogs(self, filters=None, sort=None, pagination=None):
        """List service watchdogs."""
        return await self._make_request(
            "GET", "/services/service_watchdogs",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_service_watchdog(self, data, control=None):
        """Create a service watchdog."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/services/service_watchdog",
            data=data, control=control,
        )

    async def update_service_watchdog(self, item_id, updates, control=None):
        """Update a service watchdog."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/services/service_watchdog",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_service_watchdog(self, item_id, apply_immediately=True):
        """Delete a service watchdog."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/services/service_watchdog",
            data={"id": item_id}, control=control,
        )
    async def get_ssh_settings(self):
        """Get SSH settings."""
        return await self._make_request("GET", "/services/ssh")

    async def update_ssh_settings(self, updates):
        """Update SSH settings."""
        return await self._make_request(
            "PATCH", "/services/ssh",
            data=updates,
        )
    async def get_wake_on_lan_status(self):
        """Get Wake on LAN status."""
        return await self._make_request("GET", "/services/wake_on_lan/send")

    async def apply_wake_on_lan(self):
        """Trigger Wake on LAN."""
        return await self._make_request("POST", "/services/wake_on_lan/send")
    async def get_system_certificates(self, filters=None, sort=None, pagination=None):
        """List system certificates."""
        return await self._make_request(
            "GET", "/system/certificates",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_system_certificate(self, data, control=None):
        """Create a system certificate."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/system/certificate",
            data=data, control=control,
        )

    async def update_system_certificate(self, item_id, updates, control=None):
        """Update a system certificate."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/system/certificate",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_system_certificate(self, item_id, apply_immediately=True):
        """Delete a system certificate."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/system/certificate",
            data={"id": item_id}, control=control,
        )
    async def get_system_cas(self, filters=None, sort=None, pagination=None):
        """List certificate authoritys."""
        return await self._make_request(
            "GET", "/system/certificate_authorities",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_system_ca(self, data, control=None):
        """Create a certificate authority."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/system/certificate_authority",
            data=data, control=control,
        )

    async def update_system_ca(self, item_id, updates, control=None):
        """Update a certificate authority."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/system/certificate_authority",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_system_ca(self, item_id, apply_immediately=True):
        """Delete a certificate authority."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/system/certificate_authority",
            data={"id": item_id}, control=control,
        )
    async def get_system_crls(self, filters=None, sort=None, pagination=None):
        """List certificate revocation lists."""
        return await self._make_request(
            "GET", "/system/crls",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_system_crl(self, data, control=None):
        """Create a certificate revocation list."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/system/crl",
            data=data, control=control,
        )

    async def update_system_crl(self, item_id, updates, control=None):
        """Update a certificate revocation list."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/system/crl",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_system_crl(self, item_id, apply_immediately=True):
        """Delete a certificate revocation list."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/system/crl",
            data={"id": item_id}, control=control,
        )
    async def get_system_tunables(self, filters=None, sort=None, pagination=None):
        """List system tunables."""
        return await self._make_request(
            "GET", "/system/tunables",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_system_tunable(self, data, control=None):
        """Create a system tunable."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/system/tunable",
            data=data, control=control,
        )

    async def update_system_tunable(self, item_id, updates, control=None):
        """Update a system tunable."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/system/tunable",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_system_tunable(self, item_id, apply_immediately=True):
        """Delete a system tunable."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/system/tunable",
            data={"id": item_id}, control=control,
        )
    async def get_restapi_access_list_entrys(self, filters=None, sort=None, pagination=None):
        """List REST API access list entrys."""
        return await self._make_request(
            "GET", "/system/restapi/access_list",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_restapi_access_list_entry(self, data, control=None):
        """Create a REST API access list entry."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/system/restapi/access_list/entry",
            data=data, control=control,
        )

    async def update_restapi_access_list_entry(self, item_id, updates, control=None):
        """Update a REST API access list entry."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/system/restapi/access_list/entry",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_restapi_access_list_entry(self, item_id, apply_immediately=True):
        """Delete a REST API access list entry."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/system/restapi/access_list/entry",
            data={"id": item_id}, control=control,
        )
    async def get_system_console(self):
        """Get system console settings."""
        return await self._make_request("GET", "/system/console")

    async def update_system_console(self, updates):
        """Update system console settings."""
        return await self._make_request(
            "PATCH", "/system/console",
            data=updates,
        )
    async def get_system_dns(self):
        """Get system DNS settings."""
        return await self._make_request("GET", "/system/dns")

    async def update_system_dns(self, updates):
        """Update system DNS settings."""
        return await self._make_request(
            "PATCH", "/system/dns",
            data=updates,
        )
    async def get_system_hostname(self):
        """Get system hostname."""
        return await self._make_request("GET", "/system/hostname")

    async def update_system_hostname(self, updates):
        """Update system hostname."""
        return await self._make_request(
            "PATCH", "/system/hostname",
            data=updates,
        )
    async def get_system_timezone(self):
        """Get system timezone."""
        return await self._make_request("GET", "/system/timezone")

    async def update_system_timezone(self, updates):
        """Update system timezone."""
        return await self._make_request(
            "PATCH", "/system/timezone",
            data=updates,
        )
    async def get_system_version(self):
        """Get system version."""
        return await self._make_request("GET", "/system/version")
    async def get_webgui_settings(self):
        """Get WebGUI settings."""
        return await self._make_request("GET", "/system/webgui/settings")

    async def update_webgui_settings(self, updates):
        """Update WebGUI settings."""
        return await self._make_request(
            "PATCH", "/system/webgui/settings",
            data=updates,
        )
    async def get_email_notification_settings(self):
        """Get email notification settings."""
        return await self._make_request("GET", "/system/notifications/email_settings")

    async def update_email_notification_settings(self, updates):
        """Update email notification settings."""
        return await self._make_request(
            "PATCH", "/system/notifications/email_settings",
            data=updates,
        )
    async def get_restapi_settings(self):
        """Get REST API settings."""
        return await self._make_request("GET", "/system/restapi/settings")

    async def update_restapi_settings(self, updates):
        """Update REST API settings."""
        return await self._make_request(
            "PATCH", "/system/restapi/settings",
            data=updates,
        )
    async def get_restapi_version(self):
        """Get REST API version."""
        return await self._make_request("GET", "/system/restapi/version")

    async def update_restapi_version(self, updates):
        """Update REST API version."""
        return await self._make_request(
            "PATCH", "/system/restapi/version",
            data=updates,
        )
    async def get_system_packages(self, filters=None, sort=None, pagination=None):
        """List system packages."""
        return await self._make_request(
            "GET", "/system/packages",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_system_package(self, data, control=None):
        """Create a system package."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/system/package",
            data=data, control=control,
        )

    async def update_system_package(self, item_id, updates, control=None):
        """Update a system package."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/system/package",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_system_package(self, item_id, apply_immediately=True):
        """Delete a system package."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/system/package",
            data={"id": item_id}, control=control,
        )
    async def get_users(self, filters=None, sort=None, pagination=None):
        """List users."""
        return await self._make_request(
            "GET", "/users",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_user(self, data, control=None):
        """Create a user."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/user",
            data=data, control=control,
        )

    async def update_user(self, item_id, updates, control=None):
        """Update a user."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/user",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_user(self, item_id, apply_immediately=True):
        """Delete a user."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/user",
            data={"id": item_id}, control=control,
        )
    async def get_user_groups(self, filters=None, sort=None, pagination=None):
        """List user groups."""
        return await self._make_request(
            "GET", "/user/groups",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_user_group(self, data, control=None):
        """Create a user group."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/user/group",
            data=data, control=control,
        )

    async def update_user_group(self, item_id, updates, control=None):
        """Update a user group."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/user/group",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_user_group(self, item_id, apply_immediately=True):
        """Delete a user group."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/user/group",
            data={"id": item_id}, control=control,
        )
    async def get_user_auth_servers(self, filters=None, sort=None, pagination=None):
        """List authentication servers."""
        return await self._make_request(
            "GET", "/user/auth_servers",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_user_auth_server(self, data, control=None):
        """Create a authentication server."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/user/auth_server",
            data=data, control=control,
        )

    async def update_user_auth_server(self, item_id, updates, control=None):
        """Update a authentication server."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/user/auth_server",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_user_auth_server(self, item_id, apply_immediately=True):
        """Delete a authentication server."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/user/auth_server",
            data={"id": item_id}, control=control,
        )
    async def get_ipsec_apply_status(self):
        """Get IPsec apply status."""
        return await self._make_request("GET", "/vpn/ipsec/apply")

    async def apply_ipsec_apply(self):
        """Trigger IPsec apply."""
        return await self._make_request("POST", "/vpn/ipsec/apply")
    async def get_ipsec_phase1s(self, filters=None, sort=None, pagination=None):
        """List IPsec Phase 1s."""
        return await self._make_request(
            "GET", "/vpn/ipsec/phase1s",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_ipsec_phase1(self, data, control=None):
        """Create a IPsec Phase 1."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/ipsec/phase1",
            data=data, control=control,
        )

    async def update_ipsec_phase1(self, item_id, updates, control=None):
        """Update a IPsec Phase 1."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/ipsec/phase1",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_ipsec_phase1(self, item_id, apply_immediately=True):
        """Delete a IPsec Phase 1."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/ipsec/phase1",
            data={"id": item_id}, control=control,
        )
    async def get_ipsec_phase1_encryptions(self, filters=None, sort=None, pagination=None):
        """List IPsec Phase 1 encryptions."""
        return await self._make_request(
            "GET", "/vpn/ipsec/phase1/encryptions",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_ipsec_phase1_encryption(self, data, control=None):
        """Create a IPsec Phase 1 encryption. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/ipsec/phase1/encryption",
            data=data, control=control,
        )

    async def update_ipsec_phase1_encryption(self, item_id, updates, control=None):
        """Update a IPsec Phase 1 encryption."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/ipsec/phase1/encryption",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_ipsec_phase1_encryption(self, item_id, apply_immediately=True):
        """Delete a IPsec Phase 1 encryption."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/ipsec/phase1/encryption",
            data={"id": item_id}, control=control,
        )
    async def get_ipsec_phase2s(self, filters=None, sort=None, pagination=None):
        """List IPsec Phase 2s."""
        return await self._make_request(
            "GET", "/vpn/ipsec/phase2s",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_ipsec_phase2(self, data, control=None):
        """Create a IPsec Phase 2."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/ipsec/phase2",
            data=data, control=control,
        )

    async def update_ipsec_phase2(self, item_id, updates, control=None):
        """Update a IPsec Phase 2."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/ipsec/phase2",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_ipsec_phase2(self, item_id, apply_immediately=True):
        """Delete a IPsec Phase 2."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/ipsec/phase2",
            data={"id": item_id}, control=control,
        )
    async def get_ipsec_phase2_encryptions(self, filters=None, sort=None, pagination=None):
        """List IPsec Phase 2 encryptions."""
        return await self._make_request(
            "GET", "/vpn/ipsec/phase2/encryptions",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_ipsec_phase2_encryption(self, data, control=None):
        """Create a IPsec Phase 2 encryption. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/ipsec/phase2/encryption",
            data=data, control=control,
        )

    async def update_ipsec_phase2_encryption(self, item_id, updates, control=None):
        """Update a IPsec Phase 2 encryption."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/ipsec/phase2/encryption",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_ipsec_phase2_encryption(self, item_id, apply_immediately=True):
        """Delete a IPsec Phase 2 encryption."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/ipsec/phase2/encryption",
            data={"id": item_id}, control=control,
        )
    async def get_openvpn_servers(self, filters=None, sort=None, pagination=None):
        """List OpenVPN servers."""
        return await self._make_request(
            "GET", "/vpn/openvpn/servers",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_openvpn_server(self, data, control=None):
        """Create a OpenVPN server."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/openvpn/server",
            data=data, control=control,
        )

    async def update_openvpn_server(self, item_id, updates, control=None):
        """Update a OpenVPN server."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/openvpn/server",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_openvpn_server(self, item_id, apply_immediately=True):
        """Delete a OpenVPN server."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/openvpn/server",
            data={"id": item_id}, control=control,
        )
    async def get_openvpn_clients(self, filters=None, sort=None, pagination=None):
        """List OpenVPN clients."""
        return await self._make_request(
            "GET", "/vpn/openvpn/clients",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_openvpn_client(self, data, control=None):
        """Create a OpenVPN client."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/openvpn/client",
            data=data, control=control,
        )

    async def update_openvpn_client(self, item_id, updates, control=None):
        """Update a OpenVPN client."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/openvpn/client",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_openvpn_client(self, item_id, apply_immediately=True):
        """Delete a OpenVPN client."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/openvpn/client",
            data={"id": item_id}, control=control,
        )
    async def get_openvpn_csos(self, filters=None, sort=None, pagination=None):
        """List OpenVPN client-specific overrides."""
        return await self._make_request(
            "GET", "/vpn/openvpn/csos",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_openvpn_cso(self, data, control=None):
        """Create a OpenVPN client-specific override."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/openvpn/cso",
            data=data, control=control,
        )

    async def update_openvpn_cso(self, item_id, updates, control=None):
        """Update a OpenVPN client-specific override."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/openvpn/cso",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_openvpn_cso(self, item_id, apply_immediately=True):
        """Delete a OpenVPN client-specific override."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/openvpn/cso",
            data={"id": item_id}, control=control,
        )
    async def get_wireguard_tunnels(self, filters=None, sort=None, pagination=None):
        """List WireGuard tunnels."""
        return await self._make_request(
            "GET", "/vpn/wireguard/tunnels",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_wireguard_tunnel(self, data, control=None):
        """Create a WireGuard tunnel."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/wireguard/tunnel",
            data=data, control=control,
        )

    async def update_wireguard_tunnel(self, item_id, updates, control=None):
        """Update a WireGuard tunnel."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/wireguard/tunnel",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_wireguard_tunnel(self, item_id, apply_immediately=True):
        """Delete a WireGuard tunnel."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/wireguard/tunnel",
            data={"id": item_id}, control=control,
        )
    async def get_wireguard_tunnel_addresss(self, filters=None, sort=None, pagination=None):
        """List WireGuard tunnel addresss."""
        return await self._make_request(
            "GET", "/vpn/wireguard/tunnel/addresses",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_wireguard_tunnel_address(self, data, control=None):
        """Create a WireGuard tunnel address. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/wireguard/tunnel/address",
            data=data, control=control,
        )

    async def update_wireguard_tunnel_address(self, item_id, updates, control=None):
        """Update a WireGuard tunnel address."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/wireguard/tunnel/address",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_wireguard_tunnel_address(self, item_id, apply_immediately=True):
        """Delete a WireGuard tunnel address."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/wireguard/tunnel/address",
            data={"id": item_id}, control=control,
        )
    async def get_wireguard_peers(self, filters=None, sort=None, pagination=None):
        """List WireGuard peers."""
        return await self._make_request(
            "GET", "/vpn/wireguard/peers",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_wireguard_peer(self, data, control=None):
        """Create a WireGuard peer."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/wireguard/peer",
            data=data, control=control,
        )

    async def update_wireguard_peer(self, item_id, updates, control=None):
        """Update a WireGuard peer."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/wireguard/peer",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_wireguard_peer(self, item_id, apply_immediately=True):
        """Delete a WireGuard peer."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/wireguard/peer",
            data={"id": item_id}, control=control,
        )
    async def get_wireguard_peer_allowed_ips(self, filters=None, sort=None, pagination=None):
        """List WireGuard peer allowed IPs."""
        return await self._make_request(
            "GET", "/vpn/wireguard/peer/allowed_ips",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def create_wireguard_peer_allowed_ip(self, data, control=None):
        """Create a WireGuard peer allowed IP. Include 'parent_id' in data."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "POST", "/vpn/wireguard/peer/allowed_ip",
            data=data, control=control,
        )

    async def update_wireguard_peer_allowed_ip(self, item_id, updates, control=None):
        """Update a WireGuard peer allowed IP."""
        from pfsense_api_enhanced import ControlParameters
        if not control:
            control = ControlParameters(apply=True)
        return await self._make_request(
            "PATCH", "/vpn/wireguard/peer/allowed_ip",
            data={"id": item_id, **updates}, control=control,
        )

    async def delete_wireguard_peer_allowed_ip(self, item_id, apply_immediately=True):
        """Delete a WireGuard peer allowed IP."""
        from pfsense_api_enhanced import ControlParameters
        control = ControlParameters(apply=apply_immediately)
        return await self._make_request(
            "DELETE", "/vpn/wireguard/peer/allowed_ip",
            data={"id": item_id}, control=control,
        )
    async def get_wireguard_apply_status(self):
        """Get WireGuard apply status."""
        return await self._make_request("GET", "/vpn/wireguard/apply")

    async def apply_wireguard_apply(self):
        """Trigger WireGuard apply."""
        return await self._make_request("POST", "/vpn/wireguard/apply")
    async def get_wireguard_settings(self):
        """Get WireGuard settings."""
        return await self._make_request("GET", "/vpn/wireguard/settings")

    async def update_wireguard_settings(self, updates):
        """Update WireGuard settings."""
        return await self._make_request(
            "PATCH", "/vpn/wireguard/settings",
            data=updates,
        )
    async def get_arp_table_entrys(self, filters=None, sort=None, pagination=None):
        """List ARP table entrys."""
        return await self._make_request(
            "GET", "/diagnostics/arp_table",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def delete_arp_table_entrys(self):
        """Delete all ARP table entrys."""
        return await self._make_request("DELETE", "/diagnostics/arp_table")
    async def get_config_history_revisions(self, filters=None, sort=None, pagination=None):
        """List config history revisions."""
        return await self._make_request(
            "GET", "/diagnostics/config_history/revisions",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def delete_config_history_revisions(self):
        """Delete all config history revisions."""
        return await self._make_request("DELETE", "/diagnostics/config_history/revisions")
    async def get_pf_tables(self, filters=None, sort=None, pagination=None):
        """List pf tables."""
        return await self._make_request(
            "GET", "/diagnostics/tables",
            filters=filters, sort=sort, pagination=pagination,
        )

    async def delete_pf_tables(self):
        """Delete all pf tables."""
        return await self._make_request("DELETE", "/diagnostics/tables")
    async def get_carp_status(self):
        """Get CARP status."""
        return await self._make_request("GET", "/status/carp")

    async def update_carp_status(self, updates):
        """Update CARP status."""
        return await self._make_request(
            "PATCH", "/status/carp",
            data=updates,
        )
    async def get_gateway_status(self):
        """Get gateway status."""
        return await self._make_request("GET", "/status/gateways")
    async def get_log_settings(self):
        """Get log settings."""
        return await self._make_request("GET", "/status/logs/settings")

    async def update_log_settings(self, updates):
        """Update log settings."""
        return await self._make_request(
            "PATCH", "/status/logs/settings",
            data=updates,
        )
    async def get_openvpn_server_status(self):
        """Get OpenVPN server status."""
        return await self._make_request("GET", "/status/openvpn/servers")
    async def get_ipsec_sa_status(self):
        """Get IPsec SA status."""
        return await self._make_request("GET", "/status/ipsec/sas")