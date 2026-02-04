# Live API Integration Testing & Code Generation

## Status: Phase 1 Complete

### What's Done

**Hand-written integration tests** (`tests/test_integration.py`):
- Read-only tests: system status, interfaces, firewall logs, services, DHCP leases, object ID management, HATEOAS navigation
- CRUD lifecycle tests: firewall rules, NAT port forwards, aliases
- All pass against live pfSense instance (50 passed, 1 skipped)

**Code generator** (`scripts/generate_from_spec.py`):
- Reads OpenAPI spec and endpoint configuration registry
- Generates three files from 80 endpoint configurations:
  - `src/generated_client.py` — 288 async client methods (mixin class)
  - `src/generated_tools.py` — 288 MCP tool registrations
  - `tests/test_generated_integration.py` — 131 test classes
- Read-only tests: 91 passed, 1 skipped (WoL — POST-only action)
- CRUD lifecycle tests: generated but not yet validated against live API

**Coverage: 161 of 258 API paths (62.4%)**
- Core pfSense coverage (excluding optional packages): ~82%

### Endpoint Categories

The generator classifies endpoints into these categories:

| Category | Pattern | Generated Methods |
|----------|---------|-------------------|
| `crud` | GET/POST/PATCH/DELETE | `get_Xs`, `create_X`, `update_X`, `delete_X` |
| `nested_crud` | CRUD with parent_id | Same as crud, with `parent_id` parameter |
| `settings` | GET + PATCH only | `get_X`, `update_X` |
| `action` | GET status + POST trigger | `get_X_status`, `apply_X` |
| `read_delete` | GET + DELETE only | `get_X`, `delete_X` |

### Domains Covered

| Domain | Endpoint Configs | Status |
|--------|-----------------|--------|
| Firewall (rules, aliases, NAT, schedules, shapers, VIPs, states) | 16 | Read-only tested |
| Routing (gateways, groups, static routes) | 6 | Read-only tested |
| Interfaces (physical, bridges, groups, VLANs, GRE, LAGG) | 8 | Read-only tested |
| Services (DHCP, DNS resolver/forwarder, cron, NTP, SSH, WoL) | 17 | Read-only tested |
| System (certs, CAs, CRLs, tunables, settings, packages) | 16 | Read-only tested |
| Users & Auth (users, groups, auth servers) | 3 | Read-only tested |
| VPN (IPsec, OpenVPN, WireGuard) | 12 | Read-only tested |
| Diagnostics & Status (ARP, config history, CARP, gateway status, logs) | 6 | Read-only tested |

### Uncovered Paths (97)

Grouped by reason:

**Optional packages (62 paths, 64% of gap):**
- HAProxy: 30 paths
- BIND DNS: 13 paths
- ACME/Let's Encrypt: 13 paths
- FreeRADIUS: 6 paths

**Action/trigger endpoints (14 paths):**
- Certificate generate/renew/export/CSR: 7 paths
- Certificate authority generate/renew: 2 paths
- Diagnostics (command_prompt, ping, halt, reboot): 4 paths
- REST API settings sync: 1 path

**Status/read-only endpoints (10 paths):**
- Log endpoints (auth, DHCP, OpenVPN, system, REST API): 5 paths
- OpenVPN status/connections: 5 paths

**Special cases (11 paths):**
- Auth/JWT token management: 3 paths
- OpenVPN client export: 3 paths
- IPsec child SA status: 2 paths
- CRL revoked certificates (requires parent_id for GET): 1 path
- DHCP server backend: 1 path
- GraphQL: 1 path

### Running Tests

```bash
# All read-only tests (safe)
nix develop --command pytest tests/test_generated_integration.py -v -k "not Lifecycle"

# Hand-written tests only
nix develop --command pytest tests/test_integration.py -v

# All tests together
nix develop --command pytest tests/ -v --ignore=tests/test_enhanced_features.py

# Without credentials (all skip)
unset PFSENSE_URL && pytest tests/test_generated_integration.py -v
```

### Regenerating

```bash
# Edit scripts/generate_from_spec.py, then:
nix develop --command python scripts/generate_from_spec.py

# Never hand-edit generated files — fix the generator and re-run
```

## Next Steps

1. **Run CRUD lifecycle tests** against live instance (requires explicit go-ahead — these create/modify/delete resources)
2. **Add optional package endpoints** (HAProxy, BIND, ACME, FreeRADIUS) — only useful if those packages are installed
3. **Add log endpoints** (`/status/logs/*`) — read-only, low risk
4. **Add certificate action endpoints** — generate, renew, export (destructive, needs careful test data)
5. **Add OpenVPN status endpoints** — read-only status and connection info
