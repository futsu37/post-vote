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
from app.services import user

router = APIRouter(
  prefix=("/profiles"),
  tags=["Profile"]
)
def get_user_profile(db: Session, user_id: int):
  user.get_user_or_404(db,user_id)
  profile = db.query(Profile).filter(Profile.user_id == user_id).first()
  if not profile:
    raise http_404_exc_request_object_not_found("Profile")
  return profile

@router.get("/current/",response_model=ProfileOut)
def get_current_user_profile(db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)):
  return get_user_profile(db,current_user.id)

@router.get("/{user_id}",response_model=ProfileOut)
def get_profile(user_id: int,
                db: Session = Depends(get_db)):
  return get_user_profile(db,user_id)

@router.post("/",response_model=ProfileOut)
def create_profile(profile_create: ProfileUserCreate,
                   db: Session = Depends(get_db), 
                   current_user: User = Depends(get_current_user)):
  existing_profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
  if existing_profile:
    raise http_409_exc_profile_create_request_conflict()
  valid_bio: str = ""
  if profile_create.bio:
    valid_bio = profile_create.bio

  profile_schema = ProfileCreate(bio=valid_bio,user_id=current_user.id)
  profile = Profile(**profile_schema.model_dump())
  db.add(profile)
  db.commit()
  db.refresh(profile)
  return profile

@router.patch("/",response_model=ProfileOut)
def edit_profile(edited_profile: ProfileUserCreate,
                db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)):
  existing_profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
  if not existing_profile:
    raise http_404_exc_request_object_not_found("Profile")
  existing_profile.bio = edited_profile.bio
  db.commit()
  db.refresh(existing_profile)
  return existing_profile
@router.delete("/")
def delete_profile(db: Session = Depends(get_db), 
                   current_user: User = Depends(get_current_user)):
  existing_profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
  if not existing_profile:
    raise http_404_exc_request_object_not_found("Profile")

  db.delete(existing_profile)
  db.commit()
  return {"Profile was successfully deleted!"}