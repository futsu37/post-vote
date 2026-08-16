from typing import List

from fastapi import APIRouter, Depends
from app.core.dependencies import get_db, get_current_user
from app.models import User
from app.schemas.comment import CommentUserCreate, CommentOut
from sqlalchemy.orm import Session

from app.services import comment
router = APIRouter(
  prefix=("/comments"),
  tags=["Comment"]
)

@router.get("/all/{post_id}", response_model=List[CommentOut])
def get_all_comments(post_id: int,
                    db: Session = Depends(get_db)):
  return comment.get_all_comments(post_id,db)

@router.get("/{comment_id}", response_model=CommentOut)
def get_comment(comment_id: int,
                    db: Session = Depends(get_db)):
  return comment.get_comment(comment_id,db)

@router.post("/{post_id}",response_model=CommentOut)
def create_comment(post_id: int,
                   user_comment: CommentUserCreate,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
  return comment.create_comment(post_id,user_comment,db,current_user)

@router.patch("/{comment_id}", response_model=CommentOut)
def edit_comment(comment_id: int,
                 new_comment: CommentUserCreate,
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)):
  return comment.edit_comment(comment_id,new_comment,db,current_user)

@router.delete("/{comment_id}")
def delete_comment(comment_id: int,
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)):
  return comment.delete_comment(comment_id,db,current_user)