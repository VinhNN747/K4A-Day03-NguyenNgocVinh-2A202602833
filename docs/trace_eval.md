# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Ngọc Vĩnh    
> **Mã Sinh Viên / Mã Học viên:**   2A202602833
> **Chủ đề Lựa chọn:** Trợ lý Hỗ trợ Kỹ thuật IT Helpdesk: Tra cứu ticket sự cố mạng, tài khoản và tạo yêu cầu hỗ trợ kỹ thuật.

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 2 / 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 3 / 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 2 / 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 2 / 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | **12 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "note vao ticket IT-1004 la \"dang gui yeu cau sang co so khac\"",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "update_ticket_status",
    "arguments": {
      "ticket_id": "IT-1004",
      "status": "Chờ người dùng",
      "note": "dang gui yeu cau sang co so khac"
    },
    "observation": {
      "status": "SUCCESS",
      "data": {
        "ticket_id": "IT-1004",
        "requester": "Nguyễn Ngọc Vĩnh",
        "issue_type": "Thiết bị",
        "summary": "Màn hình ngoài chập chờn",
        "status": "Chờ người dùng",
        "priority": "medium",
        "assigned_to": "Chưa phân công",
        "last_note": "dang gui yeu cau sang co so khac"
      }
    },
    "latency_ms": 4283.74
  },
  {
    "step": 2,
    "query": "note vao ticket IT-1004 la \"dang gui yeu cau sang co so khac\"",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Kết quả Helpdesk: {\"ticket_id\": \"IT-1004\", \"requester\": \"Nguyễn Ngọc Vĩnh\", \"issue_type\": \"Thiết bị\", \"summary\": \"Màn hình ngoài chập chờn\", \"status\": \"Chờ người dùng\", \"priority\": \"medium\", \"assigned_to\": \"Chưa phân công\", \"last_note\": \"dang gui yeu cau sang co so khac\"}",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 10 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
