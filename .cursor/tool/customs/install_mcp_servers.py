import os
import sys
import json
from pathlib import Path

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def server_to_mcp_entry(server):
    pkg = server.get("package_name")
    if not pkg:
        return None
    args = [f"{pkg}@latest"]
    entry = {
        "command": "npx",
        "args": args
    }
    return entry

def main():
    if len(sys.argv) < 2:
        print('用法: python install_mcp_servers.py <mcp_search_output.json>')
        sys.exit(1)
    input_path = sys.argv[1]
    new_data = load_json(input_path)
    new_servers = new_data.get('servers', [])

    cursor_dir = Path('.cursor')
    cursor_dir.mkdir(exist_ok=True)
    mcp_json_path = cursor_dir / 'mcp.json'
    existing_data = load_json(mcp_json_path)
    mcp_servers = existing_data.get('mcpServers', {})

    for srv in new_servers:
        name = srv.get("name")
        entry = server_to_mcp_entry(srv)
        if name and entry:
            if name in mcp_servers:
                mcp_servers[name].update(entry)
            else:
                mcp_servers[name] = entry

    save_json(mcp_json_path, {"mcpServers": mcp_servers})
    print(f'已合并 {len(new_servers)} 个服务器到 {mcp_json_path}')

if __name__ == '__main__':
    main() 