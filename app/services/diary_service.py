from app.models.diary import Diary
from app.repositories.diary_repo import DiaryRepository
from app.repositories.tag_repo import TagRepository


class DiaryService:
    # 태그 저장소 인스턴스
    tag_repo = TagRepository()

    @staticmethod
    async def create_diary_with_tags(
        user_id: int, title: str, content: str, tag_names: list[str] | None = None
    ) -> Diary:
        # 일기 생성 (태그 포함)
        diary = await DiaryRepository.create_diary(user_id, title, content)

        if tag_names:
            tags = [await DiaryService.tag_repo.get_or_create(name) for name in tag_names]
            await diary.tags.add(*tags)

        return diary

    @staticmethod
    async def update_diary_with_tags(
        diary: Diary,
        title: str | None = None,
        content: str | None = None,
        tag_names: list[str] | None = None,
    ) -> Diary:
        # 일기 수정 (태그 포함)
        await DiaryRepository.update_diary(diary, title, content)

        if tag_names is not None:
            await diary.tags.clear()
            tags = [await DiaryService.tag_repo.get_or_create(name) for name in tag_names]
            await diary.tags.add(*tags)

        return diary

    @staticmethod
    async def get_diary(user_id: int, diary_id: int) -> Diary | None:
        # 단일 일기 조회 (태그 + 감정키워드 포함)
        diary = await DiaryRepository.get_diary_by_id(user_id, diary_id)
        if diary:
            await diary.fetch_related("tags", "emotion_keywords")
        return diary

    @staticmethod
    async def list_diaries(user_id: int, oldest_first: bool = False) -> list[Diary]:
        # 사용자 일기 목록 조회
        diaries = await DiaryRepository.list_diaries(user_id, oldest_first)
        for diary in diaries:
            await diary.fetch_related("tags", "emotion_keywords")
        return diaries

    @staticmethod
    async def search_diaries(user_id: int, keyword: str) -> list[Diary]:
        # 키워드 검색
        if not keyword:
            return []
        diaries = await DiaryRepository.search_diaries(user_id, keyword)
        for diary in diaries:
            await diary.fetch_related("tags", "emotion_keywords")
        return diaries

    @staticmethod
    async def list_diaries_by_tag(
        user_id: int, tag_name: str, limit: int = 10
    ) -> list[Diary]:
        # 태그 기반 조회 (10개 제한)
        if not tag_name:
            return []
        diaries = await DiaryRepository.list_diaries_by_tag(user_id, tag_name, limit)
        for diary in diaries:
            await diary.fetch_related("tags", "emotion_keywords")
        return diaries

    @staticmethod
    async def delete_diary(diary: Diary) -> dict:
        # 단일 일기 삭제
        await diary.delete()
        return {"detail": "Diary deleted successfully"}

    @staticmethod
    async def summarize_diary(diary_id: int, user_id: int) -> None:
        # 요약 기능 (AI 제거)
        diary = await DiaryService.get_diary(user_id, diary_id)
        if not diary:
            return None
        return None

    @staticmethod
    async def analyze_emotion(diary: Diary) -> list:
        # 감정 분석 기능 (AI 제거)
        return []

    @staticmethod
    async def analyze_diary_emotions(diary_id: int, user_id: int) -> list | None:
        # 단일 일기 감정 분석
        diary = await DiaryService.get_diary(user_id, diary_id)
        if not diary:
            return None
        return await DiaryService.analyze_emotion(diary)
