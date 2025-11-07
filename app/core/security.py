from passlib.context import CryptContext

# 비밀번호 암호화를 위한 bcrypt 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    비밀번호를 bcrypt 알고리즘으로 해시합니다.
    """
    if not password:
        raise ValueError("비밀번호가 비어 있습니다.")
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    사용자가 입력한 비밀번호가 저장된 해시와 일치하는지 확인합니다.
    """
    if not plain_password or not hashed_password:
        return False
    return pwd_context.verify(plain_password, hashed_password)
