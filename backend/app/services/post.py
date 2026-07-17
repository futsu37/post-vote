from typing import List

from app.models import User, Post
from app.schemas.post import PostOut, PostCreate, PostUserCreate, PostUpdate
from sqlalchemy.orm import Session
from app.utils.exceptions.http.exc_404 import http_404_exc_request_object_id_not_found
from app.utils.exceptions.http.exc_403 import (http_403_exc_forbidden_post_update_request, 
                                               http_403_exc_forbidden_post_delete_request)
from app.repository.post import create, get_all, get, update, delete
from app.services.user import existing_user

def get_post_or_404(post_id: int, db: Session) -> Post:
  existing_post = get(db, post_id)
  if not existing_post:
    raise http_404_exc_request_object_id_not_found(post_id,"Post")
  return existing_post

def create_post(post: PostUserCreate, db: Session, current_user: User) -> PostOut:
  post_schema = PostCreate(title=post.title, content=post.content, author_id=current_user.id)
  new_post = Post(**post_schema.model_dump())

  return create(db, new_post)

def get_current_user_posts(db: Session, current_user: User) -> List[PostOut]:
  return get_all(db,current_user.id)

def get_user_posts(user_id: int, db: Session) -> List[PostOut]:
  existing_user(user_id,db)
  
  return get_all(db,user_id)

def edit_post(post_id: int, updated_post: PostUpdate,db: Session, current_user: User) -> PostOut:
  
  post = get_post_or_404(post_id, db)
  valid_author = post.author_id == current_user.id
  if not valid_author:
    raise http_403_exc_forbidden_post_update_request()
  
  update_data = updated_post.model_dump(exclude_unset=True)

  for field, value in update_data.items():
      setattr(post, field, value)

  return update(post)

def delete_post(post_id: int, db: Session, current_user: User):
  post = get_post_or_404(post_id,db) 
  valid_author = post.author_id == current_user.id
  if not valid_author:
    raise http_403_exc_forbidden_post_delete_request()
  return delete(db, post)
  
  