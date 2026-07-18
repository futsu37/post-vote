from sqlalchemy.orm import Session
from app.models.profile import Profile

def create(db: Session, profile: Profile) -> Profile:
  db.add(profile)
  db.commit()
  db.refresh(profile)
  return profile

def get(db: Session, user_id: int) -> Profile:
  return db.query(Profile).filter(Profile.user_id == user_id).first()

def update(db: Session, profile: Profile) -> Profile:
  db.commit()
  db.refresh(profile)
  return profile

def delete(db: Session, profile: Profile):
  db.delete(profile)
  db.commit()
  return {"Profile was successfuly deleted!"}
  