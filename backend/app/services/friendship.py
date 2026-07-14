from app.schemas.friendship import FriendshipCreate
from sqlalchemy.orm import Session
from app.utils.exceptions.http.exc_404 import (http_404_exc_request_object_id_not_found,
                                               http_404_exc_request_object_not_found)
from app.utils.exceptions.http.exc_403 import http_403_forbidden_befriend_oneself_request
from app.utils.exceptions.http.exc_409 import (http_409_exc_friendship_request_pending_conflict, 
                                               http_409_exc_friendship_request_accepted_conflict)
from app.models.user import User
from app.models.friendship import Friendship, Status
from app.repository import user, friendship
def get_friends(db: Session, current_user: User):
  return friendship.get_all(db, current_user)

def send_friend_request(receiver_id: int, current_user: User,db: Session):
  if receiver_id == current_user.id:
    raise http_403_forbidden_befriend_oneself_request()

  receiver = user.get_by_id(receiver_id)

  if not receiver:
    raise http_404_exc_request_object_id_not_found(id=receiver_id,object_name="User")

  existing_friendship = friendship.get(db,current_user, receiver)

  if existing_friendship:
    if existing_friendship.status == Status.PENDING:
      raise http_409_exc_friendship_request_pending_conflict()
    else:
      raise http_409_exc_friendship_request_accepted_conflict()

  friendship_schema = FriendshipCreate(receiver_id=receiver_id,sender_id=current_user.id,status=Status.PENDING)
  new_friendship = Friendship(**friendship_schema.model_dump())
  return friendship.create(db, new_friendship)

def receive_friend_requset(sender_id: int, current_user: User, db: Session):
  if sender_id == current_user.id:
    raise http_403_forbidden_befriend_oneself_request()
  
  sender = user.get_by_id(sender_id)

  if not sender:
    raise http_404_exc_request_object_id_not_found(id=sender_id,object_name="User")
  
  existing_friendship = friendship.get(db,current_user, sender)
  
  if not existing_friendship:
    raise http_404_exc_request_object_not_found(object_name="Friendship")
  if existing_friendship.status == Status.ACCEPTED:
    raise http_409_exc_friendship_request_accepted_conflict()
  
  existing_friendship.status = Status.ACCEPTED
  friendship.update(db, existing_friendship)
  return {f"You've accepted friend request from {sender.username}"}

def remove_friendship(other_user_id: int, current_user: User, db: Session):
  if other_user_id == current_user.id:
    raise http_403_forbidden_befriend_oneself_request()
  
  other_user = user.get_by_id(db,other_user_id)
  
  if not other_user:
    raise http_404_exc_request_object_id_not_found(id=other_user_id,object_name="User")

  existing_friendship = friendship.get(db,other_user,current_user)
  if not existing_friendship:
    raise http_404_exc_request_object_not_found(object_name="Friendship")
  return friendship.delete(db, existing_friendship)

def reject_friend_request(sender_id: int, current_user: User, db: Session):
  return remove_friendship(sender_id,current_user,db)

def remove_friend(friend_id: int, current_user: User, db: Session):
  return remove_friendship(friend_id, current_user, db)

def cancel_friend_request(receiver_id: int, current_user: User, db: Session):
  return remove_friendship(receiver_id, current_user, db)
