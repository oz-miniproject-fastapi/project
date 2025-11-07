from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserProfileResponse(BaseModel):
    # 사용자 정보 조회 응답
    id: int
    email: EmailStr
    nickname: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    created_at: datetime


class UserUpdateRequest(BaseModel):
    # 사용자 정보 수정 요청
    nickname: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None


class UserDeleteResponse(BaseModel):
    # 사용자 삭제 응답
    message: str = "Deleted successfully"
