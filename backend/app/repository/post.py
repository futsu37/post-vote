from typing import List

from sqlalchemy.orm import Session
from app.models.post import Post

def create(db: Session, post: Post) -> Post :
  db.add(post)
  db.commit()
  db.refresh(post)
  return post

def get_all(db: Session, author_id: int) -> List[Post]:
  return db.query(Post).filter(Post.author_id == author_id).all()

def get(db: Session, post_id: int) -> Post:
  return db.query(Post).filter(Post.id == post_id).first()

def update(db: Session, post: Post) -> Post:
  db.commit()
  db.refresh(post)
  return post
def delete(db: Session, post: Post):
  db.delete(post)
  db.commit()
  return {"Post was successfuly deleted!"}
  