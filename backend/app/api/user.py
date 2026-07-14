from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.user import UserOut, UserCreate
from app.core.dependencies import get_db
from app.services import user
from app.models.user import User
from app.core import dependencies
router = APIRouter(
  prefix=("/users"),
  tags=["User"]
)

@router.post("/",response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_create_form: UserCreate,db: Session = Depends(get_db)):
  return user.create_user(user_create_form, db)

@router.get("/current",response_model=UserOut)
def get_current_user(current_user: User = Depends(dependencies.get_current_user)):
  return current_user