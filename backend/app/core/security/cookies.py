from fastapi import Response


def set_access_token_cookie(response: Response,access_token: str):
  response.set_cookie(
    key="access_token",
    value=access_token,
    secure=False,
    httponly=True,
    samesite="lax"
  )