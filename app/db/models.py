from tortoise import fields
from tortoise.models import Model


class User(Model):
    """
    사용자 정보를 저장하는 모델
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100, unique=True)

    class Meta:
        table = "users"

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"
