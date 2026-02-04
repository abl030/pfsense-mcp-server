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