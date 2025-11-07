from app.repositories.token_repo import TokenRepository


class TokenService:
    # 토큰 관련 비즈니스 로직
    def __init__(self):
        self.repo = TokenRepository()

    async def blacklist_token(self, token: str):
        # 토큰을 블랙리스트에 추가 (로그아웃 처리)
        await self.repo.add(token)
        return {"message": "로그아웃 완료"}
