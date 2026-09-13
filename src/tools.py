"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    {
        "name": "helpdesk_query",
        "description": "Tra cứu ticket sự cố kỹ thuật hoặc trạng thái tài khoản người dùng.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Mã ticket, email hoặc từ khóa cần tra cứu (ví dụ: 'IT-1001' hoặc 'vinh@example.com')"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "create_support_request",
        "description": "Tạo ticket yêu cầu hỗ trợ kỹ thuật IT Helpdesk.",
        "parameters": {
            "type": "object",
            "properties": {
                "requester": {"type": "string", "description": "Tên hoặc email người yêu cầu"},
                "issue_type": {"type": "string", "description": "Loại sự cố: mạng, tài khoản, phần mềm hoặc phần cứng"},
                "description": {"type": "string", "description": "Mô tả chi tiết sự cố"},
                "priority": {"type": "string", "description": "Mức độ ưu tiên: low, medium hoặc high"}
            },
            "required": ["requester", "issue_type", "description"]
        }
    },
    {
        "name": "list_open_tickets",
        "description": "Liệt kê các ticket Helpdesk đang mở hoặc đang được xử lý của một người dùng.",
        "parameters": {
            "type": "object",
            "properties": {
                "requester": {
                    "type": "string",
                    "description": "Tên hoặc email người yêu cầu; bỏ trống để xem tất cả ticket đang mở"
                }
            },
            "required": []
        }
    },
    {
        "name": "update_ticket_status",
        "description": "Cập nhật trạng thái và ghi chú xử lý cho một ticket Helpdesk.",
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_id": {"type": "string", "description": "Mã ticket, ví dụ IT-1001"},
                "status": {"type": "string", "description": "Trạng thái mới: Đang xử lý, Chờ người dùng hoặc Đã đóng"},
                "note": {"type": "string", "description": "Ghi chú xử lý của kỹ thuật viên"}
            },
            "required": ["ticket_id", "status"]
        }
    },
    {
        "name": "reset_account_access",
        "description": "Mở khóa tài khoản hoặc gửi yêu cầu đặt lại mật khẩu cho người dùng.",
        "parameters": {
            "type": "object",
            "properties": {
                "account": {"type": "string", "description": "Email tài khoản cần hỗ trợ"},
                "action": {"type": "string", "description": "Thao tác: unlock hoặc reset_password"}
            },
            "required": ["account", "action"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "IT-1001": {
        "ticket_id": "IT-1001", "requester": "Nguyễn Ngọc Vĩnh", "issue_type": "Mạng",
        "summary": "Không thể kết nối Wi-Fi tầng 3", "status": "Đang xử lý", "priority": "high",
        "assigned_to": "IT Helpdesk"
    },
    "IT-1002": {
        "ticket_id": "IT-1002", "requester": "Trần Minh Anh", "issue_type": "Tài khoản",
        "summary": "Tài khoản bị khóa sau nhiều lần đăng nhập sai", "status": "Chờ người dùng",
        "priority": "medium", "assigned_to": "Lê Hoàng Nam"
    },
    "IT-1003": {
        "ticket_id": "IT-1003", "requester": "Phạm Quốc Bảo", "issue_type": "Phần mềm",
        "summary": "Không cài được bộ công cụ phát triển", "status": "Đã đóng", "priority": "low",
        "assigned_to": "IT Helpdesk"
    },
    "IT-1004": {
        "ticket_id": "IT-1004", "requester": "Nguyễn Ngọc Vĩnh", "issue_type": "Thiết bị",
        "summary": "Màn hình ngoài chập chờn", "status": "Mới tạo", "priority": "medium",
        "assigned_to": "Chưa phân công"
    },
    "vinh@example.com": {
        "account": "vinh@example.com", "account_status": "Hoạt động",
        "last_password_change": "2026-08-20", "mfa_enabled": True, "department": "AI Lab"
    },
    "minhanh@example.com": {
        "account": "minhanh@example.com", "account_status": "Bị khóa",
        "last_password_change": "2026-07-12", "mfa_enabled": False, "department": "Operations"
    },
    "quocbao@example.com": {
        "account": "quocbao@example.com", "account_status": "Hoạt động",
        "last_password_change": "2026-09-01", "mfa_enabled": True, "department": "Engineering"
    },
    "LAPTOP-001": {
        "asset_id": "LAPTOP-001", "owner": "Nguyễn Ngọc Vĩnh", "device_type": "Laptop",
        "model": "Dell Latitude 7440", "asset_status": "Đang sử dụng", "location": "Tầng 3"
    },
    "LAPTOP-002": {
        "asset_id": "LAPTOP-002", "owner": "Trần Minh Anh", "device_type": "Laptop",
        "model": "Lenovo ThinkPad T14", "asset_status": "Đang bảo trì", "location": "Phòng IT"
    }
}


def execute_helpdesk_query(query: str) -> str:
    """Tra cứu ticket sự cố hoặc trạng thái tài khoản."""
    normalized_query = query.strip()
    record = MOCK_DATABASE.get(normalized_query.upper()) or MOCK_DATABASE.get(normalized_query.lower())
    if record:
        return json.dumps({
            "status": "SUCCESS",
            "query": query,
            "data": record
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy ticket hoặc tài khoản phù hợp với '{query}'"
        }, ensure_ascii=False)


def execute_create_support_request(requester: str, issue_type: str, description: str, priority: str = "medium") -> str:
    """Tạo ticket hỗ trợ kỹ thuật mới."""
    return json.dumps({
        "status": "SUCCESS",
        "ticket_id": "IT-NEW-1001",
        "requester": requester,
        "issue_type": issue_type,
        "priority": priority,
        "status_detail": "Đã tiếp nhận",
        "message": f"Đã tạo yêu cầu hỗ trợ {issue_type} cho {requester} với mức ưu tiên {priority}."
    }, ensure_ascii=False)


def execute_list_open_tickets(requester: str = "") -> str:
    """Liệt kê ticket chưa đóng, có thể lọc theo người yêu cầu."""
    normalized_requester = requester.strip().lower()
    tickets = [
        record for record in MOCK_DATABASE.values()
        if "ticket_id" in record
        and record.get("status") != "Đã đóng"
        and (not normalized_requester or normalized_requester in record.get("requester", "").lower())
    ]
    return json.dumps({
        "status": "SUCCESS",
        "count": len(tickets),
        "tickets": tickets
    }, ensure_ascii=False)


def execute_update_ticket_status(ticket_id: str, status: str, note: str = "") -> str:
    """Cập nhật trạng thái ticket trong DB mô phỏng."""
    ticket = MOCK_DATABASE.get(ticket_id.strip().upper())
    if not ticket or "ticket_id" not in ticket:
        return json.dumps({"status": "NOT_FOUND", "message": f"Không tìm thấy ticket '{ticket_id}'"}, ensure_ascii=False)
    ticket["status"] = status
    if note:
        ticket["last_note"] = note
    return json.dumps({"status": "SUCCESS", "data": ticket}, ensure_ascii=False)


def execute_reset_account_access(account: str, action: str) -> str:
    """Mở khóa hoặc tạo yêu cầu reset mật khẩu cho tài khoản."""
    normalized_account = account.strip().lower()
    record = MOCK_DATABASE.get(normalized_account)
    if not record or "account" not in record:
        return json.dumps({"status": "NOT_FOUND", "message": f"Không tìm thấy tài khoản '{account}'"}, ensure_ascii=False)
    if action not in {"unlock", "reset_password"}:
        return json.dumps({"status": "INVALID_ACTION", "message": "action phải là unlock hoặc reset_password"}, ensure_ascii=False)
    if action == "unlock":
        record["account_status"] = "Hoạt động"
        message = f"Đã mở khóa tài khoản {account}."
    else:
        message = f"Đã gửi liên kết đặt lại mật khẩu tới {account}."
    return json.dumps({"status": "SUCCESS", "account": account, "action": action, "message": message}, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "helpdesk_query": execute_helpdesk_query,
    "create_support_request": execute_create_support_request,
    "list_open_tickets": execute_list_open_tickets,
    "update_ticket_status": execute_update_ticket_status,
    "reset_account_access": execute_reset_account_access
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
