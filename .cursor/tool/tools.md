# Tools

## Custom Tools

Custom Tools are on .cursor/tool/customs.

### Project Isolation Knowledge Management
- **project_detector.py**: Automatic project detection and registration
  - usage: python3 .cursor/tool/customs/project_detector.py --scan
  - features: project discovery, registration, metadata extraction
  - status: [VERIFIED] - Phase 1 implementation complete

- **mcp_search.py**: Browse thousands of MCP servers
  - usage: python tools/mcp_search.py target_name --top_k num_of_rank
  - features: MCP server discovery, ranking, search functionality
  - status: [VERIFIED] - Functional and ready for use

- **install_mcp_servers.py**: Automatic MCP server registration and management
  - usage: python tools/install_mcp_servers.py [json_file]
  - features: Parse mcp_search.py output (JSON), merge server info into mcpServers dictionary format to .cursor/mcp.json, automatic MCP server registration and management
  - status: [VERIFIED] - Automated MCP server management tool