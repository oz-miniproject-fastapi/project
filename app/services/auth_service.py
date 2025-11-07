import os
from datetime import timedelta
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist

from app.models.user import User
from app.models.token_blacklist import TokenBlacklist
from app.utils.jwt import create_access_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))


class AuthService:
    # 비밀번호 해시
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    # 비밀번호 검증
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    # 회원가입
    async def register_user(
        self, email: str, password: str, nickname: str | None = None, phone: str | None = None
    ) -> User:
        hashed_pw = self.hash_password(password)
        return await User.create(
            email=email,
            password=hashed_pw,
            nickname=nickname,
            phone=phone,
        )

    # 로그인
    async def login(self, email: str, password: str) -> dict:
        try:
            user = await User.get(email=email)
        except DoesNotExist:
            raise ValueError("잘못된 이메일 또는 비밀번호입니다.")

        if not self.verify_password(password, user.password):
            raise ValueError("잘못된 이메일 또는 비밀번호입니다.")

        access_token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta_minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        refresh_token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta_minutes=REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60,
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    # 로그아웃
    async def logout(self, token: str) -> None:
        await TokenBlacklist.create(token=token)
