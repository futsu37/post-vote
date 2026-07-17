from sqlalchemy.orm import Session

from app.schemas.user import  UserCreate
from app.models.user import User
from app.core.security.hash import hash_password
from app.repository.user import create, get_by_username
from app.utils.exceptions.http.exc_409 import http_409_exc_username_request_conflict
from app.utils.exceptions.http.exc_404 import http_404_exc_request_object_id_not_found

def get_user_or_404(db: Session,user_id: int) -> User:
  existing_user = db.query(User).filter(User.id == user_id).first()
  if not existing_user:
    raise http_404_exc_request_object_id_not_found(user_id,"User")
  return existing_user

def create_user(user_create_form: UserCreate,db: Session) -> User:
  new_user = User(**user_create_form.model_dump())
  if get_by_username(new_user.username):
    raise http_409_exc_username_request_conflict()
  new_user.password = hash_password(new_user.password)
  return create(db, new_user)

def existing_user(db: Session, user_id: int) -> User:
  return get_user_or_404(db,user_id)