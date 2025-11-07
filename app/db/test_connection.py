import asyncio
from tortoise import Tortoise
from app.db.database import TORTOISE_ORM


async def test_connection() -> None:
    """
    데이터베이스 연결 테스트 스크립트.
    정상적으로 연결되면 메시지를 출력합니다.
    """
    try:
        await Tortoise.init(config=TORTOISE_ORM)
        print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")
    finally:
        await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(test_connection())
