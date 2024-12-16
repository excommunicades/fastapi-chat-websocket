from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from authx import AuthX
from jose import JWTError, jwt
from typing import Optional

from FastAPI.pkg.jwt.jwt_config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    SECRET_KEY,
    ALGORITHM
)


class JWTRepository:

    def create_access_token(data: dict, expires_delta: Optional[int] = None):

        to_encode = data.copy()

        if expires_delta:

            to_encode.update({"exp": expires_delta})

        else:

            to_encode.update({"exp": ACCESS_TOKEN_EXPIRE_MINUTES})

        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return encoded_jwt