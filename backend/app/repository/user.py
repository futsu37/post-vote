from sqlalchemy.orm import Session
from app.models.user import User

def create(db: Session, user: User) -> User :
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def get_by_id(db: Session, user_id: int) -> User:
  return db.query(User).filter(User.id == user_id).first()

def get_by_username(db: Session, username: str) -> User:
  return db.query(User).filter(User.username == username).first()