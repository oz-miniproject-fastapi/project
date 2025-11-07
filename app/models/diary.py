from tortoise import fields, models


class Diary(models.Model):
    """
    사용자 일기 모델
    - 제목, 내용, 작성자, 작성/수정 시간 관리
    - Tag 및 EmotionKeyword 모델과 다대다 관계
    """

    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField(
        "models.User",
        related_name="diaries",
        on_delete=fields.CASCADE,
    )
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # 다대다: Tag
    tags: fields.ManyToManyRelation["Tag"] = fields.ManyToManyField(
        "models.Tag",
        related_name="diaries",
        through="diary_tag",
    )

    # 다대다: EmotionKeyword
    emotion_keywords: fields.ManyToManyRelation["EmotionKeyword"] = fields.ManyToManyField(
        "models.EmotionKeyword",
        related_name="diaries",
        through="diary_emotion",
    )

    class Meta:
        table = "diaries"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"
