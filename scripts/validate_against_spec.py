#!/usr/bin/env python3
"""
Validate our API client implementation against the OpenAPI spec.

This script:
1. Parses the OpenAPI spec to extract expected field names/types
2. Scans our Python code for field names we're using
3. Reports mismatches

Run: nix develop --command python scripts/validate_against_spec.py
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set


def load_openapi_spec() -> Dict:
    """Load the OpenAPI spec."""
    spec_path = Path(__file__).parent.parent / "openapi" / "pfsense-api-v2.json"
    if not spec_path.exists():
        raise FileNotFoundError(f"OpenAPI spec not found at {spec_path}")
    with open(spec_path) as f:
        return json.load(f)


def get_schema_fields(spec: Dict, schema_name: str) -> Dict[str, Dict]:
    """Get fields and their types from a schema."""
    schema = spec.get("components", {}).get("schemas", {}).get(schema_name, {})
    return schema.get("properties", {})


def get_required_fields(spec: Dict, path: str, method: str) -> List[str]:
    """Get required fields for an endpoint."""
    endpoint = spec.get("paths", {}).get(path, {}).get(method, {})
    body = endpoint.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema", {})

    required = []
    for item in body.get("allOf", []):
        if "required" in item:
            required.extend(item["required"])
    return required


def find_dict_fields_in_code(code: str, marker: str) -> List[Dict]:
    """Find dictionary field names near a marker string using regex."""
    results = []
    lines = code.split('\n')

    for i, line in enumerate(lines):
        if marker in line:
            # Look at next 30 lines for dict fields
            context_lines = lines[i:min(i+30, len(lines))]
            context = '\n'.join(context_lines)

            # Find "field": or 'field': patterns
            field_pattern = r'["\'](\w+)["\']:\s*'
            fields = re.findall(field_pattern, context)

            if fields:
                results.append({
                    "line": i + 1,
                    "marker": marker,
                    "fields": set(fields)
                })
    return results


# Known wrong -> correct field mappings
KNOWN_MISTAKES = {
    "src": "source",
    "dst": "destination",
    "dstport": "destination_port",
    "srcport": "source_port",
    "descr": None,  # descr is actually correct
}


def validate_fields(
    our_fields: Set[str],
    spec_fields: Set[str],
    context: str
) -> List[str]:
    """Check for field name mismatches."""
    issues = []

    for field in our_fields:
        # Skip known-good fields
        if field in ["descr", "type", "id", "data", "success", "message", "error"]:
            continue

        if field in KNOWN_MISTAKES and KNOWN_MISTAKES[field] is not None:
            correct = KNOWN_MISTAKES[field]
            if correct in spec_fields:
                issues.append(f"    ✗ WRONG: '{field}' should be '{correct}'")

        elif field not in spec_fields and len(field) > 2:
            # Check for similar names in spec
            similar = [s for s in spec_fields if (
                field.lower() in s.lower() or
                s.lower() in field.lower() or
                field.replace("_", "") == s.replace("_", "")
            )]
            if similar:
                issues.append(f"    ? UNKNOWN: '{field}' - similar in spec: {similar}")

    return issues


def check_interface_is_array(code: str) -> List[str]:
    """Check that interface is passed as array for firewall rules.

    NOTE: Per OpenAPI spec:
    - FirewallRule.interface is an ARRAY
    - PortForward.interface is a STRING (not array)

    This check looks for firewall rule creation patterns specifically.
    """
    issues = []
    lines = code.split('\n')

    # Find patterns like "interface": interface (not array)
    # vs "interface": [interface] (array - correct)
    pattern_wrong = r'"interface":\s*interface[,\s\n}]'
    pattern_correct = r'"interface":\s*\[interface\]'

    wrong_matches = list(re.finditer(pattern_wrong, code))
    correct_matches = list(re.finditer(pattern_correct, code))

    if wrong_matches:
        for m in wrong_matches:
            line_num = code[:m.start()].count('\n') + 1
            # Get surrounding context to determine if this is:
            # 1. Response metadata (filters_applied) - OK to be plain string
            # 2. Port forward data - OK to be plain string (per spec)
            # 3. Firewall rule data - MUST be array
            context_start = max(0, line_num - 15)
            context = '\n'.join(lines[context_start:line_num + 5])

            # Skip if in response metadata
            if 'filters_applied' in context:
                continue

            # Skip if in port forward data (PortForward uses string, not array)
            if 'port_forward_data' in context or 'PortForward' in context:
                continue

            # This is likely firewall rule data - flag it
            issues.append(f"    ✗ Line {line_num}: 'interface' should be [interface] not interface")

    if correct_matches:
        issues.append(f"    ✓ Found {len(correct_matches)} correct [interface] usages (firewall rules)")

    return issues


def validate_file(spec: Dict, file_path: Path, schemas: Dict[str, str]) -> List[str]:
    """Validate a file against relevant schemas."""
    code = file_path.read_text()
    all_issues = []

    for marker, schema_name in schemas.items():
        spec_fields = set(get_schema_fields(spec, schema_name).keys())
        matches = find_dict_fields_in_code(code, marker)

        if matches:
            all_issues.append(f"\n  {marker} (schema: {schema_name}):")
            for match in matches:
                issues = validate_fields(match["fields"], spec_fields, f"line {match['line']}")
                if issues:
                    all_issues.append(f"    Line {match['line']}:")
                    all_issues.extend(issues)

    return all_issues


def main():
    print("=" * 60)
    print("Validating implementation against OpenAPI spec")
    print("=" * 60)

    try:
        spec = load_openapi_spec()
        print(f"Loaded spec: {len(spec.get('paths', {}))} endpoints\n")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1

    all_issues = []
    error_count = 0

    # Validate main.py
    main_path = Path(__file__).parent.parent / "src" / "main.py"
    print(f"Checking {main_path.name}...")

    schemas = {
        "rule_data": "FirewallRule",
        "port_forward_data": "PortForward",
        "nat_data": "PortForward",
        "alias_data": "FirewallAlias",
    }
    issues = validate_file(spec, main_path, schemas)
    all_issues.extend(issues)

    # Check interface array pattern
    code = main_path.read_text()
    print("\nChecking interface array pattern...")
    interface_issues = check_interface_is_array(code)
    all_issues.extend(interface_issues)

    # Validate pfsense_api_enhanced.py
    api_path = Path(__file__).parent.parent / "src" / "pfsense_api_enhanced.py"
    print(f"\nChecking {api_path.name}...")

    # Check DELETE patterns
    api_code = api_path.read_text()
    print("\nChecking DELETE patterns...")

    if 'data={"id":' in api_code or "data={'id':" in api_code:
        all_issues.append("    ✓ DELETE methods use body for ID")
    if re.search(r'DELETE.*\{.*id\}', api_code):
        all_issues.append("    ✗ DELETE may use URL path for ID (should use body)")
        error_count += 1

    # Print required fields reference
    print("\n" + "=" * 60)
    print("Required fields per endpoint (from spec):")
    print("=" * 60)

    endpoints = [
        ("/api/v2/firewall/rule", "post"),
        ("/api/v2/firewall/nat/port_forward", "post"),
        ("/api/v2/firewall/alias", "post"),
    ]

    for path, method in endpoints:
        required = get_required_fields(spec, path, method)
        print(f"  {method.upper()} {path}")
        print(f"    Required: {required}")

    # Summary
    print("\n" + "=" * 60)
    print("Validation Results:")
    print("=" * 60)

    for issue in all_issues:
        print(issue)
        if "✗" in issue:
            error_count += 1

    print(f"\nErrors found: {error_count}")

    return 1 if error_count > 0 else 0


if __name__ == "__main__":
    exit(main())
