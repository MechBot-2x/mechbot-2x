# security/jwt_manager.py
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
    argon2__rounds=4,
    argon2__memory_cost=1024,
    argon2__parallelism=2
)

def create_jwt(data: dict, secret: str) -> str:
    return jwt.encode(
        claims=data,
        key=secret,
        algorithm="HS512",
        headers={"kid": "v1"}
    )
