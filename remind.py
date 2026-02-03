import os
import requests
from google import genai
from plyer import notification

MODEL = "gemini-2.5-flash"

SYSTEM_STYLE = (
    "Bạn là bản thể khắc nghiệt nhất của David Goggins. Giọng điệu đanh thép, trực diện, không an ủi. Tập trung duy nhất vào tính kỷ luật và hành động tức thì. Không mạo danh, không chửi thề, nhưng mỗi từ phải như một cú đấm vào sự lười biếng."
)

USER_PROMPT = (
    "Viết lời nhắc nhở hằng ngày (90–140 từ) bằng tiếng Việt. Nội dung: Sự thật phũ phàng rằng không ai cứu bạn ngoài chính mình. Ép buộc hành động ngay bây giờ. Kết thúc đoạn văn bằng đúng một câu hỏi thách thức trực diện. Sau đó, lập checklist 3 hành động cụ thể, đo lường được để thực hiện dứt điểm trong hôm nay."
)



from datetime import date
from pathlib import Path

CACHE_DIR = Path(__file__).parent / "cache"

def generate_message() -> str:
    CACHE_DIR.mkdir(exist_ok=True)
    today = date.today().isoformat()
    cache_file = CACHE_DIR / f"{today}.txt"

    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8").strip()

    client = genai.Client()
    resp = client.models.generate_content(
        model=MODEL,
        contents=[SYSTEM_STYLE, USER_PROMPT],
    )
    text = (resp.text or "").strip()
    if not text:
        text = "Dậy. Làm việc khó trước. Không thương lượng với sự lười.\n- 1 việc khó\n- 1 việc sức khoẻ\n- 1 việc học"

    cache_file.write_text(text, encoding="utf-8")
    return text



def desktop_popup(title: str, message: str) -> None:
    notification.notify(
        title=title,
        message=message,
        timeout=12,
        app_name="Goggins Reminder",
    )


def send_telegram(text: str) -> None:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    r = requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=20)
    r.raise_for_status()


if __name__ == "__main__":
    msg = generate_message()

    popup_msg = msg
    if len(popup_msg) > 220:
        popup_msg = popup_msg[:220].rstrip() + "..."

    desktop_popup("KỶ LUẬT HÔM NAY", popup_msg)
    send_telegram(msg)

    print("OK: generated + popup + telegram sent")
