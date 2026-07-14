from fastapi import Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from app.core.security.authorization import create_access_token
from app.utils.exceptions.http.exc_401 import http_401_exc_unauthorized_request
from app.core.security.hash import verify_password
from app.repository.user import get_by_username
from app.core.security.cookies import set_access_token_cookie

def log_in(response: Response,
          data_form: OAuth2PasswordRequestForm, 
          db: Session):
  
  existing_user = get_by_username(db,data_form.username)

  if not existing_user:
    raise http_401_exc_unauthorized_request()
  if not verify_password(data_form.password,existing_user.password):
    raise http_401_exc_unauthorized_request()

  access_token = create_access_token({"user_id":existing_user.id})
  set_access_token_cookie(response,access_token)

  return {"message":f"logged in as {existing_user.username}"}