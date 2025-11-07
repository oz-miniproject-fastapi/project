from app.models.tag import Tag


class TagRepository:
    """
    Tag 모델의 데이터 접근을 담당하는 Repository 클래스
    """

    @staticmethod
    async def get_or_create(name: str) -> Tag:
        """
        태그 이름으로 조회 후, 없으면 새로 생성합니다.
        """
        if not name or not name.strip():
            raise ValueError("태그 이름은 비어 있을 수 없습니다.")
        tag, _ = await Tag.get_or_create(name=name.strip())
        return tag

    @staticmethod
    async def list_all() -> list[Tag]:
        """
        모든 태그 목록을 반환합니다.
        """
        return await Tag.all().order_by("id")
