import os
import json
import httpx
from dotenv import load_dotenv

# .env 로드
load_dotenv()


class AIService:
    # Gemini API 기본 설정
    API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    API_KEY = os.getenv("GEMINI_API_KEY")

    @staticmethod
    async def _post_to_gemini(payload: dict) -> dict:
        # 기본 API 요청 메서드
        if not AIService.API_KEY:
            raise ValueError("Gemini API 키가 설정되지 않았습니다.")

        async with httpx.AsyncClient() as client:
            response = await client.post(
                AIService.API_URL,
                headers={
                    "Authorization": f"Bearer {AIService.API_KEY}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
            response.raise_for_status()
            return response.json()

    @staticmethod
    async def get_emotion_summary(diary_content: str) -> str:
        # 일기 요약 요청
        prompt = (
            "아래는 사용자가 작성한 일기 내용입니다.\n"
            "이 일기의 핵심 내용을 2~3문장으로 간결하게 요약해 주세요.\n\n"
            f"---\n{diary_content}\n---"
        )

        payload = {
            "prompt": {"text": prompt},
            "temperature": 0.5,
            "max_output_tokens": 200,
        }

        data = await AIService._post_to_gemini(payload)
        return data.get("candidates", [{}])[0].get("content", "")

    @staticmethod
    async def get_emotion_keywords(diary_id: int, user_id: int, diary_content: str) -> list[dict]:
        # 감정 키워드 추출 요청
        prompt = (
            f"아래는 사용자가 작성한 일기 내용입니다. 문장에서 나타나는 감정 키워드를 추출해주세요.\n"
            f"긍정, 부정, 중립으로 나누어 JSON 형태로 반환합니다.\n\n"
            f"{{\n  \"diary_id\": {diary_id},\n  \"user_id\": {user_id},\n  \"keywords\": []\n}}\n\n"
            f"---\n{diary_content}\n---"
        )

        payload = {
            "prompt": {"text": prompt},
            "temperature": 0,
            "max_output_tokens": 300,
        }

        data = await AIService._post_to_gemini(payload)
        text_output = data.get("candidates", [{}])[0].get("content", "")

        try:
            result = json.loads(text_output)
            return result.get("keywords", [])
        except Exception:
            return []
