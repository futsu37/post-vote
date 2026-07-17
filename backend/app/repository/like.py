from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.models.like import Like

def create(db: Session, like: Like) -> Like:
  db.add(like)
  db.commit()
  db.refresh(like)
  return like

def get(db: Session, post_id: int, user_id: int) -> Like:
  return db.query(Like).filter(
    and_(Like.post_id == post_id,
         Like.user_id == user_id)).first()

def get_all(db: Session, post_id: int) -> List[Like]:
  return db.query(Like).filter(Like.post_id == post_id).all()

def remove(db: Session, like: Like):
  db.delete(like)
  db.commit()
  return {"Like was successfully removed!"}
