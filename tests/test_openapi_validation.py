#!/usr/bin/env python3
"""
Validate API client against OpenAPI spec.

These tests ensure our request formats match what the pfSense API expects,
catching drift between our implementation and the actual API.

Run with: nix develop --command pytest tests/test_openapi_validation.py -v
"""

import json
import os
import sys
from pathlib import Path

import pytest

# Load OpenAPI spec
SPEC_PATH = Path(__file__).parent.parent / "openapi" / "pfsense-api-v2.json"


@pytest.fixture(scope="module")
def openapi_spec():
    """Load the OpenAPI specification."""
    if not SPEC_PATH.exists():
        pytest.skip(f"OpenAPI spec not found at {SPEC_PATH}")
    with open(SPEC_PATH) as f:
        return json.load(f)


@pytest.fixture(scope="module")
def firewall_rule_schema(openapi_spec):
    """Get the FirewallRule schema from the spec."""
    return openapi_spec["components"]["schemas"]["FirewallRule"]


class TestFirewallRuleSchema:
    """Validate our firewall rule format matches the OpenAPI spec."""

    def test_interface_is_array(self, firewall_rule_schema):
        """Interface field must be an array, not a string."""
        interface_prop = firewall_rule_schema["properties"]["interface"]
        assert interface_prop["type"] == "array", (
            "interface must be array type. "
            "Use: {'interface': ['lan']} not {'interface': 'lan'}"
        )

    def test_source_is_string(self, firewall_rule_schema):
        """Source field must be a string."""
        source_prop = firewall_rule_schema["properties"]["source"]
        assert source_prop["type"] == "string", (
            "source must be string type. "
            "Use: {'source': 'any'} not {'source': {'address': 'any'}}"
        )

    def test_destination_is_string(self, firewall_rule_schema):
        """Destination field must be a string."""
        dest_prop = firewall_rule_schema["properties"]["destination"]
        assert dest_prop["type"] == "string", (
            "destination must be string type. "
            "Use: {'destination': '1.1.1.1'} not {'destination': {'address': '1.1.1.1'}}"
        )

    def test_source_port_is_string(self, firewall_rule_schema):
        """Source port field must be a string (nullable)."""
        port_prop = firewall_rule_schema["properties"]["source_port"]
        assert port_prop["type"] == "string", (
            "source_port must be string type. "
            "Use: {'source_port': '80'} not {'source_port': 80}"
        )

    def test_destination_port_is_string(self, firewall_rule_schema):
        """Destination port field must be a string (nullable)."""
        port_prop = firewall_rule_schema["properties"]["destination_port"]
        assert port_prop["type"] == "string", (
            "destination_port must be string type. "
            "Use: {'destination_port': '443'} not {'destination_port': 443}"
        )

    def test_required_fields_for_post(self, openapi_spec):
        """POST requires specific fields."""
        post_schema = openapi_spec["paths"]["/api/v2/firewall/rule"]["post"]
        content = post_schema["requestBody"]["content"]["application/json"]["schema"]

        # Find required fields in allOf
        required = []
        for item in content.get("allOf", []):
            if "required" in item:
                required.extend(item["required"])

        expected_required = ["type", "interface", "ipprotocol", "source", "destination"]
        for field in expected_required:
            assert field in required, f"Field '{field}' should be required for POST"


class TestDeleteEndpoints:
    """Document DELETE endpoint spec vs reality.

    IMPORTANT: The OpenAPI spec says DELETE uses query params (?id=X),
    but in practice httpx DELETE with query params returns 400.
    The body approach ({"id": X}) works reliably.

    These tests document what the SPEC says, not what we implement.
    """

    def test_spec_says_delete_uses_query_param(self, openapi_spec):
        """OpenAPI spec says DELETE /firewall/rule uses ?id= query parameter.

        NOTE: This documents the spec, but our implementation uses body
        because httpx DELETE with query params doesn't work with pfSense.
        """
        delete_op = openapi_spec["paths"]["/api/v2/firewall/rule"]["delete"]
        params = delete_op.get("parameters", [])

        id_param = next((p for p in params if p["name"] == "id"), None)
        assert id_param is not None, "Spec says DELETE should have 'id' parameter"
        assert id_param["in"] == "query", "Spec says id should be query param"
        # Our implementation uses body instead - see pfsense_api_enhanced.py

    def test_spec_says_nat_delete_uses_query_param(self, openapi_spec):
        """OpenAPI spec says DELETE /firewall/nat/port_forward uses ?id=."""
        path = "/api/v2/firewall/nat/port_forward"
        if path not in openapi_spec["paths"]:
            pytest.skip(f"Path {path} not in spec")

        delete_op = openapi_spec["paths"][path].get("delete")
        if not delete_op:
            pytest.skip(f"DELETE not defined for {path}")

        params = delete_op.get("parameters", [])
        id_param = next((p for p in params if p["name"] == "id"), None)
        assert id_param is not None, "Spec says DELETE should have 'id' parameter"
        # Our implementation uses body instead


class TestEndpointPaths:
    """Validate endpoint paths match the spec."""

    def test_firewall_rules_read_path(self, openapi_spec):
        """GET uses plural /rules for listing."""
        assert "/api/v2/firewall/rules" in openapi_spec["paths"], (
            "Read endpoint should be /api/v2/firewall/rules (plural)"
        )

    def test_firewall_rule_write_path(self, openapi_spec):
        """POST/PATCH/DELETE use singular /rule."""
        rule_path = openapi_spec["paths"].get("/api/v2/firewall/rule", {})
        assert "post" in rule_path, "POST should be on /api/v2/firewall/rule (singular)"
        assert "patch" in rule_path, "PATCH should be on /api/v2/firewall/rule (singular)"
        assert "delete" in rule_path, "DELETE should be on /api/v2/firewall/rule (singular)"


class TestFieldNaming:
    """Validate we use correct field names."""

    def test_no_src_dst_shorthand(self, firewall_rule_schema):
        """Verify the API uses full names, not shorthand."""
        props = firewall_rule_schema["properties"]

        # These should NOT exist
        assert "src" not in props, "Use 'source' not 'src'"
        assert "dst" not in props, "Use 'destination' not 'dst'"
        assert "srcport" not in props, "Use 'source_port' not 'srcport'"
        assert "dstport" not in props, "Use 'destination_port' not 'dstport'"

        # These SHOULD exist
        assert "source" in props, "Field 'source' should exist"
        assert "destination" in props, "Field 'destination' should exist"
        assert "source_port" in props, "Field 'source_port' should exist"
        assert "destination_port" in props, "Field 'destination_port' should exist"


class TestClientImplementation:
    """Test that our client implementation matches the spec."""

    def test_create_rule_data_format(self):
        """Verify create_firewall_rule_advanced uses correct format."""
        # This is a static analysis test - we check the source code
        src_path = Path(__file__).parent.parent / "src" / "main.py"
        if not src_path.exists():
            pytest.skip("main.py not found")

        source = src_path.read_text()

        # Check for correct patterns
        assert '"interface": [interface]' in source or "'interface': [interface]" in source, (
            "interface should be wrapped in array: [interface]"
        )
        assert '"source": source' in source or "'source': source" in source, (
            "Should use 'source' field name"
        )
        assert '"destination": destination' in source or "'destination': destination" in source, (
            "Should use 'destination' field name"
        )

    def test_delete_uses_body_not_query_param(self):
        """Verify delete methods use body (data=) not query params.

        Despite OpenAPI spec saying query params, httpx DELETE with query
        params returns 400 from pfSense. Body approach works.
        """
        src_path = Path(__file__).parent.parent / "src" / "pfsense_api_enhanced.py"
        if not src_path.exists():
            pytest.skip("pfsense_api_enhanced.py not found")

        source = src_path.read_text()

        # Check delete_firewall_rule uses data={"id": ...}
        assert 'data={"id": rule_id}' in source or "data={'id': rule_id}" in source, (
            "DELETE should pass id via body (data=), not query params"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
