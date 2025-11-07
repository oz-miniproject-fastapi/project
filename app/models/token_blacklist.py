from tortoise import fields, models


class TokenBlacklist(models.Model):
    """
    만료되었거나 무효화된 JWT 토큰을 저장하는 블랙리스트 테이블.
    주로 로그아웃 처리나 토큰 차단 시 사용됩니다.
    """

    id = fields.IntField(pk=True)
    token = fields.CharField(max_length=512, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "token_blacklist"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"TokenBlacklist(id={self.id})"
