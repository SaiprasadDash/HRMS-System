import asyncio
from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_groq import ChatGroq
from mcp_client import get_tools
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="qwen/qwen3.8-27b", temperature=0)

class HRState(TypedDict):
    user_query: str
    employee_id: int
    result: str

async def leave_agent(state: HRState) -> dict:
    tools = await get_tools()
    agent_llm = llm.bind_tools(tools)

    response = await agent_llm.ainvoke(
        f"Employee ID is {state['employee_id']}. Request: {state['user_query']}"
    )

    if not response.tool_calls:
        return {"result": response.content}

    call = response.tool_calls[0]
    tool = next(t for t in tools if t.name == call["name"])
    tool_result = await tool.ainvoke(call["args"])

    return {"result": str(tool_result)}

builder = StateGraph(HRState)
builder.add_node("leave_agent", leave_agent)
builder.set_entry_point("leave_agent")
builder.add_edge("leave_agent", END)
graph = builder.compile()

async def main():
    result = await graph.ainvoke({
        "user_query": "How many annual leaves do I have left?",
        "employee_id": 4,
    })
    print(result)

if __name__ == "__main__":
    asyncio.run(main())