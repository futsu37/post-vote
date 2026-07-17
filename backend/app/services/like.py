from typing import List

from app.models import User, Like
from app.schemas.like import LikeOut, LikeCreate
from sqlalchemy.orm import Session
from app.repository import like
from app.utils.exceptions.http.exc_404 import http_404_exc_request_object_not_found
from app.utils.exceptions.http.exc_409 import http_409_exc_like_post_request_conflict
from app.services.post import get_post_or_404 
def get_like_or_404(db: Session, post_id: int, user_id: int) -> Like:
  existing_like = like.get(db,post_id,user_id)
  if not existing_like:
    raise http_404_exc_request_object_not_found("Like")
  return existing_like

def get_likes(post_id: int, db: Session) -> List[LikeOut]:
  get_post_or_404(post_id, db)

  return like.get_all(db,post_id)

def like_post(post_id: int, db: Session, current_user: User) -> LikeOut:
  get_post_or_404(post_id, db)
  existing_like = like.get(db,post_id,current_user.id)
  if existing_like:
      raise http_409_exc_like_post_request_conflict()

  liked_post_schema = LikeCreate(post_id=post_id,user_id=current_user.id) 
  liked_post = Like(**liked_post_schema.model_dump())
  return like.create(db,liked_post)

def remove_like(post_id: int, db: Session, current_user: User):
  get_post_or_404(post_id, db)
  existing_like = get_like_or_404(db,post_id,current_user.id)
  return like.remove(db, existing_like)

