from typing import List

from fastapi import APIRouter, Depends
from app.core.dependencies import get_db, get_current_user
from app.models import User
from sqlalchemy.orm import Session
from app.schemas.like import LikeOut
from app.services import like
router = APIRouter(
  prefix=("/likes"),
  tags=["Like"]
)

@router.get("/{post_id}", response_model=List[LikeOut])
def get_likes(post_id: int, 
              db: Session = Depends(get_db)):
  return like.get_likes(post_id,db)

@router.post("/{post_id}",response_model=LikeOut)
def like_post(post_id: int, 
              db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)):
  return like.like_post(post_id,db,current_user)
@router.delete("/{post_id}")
def remove_like(post_id: int, 
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
  return like.remove_like(post_id,db,current_user)