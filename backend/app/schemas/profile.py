from pydantic import BaseModel, Field, AliasPath
from pydantic.config import ConfigDict

class ProfileOut(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  display_name: str = Field(validation_alias=AliasPath("user","display_name"))
  username: str = Field(validation_alias=AliasPath("user","username"))
  bio: str | None

class ProfileUserCreate(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  bio: str | None = None

class ProfileCreate(BaseModel):
  bio: str | None
  user_id: int

