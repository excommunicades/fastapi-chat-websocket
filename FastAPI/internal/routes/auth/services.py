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