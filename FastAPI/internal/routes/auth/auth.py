import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy.orm import Session

from authx import AuthX
from authx.models import AuthConfig

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from FastAPI.pkg.db.database import get_db
from FastAPI.pkg.db.repositories import UserRepository

from FastAPI.internal.routes.auth.schemas import (
    RegistrationSchema,
    LoginSchema,
)

router = APIRouter(
    prefix='/auth',
    tags=['User services']
)

authx = AuthX(
    AuthConfig(
        secret=os.getenv("SECRET_KEY"),
        algorithms=["HS256"],  
    )
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user_service(db: Session = Depends(get_db)):

    return UserRepository(db)


@router.post("/register")
def register_user(data: RegistrationSchema, userRepository: UserRepository = Depends(get_user_service)):

    try:

        return userRepository.register(username=data.username, email=data.email, password=data.password)

    except HTTPException as e:

        return JSONResponse(
                status_code=e.status_code,
                content={
                    "errors": e.detail,
                })

@router.post("/login")
def login_user(data:LoginSchema,  userRepository: UserRepository = Depends(get_user_service)):

    try:

        return userRepository.login(email=data.email, password=data.password)

    except HTTPException as e:

        return JSONResponse(
                status_code=e.status_code,
                content={
                    "errors": e.detail,
                })
