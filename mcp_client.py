from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({
    "hr": {
        "command": "python",
        "args": ["mcp_server.py"],
        "transport": "stdio",
    }
})

async def get_tools():
    return await client.get_tools()