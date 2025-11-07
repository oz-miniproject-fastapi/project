from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# 회원가입
class UserSignupRequest(BaseModel):
    email: EmailStr  # 이메일
    password: str  # 비밀번호
    nickname: Optional[str] = None  # 닉네임
    phone: Optional[str] = None  # 전화번호


class UserSignupResponse(BaseModel):
    id: int
    email: EmailStr
    nickname: Optional[str] = None
    phone: Optional[str] = None
    created_at: Optional[datetime] = None


# 로그인
class UserLoginRequest(BaseModel):
    email: EmailStr  # 이메일
    password: str  # 비밀번호


class UserLoginResponse(BaseModel):
    access_token: str  # 액세스 토큰
    refresh_token: str  # 리프레시 토큰
    token_type: str = "bearer"  # 토큰 타입


# 로그아웃
class UserLogoutRequest(BaseModel):
    refresh_token: str  # 리프레시 토큰


class UserLogoutResponse(BaseModel):
    message: str = "Logout successful"  # 응답 메시지
