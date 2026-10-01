import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"],
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Discovered tools:", [t.name for t in tools.tools])

            result = await session.call_tool("leave_balance", {"employee_id": 4})
            print("leave_balance(4) ->", result)

asyncio.run(main())