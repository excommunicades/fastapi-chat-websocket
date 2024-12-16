from datetime import datetime, timedelta
from jose import jwt
from typing import Optional

from FastAPI.pkg.jwt.jwt_config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_SECRET_KEY,
    ALGORITHM
)


class JWTRepository:

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[int] = None):

        to_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + timedelta(minutes=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)

        return encoded_jwt