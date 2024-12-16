from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from FastAPI.pkg.jwt.jwt_config import JWT_SECRET_KEY, ALGORITHM
from FastAPI.pkg.db.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="access_token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    print(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Couldn\'t validate creditials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:

        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        username: str = payload.get('sub')

        if username is None:

            raise credentials_exception

        return User(username=username)

    except JWTError:

        raise credentials_exception