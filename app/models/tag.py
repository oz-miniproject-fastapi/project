from tortoise import fields, models


class Tag(models.Model):
    """
    일기(Diary)에 연결되는 태그 모델
    예: 여행, 가족, 공부 등
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)

    # 다대다 역참조: Diary 모델에서 tags 필드로 접근 가능
    diaries: fields.ReverseRelation["Diary"]

    class Meta:
        table = "tags"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name
