from pydantic import BaseModel, EmailStr
from pydantic.config import ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  username: str
  display_name: str
  email: EmailStr
  password: str

class UserOut(BaseModel):
  id: int
  username: str
  display_name: str
  created_at: datetime