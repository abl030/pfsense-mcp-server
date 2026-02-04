"""Auto-generated MCP tools. DO NOT EDIT.
Regenerate: python scripts/generate_from_spec.py
"""

from datetime import datetime
from typing import Dict, List, Optional


def register_generated_tools(mcp, get_api_client):
    """Register all generated MCP tools on the given FastMCP instance."""

    # Lazy import to avoid circular imports at module level
    try:
        from .pfsense_api_enhanced import create_pagination
    except ImportError:
        from pfsense_api_enhanced import create_pagination

    @mcp.tool()
    async def list_nat_one_to_one_mappings(page: int = 1, page_size: int = 20) -> Dict:
        """List NAT one-to-one mappings with pagination."""
        client = get_api_client()
        try:
            result = await client.get_nat_one_to_one_mappings(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_nat_one_to_one_mapping(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a NAT one-to-one mapping."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_nat_one_to_one_mapping(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_nat_one_to_one_mapping(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a NAT one-to-one mapping."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_nat_one_to_one_mapping(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_nat_one_to_one_mapping(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a NAT one-to-one mapping."""
        client = get_api_client()
        try:
            result = await client.delete_nat_one_to_one_mapping(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_nat_outbound_mappings(page: int = 1, page_size: int = 20) -> Dict:
        """List NAT outbound mappings with pagination."""
        client = get_api_client()
        try:
            result = await client.get_nat_outbound_mappings(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_nat_outbound_mapping(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a NAT outbound mapping."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_nat_outbound_mapping(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_nat_outbound_mapping(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a NAT outbound mapping."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_nat_outbound_mapping(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_nat_outbound_mapping(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a NAT outbound mapping."""
        client = get_api_client()
        try:
            result = await client.delete_nat_outbound_mapping(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_nat_outbound_mode() -> Dict:
        """Get NAT outbound mode."""
        client = get_api_client()
        try:
            result = await client.get_nat_outbound_mode()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_nat_outbound_mode(updates: Dict) -> Dict:
        """Update NAT outbound mode."""
        client = get_api_client()
        try:
            result = await client.update_nat_outbound_mode(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_firewall_schedules(page: int = 1, page_size: int = 20) -> Dict:
        """List firewall schedules with pagination."""
        client = get_api_client()
        try:
            result = await client.get_firewall_schedules(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_firewall_schedule(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a firewall schedule."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_firewall_schedule(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_firewall_schedule(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a firewall schedule."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_firewall_schedule(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_firewall_schedule(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a firewall schedule."""
        client = get_api_client()
        try:
            result = await client.delete_firewall_schedule(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_firewall_schedule_time_ranges(page: int = 1, page_size: int = 20) -> Dict:
        """List firewall schedule time ranges with pagination."""
        client = get_api_client()
        try:
            result = await client.get_firewall_schedule_time_ranges(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_firewall_schedule_time_range(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a firewall schedule time range."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_firewall_schedule_time_range(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_firewall_schedule_time_range(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a firewall schedule time range."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_firewall_schedule_time_range(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_firewall_schedule_time_range(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a firewall schedule time range."""
        client = get_api_client()
        try:
            result = await client.delete_firewall_schedule_time_range(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_traffic_shapers(page: int = 1, page_size: int = 20) -> Dict:
        """List traffic shapers with pagination."""
        client = get_api_client()
        try:
            result = await client.get_traffic_shapers(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_traffic_shaper(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a traffic shaper."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_traffic_shaper(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_traffic_shaper(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a traffic shaper."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_traffic_shaper(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_traffic_shaper(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a traffic shaper."""
        client = get_api_client()
        try:
            result = await client.delete_traffic_shaper(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_traffic_shaper_queues(page: int = 1, page_size: int = 20) -> Dict:
        """List traffic shaper queues with pagination."""
        client = get_api_client()
        try:
            result = await client.get_traffic_shaper_queues(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_traffic_shaper_queue(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a traffic shaper queue."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_traffic_shaper_queue(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_traffic_shaper_queue(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a traffic shaper queue."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_traffic_shaper_queue(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_traffic_shaper_queue(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a traffic shaper queue."""
        client = get_api_client()
        try:
            result = await client.delete_traffic_shaper_queue(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_traffic_shaper_limiters(page: int = 1, page_size: int = 20) -> Dict:
        """List traffic shaper limiters with pagination."""
        client = get_api_client()
        try:
            result = await client.get_traffic_shaper_limiters(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_traffic_shaper_limiter(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a traffic shaper limiter."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_traffic_shaper_limiter(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_traffic_shaper_limiter(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a traffic shaper limiter."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_traffic_shaper_limiter(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_traffic_shaper_limiter(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a traffic shaper limiter."""
        client = get_api_client()
        try:
            result = await client.delete_traffic_shaper_limiter(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_traffic_shaper_limiter_queues(page: int = 1, page_size: int = 20) -> Dict:
        """List traffic shaper limiter queues with pagination."""
        client = get_api_client()
        try:
            result = await client.get_traffic_shaper_limiter_queues(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_traffic_shaper_limiter_queue(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a traffic shaper limiter queue."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_traffic_shaper_limiter_queue(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_traffic_shaper_limiter_queue(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a traffic shaper limiter queue."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_traffic_shaper_limiter_queue(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_traffic_shaper_limiter_queue(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a traffic shaper limiter queue."""
        client = get_api_client()
        try:
            result = await client.delete_traffic_shaper_limiter_queue(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_traffic_shaper_limiter_bandwidths(page: int = 1, page_size: int = 20) -> Dict:
        """List traffic shaper limiter bandwidths with pagination."""
        client = get_api_client()
        try:
            result = await client.get_traffic_shaper_limiter_bandwidths(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_traffic_shaper_limiter_bandwidth(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a traffic shaper limiter bandwidth."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_traffic_shaper_limiter_bandwidth(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_traffic_shaper_limiter_bandwidth(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a traffic shaper limiter bandwidth."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_traffic_shaper_limiter_bandwidth(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_traffic_shaper_limiter_bandwidth(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a traffic shaper limiter bandwidth."""
        client = get_api_client()
        try:
            result = await client.delete_traffic_shaper_limiter_bandwidth(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_virtual_ips(page: int = 1, page_size: int = 20) -> Dict:
        """List virtual IPs with pagination."""
        client = get_api_client()
        try:
            result = await client.get_virtual_ips(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_virtual_ip(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a virtual IP."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_virtual_ip(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_virtual_ip(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a virtual IP."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_virtual_ip(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_virtual_ip(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a virtual IP."""
        client = get_api_client()
        try:
            result = await client.delete_virtual_ip(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_virtual_ip_apply_status() -> Dict:
        """Get virtual IP apply status."""
        client = get_api_client()
        try:
            result = await client.get_virtual_ip_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_virtual_ip_apply() -> Dict:
        """Trigger virtual IP apply."""
        client = get_api_client()
        try:
            result = await client.apply_virtual_ip_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_firewall_states(page: int = 1, page_size: int = 20) -> Dict:
        """List firewall states with pagination."""
        client = get_api_client()
        try:
            result = await client.get_firewall_states(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_all_firewall_states() -> Dict:
        """Delete all firewall states."""
        client = get_api_client()
        try:
            result = await client.delete_firewall_states()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_firewall_states_size() -> Dict:
        """Get firewall states size."""
        client = get_api_client()
        try:
            result = await client.get_firewall_states_size()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_firewall_states_size(updates: Dict) -> Dict:
        """Update firewall states size."""
        client = get_api_client()
        try:
            result = await client.update_firewall_states_size(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_firewall_advanced_settings() -> Dict:
        """Get firewall advanced settings."""
        client = get_api_client()
        try:
            result = await client.get_firewall_advanced_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_firewall_advanced_settings(updates: Dict) -> Dict:
        """Update firewall advanced settings."""
        client = get_api_client()
        try:
            result = await client.update_firewall_advanced_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_firewall_apply_status() -> Dict:
        """Get firewall apply status."""
        client = get_api_client()
        try:
            result = await client.get_firewall_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_firewall_apply() -> Dict:
        """Trigger firewall apply."""
        client = get_api_client()
        try:
            result = await client.apply_firewall_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_routing_gateways(page: int = 1, page_size: int = 20) -> Dict:
        """List routing gateways with pagination."""
        client = get_api_client()
        try:
            result = await client.get_routing_gateways(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_routing_gateway(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a routing gateway."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_routing_gateway(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_routing_gateway(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a routing gateway."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_routing_gateway(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_routing_gateway(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a routing gateway."""
        client = get_api_client()
        try:
            result = await client.delete_routing_gateway(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_routing_gateway_default() -> Dict:
        """Get default routing gateway."""
        client = get_api_client()
        try:
            result = await client.get_routing_gateway_default()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_routing_gateway_default(updates: Dict) -> Dict:
        """Update default routing gateway."""
        client = get_api_client()
        try:
            result = await client.update_routing_gateway_default(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_routing_gateway_groups(page: int = 1, page_size: int = 20) -> Dict:
        """List routing gateway groups with pagination."""
        client = get_api_client()
        try:
            result = await client.get_routing_gateway_groups(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_routing_gateway_group(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a routing gateway group."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_routing_gateway_group(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_routing_gateway_group(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a routing gateway group."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_routing_gateway_group(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_routing_gateway_group(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a routing gateway group."""
        client = get_api_client()
        try:
            result = await client.delete_routing_gateway_group(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_routing_gateway_group_prioritys(page: int = 1, page_size: int = 20) -> Dict:
        """List routing gateway group prioritys with pagination."""
        client = get_api_client()
        try:
            result = await client.get_routing_gateway_group_prioritys(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_routing_gateway_group_priority(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a routing gateway group priority."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_routing_gateway_group_priority(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_routing_gateway_group_priority(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a routing gateway group priority."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_routing_gateway_group_priority(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_routing_gateway_group_priority(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a routing gateway group priority."""
        client = get_api_client()
        try:
            result = await client.delete_routing_gateway_group_priority(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_routing_static_routes(page: int = 1, page_size: int = 20) -> Dict:
        """List static routes with pagination."""
        client = get_api_client()
        try:
            result = await client.get_routing_static_routes(
                pagination=create_pagination(page, page_size),
            )
            return {
                "success": True,
                "data": result.get("data", []),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def create_routing_static_route(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a static route."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_routing_static_route(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_routing_static_route(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a static route."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_routing_static_route(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_routing_static_route(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a static route."""
        client = get_api_client()
        try:
            result = await client.delete_routing_static_route(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_routing_apply_status() -> Dict:
        """Get routing apply status."""
        client = get_api_client()
        try:
            result = await client.get_routing_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_routing_apply() -> Dict:
        """Trigger routing apply."""
        client = get_api_client()
        try:
            result = await client.apply_routing_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}