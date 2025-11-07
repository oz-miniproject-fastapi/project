from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import TokenBlacklist


class TokenBlacklistRepository:
    """
    JWT 토큰 블랙리스트를 관리하는 Repository 클래스.
    로그아웃 또는 무효화된 토큰을 저장 및 조회합니다.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def add(self, token: str) -> TokenBlacklist:
        """
        블랙리스트에 토큰을 추가합니다.
        """
        if not token:
            raise ValueError("토큰 값이 비어 있습니다.")
        token_entry = TokenBlacklist(token=token)
        self.db.add(token_entry)
        await self.db.commit()
        await self.db.refresh(token_entry)
        return token_entry

    async def exists(self, token: str) -> bool:
        """
        해당 토큰이 블랙리스트에 존재하는지 확인합니다.
        """
        if not token:
            return False

        result = await self.db.execute(
            select(TokenBlacklist).where(TokenBlacklist.token == token)
        )
        return result.scalars().first() is not None
