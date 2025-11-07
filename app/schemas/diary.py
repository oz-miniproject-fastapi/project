from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class DiaryCreate(BaseModel):
    # 일기 작성 요청
    title: str
    content: str
    tags: list[str] = []
    emotion_keywords: list[str] = []


class DiaryUpdate(BaseModel):
    # 일기 수정 요청
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[list[str]] = None
    emotion_keywords: Optional[list[str]] = None


class DiaryResponse(BaseModel):
    # 일기 응답
    id: int
    title: str
    content: str
    tags: list[str] = []
    emotion_keywords: list[str] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
