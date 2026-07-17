from pydantic import BaseModel, Field, AliasPath
from datetime import datetime
from pydantic.config import ConfigDict

class LikeOut(BaseModel):
  post_title: str = Field(validation_alias=AliasPath("post","title"))
  user_display_name: str = Field(validation_alias=AliasPath("user","display_name"))

class LikeCreate(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  post_id: int
  user_id: int
