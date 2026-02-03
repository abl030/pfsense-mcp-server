# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Model Context Protocol (MCP) server that enables natural language interaction with pfSense firewalls through Claude Desktop and other GenAI applications. It uses the pfSense REST API v2 package ([jaredhendrickson13/pfsense-api](https://github.com/jaredhendrickson13/pfsense-api)).

## Commands

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the MCP server (stdio mode for Claude Desktop)
```bash
MCP_MODE=stdio python -m src.main
```

### Run as HTTP server (for testing)
```bash
MCP_MODE=http python -m src.main
```

### Run tests
```bash
# Run all tests
pytest tests/ -v

# Test specific enhanced features
python tests/test_enhanced_features.py

# Test API connection
python scripts/test_connection.py
```

### Linting and formatting
```bash
ruff check .
black .
mypy src/
```

## Architecture

### Core Components

- **`src/main.py`** - FastMCP server entry point. Defines all MCP tools (25+) that expose pfSense functionality. Uses a global `EnhancedPfSenseAPIClient` singleton initialized from environment variables.

- **`src/pfsense_api_enhanced.py`** - HTTP client for pfSense REST API v2. Contains:
  - `EnhancedPfSenseAPIClient` - async HTTP client with auth (API key, Basic, JWT)
  - Data classes for queries: `QueryFilter`, `SortOptions`, `PaginationOptions`, `ControlParameters`
  - Helper functions: `create_ip_filter()`, `create_port_filter()`, `create_pagination()`, etc.

### Key Patterns

**MCP Tool Registration**: Tools are registered with the `@mcp.tool()` decorator from FastMCP:
```python
@mcp.tool()
async def search_firewall_rules(interface: Optional[str] = None, ...) -> Dict:
    client = get_api_client()
    # ... implementation
```

**API Client Initialization**: The client is lazily initialized from environment variables via `get_api_client()`.

**Query Filtering**: Uses `QueryFilter` dataclass with operators: exact, startswith, endswith, contains, lt, lte, gt, gte, regex.

**Control Parameters**: Operations support `ControlParameters` for apply (immediate), async mode, and placement (rule ordering).

### Configuration

Configuration via environment variables (see `.env.example`):

| Variable | Purpose |
|----------|---------|
| `PFSENSE_URL` | pfSense base URL |
| `PFSENSE_VERSION` | `CE_2_8_0` or `PLUS_24_11` |
| `AUTH_METHOD` | `api_key`, `basic`, or `jwt` |
| `PFSENSE_API_KEY` | API key for authentication |
| `MCP_MODE` | `stdio` (Claude Desktop) or `http` (standalone) |
| `ENABLE_HATEOAS` | Enable navigation links in responses |

### Claude Desktop Integration

Configure in Claude Desktop settings:
```json
{
  "mcpServers": {
    "pfsense-enhanced": {
      "command": "python",
      "args": ["-m", "src.main"],
      "cwd": "/path/to/pfsense-mcp-server",
      "env": {
        "MCP_MODE": "stdio",
        "PFSENSE_URL": "https://your-pfsense.local",
        "AUTH_METHOD": "api_key",
        "PFSENSE_API_KEY": "your-key"
      }
    }
  }
}
```

## API Endpoints Used

The server communicates with pfSense REST API v2 endpoints:
- `/api/v2/status/system` - System status
- `/api/v2/status/interfaces` - Network interfaces
- `/api/v2/firewall/rules` - Firewall rules (GET/POST/PATCH/DELETE)
- `/api/v2/firewall/aliases` - Firewall aliases
- `/api/v2/status/dhcp_server/leases` - DHCP leases
- `/api/v2/status/logs/firewall` - Firewall logs
- `/api/v2/status/services` - Service status
