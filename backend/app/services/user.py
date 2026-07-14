from sqlalchemy.orm import Session

from app.schemas.user import  UserCreate
from app.models.user import User
from app.core.security.hash import hash_password
from app.repository.user import create, get_by_username
from app.utils.exceptions.http.exc_409 import http_409_exc_username_request_conflict

def create_user(user_create_form: UserCreate,db: Session) -> User:
  new_user = User(**user_create_form.model_dump())
  if get_by_username(new_user.username):
    raise http_409_exc_username_request_conflict()
  new_user.password = hash_password(new_user.password)
  return create(db, new_user)