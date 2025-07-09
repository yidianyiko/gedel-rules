import argparse
from camel.toolkits.pulse_mcp_search_toolkit import PulseMCPSearchToolkit

def search_mcp(query, top_k=1):
    search_toolkit = PulseMCPSearchToolkit()
    results = search_toolkit.search_mcp_servers(query=query, top_k=top_k)
    return results

def main():
    parser = argparse.ArgumentParser(description="Search MCP servers via PulseMCP.")
    parser.add_argument("query", type=str, help="Search keyword for MCP servers")
    parser.add_argument("--top_k", type=int, default=1, help="Number of top results to return")
    args = parser.parse_args()
    results = search_mcp(args.query, args.top_k)
    print(results)

if __name__ == "__main__":
    main() 