from app.repositories.tag_repo import TagRepository


class TagService:
    # 태그 관련 비즈니스 로직 처리
    def __init__(self):
        self.repo = TagRepository()

    async def list_tags(self):
        # 전체 태그 목록 조회
        return await self.repo.list_all()
