import authx
from datetime import timedelta

from passlib.context import CryptContext

from sqlalchemy.orm import Session

from fastapi import HTTPException
from fastapi.responses import JSONResponse

from FastAPI.pkg.db.models import User
from FastAPI.pkg.jwt.repositories import JWTRepository

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def check_password(stored_hash: str, password: str) -> bool:
    return pwd_context.verify(password, stored_hash)

class UserRepository:

    def __init__(self, db: Session):

        self.db = db

    def register(self, username: str, email: str, password: str) -> JSONResponse:

        if self.db.query(User).filter_by(email=email).first():

            raise HTTPException(status_code=400, detail="User with this email already exist.")

        hashed_password = hash_password(password=password)

        user = User(username=username, email=email, password=hashed_password)

        self.db.add(user)
        self.db.commit()

        return JSONResponse(status_code=201, content={"Message": "You are registered successfully!"})

    def login(self, response: str, email: str, password: str) -> JSONResponse:

        if not self.db.query(User).filter_by(email=email).first():

            raise HTTPException(status_code=400, detail="User does not exist.")

        user = self.db.query(User).filter_by(email=email).first()


        if check_password(password=password, stored_hash=user.password):

            access_token = JWTRepository.create_access_token(data={"sub": user.username})

            response = JSONResponse(status_code=200, content={"message": "Success login!"})

            response.set_cookie(key='access_token', value=access_token, httponly=True)

            return response
  
        raise HTTPException(status_code=401, detail="Invalid password.")
