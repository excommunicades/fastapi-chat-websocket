from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from FastAPI.internal.routes.auth.auth import aouth2_scheme
from FastAPI.pkg.jwt.jwt_config import JWT_SECRET_KEY, ALGORITHM
from FastAPI.pkg.db.models import User
def get_current_user(token: str = Depends(aouth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Couldn\'t validate creditials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:

        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')

        if username is None:

            raise credentials_exception

        return User(username=username)

    except JWTError:

        raise credentials_exception