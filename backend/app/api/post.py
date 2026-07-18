from typing import List

from fastapi import APIRouter, Depends
from app.core.dependencies import get_db, get_current_user
from app.models import User
from app.schemas.post import PostOut, PostUserCreate, PostUpdate
from app.schemas.like import LikeOut
from app.schemas.comment import CommentOut
from sqlalchemy.orm import Session
from app.services import post 

router = APIRouter(
  prefix=("/posts"),
  tags=["Post"]
)

@router.get("/all",response_model=List[PostOut])
def get_current_user_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return post.get_all(db,current_user.id)

@router.get("/all/{user_id}",response_model=List[PostOut])
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
  return post.get_all(db,user_id)

@router.post("/",response_model=PostOut)
def create_post(post_data: PostUserCreate, 
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):

  return post.create_post(post_data,db, current_user)

@router.put("/{post_id}",response_model=PostOut)
def edit_post(post_id: int,
              updated_post: PostUpdate,
              db: Session = Depends(get_db), 
              current_user: User = Depends(get_current_user)):
  return post.edit_post(post_id,updated_post,db,current_user)

@router.delete("/{post_id}")
def delete_post(post_id: int, 
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
  return post.delete_post(post_id,db,current_user)
  
  