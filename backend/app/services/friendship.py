from app.schemas.friendship import FriendshipCreate
from sqlalchemy.orm import Session
from app.utils.exceptions.http.exc_404 import (http_404_exc_request_object_not_found)
from app.utils.exceptions.http.exc_403 import (http_403_exc_forbidden_befriend_oneself_request,
                                               http_403_exc_forbidden_friend_sender_operation_request,)
from app.utils.exceptions.http.exc_409 import (http_409_exc_friendship_request_pending_conflict, 
                                               http_409_exc_friendship_request_accepted_conflict)
from app.models.user import User
from app.models.friendship import Friendship, Status
from app.repository import friendship
from app.services.user import get_user_or_404

def get_frinedship_or_404(db: Session, user_1: User, user_2: User) -> Friendship:
  existing_friendship = friendship.get(db,user_1, user_2)
  if not existing_friendship:
    raise http_404_exc_request_object_not_found(object_name="Friendship")
  return existing_friendship

def get_friends(db: Session, current_user: User):
  return friendship.get_all(db, current_user)

def send_friend_request(receiver_id: int, current_user: User,db: Session):
  if receiver_id == current_user.id:
    raise http_403_exc_forbidden_befriend_oneself_request()

  receiver = get_user_or_404(db,receiver_id)

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
    raise http_403_exc_forbidden_befriend_oneself_request()
  
  sender = get_user_or_404(db,sender_id)
  
  existing_friendship = get_frinedship_or_404(db,current_user,sender)

  if existing_friendship.status == Status.ACCEPTED:
    raise http_409_exc_friendship_request_accepted_conflict()
  if existing_friendship.sender_id == current_user.id:
    raise http_403_exc_forbidden_friend_sender_operation_request()
  
  existing_friendship.status = Status.ACCEPTED
  friendship.update(db, existing_friendship)
  return {f"You've accepted friend request from {sender.username}"}

def remove_friendship(friend_id: int, current_user: User, db: Session):
  
  sender = get_user_or_404(db,friend_id)
  existing_friendship = get_frinedship_or_404(db, sender, current_user)
  
  return friendship.delete(db, existing_friendship)


