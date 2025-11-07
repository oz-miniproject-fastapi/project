from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# 데이터베이스 URL 설정 (환경 변수로 관리 권장)
DATABASE_URL = "postgresql+asyncpg://admin:admin1@localhost:5432/fastapi_db"

# 비동기 엔진 생성
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # 개발 중 True로 두면 SQL 로그 출력
    future=True,  # SQLAlchemy 2.x 스타일 사용
)

# 비동기 세션 팩토리
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# FastAPI 종속성 주입용 세션
async def get_db():
    """
    요청마다 새로운 DB 세션을 생성하고,
    요청 종료 시 자동으로 정리합니다.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
