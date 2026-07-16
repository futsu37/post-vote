from typing import List

from sqlalchemy.orm import Session
from app.models.comment import Comment

def create(db: Session, Comment: Comment) -> Comment :
  db.add(Comment)
  db.commit()
  db.refresh(Comment)
  return Comment

def get_all(db: Session, post_id: int) -> List[Comment]:
  return db.query(Comment).filter(Comment.post_id == post_id).all()

def get(db: Session, comment_id: int) -> Comment:
  return db.query(Comment).filter(Comment.id == comment_id).first()

def update(db: Session, comment: Comment) -> Comment:
  db.commit()
  db.refresh(comment)
  return comment
def delete(db: Session, comment: Comment):
  db.delete(comment)
  db.commit()
  return {"Comment was successfuly deleted!"}