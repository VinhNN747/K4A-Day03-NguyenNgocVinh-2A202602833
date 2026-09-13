"""
📚 [REFERENCE ONLY / CODE MẪU THAM KHẢO]
🧠 CẤP ĐỘ 3: NATIVE MCP AGENT (Native Tool Calling + MCP Server Integration)
⚠️ Lưu ý: File này chỉ dùng để đọc tham khảo kiến trúc. Không chỉnh sửa hay debug file này.
"""

import json

def get_weather(city: str) -> str:
    return f"Thời tiết {city}: 28°C, Nắng nhẹ."

def run_level3_demo():
    print("=== DEMO CẤP ĐỘ 3: NATIVE MCP AGENT ===")
    user_goal = "Tra cứu trạng thái ticket IT-1001"
    print(f"🎯 Goal: {user_goal}")
    print("🧠 [Thought]: Phát sinh Native Tool Call 'helpdesk_query'...")
    print("🛠️ [Native Tool Call]: helpdesk_query({'query': 'IT-1001'})")
    print("👁️ [MCP Server Observation]: {'ticket_id': 'IT-1001', 'status': 'Đang xử lý', 'priority': 'high'}")
    print("🏁 [Final Answer]: Ticket IT-1001 đang được IT Helpdesk xử lý với mức ưu tiên cao.")

if __name__ == "__main__":
    run_level3_demo()
