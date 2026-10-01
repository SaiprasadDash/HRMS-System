from mock_data import LEAVE_BALANCES, LEAVE_REQUESTS

def get_leave_balance(employee_id: int) -> dict:
    return LEAVE_BALANCES.get(employee_id, {})

def apply_leave(employee_id: int, leave_type: str, start_date: str, end_date: str) -> dict:
    request = {
        "id": len(LEAVE_REQUESTS) + 1,
        "employee_id": employee_id,
        "leave_type": leave_type,
        "start_date": start_date,
        "end_date": end_date,
        "status": "pending",
    }
    LEAVE_REQUESTS.append(request)
    return request