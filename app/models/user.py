from tortoise import fields, models


class User(models.Model):
    """
    사용자(User) 모델
    - 기본 회원 정보 및 인증 상태를 관리
    - Diary 모델과 1:N 관계 (한 사용자는 여러 일기를 작성 가능)
    """

    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    nickname = fields.CharField(max_length=50, null=True)
    name = fields.CharField(max_length=50, null=True)
    phone = fields.CharField(max_length=20, null=True)
    is_verified = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)

    # 다이어리 역참조: 한 사용자가 작성한 여러 일기
    diaries: fields.ReverseRelation["Diary"]

    class Meta:
        table = "users"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.email} ({self.nickname or 'No nickname'})"
