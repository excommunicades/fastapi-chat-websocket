import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy.orm import Session

from authx import AuthX, AuthXConfig

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from FastAPI.pkg.db.database import get_db
from FastAPI.pkg.db.repositories import UserRepository

from FastAPI.internal.routes.auth.schemas import (
    RegistrationSchema,
    LoginSchema,
)
from FastAPI.internal.routes.auth.services import (
    get_current_user_from_cookies,
)

router = APIRouter(
    prefix='/auth',
    tags=['User services']
)

config = AuthXConfig()
config.JWT_SECRET_KEY="SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME="access_token"
config.JWT_TOKEN_LOCATION=["cookies"]

security = AuthX(config=config)

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
async def login_user(data:LoginSchema, response: Response,  userRepository: UserRepository = Depends(get_user_service)):

    try:

        return userRepository.login(response=response, email=data.email, password=data.password)

    except HTTPException as e:

        return JSONResponse(
                status_code=e.status_code,
                content={
                    "errors": e.detail,
                })
