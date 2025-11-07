from app.models.diary import Diary
from app.models.user import User


class DiaryRepository:
    """
    Diary 모델에 대한 CRUD 및 검색 로직을 담당하는 저장소(Repository) 클래스
    """

    @staticmethod
    async def create_diary(user_id: int, title: str, content: str) -> Diary:
        """
        새 일기를 생성합니다.
        """
        user = await User.get_or_none(id=user_id)
        if not user:
            raise ValueError(f"User with id={user_id} not found.")
        return await Diary.create(user=user, title=title, content=content)

    @staticmethod
    async def get_diary_by_id(user_id: int, diary_id: int) -> Diary | None:
        """
        특정 사용자의 일기 상세 조회
        """
        return await Diary.get_or_none(id=diary_id, user_id=user_id)

    @staticmethod
    async def list_diaries(user_id: int, oldest_first: bool = False) -> list[Diary]:
        """
        특정 사용자의 일기 목록 조회
        - oldest_first: True면 오래된 순, False면 최신 순
        """
        order = "created_at" if oldest_first else "-created_at"
        return await Diary.filter(user_id=user_id).order_by(order)

    @staticmethod
    async def update_diary(
        diary: Diary, title: str | None = None, content: str | None = None
    ) -> Diary:
        """
        일기 제목/내용을 수정합니다.
        """
        if title:
            diary.title = title
        if content:
            diary.content = content
        await diary.save()
        return diary

    @staticmethod
    async def delete_diary(diary: Diary) -> None:
        """
        일기를 삭제합니다.
        """
        await diary.delete()

    @staticmethod
    async def search_diaries(user_id: int, keyword: str) -> list[Diary]:
        """
        키워드로 일기 내용을 검색합니다.
        """
        return await Diary.filter(
            user_id=user_id,
            content__icontains=keyword,
        ).all()

    @staticmethod
    async def list_diaries_by_tag(
        user_id: int, tag_name: str, limit: int = 10
    ) -> list[Diary]:
        """
        특정 태그 이름으로 연결된 일기 목록 조회 (기본 10개 제한)
        """
        return (
            await Diary.filter(user_id=user_id, tags__name=tag_name)
            .prefetch_related("tags", "emotion_keywords")
            .limit(limit)
        )
