
David Goggins Reminder (Gemini + Telegram + Desktop Popup)

Chatbot/nhắc nhở kỷ luật theo phong cách “tough-love” (lấy cảm hứng tinh thần David Goggins) sử dụng Gemini API để tạo nội dung, sau đó:

Hiện desktop notification trên Windows

Gửi tin nhắn qua Telegram bot

Cache theo ngày: trong 1 ngày dùng lại message cũ, sang ngày mới tự tạo message mới

Tính năng

✅ Gemini tạo lời nhắc 90–140 từ + checklist 3 việc

✅ Desktop pop-up (plyer)

✅ Telegram push (requests)

✅ Cache cache/YYYY-MM-DD.txt để tránh gọi API nhiều lần

✅ Chạy tự động mỗi 30 phút bằng Windows Task Scheduler

Yêu cầu

Python 3.9+ (khuyến nghị 3.11/3.12; 3.13 thường vẫn OK)

Windows 10/11

Gemini API Key

Telegram bot token + chat id

Cài đặt
1) Clone repo
git clone https://github.com/QuanWou/David-goggins-reminder.git
cd David-goggins-reminder

2) Tạo môi trường ảo
python -m venv .venv


Kích hoạt:

PowerShell:

.\.venv\Scripts\Activate.ps1

3) Cài dependencies
pip install -U pip setuptools wheel
pip install -U google-genai requests plyer

4) Thiết lập biến môi trường

Bạn cần 3 biến:

GEMINI_API_KEY

TELEGRAM_BOT_TOKEN

TELEGRAM_CHAT_ID

Windows (PowerShell):

setx GEMINI_API_KEY "YOUR_GEMINI_KEY"
setx TELEGRAM_BOT_TOKEN "YOUR_TELEGRAM_BOT_TOKEN"
setx TELEGRAM_CHAT_ID "YOUR_CHAT_ID"


Sau khi dùng setx, hãy mở terminal mới hoặc restart VS Code để biến môi trường có hiệu lực.

Lấy Telegram BOT TOKEN + CHAT ID
Tạo bot token

Telegram → tìm @BotFather

/newbot → tạo bot

Copy token dạng 123456:AA...

Lấy chat id

Mở chat với bot → nhắn hi

Mở link (thay token của bạn):

https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates


Tìm "chat":{"id": ... } → đó là TELEGRAM_CHAT_ID

Chạy thủ công

Chạy script:

python remind.py


Kỳ vọng:

Desktop hiện notification

Telegram nhận message

Tạo file cache: cache/YYYY-MM-DD.txt

Tự động chạy mỗi 30 phút (Windows Task Scheduler)
Khuyến nghị: Trigger “At log on” để pop-up chắc chắn hiện

Mở Task Scheduler

Create Task…

Tab General:

Name: Goggins Reminder

Chọn Run only when user is logged on (để pop-up hiển thị)

Tick Run with highest privileges

Tab Triggers → New…

Begin the task: At log on

Tick Repeat task every: 30 minutes

for a duration of: Indefinitely

Tab Actions → New…

Program/script:

D:\goggins-reminder\.venv\Scripts\python.exe


(đổi theo đường dẫn dự án của bạn)

Add arguments:

D:\goggins-reminder\remind.py


Start in:

D:\goggins-reminder


Chọn task → Run để test ngay.

Cấu trúc thư mục
.
├─ remind.py
├─ gen_test.py
├─ cache/
│  └─ YYYY-MM-DD.txt
└─ .venv/   (không commit)

.gitignore (khuyến nghị)

Tạo .gitignore:

.venv/
__pycache__/
cache/
*.pyc
.env

Lưu ý
