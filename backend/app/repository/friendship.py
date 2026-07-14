from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from app.models.friendship import Friendship, Status
from app.models.user import User
from typing import List

def get_all(db: Session, current_user: User) -> List[Friendship]:
    friendship = db.query(Friendship).filter(
    or_( 
      and_(Friendship.sender_id == current_user.id, Friendship.status == Status.ACCEPTED),
      and_(Friendship.receiver_id == current_user.id, Friendship.status == Status.ACCEPTED)
    )).all()
    return friendship

def create(db: Session, friendship: Friendship) -> Friendship:
  db.add(friendship)
  db.commit()
  db.refresh(friendship)
  return friendship

def update(db: Session, friendship: Friendship) -> Friendship:
  db.commit()
  db.refresh(friendship)
  return friendship

def get(db: Session, user_1: User, user_2: User) -> Friendship:
  friendship = db.query(Friendship).filter(
    or_( 
      and_(Friendship.sender_id == user_1.id, Friendship.receiver_id == user_2.id),
      and_(Friendship.receiver_id == user_1.id, Friendship.sender_id == user_2.id)
    )).first()
  return friendship
def delete(db: Session, friendship: Friendship):
  db.delete(friendship)
  db.commit()
  return {"Friendship was successfully deleted!"}
