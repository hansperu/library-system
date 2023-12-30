from jwt import encode, decode, PyJWTError 
from fastapi.security import HTTPBearer
from pydantic import BaseModel

from src.models.user import Role


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request):
        credentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPBearer(auto_error=False)
            return credentials.credentials
        else:
            raise HTTPBearer(auto_error=False)


class JwtPayload(BaseModel):
    user_id: int
    role: Role


def encode_jwt(payload: JwtPayload, secret: str, algorithm: str = "HS256") -> str:
    payload_json =payload.model_dump()
    print(payload_json)
    token = encode(payload_json, secret, algorithm=algorithm)
    return token


def decode_jwt(token: str, secret: str, algorithm: str = "HS256") -> dict:
    try:
        data = decode(token, secret, algorithms=[algorithm])
        return data
    except PyJWTError:
        return {}