from fastapi import APIRouter, Depends
from app.schemas.friendship import FriendshipOut
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.services import friendship
from typing import List
router = APIRouter(
  prefix="/friendships",
  tags=["Friendship"]
)
@router.get("/friends", response_model=List[FriendshipOut])
def get_friends(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
  return friendship.get_friends(db,current_user)

@router.post("/send/{receiver_id}",response_model=FriendshipOut)
def send_friend_request(receiver_id: int, 
                        current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
 
  return friendship.send_friend_request(receiver_id,current_user,db)

@router.patch("/receive/{sender_id}")
def receive_friend_requset(sender_id: int, 
                        current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
 
  return friendship.receive_friend_requset(sender_id,current_user,db)

@router.delete("/reject/{sender_id}")
def reject_friend_request(sender_id: int, 
                        current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
  
  return friendship.reject_friend_request(sender_id, current_user, db)
@router.delete("/remove/{friend_id}")
def remove_friend(friend_id: int, 
                  current_user: User = Depends(get_current_user),
                  db: Session = Depends(get_db)):
  
  return friendship.remove_friend(friend_id, current_user, db)

@router.delete("/reject/{receiver_id}")
def cancel_friend_request(receiver_id: int, 
                        current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
  
  return friendship.cancel_friend_request(receiver_id, current_user, db)


  

