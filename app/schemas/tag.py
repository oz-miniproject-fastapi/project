from pydantic import BaseModel


class TagCreate(BaseModel):
    # 태그 생성 요청
    name: str


class TagRead(BaseModel):
    # 태그 응답
    id: int
    name: str

    class Config:
        orm_mode = True
