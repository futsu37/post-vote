from app.models import User, Profile
from app.schemas.profile import ProfileOut, ProfileUserCreate, ProfileCreate
from app.utils.exceptions.http.exc_404 import http_404_exc_request_object_not_found
from app.utils.exceptions.http.exc_409 import http_409_exc_profile_create_request_conflict
from sqlalchemy.orm import Session
from app.services import user
from app.repository import profile

def get_user_profile_or_404(db: Session, user_id: int) -> Profile:
  user.get_user_or_404(db,user_id)
  existing_profile = profile.get(db,user_id)
  if not existing_profile:
    raise http_404_exc_request_object_not_found("Profile")
  return existing_profile

def get_current_user_profile(db: Session, current_user: User) -> ProfileOut:
  return get_user_profile_or_404(db,current_user.id) 

def get_profile(user_id: int, db: Session) -> ProfileOut:
  return get_user_profile_or_404(db,user_id)


def create_profile(profile_create: ProfileUserCreate,
                   db: Session, current_user: User) -> ProfileOut:
  existing_profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
  if existing_profile:
    raise http_409_exc_profile_create_request_conflict()
  valid_bio: str = ""
  if profile_create.bio:
    valid_bio = profile_create.bio

  profile_schema = ProfileCreate(bio=valid_bio,user_id=current_user.id)
  new_profile = Profile(**profile_schema.model_dump())
  return profile.create(db,new_profile)

def edit_profile(edited_profile: ProfileUserCreate,
                db: Session, 
                current_user: User) -> ProfileOut:
  existing_profile = get_user_profile_or_404(db,current_user.id)
  existing_profile.bio = edited_profile.bio

  return profile.update(db,existing_profile)

def delete_profile(db: Session, 
                   current_user: User):
  existing_profile = get_user_profile_or_404(db,current_user.id)
  return profile.delete(db,existing_profile)
