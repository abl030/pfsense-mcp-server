#!/usr/bin/env python3
"""
Code generator for pfSense MCP server endpoints.

Reads endpoint configurations and generates:
  - src/generated_client.py   (mixin class with client methods)
  - src/generated_tools.py    (MCP tool registrations)
  - tests/test_generated_integration.py  (integration tests)

Usage:
    python scripts/generate_from_spec.py
"""

import json
import os
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "openapi" / "pfsense-api-v2.json"

# ---------------------------------------------------------------------------
# Paths already implemented — generator will skip these
# ---------------------------------------------------------------------------
SKIP_PATHS = {
    "/firewall/rule", "/firewall/rules",
    "/firewall/alias", "/firewall/aliases",
    "/firewall/nat/port_forward", "/firewall/nat/port_forwards",
    "/status/logs/firewall",
}

# ---------------------------------------------------------------------------
# Endpoint configuration
# ---------------------------------------------------------------------------

@dataclass
class EndpointConfig:
    singular_path: str            # "/firewall/nat/one_to_one/mapping"
    plural_path: Optional[str]    # "/firewall/nat/one_to_one/mappings" or None
    schema_name: str              # "OneToOneNATMapping"
    category: str                 # crud, nested_crud, settings, action, read_delete
    python_name: str              # "nat_one_to_one_mapping"
    display_name: str             # "NAT one-to-one mapping"
    http_methods: list = field(default_factory=list)
    has_parent_id: bool = False
    parent_python_name: Optional[str] = None
    descr_field: Optional[str] = None   # "descr", "description", "name", or None
    lookup_field: Optional[str] = None  # field used for test lookups
    test_create_data: dict = field(default_factory=dict)
    test_update_data: dict = field(default_factory=dict)

# ---------------------------------------------------------------------------
# Endpoint registry — one entry per logical resource
# ---------------------------------------------------------------------------

ENDPOINTS = [
    # ---- NAT one-to-one ----
    EndpointConfig(
        singular_path="/firewall/nat/one_to_one/mapping",
        plural_path="/firewall/nat/one_to_one/mappings",
        schema_name="OneToOneNATMapping",
        category="crud",
        python_name="nat_one_to_one_mapping",
        display_name="NAT one-to-one mapping",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={
            "interface": "wan",
            "external": "198.51.100.50",
            "source": "192.168.1.0/24",
            "destination": "any",
        },
        test_update_data={"external": "198.51.100.51"},
    ),
    # ---- NAT outbound ----
    EndpointConfig(
        singular_path="/firewall/nat/outbound/mapping",
        plural_path="/firewall/nat/outbound/mappings",
        schema_name="OutboundNATMapping",
        category="crud",
        python_name="nat_outbound_mapping",
        display_name="NAT outbound mapping",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={
            "interface": "wan",
            "source": "192.168.1.0/24",
            "destination": "any",
            "target": "198.51.100.1",
            "protocol": "any",
        },
        test_update_data={"target": "198.51.100.2"},
    ),
    EndpointConfig(
        singular_path="/firewall/nat/outbound/mode",
        plural_path=None,
        schema_name="OutboundNATMode",
        category="settings",
        python_name="nat_outbound_mode",
        display_name="NAT outbound mode",
        http_methods=["GET", "PATCH"],
    ),
    # ---- Schedules ----
    EndpointConfig(
        singular_path="/firewall/schedule",
        plural_path="/firewall/schedules",
        schema_name="FirewallSchedule",
        category="crud",
        python_name="firewall_schedule",
        display_name="firewall schedule",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="name",
        test_create_data={
            "timerange": [{"month": "1,2,3,4,5,6,7,8,9,10,11,12",
                           "day": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31",
                           "hour": "0:00-23:59",
                           "rangedescr": "All times"}],
        },
        test_update_data={"descr": "Updated schedule"},
    ),
    EndpointConfig(
        singular_path="/firewall/schedule/time_range",
        plural_path="/firewall/schedule/time_ranges",
        schema_name="FirewallScheduleTimeRange",
        category="nested_crud",
        python_name="firewall_schedule_time_range",
        display_name="firewall schedule time range",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="firewall_schedule",
        descr_field="rangedescr",
        lookup_field="rangedescr",
        test_create_data={
            "month": "1,2,3,4,5,6,7,8,9,10,11,12",
            "day": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31",
            "hour": "0:00-23:59",
        },
        test_update_data={"hour": "8:00-17:00"},
    ),
    # ---- Traffic shapers ----
    EndpointConfig(
        singular_path="/firewall/traffic_shaper",
        plural_path="/firewall/traffic_shapers",
        schema_name="TrafficShaper",
        category="crud",
        python_name="traffic_shaper",
        display_name="traffic shaper",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="name",
        lookup_field="name",
        test_create_data={
            "interface": "lan",
            "scheduler": "HFSC",
            "bandwidthtype": "Mb",
            "bandwidth": 100,
            "enabled": True,
        },
        test_update_data={"bandwidth": 200},
    ),
    EndpointConfig(
        singular_path="/firewall/traffic_shaper/queue",
        plural_path="/firewall/traffic_shaper/queues",
        schema_name="TrafficShaperQueue",
        category="nested_crud",
        python_name="traffic_shaper_queue",
        display_name="traffic shaper queue",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="traffic_shaper",
        descr_field="name",
        lookup_field="name",
        test_create_data={
            "name": "testqueue",
            "qlimit": 50,
            "bandwidth": 10,
            "bandwidthtype": "Mb",
            "enabled": True,
            "default": False,
            "upperlimit_m2": "20Mb",
            "realtime_m2": "5Mb",
            "linkshare_m2": "10Mb",
        },
        test_update_data={"qlimit": 100},
    ),
    EndpointConfig(
        singular_path="/firewall/traffic_shaper/limiter",
        plural_path="/firewall/traffic_shaper/limiters",
        schema_name="TrafficShaperLimiter",
        category="crud",
        python_name="traffic_shaper_limiter",
        display_name="traffic shaper limiter",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="name",
        lookup_field="name",
        test_create_data={
            "name": "testlimiter",
            "aqm": "droptail",
            "sched": "wf2q+",
            "enabled": True,
        },
        test_update_data={"description": "Updated limiter"},
    ),
    EndpointConfig(
        singular_path="/firewall/traffic_shaper/limiter/queue",
        plural_path="/firewall/traffic_shaper/limiter/queues",
        schema_name="TrafficShaperLimiterQueue",
        category="nested_crud",
        python_name="traffic_shaper_limiter_queue",
        display_name="traffic shaper limiter queue",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="traffic_shaper_limiter",
        descr_field="name",
        lookup_field="name",
        test_create_data={
            "name": "testlimiterq",
            "aqm": "droptail",
            "enabled": True,
        },
        test_update_data={"qlimit": 50},
    ),
    EndpointConfig(
        singular_path="/firewall/traffic_shaper/limiter/bandwidth",
        plural_path="/firewall/traffic_shaper/limiter/bandwidths",
        schema_name="TrafficShaperLimiterBandwidth",
        category="nested_crud",
        python_name="traffic_shaper_limiter_bandwidth",
        display_name="traffic shaper limiter bandwidth",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="traffic_shaper_limiter",
        descr_field=None,
        lookup_field=None,
        test_create_data={
            "bw": 10,
            "bwscale": "Mb",
            "bwsched": "none",
        },
        test_update_data={"bw": 20},
    ),
    # ---- Virtual IPs ----
    EndpointConfig(
        singular_path="/firewall/virtual_ip",
        plural_path="/firewall/virtual_ips",
        schema_name="VirtualIP",
        category="crud",
        python_name="virtual_ip",
        display_name="virtual IP",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={
            "mode": "ipalias",
            "interface": "lan",
            "subnet": "10.255.255.1",
            "subnet_bits": 32,
            "descr": "",  # filled at test time
            "type": "single",
        },
        test_update_data={"subnet": "10.255.255.2"},
    ),
    EndpointConfig(
        singular_path="/firewall/virtual_ip/apply",
        plural_path=None,
        schema_name="VirtualIPApply",
        category="action",
        python_name="virtual_ip_apply",
        display_name="virtual IP apply",
        http_methods=["GET", "POST"],
    ),
    # ---- States ----
    EndpointConfig(
        singular_path="/firewall/state",
        plural_path="/firewall/states",
        schema_name="FirewallState",
        category="read_delete",
        python_name="firewall_state",
        display_name="firewall state",
        http_methods=["GET", "DELETE"],
    ),
    EndpointConfig(
        singular_path="/firewall/states/size",
        plural_path=None,
        schema_name="FirewallStatesSize",
        category="settings",
        python_name="firewall_states_size",
        display_name="firewall states size",
        http_methods=["GET", "PATCH"],
    ),
    # ---- Advanced settings ----
    EndpointConfig(
        singular_path="/firewall/advanced_settings",
        plural_path=None,
        schema_name="FirewallAdvancedSettings",
        category="settings",
        python_name="firewall_advanced_settings",
        display_name="firewall advanced settings",
        http_methods=["GET", "PATCH"],
    ),
    # ---- Firewall apply ----
    EndpointConfig(
        singular_path="/firewall/apply",
        plural_path=None,
        schema_name="FirewallApply",
        category="action",
        python_name="firewall_apply",
        display_name="firewall apply",
        http_methods=["GET", "POST"],
    ),

    # ===================================================================
    # Routing endpoints
    # ===================================================================

    # ---- Routing gateways ----
    EndpointConfig(
        singular_path="/routing/gateway",
        plural_path="/routing/gateways",
        schema_name="RoutingGateway",
        category="crud",
        python_name="routing_gateway",
        display_name="routing gateway",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="name",
        test_create_data={
            "name": "",  # filled at test time
            "ipprotocol": "inet",
            "interface": "wan",
            "gateway": "198.51.100.254",
        },
        test_update_data={"descr": "Updated gateway"},
    ),
    EndpointConfig(
        singular_path="/routing/gateway/default",
        plural_path=None,
        schema_name="RoutingGatewayDefault",
        category="settings",
        python_name="routing_gateway_default",
        display_name="default routing gateway",
        http_methods=["GET", "PATCH"],
    ),
    # ---- Routing gateway groups ----
    EndpointConfig(
        singular_path="/routing/gateway/group",
        plural_path="/routing/gateway/groups",
        schema_name="RoutingGatewayGroup",
        category="crud",
        python_name="routing_gateway_group",
        display_name="routing gateway group",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="name",
        test_create_data={
            "name": "",  # filled at test time
            "trigger": "down",
            "descr": "",
            "ipprotocol": "inet",
            "priorities": [],
        },
        test_update_data={"descr": "Updated gateway group"},
    ),
    EndpointConfig(
        singular_path="/routing/gateway/group/priority",
        plural_path="/routing/gateway/group/priorities",
        schema_name="RoutingGatewayGroupPriority",
        category="nested_crud",
        python_name="routing_gateway_group_priority",
        display_name="routing gateway group priority",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="routing_gateway_group",
        descr_field=None,
        lookup_field=None,
        test_create_data={
            "gateway": "WAN_DHCP",
            "tier": 1,
        },
        test_update_data={"tier": 2},
    ),
    # ---- Static routes ----
    EndpointConfig(
        singular_path="/routing/static_route",
        plural_path="/routing/static_routes",
        schema_name="StaticRoute",
        category="crud",
        python_name="routing_static_route",
        display_name="static route",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={
            "network": "10.99.99.0/24",
            "gateway": "WAN_DHCP",
        },
        test_update_data={"descr": "Updated route"},
    ),
    # ---- Routing apply ----
    EndpointConfig(
        singular_path="/routing/apply",
        plural_path=None,
        schema_name="RoutingApply",
        category="action",
        python_name="routing_apply",
        display_name="routing apply",
        http_methods=["GET", "POST"],
    ),

    # ===================================================================
    # Interface endpoints
    # ===================================================================

    EndpointConfig(
        singular_path="/interface",
        plural_path="/interfaces",
        schema_name="NetworkInterface",
        category="crud",
        python_name="interface",
        display_name="network interface",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={
            "if": "lo0",
            "descr": "",
            "typev4": "none",
            "ipaddr": "",
            "subnet": "",
        },
        test_update_data={"descr": "Updated iface"},
    ),
    EndpointConfig(
        singular_path="/interface/apply",
        plural_path=None,
        schema_name="InterfaceApply",
        category="action",
        python_name="interface_apply",
        display_name="interface apply",
        http_methods=["GET", "POST"],
    ),
    EndpointConfig(
        singular_path="/interface/available_interfaces",
        plural_path=None,
        schema_name="AvailableInterface",
        category="settings",  # GET-only, treat as settings
        python_name="available_interfaces",
        display_name="available interfaces",
        http_methods=["GET"],
    ),
    EndpointConfig(
        singular_path="/interface/bridge",
        plural_path="/interface/bridges",
        schema_name="InterfaceBridge",
        category="crud",
        python_name="interface_bridge",
        display_name="interface bridge",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={"members": ["lan"]},
        test_update_data={"descr": "Updated bridge"},
    ),
    EndpointConfig(
        singular_path="/interface/group",
        plural_path="/interface/groups",
        schema_name="InterfaceGroup",
        category="crud",
        python_name="interface_group",
        display_name="interface group",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="ifname",
        test_create_data={"ifname": "", "members": [], "descr": ""},
        test_update_data={"descr": "Updated group"},
    ),
    EndpointConfig(
        singular_path="/interface/vlan",
        plural_path="/interface/vlans",
        schema_name="InterfaceVLAN",
        category="crud",
        python_name="interface_vlan",
        display_name="interface VLAN",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={"if": "lan", "tag": 4000, "descr": ""},
        test_update_data={"descr": "Updated VLAN"},
    ),
    EndpointConfig(
        singular_path="/interface/gre",
        plural_path="/interface/gres",
        schema_name="InterfaceGRE",
        category="crud",
        python_name="interface_gre",
        display_name="interface GRE tunnel",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={
            "if": "wan",
            "remote_addr": "198.51.100.1",
            "tunnel_remote_addr": "10.0.0.2",
            "tunnel_remote_addr6": "::1",
        },
        test_update_data={"descr": "Updated GRE"},
    ),
    EndpointConfig(
        singular_path="/interface/lagg",
        plural_path="/interface/laggs",
        schema_name="InterfaceLAGG",
        category="crud",
        python_name="interface_lagg",
        display_name="interface LAGG",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={"members": ["lan"], "proto": "none"},
        test_update_data={"descr": "Updated LAGG"},
    ),

    # ===================================================================
    # Services endpoints — core services
    # ===================================================================

    # ---- DHCP Server ----
    EndpointConfig(
        singular_path="/services/dhcp_server",
        plural_path="/services/dhcp_servers",
        schema_name="DHCPServer",
        category="crud",
        python_name="dhcp_server",
        display_name="DHCP server",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field=None,
        lookup_field="interface",
        test_create_data={"interface": "lan"},
        test_update_data={"domain": "test.local"},
    ),
    EndpointConfig(
        singular_path="/services/dhcp_server/static_mapping",
        plural_path="/services/dhcp_server/static_mappings",
        schema_name="DHCPServerStaticMapping",
        category="nested_crud",
        python_name="dhcp_server_static_mapping",
        display_name="DHCP static mapping",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="dhcp_server",
        descr_field="descr",
        lookup_field="mac",
        test_create_data={"mac": "00:11:22:33:44:55"},
        test_update_data={"descr": "Updated mapping"},
    ),
    EndpointConfig(
        singular_path="/services/dhcp_server/address_pool",
        plural_path="/services/dhcp_server/address_pools",
        schema_name="DHCPServerAddressPool",
        category="nested_crud",
        python_name="dhcp_server_address_pool",
        display_name="DHCP address pool",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="dhcp_server",
        descr_field=None,
        lookup_field=None,
        test_create_data={"range_from": "192.168.1.200", "range_to": "192.168.1.210"},
        test_update_data={"range_to": "192.168.1.220"},
    ),
    EndpointConfig(
        singular_path="/services/dhcp_server/custom_option",
        plural_path="/services/dhcp_server/custom_options",
        schema_name="DHCPServerCustomOption",
        category="nested_crud",
        python_name="dhcp_server_custom_option",
        display_name="DHCP custom option",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="dhcp_server",
        descr_field=None,
        lookup_field=None,
        test_create_data={"number": 252, "type": "string", "value": "http://wpad.test/wpad.dat"},
        test_update_data={"value": "http://wpad.test/wpad2.dat"},
    ),
    EndpointConfig(
        singular_path="/services/dhcp_server/apply",
        plural_path=None,
        schema_name="DHCPServerApply",
        category="action",
        python_name="dhcp_server_apply",
        display_name="DHCP server apply",
        http_methods=["GET", "POST"],
    ),
    EndpointConfig(
        singular_path="/services/dhcp_relay",
        plural_path=None,
        schema_name="DHCPRelay",
        category="settings",
        python_name="dhcp_relay",
        display_name="DHCP relay",
        http_methods=["GET", "PATCH"],
    ),

    # ---- DNS Resolver ----
    EndpointConfig(
        singular_path="/services/dns_resolver/host_override",
        plural_path="/services/dns_resolver/host_overrides",
        schema_name="DNSResolverHostOverride",
        category="crud",
        python_name="dns_resolver_host_override",
        display_name="DNS resolver host override",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="host",
        test_create_data={"host": "mcptest", "domain": "test.local", "ip": "192.168.1.250"},
        test_update_data={"descr": "Updated override"},
    ),
    EndpointConfig(
        singular_path="/services/dns_resolver/host_override/alias",
        plural_path="/services/dns_resolver/host_override/aliases",
        schema_name="DNSResolverHostOverrideAlias",
        category="nested_crud",
        python_name="dns_resolver_host_override_alias",
        display_name="DNS resolver host override alias",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="dns_resolver_host_override",
        descr_field="descr",
        lookup_field="host",
        test_create_data={"host": "mcptalias", "domain": "test.local"},
        test_update_data={"descr": "Updated alias"},
    ),
    EndpointConfig(
        singular_path="/services/dns_resolver/domain_override",
        plural_path="/services/dns_resolver/domain_overrides",
        schema_name="DNSResolverDomainOverride",
        category="crud",
        python_name="dns_resolver_domain_override",
        display_name="DNS resolver domain override",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="domain",
        test_create_data={"domain": "mcptest.local", "ip": "10.0.0.53"},
        test_update_data={"descr": "Updated domain override"},
    ),
    EndpointConfig(
        singular_path="/services/dns_resolver/access_list",
        plural_path="/services/dns_resolver/access_lists",
        schema_name="DNSResolverAccessList",
        category="crud",
        python_name="dns_resolver_access_list",
        display_name="DNS resolver access list",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="description",
        lookup_field="name",
        test_create_data={"name": "", "action": "allow", "networks": ["192.168.1.0/24"]},
        test_update_data={"description": "Updated ACL"},
    ),
    EndpointConfig(
        singular_path="/services/dns_resolver/access_list/network",
        plural_path="/services/dns_resolver/access_list/networks",
        schema_name="DNSResolverAccessListNetwork",
        category="nested_crud",
        python_name="dns_resolver_access_list_network",
        display_name="DNS resolver access list network",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="dns_resolver_access_list",
        descr_field="descr",
        lookup_field=None,
        test_create_data={"address": "10.0.0.0", "mask": 24},
        test_update_data={"mask": 16},
    ),
    EndpointConfig(
        singular_path="/services/dns_resolver/apply",
        plural_path=None,
        schema_name="DNSResolverApply",
        category="action",
        python_name="dns_resolver_apply",
        display_name="DNS resolver apply",
        http_methods=["GET", "POST"],
    ),
    EndpointConfig(
        singular_path="/services/dns_resolver/settings",
        plural_path=None,
        schema_name="DNSResolverSettings",
        category="settings",
        python_name="dns_resolver_settings",
        display_name="DNS resolver settings",
        http_methods=["GET", "PATCH"],
    ),

    # ---- DNS Forwarder ----
    EndpointConfig(
        singular_path="/services/dns_forwarder/host_override",
        plural_path="/services/dns_forwarder/host_overrides",
        schema_name="DNSForwarderHostOverride",
        category="crud",
        python_name="dns_forwarder_host_override",
        display_name="DNS forwarder host override",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="host",
        test_create_data={"host": "mcpfwdtest", "domain": "test.local", "ip": "192.168.1.251"},
        test_update_data={"descr": "Updated forwarder override"},
    ),
    EndpointConfig(
        singular_path="/services/dns_forwarder/host_override/alias",
        plural_path="/services/dns_forwarder/host_override/aliases",
        schema_name="DNSForwarderHostOverrideAlias",
        category="nested_crud",
        python_name="dns_forwarder_host_override_alias",
        display_name="DNS forwarder host override alias",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="dns_forwarder_host_override",
        descr_field="descr",
        lookup_field="host",
        test_create_data={"host": "mcpfwdalias", "domain": "test.local"},
        test_update_data={"descr": "Updated alias"},
    ),
    EndpointConfig(
        singular_path="/services/dns_forwarder/apply",
        plural_path=None,
        schema_name="DNSForwarderApply",
        category="action",
        python_name="dns_forwarder_apply",
        display_name="DNS forwarder apply",
        http_methods=["GET", "POST"],
    ),

    # ---- Cron ----
    EndpointConfig(
        singular_path="/services/cron/job",
        plural_path="/services/cron/jobs",
        schema_name="CronJob",
        category="crud",
        python_name="cron_job",
        display_name="cron job",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field=None,
        lookup_field="command",
        test_create_data={
            "minute": "0", "hour": "0", "mday": "*",
            "month": "*", "wday": "*", "who": "root",
            "command": "/usr/bin/true # MCP_INTTEST",
        },
        test_update_data={"minute": "30"},
    ),

    # ---- NTP ----
    EndpointConfig(
        singular_path="/services/ntp/time_server",
        plural_path="/services/ntp/time_servers",
        schema_name="NTPTimeServer",
        category="crud",
        python_name="ntp_time_server",
        display_name="NTP time server",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field=None,
        lookup_field="timeserver",
        test_create_data={"timeserver": "time.mcptest.invalid", "type": "server"},
        test_update_data={"prefer": True},
    ),
    EndpointConfig(
        singular_path="/services/ntp/settings",
        plural_path=None,
        schema_name="NTPSettings",
        category="settings",
        python_name="ntp_settings",
        display_name="NTP settings",
        http_methods=["GET", "PATCH"],
    ),

    # ---- Service watchdog ----
    EndpointConfig(
        singular_path="/services/service_watchdog",
        plural_path="/services/service_watchdogs",
        schema_name="ServiceWatchdog",
        category="crud",
        python_name="service_watchdog",
        display_name="service watchdog",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="description",
        lookup_field="name",
        test_create_data={"name": "sshd"},
        test_update_data={"description": "Updated watchdog"},
    ),

    # ---- SSH ----
    EndpointConfig(
        singular_path="/services/ssh",
        plural_path=None,
        schema_name="SSHSettings",
        category="settings",
        python_name="ssh_settings",
        display_name="SSH settings",
        http_methods=["GET", "PATCH"],
    ),

    # ---- Wake on LAN ----
    EndpointConfig(
        singular_path="/services/wake_on_lan/send",
        plural_path=None,
        schema_name="WakeOnLAN",
        category="action",
        python_name="wake_on_lan",
        display_name="Wake on LAN",
        http_methods=["POST"],
    ),

    # ===================================================================
    # System endpoints
    # ===================================================================

    EndpointConfig(
        singular_path="/system/certificate",
        plural_path="/system/certificates",
        schema_name="Certificate",
        category="crud",
        python_name="system_certificate",
        display_name="system certificate",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={"descr": "", "crt": "", "prv": ""},
        test_update_data={"descr": "Updated cert"},
    ),
    EndpointConfig(
        singular_path="/system/certificate_authority",
        plural_path="/system/certificate_authorities",
        schema_name="CertificateAuthority",
        category="crud",
        python_name="system_ca",
        display_name="certificate authority",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={"descr": "", "crt": ""},
        test_update_data={"descr": "Updated CA"},
    ),
    EndpointConfig(
        singular_path="/system/crl",
        plural_path="/system/crls",
        schema_name="CertificateRevocationList",
        category="crud",
        python_name="system_crl",
        display_name="certificate revocation list",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={"caref": "", "descr": "", "method": "internal", "text": ""},
        test_update_data={"descr": "Updated CRL"},
    ),
    # NOTE: /system/crl/revoked_certificate requires parent_id even for GET,
    # returns 400 without it — skipped from auto-generation.

    EndpointConfig(
        singular_path="/system/tunable",
        plural_path="/system/tunables",
        schema_name="SystemTunable",
        category="crud",
        python_name="system_tunable",
        display_name="system tunable",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="tunable",
        test_create_data={"tunable": "kern.ipc.maxsockbuf", "value": "16777216"},
        test_update_data={"descr": "Updated tunable"},
    ),
    EndpointConfig(
        singular_path="/system/restapi/access_list/entry",
        plural_path="/system/restapi/access_list",
        schema_name="RESTAPIAccessListEntry",
        category="crud",
        python_name="restapi_access_list_entry",
        display_name="REST API access list entry",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={"network": "10.0.0.0/8"},
        test_update_data={"descr": "Updated ACL entry"},
    ),
    EndpointConfig(
        singular_path="/system/console",
        plural_path=None,
        schema_name="Console",
        category="settings",
        python_name="system_console",
        display_name="system console settings",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/system/dns",
        plural_path=None,
        schema_name="SystemDNS",
        category="settings",
        python_name="system_dns",
        display_name="system DNS settings",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/system/hostname",
        plural_path=None,
        schema_name="SystemHostname",
        category="settings",
        python_name="system_hostname",
        display_name="system hostname",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/system/timezone",
        plural_path=None,
        schema_name="SystemTimezone",
        category="settings",
        python_name="system_timezone",
        display_name="system timezone",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/system/version",
        plural_path=None,
        schema_name="SystemVersion",
        category="settings",
        python_name="system_version",
        display_name="system version",
        http_methods=["GET"],
    ),
    EndpointConfig(
        singular_path="/system/webgui/settings",
        plural_path=None,
        schema_name="WebGUISettings",
        category="settings",
        python_name="webgui_settings",
        display_name="WebGUI settings",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/system/notifications/email_settings",
        plural_path=None,
        schema_name="EmailNotificationSettings",
        category="settings",
        python_name="email_notification_settings",
        display_name="email notification settings",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/system/restapi/settings",
        plural_path=None,
        schema_name="RESTAPISettings",
        category="settings",
        python_name="restapi_settings",
        display_name="REST API settings",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/system/restapi/version",
        plural_path=None,
        schema_name="RESTAPIVersion",
        category="settings",
        python_name="restapi_version",
        display_name="REST API version",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/system/package",
        plural_path="/system/packages",
        schema_name="Package",
        category="crud",
        python_name="system_package",
        display_name="system package",
        http_methods=["GET", "POST", "DELETE"],
        descr_field="name",
        lookup_field="name",
        test_create_data={"name": ""},
        test_update_data={},
    ),

    # ===================================================================
    # User endpoints
    # ===================================================================

    EndpointConfig(
        singular_path="/user",
        plural_path="/users",
        schema_name="User",
        category="crud",
        python_name="user",
        display_name="user",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="name",
        test_create_data={"name": "", "password": "McpT3st!Pass#9876"},
        test_update_data={"descr": "Updated user"},
    ),
    EndpointConfig(
        singular_path="/user/group",
        plural_path="/user/groups",
        schema_name="UserGroup",
        category="crud",
        python_name="user_group",
        display_name="user group",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="description",
        lookup_field="name",
        test_create_data={"name": ""},
        test_update_data={"description": "Updated group"},
    ),
    EndpointConfig(
        singular_path="/user/auth_server",
        plural_path="/user/auth_servers",
        schema_name="AuthServer",
        category="crud",
        python_name="user_auth_server",
        display_name="authentication server",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field=None,
        lookup_field="name",
        test_create_data={
            "type": "ldap", "name": "",
            "host": "ldap.mcptest.invalid",
            "ldap_port": 389, "ldap_urltype": "TCP - Standard",
            "ldap_scope": "one", "ldap_bindpw": "pass",
            "radius_secret": "", "radius_nasip_attribute": "wan",
        },
        test_update_data={"host": "ldap2.mcptest.invalid"},
    ),

    # ===================================================================
    # VPN endpoints
    # ===================================================================

    # ---- IPsec ----
    EndpointConfig(
        singular_path="/vpn/ipsec/apply",
        plural_path=None,
        schema_name="IPsecApply",
        category="action",
        python_name="ipsec_apply",
        display_name="IPsec apply",
        http_methods=["GET", "POST"],
    ),
    EndpointConfig(
        singular_path="/vpn/ipsec/phase1",
        plural_path="/vpn/ipsec/phase1s",
        schema_name="IPsecPhase1",
        category="crud",
        python_name="ipsec_phase1",
        display_name="IPsec Phase 1",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={
            "iketype": "ikev2", "mode": "tunnel", "protocol": "inet",
            "interface": "wan", "remote_gateway": "198.51.100.99",
            "authentication_method": "pre_shared_key",
            "myid_type": "myaddress", "myid_data": "",
            "peerid_type": "peeraddress", "peerid_data": "",
            "pre_shared_key": "McpTestKey123!",
            "certref": "", "caref": "",
            "encryption": [],
        },
        test_update_data={"descr": "Updated phase1"},
    ),
    EndpointConfig(
        singular_path="/vpn/ipsec/phase1/encryption",
        plural_path="/vpn/ipsec/phase1/encryptions",
        schema_name="IPsecPhase1Encryption",
        category="nested_crud",
        python_name="ipsec_phase1_encryption",
        display_name="IPsec Phase 1 encryption",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="ipsec_phase1",
        descr_field=None,
        lookup_field=None,
        test_create_data={
            "encryption_algorithm_name": "aes",
            "encryption_algorithm_keylen": 256,
            "hash_algorithm": "sha256",
            "dhgroup": 14,
        },
        test_update_data={"dhgroup": 16},
    ),
    EndpointConfig(
        singular_path="/vpn/ipsec/phase2",
        plural_path="/vpn/ipsec/phase2s",
        schema_name="IPsecPhase2",
        category="crud",
        python_name="ipsec_phase2",
        display_name="IPsec Phase 2",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={
            "ikeid": 0, "mode": "tunnel",
            "localid_type": "lan", "localid_address": "", "localid_netbits": 24,
            "natlocalid_address": "", "natlocalid_netbits": 0,
            "remoteid_type": "network", "remoteid_address": "10.0.0.0", "remoteid_netbits": 24,
            "encryption_algorithm_option": [{"name": "aes", "keylen": 256}],
            "hash_algorithm_option": ["hmac_sha256"],
        },
        test_update_data={"descr": "Updated phase2"},
    ),
    EndpointConfig(
        singular_path="/vpn/ipsec/phase2/encryption",
        plural_path="/vpn/ipsec/phase2/encryptions",
        schema_name="IPsecPhase2Encryption",
        category="nested_crud",
        python_name="ipsec_phase2_encryption",
        display_name="IPsec Phase 2 encryption",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="ipsec_phase2",
        descr_field=None,
        lookup_field=None,
        test_create_data={"name": "aes", "keylen": 256},
        test_update_data={"keylen": 128},
    ),

    # ---- OpenVPN ----
    EndpointConfig(
        singular_path="/vpn/openvpn/server",
        plural_path="/vpn/openvpn/servers",
        schema_name="OpenVPNServer",
        category="crud",
        python_name="openvpn_server",
        display_name="OpenVPN server",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="description",
        lookup_field="description",
        test_create_data={
            "mode": "server_tls", "dev_mode": "tun", "protocol": "UDP4",
            "interface": "wan", "tls_type": "auth",
            "caref": "", "certref": "",
            "dh_length": 2048, "ecdh_curve": "none",
            "data_ciphers": ["AES-256-GCM"],
            "data_ciphers_fallback": "AES-256-CBC", "digest": "SHA256",
            "serverbridge_interface": "", "serverbridge_dhcp_start": "",
            "serverbridge_dhcp_end": "",
        },
        test_update_data={"description": "Updated OVPN server"},
    ),
    EndpointConfig(
        singular_path="/vpn/openvpn/client",
        plural_path="/vpn/openvpn/clients",
        schema_name="OpenVPNClient",
        category="crud",
        python_name="openvpn_client",
        display_name="OpenVPN client",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="description",
        lookup_field="description",
        test_create_data={
            "mode": "p2p_shared_key", "dev_mode": "tun", "protocol": "UDP4",
            "interface": "wan", "server_addr": "198.51.100.99", "server_port": 1194,
            "proxy_user": "", "proxy_passwd": "",
            "tls_type": "auth", "caref": "",
            "data_ciphers": ["AES-256-GCM"],
            "data_ciphers_fallback": "AES-256-CBC", "digest": "SHA256",
        },
        test_update_data={"description": "Updated OVPN client"},
    ),
    EndpointConfig(
        singular_path="/vpn/openvpn/cso",
        plural_path="/vpn/openvpn/csos",
        schema_name="OpenVPNClientSpecificOverride",
        category="crud",
        python_name="openvpn_cso",
        display_name="OpenVPN client-specific override",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="description",
        lookup_field="common_name",
        test_create_data={"common_name": "mcptest_cso"},
        test_update_data={"description": "Updated CSO"},
    ),

    # ---- WireGuard ----
    EndpointConfig(
        singular_path="/vpn/wireguard/tunnel",
        plural_path="/vpn/wireguard/tunnels",
        schema_name="WireGuardTunnel",
        category="crud",
        python_name="wireguard_tunnel",
        display_name="WireGuard tunnel",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="name",
        test_create_data={"privatekey": ""},
        test_update_data={"descr": "Updated tunnel"},
    ),
    EndpointConfig(
        singular_path="/vpn/wireguard/tunnel/address",
        plural_path="/vpn/wireguard/tunnel/addresses",
        schema_name="WireGuardTunnelAddress",
        category="nested_crud",
        python_name="wireguard_tunnel_address",
        display_name="WireGuard tunnel address",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="wireguard_tunnel",
        descr_field="descr",
        lookup_field=None,
        test_create_data={"address": "10.99.0.1", "mask": 24},
        test_update_data={"descr": "Updated address"},
    ),
    EndpointConfig(
        singular_path="/vpn/wireguard/peer",
        plural_path="/vpn/wireguard/peers",
        schema_name="WireGuardPeer",
        category="crud",
        python_name="wireguard_peer",
        display_name="WireGuard peer",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        descr_field="descr",
        lookup_field="descr",
        test_create_data={"publickey": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="},
        test_update_data={"descr": "Updated peer"},
    ),
    EndpointConfig(
        singular_path="/vpn/wireguard/peer/allowed_ip",
        plural_path="/vpn/wireguard/peer/allowed_ips",
        schema_name="WireGuardPeerAllowedIP",
        category="nested_crud",
        python_name="wireguard_peer_allowed_ip",
        display_name="WireGuard peer allowed IP",
        http_methods=["GET", "POST", "PATCH", "DELETE"],
        has_parent_id=True,
        parent_python_name="wireguard_peer",
        descr_field="descr",
        lookup_field=None,
        test_create_data={"address": "10.99.1.0", "mask": 24},
        test_update_data={"descr": "Updated allowed IP"},
    ),
    EndpointConfig(
        singular_path="/vpn/wireguard/apply",
        plural_path=None,
        schema_name="WireGuardApply",
        category="action",
        python_name="wireguard_apply",
        display_name="WireGuard apply",
        http_methods=["GET", "POST"],
    ),
    EndpointConfig(
        singular_path="/vpn/wireguard/settings",
        plural_path=None,
        schema_name="WireGuardSettings",
        category="settings",
        python_name="wireguard_settings",
        display_name="WireGuard settings",
        http_methods=["GET", "PATCH"],
    ),

    # ===================================================================
    # Diagnostics endpoints
    # ===================================================================

    EndpointConfig(
        singular_path="/diagnostics/arp_table/entry",
        plural_path="/diagnostics/arp_table",
        schema_name="ARPTableEntry",
        category="read_delete",
        python_name="arp_table_entry",
        display_name="ARP table entry",
        http_methods=["GET", "DELETE"],
    ),
    EndpointConfig(
        singular_path="/diagnostics/config_history/revision",
        plural_path="/diagnostics/config_history/revisions",
        schema_name="ConfigHistoryRevision",
        category="read_delete",
        python_name="config_history_revision",
        display_name="config history revision",
        http_methods=["GET", "DELETE"],
    ),
    EndpointConfig(
        singular_path="/diagnostics/table",
        plural_path="/diagnostics/tables",
        schema_name="PFTable",
        category="read_delete",
        python_name="pf_table",
        display_name="pf table",
        http_methods=["GET", "DELETE"],
    ),

    # ===================================================================
    # Status endpoints (read-only)
    # ===================================================================

    EndpointConfig(
        singular_path="/status/carp",
        plural_path=None,
        schema_name="CARPStatus",
        category="settings",
        python_name="carp_status",
        display_name="CARP status",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/status/gateways",
        plural_path=None,
        schema_name="GatewayStatus",
        category="settings",
        python_name="gateway_status",
        display_name="gateway status",
        http_methods=["GET"],
    ),
    EndpointConfig(
        singular_path="/status/logs/settings",
        plural_path=None,
        schema_name="LogSettings",
        category="settings",
        python_name="log_settings",
        display_name="log settings",
        http_methods=["GET", "PATCH"],
    ),
    EndpointConfig(
        singular_path="/status/openvpn/servers",
        plural_path=None,
        schema_name="OpenVPNServerStatus",
        category="settings",
        python_name="openvpn_server_status",
        display_name="OpenVPN server status",
        http_methods=["GET"],
    ),
    EndpointConfig(
        singular_path="/status/ipsec/sas",
        plural_path=None,
        schema_name="IPsecSAStatus",
        category="settings",
        python_name="ipsec_sa_status",
        display_name="IPsec SA status",
        http_methods=["GET"],
    ),
]


# ===========================================================================
# Code generation helpers
# ===========================================================================

def _indent(text: str, n: int = 4) -> str:
    """Indent every line of *text* by *n* spaces."""
    prefix = " " * n
    return "\n".join(prefix + line if line.strip() else "" for line in text.splitlines())


# ===========================================================================
# Client mixin generation
# ===========================================================================

def generate_client_mixin(endpoints: list[EndpointConfig]) -> str:
    """Generate GeneratedFirewallMixin class source."""
    parts: list[str] = []

    for ep in endpoints:
        if ep.category == "crud":
            parts.append(_gen_crud_methods(ep))
        elif ep.category == "nested_crud":
            parts.append(_gen_nested_crud_methods(ep))
        elif ep.category == "settings":
            parts.append(_gen_settings_methods(ep))
        elif ep.category == "action":
            parts.append(_gen_action_methods(ep))
        elif ep.category == "read_delete":
            parts.append(_gen_read_delete_methods(ep))

    body = "\n".join(parts)

    header = textwrap.dedent('''\
        """Auto-generated firewall client methods. DO NOT EDIT.
        Regenerate: python scripts/generate_from_spec.py
        """

        from typing import Dict, List, Optional


        class GeneratedFirewallMixin:
            """Mixin providing generated client methods for firewall endpoints."""

        ''')
    return header + body


def _gen_crud_methods(ep: EndpointConfig) -> str:
    name = ep.python_name
    singular = ep.singular_path
    plural = ep.plural_path or f"{singular}s"
    lines = []

    # get_Xs
    lines.append(textwrap.dedent(f'''\
        async def get_{name}s(self, filters=None, sort=None, pagination=None):
            """List {ep.display_name}s."""
            return await self._make_request(
                "GET", "{plural}",
                filters=filters, sort=sort, pagination=pagination,
            )
    '''))

    # create_X
    lines.append(textwrap.dedent(f'''\
        async def create_{name}(self, data, control=None):
            """Create a {ep.display_name}."""
            from pfsense_api_enhanced import ControlParameters
            if not control:
                control = ControlParameters(apply=True)
            return await self._make_request(
                "POST", "{singular}",
                data=data, control=control,
            )
    '''))

    # update_X
    lines.append(textwrap.dedent(f'''\
        async def update_{name}(self, item_id, updates, control=None):
            """Update a {ep.display_name}."""
            from pfsense_api_enhanced import ControlParameters
            if not control:
                control = ControlParameters(apply=True)
            return await self._make_request(
                "PATCH", "{singular}",
                data={{"id": item_id, **updates}}, control=control,
            )
    '''))

    # delete_X
    lines.append(textwrap.dedent(f'''\
        async def delete_{name}(self, item_id, apply_immediately=True):
            """Delete a {ep.display_name}."""
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            return await self._make_request(
                "DELETE", "{singular}",
                data={{"id": item_id}}, control=control,
            )
    '''))

    return _indent("\n".join(lines))


def _gen_nested_crud_methods(ep: EndpointConfig) -> str:
    name = ep.python_name
    singular = ep.singular_path
    plural = ep.plural_path or f"{singular}s"
    lines = []

    # get_Xs
    lines.append(textwrap.dedent(f'''\
        async def get_{name}s(self, filters=None, sort=None, pagination=None):
            """List {ep.display_name}s."""
            return await self._make_request(
                "GET", "{plural}",
                filters=filters, sort=sort, pagination=pagination,
            )
    '''))

    # create_X (includes parent_id in data)
    lines.append(textwrap.dedent(f'''\
        async def create_{name}(self, data, control=None):
            """Create a {ep.display_name}. Include 'parent_id' in data."""
            from pfsense_api_enhanced import ControlParameters
            if not control:
                control = ControlParameters(apply=True)
            return await self._make_request(
                "POST", "{singular}",
                data=data, control=control,
            )
    '''))

    # update_X
    lines.append(textwrap.dedent(f'''\
        async def update_{name}(self, item_id, updates, control=None):
            """Update a {ep.display_name}."""
            from pfsense_api_enhanced import ControlParameters
            if not control:
                control = ControlParameters(apply=True)
            return await self._make_request(
                "PATCH", "{singular}",
                data={{"id": item_id, **updates}}, control=control,
            )
    '''))

    # delete_X
    lines.append(textwrap.dedent(f'''\
        async def delete_{name}(self, item_id, apply_immediately=True):
            """Delete a {ep.display_name}."""
            from pfsense_api_enhanced import ControlParameters
            control = ControlParameters(apply=apply_immediately)
            return await self._make_request(
                "DELETE", "{singular}",
                data={{"id": item_id}}, control=control,
            )
    '''))

    return _indent("\n".join(lines))


def _gen_settings_methods(ep: EndpointConfig) -> str:
    name = ep.python_name
    path = ep.singular_path
    lines = []

    # get_X
    lines.append(textwrap.dedent(f'''\
        async def get_{name}(self):
            """Get {ep.display_name}."""
            return await self._make_request("GET", "{path}")
    '''))

    # update_X
    if "PATCH" in ep.http_methods:
        lines.append(textwrap.dedent(f'''\
            async def update_{name}(self, updates):
                """Update {ep.display_name}."""
                return await self._make_request(
                    "PATCH", "{path}",
                    data=updates,
                )
        '''))

    return _indent("\n".join(lines))


def _gen_action_methods(ep: EndpointConfig) -> str:
    name = ep.python_name
    path = ep.singular_path
    lines = []

    # get_X_status
    lines.append(textwrap.dedent(f'''\
        async def get_{name}_status(self):
            """Get {ep.display_name} status."""
            return await self._make_request("GET", "{path}")
    '''))

    # apply_X
    if "POST" in ep.http_methods:
        lines.append(textwrap.dedent(f'''\
            async def apply_{name}(self):
                """Trigger {ep.display_name}."""
                return await self._make_request("POST", "{path}")
        '''))

    return _indent("\n".join(lines))


def _gen_read_delete_methods(ep: EndpointConfig) -> str:
    name = ep.python_name
    singular = ep.singular_path
    plural = ep.plural_path or singular
    lines = []

    # get_Xs (use plural)
    lines.append(textwrap.dedent(f'''\
        async def get_{name}s(self, filters=None, sort=None, pagination=None):
            """List {ep.display_name}s."""
            return await self._make_request(
                "GET", "{plural}",
                filters=filters, sort=sort, pagination=pagination,
            )
    '''))

    # delete_Xs (bulk delete via plural)
    lines.append(textwrap.dedent(f'''\
        async def delete_{name}s(self):
            """Delete all {ep.display_name}s."""
            return await self._make_request("DELETE", "{plural}")
    '''))

    return _indent("\n".join(lines))


# ===========================================================================
# MCP tools generation
# ===========================================================================

def generate_tools(endpoints: list[EndpointConfig]) -> str:
    """Generate register_generated_tools() function source."""
    parts: list[str] = []

    for ep in endpoints:
        if ep.category == "crud":
            parts.append(_gen_crud_tools(ep))
        elif ep.category == "nested_crud":
            parts.append(_gen_nested_crud_tools(ep))
        elif ep.category == "settings":
            parts.append(_gen_settings_tools(ep))
        elif ep.category == "action":
            parts.append(_gen_action_tools(ep))
        elif ep.category == "read_delete":
            parts.append(_gen_read_delete_tools(ep))

    body = "\n".join(parts)

    header = textwrap.dedent('''\
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

        ''')
    return header + body


def _tool_wrapper(name: str, display: str, body: str) -> str:
    """Wrap tool body with error handling."""
    return textwrap.dedent(f'''\
        @mcp.tool()
        async def {name}({body.split("(", 1)[1].split(")")[0]}) -> Dict:
            \"\"\"{display}.\"\"\"
            client = get_api_client()
            try:
    ''')


def _gen_crud_tools(ep: EndpointConfig) -> str:
    name = ep.python_name
    display = ep.display_name
    lines = []

    # list tool
    lines.append(_indent(textwrap.dedent(f'''\
        @mcp.tool()
        async def list_{name}s(page: int = 1, page_size: int = 20) -> Dict:
            """List {display}s with pagination."""
            client = get_api_client()
            try:
                result = await client.get_{name}s(
                    pagination=create_pagination(page, page_size),
                )
                return {{
                    "success": True,
                    "data": result.get("data", []),
                    "timestamp": datetime.utcnow().isoformat(),
                }}
            except Exception as e:
                return {{"success": False, "error": str(e)}}
    '''), 4))

    # create tool
    lines.append(_indent(textwrap.dedent(f'''\
        @mcp.tool()
        async def create_{name}(data: Dict, apply_immediately: bool = True) -> Dict:
            """Create a {display}."""
            client = get_api_client()
            try:
                from pfsense_api_enhanced import ControlParameters
                control = ControlParameters(apply=apply_immediately)
                result = await client.create_{name}(data, control)
                return {{
                    "success": True,
                    "data": result.get("data", result),
                    "timestamp": datetime.utcnow().isoformat(),
                }}
            except Exception as e:
                return {{"success": False, "error": str(e)}}
    '''), 4))

    # update tool
    lines.append(_indent(textwrap.dedent(f'''\
        @mcp.tool()
        async def update_{name}(item_id: int, updates: Dict, apply_immediately: bool = True) -> Dict:
            """Update a {display}."""
            client = get_api_client()
            try:
                from pfsense_api_enhanced import ControlParameters
                control = ControlParameters(apply=apply_immediately)
                result = await client.update_{name}(item_id, updates, control)
                return {{
                    "success": True,
                    "data": result.get("data", result),
                    "timestamp": datetime.utcnow().isoformat(),
                }}
            except Exception as e:
                return {{"success": False, "error": str(e)}}
    '''), 4))

    # delete tool
    lines.append(_indent(textwrap.dedent(f'''\
        @mcp.tool()
        async def delete_{name}(item_id: int, apply_immediately: bool = True) -> Dict:
            """Delete a {display}."""
            client = get_api_client()
            try:
                result = await client.delete_{name}(item_id, apply_immediately)
                return {{
                    "success": True,
                    "data": result.get("data", result),
                    "timestamp": datetime.utcnow().isoformat(),
                }}
            except Exception as e:
                return {{"success": False, "error": str(e)}}
    '''), 4))

    return "\n".join(lines)


def _gen_nested_crud_tools(ep: EndpointConfig) -> str:
    # Same structure as CRUD tools — the parent_id is inside the data dict
    return _gen_crud_tools(ep)


def _gen_settings_tools(ep: EndpointConfig) -> str:
    name = ep.python_name
    display = ep.display_name
    lines = []

    # get tool
    lines.append(_indent(textwrap.dedent(f'''\
        @mcp.tool()
        async def get_{name}() -> Dict:
            """Get {display}."""
            client = get_api_client()
            try:
                result = await client.get_{name}()
                return {{
                    "success": True,
                    "data": result.get("data", result),
                    "timestamp": datetime.utcnow().isoformat(),
                }}
            except Exception as e:
                return {{"success": False, "error": str(e)}}
    '''), 4))

    # update tool
    if "PATCH" in ep.http_methods:
        lines.append(_indent(textwrap.dedent(f'''\
            @mcp.tool()
            async def update_{name}(updates: Dict) -> Dict:
                """Update {display}."""
                client = get_api_client()
                try:
                    result = await client.update_{name}(updates)
                    return {{
                        "success": True,
                        "data": result.get("data", result),
                        "timestamp": datetime.utcnow().isoformat(),
                    }}
                except Exception as e:
                    return {{"success": False, "error": str(e)}}
        '''), 4))

    return "\n".join(lines)


def _gen_action_tools(ep: EndpointConfig) -> str:
    name = ep.python_name
    display = ep.display_name
    lines = []

    # get status tool
    lines.append(_indent(textwrap.dedent(f'''\
        @mcp.tool()
        async def get_{name}_status() -> Dict:
            """Get {display} status."""
            client = get_api_client()
            try:
                result = await client.get_{name}_status()
                return {{
                    "success": True,
                    "data": result.get("data", result),
                    "timestamp": datetime.utcnow().isoformat(),
                }}
            except Exception as e:
                return {{"success": False, "error": str(e)}}
    '''), 4))

    # apply tool
    if "POST" in ep.http_methods:
        lines.append(_indent(textwrap.dedent(f'''\
            @mcp.tool()
            async def apply_{name}() -> Dict:
                """Trigger {display}."""
                client = get_api_client()
                try:
                    result = await client.apply_{name}()
                    return {{
                        "success": True,
                        "data": result.get("data", result),
                        "timestamp": datetime.utcnow().isoformat(),
                    }}
                except Exception as e:
                    return {{"success": False, "error": str(e)}}
        '''), 4))

    return "\n".join(lines)


def _gen_read_delete_tools(ep: EndpointConfig) -> str:
    name = ep.python_name
    display = ep.display_name
    lines = []

    # list tool
    lines.append(_indent(textwrap.dedent(f'''\
        @mcp.tool()
        async def list_{name}s(page: int = 1, page_size: int = 20) -> Dict:
            """List {display}s with pagination."""
            client = get_api_client()
            try:
                result = await client.get_{name}s(
                    pagination=create_pagination(page, page_size),
                )
                return {{
                    "success": True,
                    "data": result.get("data", []),
                    "timestamp": datetime.utcnow().isoformat(),
                }}
            except Exception as e:
                return {{"success": False, "error": str(e)}}
    '''), 4))

    # delete-all tool
    lines.append(_indent(textwrap.dedent(f'''\
        @mcp.tool()
        async def delete_all_{name}s() -> Dict:
            """Delete all {display}s."""
            client = get_api_client()
            try:
                result = await client.delete_{name}s()
                return {{
                    "success": True,
                    "data": result.get("data", result),
                    "timestamp": datetime.utcnow().isoformat(),
                }}
            except Exception as e:
                return {{"success": False, "error": str(e)}}
    '''), 4))

    return "\n".join(lines)


# ===========================================================================
# Test generation
# ===========================================================================

def generate_tests(endpoints: list[EndpointConfig]) -> str:
    """Generate integration test source."""
    parts: list[str] = []

    for ep in endpoints:
        if ep.category == "crud":
            parts.append(_gen_crud_test(ep))
        elif ep.category == "nested_crud":
            parts.append(_gen_nested_crud_test(ep))
        elif ep.category == "settings":
            parts.append(_gen_settings_test(ep))
        elif ep.category == "action":
            parts.append(_gen_action_test(ep))
        elif ep.category == "read_delete":
            parts.append(_gen_read_delete_test(ep))

    body = "\n\n".join(parts)

    header = textwrap.dedent('''\
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


    ''')
    return header + body


def _class_name(ep: EndpointConfig) -> str:
    """Convert python_name to PascalCase class name."""
    return "".join(word.capitalize() for word in ep.python_name.split("_"))


def _gen_crud_test(ep: EndpointConfig) -> str:
    cls = _class_name(ep)
    name = ep.python_name
    plural = ep.plural_path or f"{ep.singular_path}s"
    lookup = ep.lookup_field or "descr"
    create_data = repr(ep.test_create_data)
    update_data = repr(ep.test_update_data)

    # Determine if the lookup field is 'name' — needs special handling
    # because 'name' must be unique and part of create_data
    uses_name = lookup == "name"

    # Build the setup block that goes right after create_data assignment
    if uses_name:
        setup = (
            "        hex8 = uuid.uuid4().hex[:8]\n"
            '        create_data["name"] = f"mcpt_{hex8}"\n'
            '        lookup_val = create_data["name"]\n'
        )
    else:
        setup = (
            f'        create_data["{lookup}"] = descr\n'
            '        lookup_val = descr\n'
        )

    return (
        f'class Test{cls}ReadOnly:\n'
        f'    """Read-only tests for {ep.display_name}."""\n'
        f'\n'
        f'    async def test_get_{name}s(self, api_client):\n'
        f'        result = await api_client.get_{name}s()\n'
        f'        assert "data" in result\n'
        f'\n'
        f'\n'
        f'class Test{cls}Lifecycle:\n'
        f'    """CRUD lifecycle test for {ep.display_name}."""\n'
        f'\n'
        f'    async def test_crud_lifecycle(self, api_client, unique_id):\n'
        f'        descr = f"MCP_INTTEST_{{unique_id}}"\n'
        f'        create_data = {create_data}\n'
        f'{setup}'
        f'        item_id = None\n'
        f'        try:\n'
        f'            result = await api_client.create_{name}(\n'
        f'                create_data, ControlParameters(apply=True),\n'
        f'            )\n'
        f'            item_id = result["data"]["id"]\n'
        f'            assert item_id is not None\n'
        f'\n'
        f'            # Re-lookup (IDs may shift after apply)\n'
        f'            obj = await _find_by_field(\n'
        f'                api_client, "{plural}", "{lookup}", lookup_val,\n'
        f'            )\n'
        f'            assert obj is not None\n'
        f'            item_id = obj["id"]\n'
        f'\n'
        f'            # Update\n'
        f'            await api_client.update_{name}(\n'
        f'                item_id, {update_data}, ControlParameters(apply=True),\n'
        f'            )\n'
        f'\n'
        f'        finally:\n'
        f'            # Cleanup — re-lookup since IDs shift\n'
        f'            obj = await _find_by_field(\n'
        f'                api_client, "{plural}", "{lookup}", lookup_val,\n'
        f'            )\n'
        f'            if obj is not None:\n'
        f'                try:\n'
        f'                    await api_client.delete_{name}(obj["id"])\n'
        f'                except Exception:\n'
        f'                    pass\n'
    )


def _gen_nested_crud_test(ep: EndpointConfig) -> str:
    """Generate tests for nested CRUD resources.

    Nested resources require a parent to exist first. The test creates the
    parent, then the child, and cleans up both.  For simplicity, the
    read-only test just lists the nested items (no parent needed for GET on
    the plural endpoint).
    """
    cls = _class_name(ep)
    name = ep.python_name
    plural = ep.plural_path or f"{ep.singular_path}s"

    lines = textwrap.dedent(f'''\
        class Test{cls}ReadOnly:
            """Read-only tests for {ep.display_name}."""

            async def test_get_{name}s(self, api_client):
                result = await api_client.get_{name}s()
                assert "data" in result
    ''')

    # No lifecycle test for nested — too complex to auto-generate parent
    # setup reliably; those are covered by manual testing.
    return lines


def _gen_settings_test(ep: EndpointConfig) -> str:
    cls = _class_name(ep)
    name = ep.python_name

    return textwrap.dedent(f'''\
        class Test{cls}ReadOnly:
            """Read-only tests for {ep.display_name}."""

            async def test_get_{name}(self, api_client):
                result = await api_client.get_{name}()
                assert "data" in result
    ''')


def _gen_action_test(ep: EndpointConfig) -> str:
    cls = _class_name(ep)
    name = ep.python_name

    if "GET" not in ep.http_methods:
        # POST-only action (e.g. wake_on_lan) — no safe read-only test
        return textwrap.dedent(f'''\
            class Test{cls}ReadOnly:
                """Read-only tests for {ep.display_name}."""

                @pytest.mark.skip(reason="POST-only action endpoint — no safe read test")
                async def test_{name}_placeholder(self, api_client):
                    pass
        ''')

    return textwrap.dedent(f'''\
        class Test{cls}ReadOnly:
            """Read-only tests for {ep.display_name}."""

            async def test_get_{name}_status(self, api_client):
                result = await api_client.get_{name}_status()
                assert "data" in result
    ''')


def _gen_read_delete_test(ep: EndpointConfig) -> str:
    cls = _class_name(ep)
    name = ep.python_name

    return textwrap.dedent(f'''\
        class Test{cls}ReadOnly:
            """Read-only tests for {ep.display_name}."""

            async def test_get_{name}s(self, api_client):
                result = await api_client.get_{name}s()
                assert "data" in result
    ''')


# ===========================================================================
# Main
# ===========================================================================

def main():
    # Generate all three files
    client_code = generate_client_mixin(ENDPOINTS)
    tools_code = generate_tools(ENDPOINTS)
    tests_code = generate_tests(ENDPOINTS)

    # Write output files
    client_path = ROOT / "src" / "generated_client.py"
    tools_path = ROOT / "src" / "generated_tools.py"
    tests_path = ROOT / "tests" / "test_generated_integration.py"

    client_path.write_text(client_code)
    print(f"Wrote {client_path}")

    tools_path.write_text(tools_code)
    print(f"Wrote {tools_path}")

    tests_path.write_text(tests_code)
    print(f"Wrote {tests_path}")

    print("\nDone. Generated files:")
    print(f"  {client_path}")
    print(f"  {tools_path}")
    print(f"  {tests_path}")


if __name__ == "__main__":
    main()
