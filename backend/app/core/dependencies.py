from fastapi import Depends, Cookie
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.repository.user import get_by_id
from app.schemas.token import TokenData

from app.utils.exceptions.http.exc_403 import http_403_exc_forbidden_request_credentials
from app.core.security.authorization import verify_access_token


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def get_current_user(access_token: str = Cookie(None),db: Session = Depends(get_db)):
  if not access_token:
    raise http_403_exc_forbidden_request_credentials()
  
  data: TokenData = verify_access_token(access_token)
  current_user = get_by_id(db,data.id)


  if not current_user:
    raise http_403_exc_forbidden_request_credentials()
  return current_user