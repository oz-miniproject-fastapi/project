from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User


class UserRepository:
    """
    User 모델에 대한 데이터 접근을 담당하는 Repository 클래스.
    회원 조회 및 생성 로직을 제공합니다.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> User | None:
        """
        이메일로 사용자 정보를 조회합니다.
        """
        if not email:
            return None

        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def create(self, user: User) -> User:
        """
        새로운 사용자를 데이터베이스에 저장합니다.
        """
        if not user or not user.email:
            raise ValueError("유효하지 않은 사용자 객체입니다.")

        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
