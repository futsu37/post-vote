from typing import List

from app.models import User, Comment
from app.schemas.comment import CommentCreate,CommentUserCreate, CommentOut
from sqlalchemy.orm import Session
from app.repository import post, comment
from app.utils.exceptions.http.exc_404 import http_404_exc_request_object_id_not_found
from app.utils.exceptions.http.exc_403 import (http_403_exc_forbidden_comment_update_request,
                                               http_403_exc_forbidden_comment_delete_request)

def get_comment(comment_id: int, db: Session) -> CommentOut:
  existing_comment = comment.get(db,comment_id)
  if not existing_comment:
    raise http_404_exc_request_object_id_not_found(comment_id,"Comment")
  return existing_comment

def get_all_comments(post_id: int, db: Session) -> List[CommentOut]:
  existing_post = post.get(db, post_id)
  if not existing_post:
    raise http_404_exc_request_object_id_not_found(post_id,"Post")

  return comment.get_all(db, post_id)

def create_comment(post_id: int,
                   user_comment: CommentUserCreate,
                   db: Session,
                   current_user: User) -> CommentOut:
  existing_post = post.get(db, post_id)
  if not existing_post:
    raise http_404_exc_request_object_id_not_found(post_id,"Post")
  comment_schema = CommentCreate(content=user_comment.content,
                                 post_id=post_id,
                                 commenter_id=current_user.id)
  
  new_comment = Comment(**comment_schema.model_dump())
  return comment.create(db,new_comment)

def edit_comment(comment_id: int,
                 new_comment: CommentUserCreate,
                 db: Session,
                 current_user: User) -> CommentOut:
  existing_comment = comment.get(db,comment_id)
  if not existing_comment:
    raise http_404_exc_request_object_id_not_found(comment_id,"Comment")
  is_valid_comment = existing_comment.commenter_id == current_user.id
  if not is_valid_comment:
    raise http_403_exc_forbidden_comment_update_request()
  existing_comment.content = new_comment.content
  
  return comment.update(db,existing_comment)

def delete_comment(comment_id: int,
                 db: Session,
                 current_user: User):
  existing_comment = comment.get(db,comment_id) 
  if not existing_comment:
    raise http_404_exc_request_object_id_not_found(comment_id,"Comment")
  is_valid_comment = existing_comment.commenter_id == current_user.id
  if not is_valid_comment:
    raise http_403_exc_forbidden_comment_delete_request()
  
  return comment.delete(db,existing_comment)