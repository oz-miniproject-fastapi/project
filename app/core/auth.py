import os
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from dotenv import load_dotenv
from app.models.user import User

# 환경 변수 로드
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

auth_scheme = HTTPBearer()


async def get_current_user(token: HTTPBearer = Depends(auth_scheme)) -> User:
    """
    요청 헤더의 Bearer 토큰을 검증하고, 해당 사용자를 반환합니다.
    """
    try:
        # JWT 디코딩
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")

        # DB에서 사용자 조회
        user = await User.get_or_none(id=user_id)
        if user is None:
            raise HTTPException(status_code=401, detail="존재하지 않는 사용자입니다.")

        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="토큰이 만료되었습니다.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="토큰이 유효하지 않습니다.")
