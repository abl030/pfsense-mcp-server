"""Shared fixtures for pfSense MCP integration tests."""

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
)

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
    version = (
        PfSenseVersion.PLUS_24_11 if ver_str == "PLUS_24_11" else PfSenseVersion.CE_2_8_0
    )

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
