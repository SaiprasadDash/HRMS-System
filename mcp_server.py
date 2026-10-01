from mcp.server.fastmcp import FastMCP
from tools import get_leave_balance, apply_leave

mcp = FastMCP("HR Server")

@mcp.tool()
def leave_balance(employee_id: int) -> dict:
    """Get an employee's remaining leave balance by type."""
    return get_leave_balance(employee_id)

@mcp.tool()
def apply_for_leave(employee_id: int, leave_type: str, start_date: str, end_date: str) -> dict:
    """Submit a leave request for an employee."""
    return apply_leave(employee_id, leave_type, start_date, end_date)

if __name__ == "__main__":
    mcp.run()