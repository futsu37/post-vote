from typing import List

from fastapi import APIRouter, Depends
from app.core.dependencies import get_db, get_current_user
from app.models import User, Profile
from app.schemas.post import PostOut, PostUserCreate, PostUpdate
from app.schemas.profile import ProfileOut, ProfileUserCreate, ProfileCreate
from app.utils.exceptions.http.exc_404 import http_404_exc_request_object_id_not_found, http_404_exc_request_object_not_found
from app.utils.exceptions.http.exc_409 import http_409_exc_profile_create_request_conflict
from app.schemas.comment import CommentOut
from sqlalchemy.orm import Session
from app.services import user,profile

router = APIRouter(
  prefix=("/profiles"),
  tags=["Profile"]
)

@router.get("/current/",response_model=ProfileOut)
def get_current_user_profile(db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)):
  return profile.get_current_user_profile(db,current_user)

@router.get("/{user_id}",response_model=ProfileOut)
def get_profile(user_id: int,
                db: Session = Depends(get_db)):
  return profile.get_profile(user_id,db)

@router.post("/",response_model=ProfileOut)
def create_profile(profile_create: ProfileUserCreate,
                   db: Session = Depends(get_db), 
                   current_user: User = Depends(get_current_user)):
  return profile.create_profile(profile_create,db,current_user)

@router.patch("/",response_model=ProfileOut)
def edit_profile(edited_profile: ProfileUserCreate,
                db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)):
  return profile.edit_profile(edited_profile,db,current_user)

@router.delete("/")
def delete_profile(db: Session = Depends(get_db), 
                   current_user: User = Depends(get_current_user)):
  return profile.delete_profile(db, current_user)