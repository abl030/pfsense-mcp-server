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
    @mcp.tool()
    async def list_interfaces(page: int = 1, page_size: int = 20) -> Dict:
        """List network interfaces with pagination."""
        client = get_api_client()
        try:
            result = await client.get_interfaces(
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
    async def create_interface(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a network interface."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_interface(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_interface(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a network interface."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_interface(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_interface(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a network interface."""
        client = get_api_client()
        try:
            result = await client.delete_interface(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_interface_apply_status() -> Dict:
        """Get interface apply status."""
        client = get_api_client()
        try:
            result = await client.get_interface_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_interface_apply() -> Dict:
        """Trigger interface apply."""
        client = get_api_client()
        try:
            result = await client.apply_interface_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_available_interfaces() -> Dict:
        """Get available interfaces."""
        client = get_api_client()
        try:
            result = await client.get_available_interfaces()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_interface_bridges(page: int = 1, page_size: int = 20) -> Dict:
        """List interface bridges with pagination."""
        client = get_api_client()
        try:
            result = await client.get_interface_bridges(
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
    async def create_interface_bridge(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a interface bridge."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_interface_bridge(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_interface_bridge(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a interface bridge."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_interface_bridge(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_interface_bridge(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a interface bridge."""
        client = get_api_client()
        try:
            result = await client.delete_interface_bridge(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_interface_groups(page: int = 1, page_size: int = 20) -> Dict:
        """List interface groups with pagination."""
        client = get_api_client()
        try:
            result = await client.get_interface_groups(
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
    async def create_interface_group(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a interface group."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_interface_group(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_interface_group(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a interface group."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_interface_group(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_interface_group(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a interface group."""
        client = get_api_client()
        try:
            result = await client.delete_interface_group(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_interface_vlans(page: int = 1, page_size: int = 20) -> Dict:
        """List interface VLANs with pagination."""
        client = get_api_client()
        try:
            result = await client.get_interface_vlans(
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
    async def create_interface_vlan(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a interface VLAN."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_interface_vlan(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_interface_vlan(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a interface VLAN."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_interface_vlan(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_interface_vlan(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a interface VLAN."""
        client = get_api_client()
        try:
            result = await client.delete_interface_vlan(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_interface_gres(page: int = 1, page_size: int = 20) -> Dict:
        """List interface GRE tunnels with pagination."""
        client = get_api_client()
        try:
            result = await client.get_interface_gres(
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
    async def create_interface_gre(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a interface GRE tunnel."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_interface_gre(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_interface_gre(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a interface GRE tunnel."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_interface_gre(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_interface_gre(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a interface GRE tunnel."""
        client = get_api_client()
        try:
            result = await client.delete_interface_gre(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_interface_laggs(page: int = 1, page_size: int = 20) -> Dict:
        """List interface LAGGs with pagination."""
        client = get_api_client()
        try:
            result = await client.get_interface_laggs(
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
    async def create_interface_lagg(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a interface LAGG."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_interface_lagg(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_interface_lagg(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a interface LAGG."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_interface_lagg(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_interface_lagg(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a interface LAGG."""
        client = get_api_client()
        try:
            result = await client.delete_interface_lagg(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dhcp_servers(page: int = 1, page_size: int = 20) -> Dict:
        """List DHCP servers with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dhcp_servers(
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
    async def create_dhcp_server(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DHCP server."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dhcp_server(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dhcp_server(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DHCP server."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dhcp_server(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dhcp_server(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DHCP server."""
        client = get_api_client()
        try:
            result = await client.delete_dhcp_server(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dhcp_server_static_mappings(page: int = 1, page_size: int = 20) -> Dict:
        """List DHCP static mappings with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dhcp_server_static_mappings(
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
    async def create_dhcp_server_static_mapping(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DHCP static mapping."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dhcp_server_static_mapping(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dhcp_server_static_mapping(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DHCP static mapping."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dhcp_server_static_mapping(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dhcp_server_static_mapping(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DHCP static mapping."""
        client = get_api_client()
        try:
            result = await client.delete_dhcp_server_static_mapping(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dhcp_server_address_pools(page: int = 1, page_size: int = 20) -> Dict:
        """List DHCP address pools with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dhcp_server_address_pools(
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
    async def create_dhcp_server_address_pool(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DHCP address pool."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dhcp_server_address_pool(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dhcp_server_address_pool(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DHCP address pool."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dhcp_server_address_pool(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dhcp_server_address_pool(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DHCP address pool."""
        client = get_api_client()
        try:
            result = await client.delete_dhcp_server_address_pool(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dhcp_server_custom_options(page: int = 1, page_size: int = 20) -> Dict:
        """List DHCP custom options with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dhcp_server_custom_options(
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
    async def create_dhcp_server_custom_option(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DHCP custom option."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dhcp_server_custom_option(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dhcp_server_custom_option(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DHCP custom option."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dhcp_server_custom_option(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dhcp_server_custom_option(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DHCP custom option."""
        client = get_api_client()
        try:
            result = await client.delete_dhcp_server_custom_option(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_dhcp_server_apply_status() -> Dict:
        """Get DHCP server apply status."""
        client = get_api_client()
        try:
            result = await client.get_dhcp_server_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_dhcp_server_apply() -> Dict:
        """Trigger DHCP server apply."""
        client = get_api_client()
        try:
            result = await client.apply_dhcp_server_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_dhcp_relay() -> Dict:
        """Get DHCP relay."""
        client = get_api_client()
        try:
            result = await client.get_dhcp_relay()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dhcp_relay(updates: Dict) -> Dict:
        """Update DHCP relay."""
        client = get_api_client()
        try:
            result = await client.update_dhcp_relay(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dns_resolver_host_overrides(page: int = 1, page_size: int = 20) -> Dict:
        """List DNS resolver host overrides with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dns_resolver_host_overrides(
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
    async def create_dns_resolver_host_override(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DNS resolver host override."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dns_resolver_host_override(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dns_resolver_host_override(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DNS resolver host override."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dns_resolver_host_override(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dns_resolver_host_override(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DNS resolver host override."""
        client = get_api_client()
        try:
            result = await client.delete_dns_resolver_host_override(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dns_resolver_host_override_aliass(page: int = 1, page_size: int = 20) -> Dict:
        """List DNS resolver host override aliass with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dns_resolver_host_override_aliass(
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
    async def create_dns_resolver_host_override_alias(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DNS resolver host override alias."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dns_resolver_host_override_alias(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dns_resolver_host_override_alias(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DNS resolver host override alias."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dns_resolver_host_override_alias(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dns_resolver_host_override_alias(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DNS resolver host override alias."""
        client = get_api_client()
        try:
            result = await client.delete_dns_resolver_host_override_alias(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dns_resolver_domain_overrides(page: int = 1, page_size: int = 20) -> Dict:
        """List DNS resolver domain overrides with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dns_resolver_domain_overrides(
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
    async def create_dns_resolver_domain_override(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DNS resolver domain override."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dns_resolver_domain_override(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dns_resolver_domain_override(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DNS resolver domain override."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dns_resolver_domain_override(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dns_resolver_domain_override(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DNS resolver domain override."""
        client = get_api_client()
        try:
            result = await client.delete_dns_resolver_domain_override(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dns_resolver_access_lists(page: int = 1, page_size: int = 20) -> Dict:
        """List DNS resolver access lists with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dns_resolver_access_lists(
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
    async def create_dns_resolver_access_list(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DNS resolver access list."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dns_resolver_access_list(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dns_resolver_access_list(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DNS resolver access list."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dns_resolver_access_list(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dns_resolver_access_list(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DNS resolver access list."""
        client = get_api_client()
        try:
            result = await client.delete_dns_resolver_access_list(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dns_resolver_access_list_networks(page: int = 1, page_size: int = 20) -> Dict:
        """List DNS resolver access list networks with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dns_resolver_access_list_networks(
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
    async def create_dns_resolver_access_list_network(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DNS resolver access list network."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dns_resolver_access_list_network(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dns_resolver_access_list_network(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DNS resolver access list network."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dns_resolver_access_list_network(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dns_resolver_access_list_network(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DNS resolver access list network."""
        client = get_api_client()
        try:
            result = await client.delete_dns_resolver_access_list_network(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_dns_resolver_apply_status() -> Dict:
        """Get DNS resolver apply status."""
        client = get_api_client()
        try:
            result = await client.get_dns_resolver_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_dns_resolver_apply() -> Dict:
        """Trigger DNS resolver apply."""
        client = get_api_client()
        try:
            result = await client.apply_dns_resolver_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_dns_resolver_settings() -> Dict:
        """Get DNS resolver settings."""
        client = get_api_client()
        try:
            result = await client.get_dns_resolver_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dns_resolver_settings(updates: Dict) -> Dict:
        """Update DNS resolver settings."""
        client = get_api_client()
        try:
            result = await client.update_dns_resolver_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dns_forwarder_host_overrides(page: int = 1, page_size: int = 20) -> Dict:
        """List DNS forwarder host overrides with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dns_forwarder_host_overrides(
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
    async def create_dns_forwarder_host_override(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DNS forwarder host override."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dns_forwarder_host_override(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dns_forwarder_host_override(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DNS forwarder host override."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dns_forwarder_host_override(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dns_forwarder_host_override(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DNS forwarder host override."""
        client = get_api_client()
        try:
            result = await client.delete_dns_forwarder_host_override(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_dns_forwarder_host_override_aliass(page: int = 1, page_size: int = 20) -> Dict:
        """List DNS forwarder host override aliass with pagination."""
        client = get_api_client()
        try:
            result = await client.get_dns_forwarder_host_override_aliass(
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
    async def create_dns_forwarder_host_override_alias(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a DNS forwarder host override alias."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_dns_forwarder_host_override_alias(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_dns_forwarder_host_override_alias(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a DNS forwarder host override alias."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_dns_forwarder_host_override_alias(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_dns_forwarder_host_override_alias(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a DNS forwarder host override alias."""
        client = get_api_client()
        try:
            result = await client.delete_dns_forwarder_host_override_alias(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_dns_forwarder_apply_status() -> Dict:
        """Get DNS forwarder apply status."""
        client = get_api_client()
        try:
            result = await client.get_dns_forwarder_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_dns_forwarder_apply() -> Dict:
        """Trigger DNS forwarder apply."""
        client = get_api_client()
        try:
            result = await client.apply_dns_forwarder_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_cron_jobs(page: int = 1, page_size: int = 20) -> Dict:
        """List cron jobs with pagination."""
        client = get_api_client()
        try:
            result = await client.get_cron_jobs(
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
    async def create_cron_job(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a cron job."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_cron_job(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_cron_job(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a cron job."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_cron_job(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_cron_job(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a cron job."""
        client = get_api_client()
        try:
            result = await client.delete_cron_job(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_ntp_time_servers(page: int = 1, page_size: int = 20) -> Dict:
        """List NTP time servers with pagination."""
        client = get_api_client()
        try:
            result = await client.get_ntp_time_servers(
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
    async def create_ntp_time_server(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a NTP time server."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_ntp_time_server(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_ntp_time_server(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a NTP time server."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_ntp_time_server(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_ntp_time_server(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a NTP time server."""
        client = get_api_client()
        try:
            result = await client.delete_ntp_time_server(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_ntp_settings() -> Dict:
        """Get NTP settings."""
        client = get_api_client()
        try:
            result = await client.get_ntp_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_ntp_settings(updates: Dict) -> Dict:
        """Update NTP settings."""
        client = get_api_client()
        try:
            result = await client.update_ntp_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_service_watchdogs(page: int = 1, page_size: int = 20) -> Dict:
        """List service watchdogs with pagination."""
        client = get_api_client()
        try:
            result = await client.get_service_watchdogs(
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
    async def create_service_watchdog(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a service watchdog."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_service_watchdog(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_service_watchdog(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a service watchdog."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_service_watchdog(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_service_watchdog(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a service watchdog."""
        client = get_api_client()
        try:
            result = await client.delete_service_watchdog(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_ssh_settings() -> Dict:
        """Get SSH settings."""
        client = get_api_client()
        try:
            result = await client.get_ssh_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_ssh_settings(updates: Dict) -> Dict:
        """Update SSH settings."""
        client = get_api_client()
        try:
            result = await client.update_ssh_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_wake_on_lan_status() -> Dict:
        """Get Wake on LAN status."""
        client = get_api_client()
        try:
            result = await client.get_wake_on_lan_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_wake_on_lan() -> Dict:
        """Trigger Wake on LAN."""
        client = get_api_client()
        try:
            result = await client.apply_wake_on_lan()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_system_certificates(page: int = 1, page_size: int = 20) -> Dict:
        """List system certificates with pagination."""
        client = get_api_client()
        try:
            result = await client.get_system_certificates(
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
    async def create_system_certificate(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a system certificate."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_system_certificate(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_certificate(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a system certificate."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_system_certificate(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_system_certificate(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a system certificate."""
        client = get_api_client()
        try:
            result = await client.delete_system_certificate(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_system_cas(page: int = 1, page_size: int = 20) -> Dict:
        """List certificate authoritys with pagination."""
        client = get_api_client()
        try:
            result = await client.get_system_cas(
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
    async def create_system_ca(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a certificate authority."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_system_ca(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_ca(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a certificate authority."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_system_ca(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_system_ca(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a certificate authority."""
        client = get_api_client()
        try:
            result = await client.delete_system_ca(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_system_crls(page: int = 1, page_size: int = 20) -> Dict:
        """List certificate revocation lists with pagination."""
        client = get_api_client()
        try:
            result = await client.get_system_crls(
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
    async def create_system_crl(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a certificate revocation list."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_system_crl(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_crl(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a certificate revocation list."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_system_crl(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_system_crl(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a certificate revocation list."""
        client = get_api_client()
        try:
            result = await client.delete_system_crl(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_system_tunables(page: int = 1, page_size: int = 20) -> Dict:
        """List system tunables with pagination."""
        client = get_api_client()
        try:
            result = await client.get_system_tunables(
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
    async def create_system_tunable(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a system tunable."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_system_tunable(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_tunable(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a system tunable."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_system_tunable(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_system_tunable(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a system tunable."""
        client = get_api_client()
        try:
            result = await client.delete_system_tunable(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_restapi_access_list_entrys(page: int = 1, page_size: int = 20) -> Dict:
        """List REST API access list entrys with pagination."""
        client = get_api_client()
        try:
            result = await client.get_restapi_access_list_entrys(
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
    async def create_restapi_access_list_entry(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a REST API access list entry."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_restapi_access_list_entry(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_restapi_access_list_entry(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a REST API access list entry."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_restapi_access_list_entry(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_restapi_access_list_entry(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a REST API access list entry."""
        client = get_api_client()
        try:
            result = await client.delete_restapi_access_list_entry(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_system_console() -> Dict:
        """Get system console settings."""
        client = get_api_client()
        try:
            result = await client.get_system_console()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_console(updates: Dict) -> Dict:
        """Update system console settings."""
        client = get_api_client()
        try:
            result = await client.update_system_console(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_system_dns() -> Dict:
        """Get system DNS settings."""
        client = get_api_client()
        try:
            result = await client.get_system_dns()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_dns(updates: Dict) -> Dict:
        """Update system DNS settings."""
        client = get_api_client()
        try:
            result = await client.update_system_dns(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_system_hostname() -> Dict:
        """Get system hostname."""
        client = get_api_client()
        try:
            result = await client.get_system_hostname()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_hostname(updates: Dict) -> Dict:
        """Update system hostname."""
        client = get_api_client()
        try:
            result = await client.update_system_hostname(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_system_timezone() -> Dict:
        """Get system timezone."""
        client = get_api_client()
        try:
            result = await client.get_system_timezone()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_timezone(updates: Dict) -> Dict:
        """Update system timezone."""
        client = get_api_client()
        try:
            result = await client.update_system_timezone(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_system_version() -> Dict:
        """Get system version."""
        client = get_api_client()
        try:
            result = await client.get_system_version()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_webgui_settings() -> Dict:
        """Get WebGUI settings."""
        client = get_api_client()
        try:
            result = await client.get_webgui_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_webgui_settings(updates: Dict) -> Dict:
        """Update WebGUI settings."""
        client = get_api_client()
        try:
            result = await client.update_webgui_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_email_notification_settings() -> Dict:
        """Get email notification settings."""
        client = get_api_client()
        try:
            result = await client.get_email_notification_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_email_notification_settings(updates: Dict) -> Dict:
        """Update email notification settings."""
        client = get_api_client()
        try:
            result = await client.update_email_notification_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_restapi_settings() -> Dict:
        """Get REST API settings."""
        client = get_api_client()
        try:
            result = await client.get_restapi_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_restapi_settings(updates: Dict) -> Dict:
        """Update REST API settings."""
        client = get_api_client()
        try:
            result = await client.update_restapi_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_restapi_version() -> Dict:
        """Get REST API version."""
        client = get_api_client()
        try:
            result = await client.get_restapi_version()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_restapi_version(updates: Dict) -> Dict:
        """Update REST API version."""
        client = get_api_client()
        try:
            result = await client.update_restapi_version(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_system_packages(page: int = 1, page_size: int = 20) -> Dict:
        """List system packages with pagination."""
        client = get_api_client()
        try:
            result = await client.get_system_packages(
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
    async def create_system_package(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a system package."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_system_package(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_system_package(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a system package."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_system_package(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_system_package(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a system package."""
        client = get_api_client()
        try:
            result = await client.delete_system_package(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_users(page: int = 1, page_size: int = 20) -> Dict:
        """List users with pagination."""
        client = get_api_client()
        try:
            result = await client.get_users(
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
    async def create_user(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a user."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_user(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_user(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a user."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_user(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_user(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a user."""
        client = get_api_client()
        try:
            result = await client.delete_user(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_user_groups(page: int = 1, page_size: int = 20) -> Dict:
        """List user groups with pagination."""
        client = get_api_client()
        try:
            result = await client.get_user_groups(
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
    async def create_user_group(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a user group."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_user_group(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_user_group(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a user group."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_user_group(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_user_group(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a user group."""
        client = get_api_client()
        try:
            result = await client.delete_user_group(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_user_auth_servers(page: int = 1, page_size: int = 20) -> Dict:
        """List authentication servers with pagination."""
        client = get_api_client()
        try:
            result = await client.get_user_auth_servers(
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
    async def create_user_auth_server(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a authentication server."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_user_auth_server(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_user_auth_server(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a authentication server."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_user_auth_server(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_user_auth_server(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a authentication server."""
        client = get_api_client()
        try:
            result = await client.delete_user_auth_server(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_ipsec_apply_status() -> Dict:
        """Get IPsec apply status."""
        client = get_api_client()
        try:
            result = await client.get_ipsec_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_ipsec_apply() -> Dict:
        """Trigger IPsec apply."""
        client = get_api_client()
        try:
            result = await client.apply_ipsec_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_ipsec_phase1s(page: int = 1, page_size: int = 20) -> Dict:
        """List IPsec Phase 1s with pagination."""
        client = get_api_client()
        try:
            result = await client.get_ipsec_phase1s(
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
    async def create_ipsec_phase1(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a IPsec Phase 1."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_ipsec_phase1(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_ipsec_phase1(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a IPsec Phase 1."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_ipsec_phase1(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_ipsec_phase1(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a IPsec Phase 1."""
        client = get_api_client()
        try:
            result = await client.delete_ipsec_phase1(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_ipsec_phase1_encryptions(page: int = 1, page_size: int = 20) -> Dict:
        """List IPsec Phase 1 encryptions with pagination."""
        client = get_api_client()
        try:
            result = await client.get_ipsec_phase1_encryptions(
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
    async def create_ipsec_phase1_encryption(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a IPsec Phase 1 encryption."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_ipsec_phase1_encryption(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_ipsec_phase1_encryption(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a IPsec Phase 1 encryption."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_ipsec_phase1_encryption(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_ipsec_phase1_encryption(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a IPsec Phase 1 encryption."""
        client = get_api_client()
        try:
            result = await client.delete_ipsec_phase1_encryption(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_ipsec_phase2s(page: int = 1, page_size: int = 20) -> Dict:
        """List IPsec Phase 2s with pagination."""
        client = get_api_client()
        try:
            result = await client.get_ipsec_phase2s(
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
    async def create_ipsec_phase2(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a IPsec Phase 2."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_ipsec_phase2(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_ipsec_phase2(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a IPsec Phase 2."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_ipsec_phase2(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_ipsec_phase2(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a IPsec Phase 2."""
        client = get_api_client()
        try:
            result = await client.delete_ipsec_phase2(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_ipsec_phase2_encryptions(page: int = 1, page_size: int = 20) -> Dict:
        """List IPsec Phase 2 encryptions with pagination."""
        client = get_api_client()
        try:
            result = await client.get_ipsec_phase2_encryptions(
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
    async def create_ipsec_phase2_encryption(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a IPsec Phase 2 encryption."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_ipsec_phase2_encryption(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_ipsec_phase2_encryption(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a IPsec Phase 2 encryption."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_ipsec_phase2_encryption(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_ipsec_phase2_encryption(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a IPsec Phase 2 encryption."""
        client = get_api_client()
        try:
            result = await client.delete_ipsec_phase2_encryption(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_openvpn_servers(page: int = 1, page_size: int = 20) -> Dict:
        """List OpenVPN servers with pagination."""
        client = get_api_client()
        try:
            result = await client.get_openvpn_servers(
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
    async def create_openvpn_server(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a OpenVPN server."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_openvpn_server(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_openvpn_server(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a OpenVPN server."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_openvpn_server(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_openvpn_server(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a OpenVPN server."""
        client = get_api_client()
        try:
            result = await client.delete_openvpn_server(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_openvpn_clients(page: int = 1, page_size: int = 20) -> Dict:
        """List OpenVPN clients with pagination."""
        client = get_api_client()
        try:
            result = await client.get_openvpn_clients(
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
    async def create_openvpn_client(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a OpenVPN client."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_openvpn_client(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_openvpn_client(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a OpenVPN client."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_openvpn_client(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_openvpn_client(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a OpenVPN client."""
        client = get_api_client()
        try:
            result = await client.delete_openvpn_client(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_openvpn_csos(page: int = 1, page_size: int = 20) -> Dict:
        """List OpenVPN client-specific overrides with pagination."""
        client = get_api_client()
        try:
            result = await client.get_openvpn_csos(
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
    async def create_openvpn_cso(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a OpenVPN client-specific override."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_openvpn_cso(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_openvpn_cso(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a OpenVPN client-specific override."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_openvpn_cso(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_openvpn_cso(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a OpenVPN client-specific override."""
        client = get_api_client()
        try:
            result = await client.delete_openvpn_cso(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_wireguard_tunnels(page: int = 1, page_size: int = 20) -> Dict:
        """List WireGuard tunnels with pagination."""
        client = get_api_client()
        try:
            result = await client.get_wireguard_tunnels(
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
    async def create_wireguard_tunnel(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a WireGuard tunnel."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_wireguard_tunnel(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_wireguard_tunnel(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a WireGuard tunnel."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_wireguard_tunnel(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_wireguard_tunnel(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a WireGuard tunnel."""
        client = get_api_client()
        try:
            result = await client.delete_wireguard_tunnel(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_wireguard_tunnel_addresss(page: int = 1, page_size: int = 20) -> Dict:
        """List WireGuard tunnel addresss with pagination."""
        client = get_api_client()
        try:
            result = await client.get_wireguard_tunnel_addresss(
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
    async def create_wireguard_tunnel_address(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a WireGuard tunnel address."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_wireguard_tunnel_address(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_wireguard_tunnel_address(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a WireGuard tunnel address."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_wireguard_tunnel_address(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_wireguard_tunnel_address(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a WireGuard tunnel address."""
        client = get_api_client()
        try:
            result = await client.delete_wireguard_tunnel_address(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_wireguard_peers(page: int = 1, page_size: int = 20) -> Dict:
        """List WireGuard peers with pagination."""
        client = get_api_client()
        try:
            result = await client.get_wireguard_peers(
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
    async def create_wireguard_peer(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a WireGuard peer."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_wireguard_peer(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_wireguard_peer(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a WireGuard peer."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_wireguard_peer(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_wireguard_peer(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a WireGuard peer."""
        client = get_api_client()
        try:
            result = await client.delete_wireguard_peer(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_wireguard_peer_allowed_ips(page: int = 1, page_size: int = 20) -> Dict:
        """List WireGuard peer allowed IPs with pagination."""
        client = get_api_client()
        try:
            result = await client.get_wireguard_peer_allowed_ips(
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
    async def create_wireguard_peer_allowed_ip(data: Dict, apply_immediately: bool = True) -> Dict:
        """Create a WireGuard peer allowed IP."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.create_wireguard_peer_allowed_ip(data, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_wireguard_peer_allowed_ip(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
        """Update a WireGuard peer allowed IP."""
        client = get_api_client()
        try:
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            result = await client.update_wireguard_peer_allowed_ip(item_id, updates, control)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def delete_wireguard_peer_allowed_ip(item_id: int, apply_immediately: bool = True) -> Dict:
        """Delete a WireGuard peer allowed IP."""
        client = get_api_client()
        try:
            result = await client.delete_wireguard_peer_allowed_ip(item_id, apply_immediately)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_wireguard_apply_status() -> Dict:
        """Get WireGuard apply status."""
        client = get_api_client()
        try:
            result = await client.get_wireguard_apply_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def apply_wireguard_apply() -> Dict:
        """Trigger WireGuard apply."""
        client = get_api_client()
        try:
            result = await client.apply_wireguard_apply()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_wireguard_settings() -> Dict:
        """Get WireGuard settings."""
        client = get_api_client()
        try:
            result = await client.get_wireguard_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_wireguard_settings(updates: Dict) -> Dict:
        """Update WireGuard settings."""
        client = get_api_client()
        try:
            result = await client.update_wireguard_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_arp_table_entrys(page: int = 1, page_size: int = 20) -> Dict:
        """List ARP table entrys with pagination."""
        client = get_api_client()
        try:
            result = await client.get_arp_table_entrys(
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
    async def delete_all_arp_table_entrys() -> Dict:
        """Delete all ARP table entrys."""
        client = get_api_client()
        try:
            result = await client.delete_arp_table_entrys()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_config_history_revisions(page: int = 1, page_size: int = 20) -> Dict:
        """List config history revisions with pagination."""
        client = get_api_client()
        try:
            result = await client.get_config_history_revisions(
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
    async def delete_all_config_history_revisions() -> Dict:
        """Delete all config history revisions."""
        client = get_api_client()
        try:
            result = await client.delete_config_history_revisions()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def list_pf_tables(page: int = 1, page_size: int = 20) -> Dict:
        """List pf tables with pagination."""
        client = get_api_client()
        try:
            result = await client.get_pf_tables(
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
    async def delete_all_pf_tables() -> Dict:
        """Delete all pf tables."""
        client = get_api_client()
        try:
            result = await client.delete_pf_tables()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_carp_status() -> Dict:
        """Get CARP status."""
        client = get_api_client()
        try:
            result = await client.get_carp_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_carp_status(updates: Dict) -> Dict:
        """Update CARP status."""
        client = get_api_client()
        try:
            result = await client.update_carp_status(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_gateway_status() -> Dict:
        """Get gateway status."""
        client = get_api_client()
        try:
            result = await client.get_gateway_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_log_settings() -> Dict:
        """Get log settings."""
        client = get_api_client()
        try:
            result = await client.get_log_settings()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def update_log_settings(updates: Dict) -> Dict:
        """Update log settings."""
        client = get_api_client()
        try:
            result = await client.update_log_settings(updates)
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_openvpn_server_status() -> Dict:
        """Get OpenVPN server status."""
        client = get_api_client()
        try:
            result = await client.get_openvpn_server_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    @mcp.tool()
    async def get_ipsec_sa_status() -> Dict:
        """Get IPsec SA status."""
        client = get_api_client()
        try:
            result = await client.get_ipsec_sa_status()
            return {
                "success": True,
                "data": result.get("data", result),
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}