from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from FastAPI.pkg.jwt.jwt_config import JWT_SECRET_KEY, ALGORITHM
from FastAPI.pkg.db.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="access_token")

import time

def get_current_user(request: Request):

    token = request.cookies.get('access_token')

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        if not token:
            token = request.cookies.get('access_token')

        if not token:
            raise credentials_exception
        
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])

        if 'exp' in payload and payload['exp'] < time.time():
            raise credentials_exception

        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

        return User(username=username)

    except JWTError:

        raise credentials_exception
