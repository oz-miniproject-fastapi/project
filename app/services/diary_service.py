from app.models.diary import Diary

from app.repositories.diary_repo import DiaryRepository
from app.repositories.tag_repo import TagRepository


class DiaryService:
    tag_repo = TagRepository()

    # 일기 생성 (태그 포함)
    @staticmethod
    async def create_diary_with_tags(user_id: int, title: str, content: str, tag_names: list[str] = None):
        diary = await DiaryRepository.create_diary(user_id, title, content)
        if tag_names:
            tags = [await DiaryService.tag_repo.get_or_create(name) for name in tag_names]
            await diary.tags.add(*tags)
        return diary

    # 일기 수정 (태그 포함)
    @staticmethod
    async def update_diary_with_tags(diary, title: str = None, content: str = None, tag_names: list[str] = None):
        await DiaryRepository.update_diary(diary, title, content)
        if tag_names is not None:
            await diary.tags.clear()
            tags = [await DiaryService.tag_repo.get_or_create(name) for name in tag_names]
            await diary.tags.add(*tags)
        return diary

    #  단일 일기 조회 (태그 + 감정키워드 포함)
    @staticmethod
    async def get_diary(user_id: int, diary_id: int):
        diary = await DiaryRepository.get_diary_by_id(user_id, diary_id)
        if diary:
            await diary.fetch_related("tags", "emotion_keywords")
        return diary

    #  사용자 일기 목록 조회
    @staticmethod
    async def list_diaries(user_id: int, oldest_first: bool = False):
        diaries = await DiaryRepository.list_diaries(user_id, oldest_first)
        for diary in diaries:
            await diary.fetch_related("tags", "emotion_keywords")
        return diaries

    #  키워드 검색
    @staticmethod
    async def search_diaries(user_id: int, keyword: str):
        if not keyword:
            return []
        diaries = await DiaryRepository.search_diaries(user_id, keyword)
        for diary in diaries:
            await diary.fetch_related("tags", "emotion_keywords")
        return diaries

    #  태그 기반 조회 (10개 제한)
    @staticmethod
    async def list_diaries_by_tag(user_id: int, tag_name: str, limit: int = 10):
        if not tag_name:
            return []
        diaries = await DiaryRepository.list_diaries_by_tag(user_id, tag_name, limit)
        for diary in diaries:
            await diary.fetch_related("tags", "emotion_keywords")
        return diaries

    # 단일 일기 삭제
    @staticmethod
    async def delete_diary(diary: Diary):
        await diary.delete()
        return {"detail": "Diary deleted successfully"}

    #  요약 기능 (AI 제거)
    @staticmethod
    async def summarize_diary(diary_id: int, user_id: int):
        diary = await DiaryService.get_diary(user_id, diary_id)
        if not diary:
            return None
        return None  # AI 요약 기능 제거

    #  감정 분석 기능 (AI 제거)
    @staticmethod
    async def analyze_emotion(diary: Diary):
        return []  # AI 기능 제거

    #  단일 일기 감정 분석
    @staticmethod
    async def analyze_diary_emotions(diary_id: int, user_id: int):
        diary = await DiaryService.get_diary(user_id, diary_id)
        if not diary:
            return None
        return await DiaryService.analyze_emotion(diary)
