from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.core import dependencies
from app.services import authentication

router = APIRouter(
  prefix="/login",
  tags=["Authentication"]
)

@router.post("/", status_code=status.HTTP_200_OK)
def log_in(response: Response,
          data_form: OAuth2PasswordRequestForm = Depends(), 
          db: Session = Depends(dependencies.get_db)):
  return authentication.log_in(response,data_form,db)