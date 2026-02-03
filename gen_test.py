from google import genai

MODEL = "gemini-2.5-flash"

SYSTEM_STYLE = (
    "Bạn là một huấn luyện viên kỷ luật kiểu tough-love, ngắn gọn, trực diện, "
    "tập trung vào hành động ngay. Không mạo danh hay nói bạn là David Goggins. "
    "Không chửi thề. Không xúc phạm cá nhân."
)

PROMPT = (
    "Viết 1 lời nhắc buổi tối bằng tiếng Việt (80–120 từ) để thúc mình kỷ luật ngày mai. "
    "Kết thúc bằng 3 gạch đầu dòng checklist."
)

client = genai.Client()
resp = client.models.generate_content(
    model=MODEL,
    contents=[SYSTEM_STYLE, PROMPT],
)

print(resp.text)
