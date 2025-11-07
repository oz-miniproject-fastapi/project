import os
import httpx
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

GEMINI_API_URL = "https://api.gemini.example/summarize"
API_KEY = os.getenv("GEMINI_API_KEY")


async def analyze_emotion(diary_content: str) -> str:
    """
    일기 내용을 요약하거나 감정을 분석하는 함수.
    Gemini(OpenAI 등) API를 호출해서 핵심 내용을 반환합니다.
    """
    if not API_KEY:
        raise ValueError("환경 변수에 GEMINI_API_KEY가 설정되어 있지 않습니다.")

    prompt = (
        "아래는 사용자가 작성한 일기 내용입니다.\n"
        "이 일기의 핵심 내용을 2~3문장으로 간결하게 요약해 주세요.\n\n"
        f"---\n{diary_content}\n---"
    )

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.post(
                GEMINI_API_URL,
                json={"prompt": prompt},
                headers={"Authorization": f"Bearer {API_KEY}"},
            )
            response.raise_for_status()

        data = response.json()
        return data.get("summary") or "요약 결과를 가져오지 못했습니다."

    except httpx.RequestError as e:
        # 네트워크 문제 (서버 접속 실패 등)
        raise RuntimeError(f"API 요청 중 오류가 발생했습니다: {e}")
    except httpx.HTTPStatusError as e:
        # 응답 코드가 4xx/5xx일 경우
        raise RuntimeError(f"API 응답 오류 ({e.response.status_code}): {e.response.text}")
