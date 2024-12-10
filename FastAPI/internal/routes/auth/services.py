import authx

from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException, Cookie, Response

def set_tokens_in_cookies(response: Response, access_token: str, refresh_token: str):

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="Strict",
        max_age=timedelta(minutes=15)
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="Strict",
        max_age=timedelta(days=1)
    )

def get_current_user_from_cookies(access_token: str = Cookie(None)):

    if access_token is None:

        raise HTTPException(status_code=401, detail="Access token is missing")

    try:

        user = authx.decode_token(access_token)

        return user

    except Exception as e:

        raise HTTPException(status_code=401, detail="Invalid token")