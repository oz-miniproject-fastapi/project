from tortoise import fields, models


class EmotionKeyword(models.Model):
    """
    감정 키워드 모델
    - 예: 행복, 슬픔, 분노 등
    - Diary 모델과 다대다 관계를 가짐
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)

    # 다대다: Diary
    diaries: fields.ManyToManyRelation["Diary"]

    class Meta:
        table = "emotion_keywords"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name
