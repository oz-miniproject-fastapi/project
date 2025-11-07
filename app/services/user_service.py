from tortoise.exceptions import DoesNotExist, IntegrityError
from app.models.user import User
from app.schemas.user import UserProfileResponse, UserDeleteResponse


class UserService:
    # 프로필 조회
    async def get_profile(self, user: User) -> UserProfileResponse:
        return UserProfileResponse(
            id=user.id,
            email=user.email,
            nickname=user.nickname,
            name=user.name,
            phone=user.phone,
            created_at=user.created_at,
        )

    # 사용자 정보 수정
    async def update_user(self, user: User, data: dict) -> UserProfileResponse:
        for key, value in data.items():
            setattr(user, key, value)
        await user.save()

        return UserProfileResponse(
            id=user.id,
            email=user.email,
            nickname=user.nickname,
            name=user.name,
            phone=user.phone,
            created_at=user.created_at,
        )

    # 사용자 삭제
    async def delete_user(self, user: User) -> UserDeleteResponse:
        try:
            await user.delete()
            return UserDeleteResponse(message="User deleted successfully")
        except IntegrityError:
            raise ValueError("삭제할 수 없습니다. 관련 데이터가 존재합니다.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise
