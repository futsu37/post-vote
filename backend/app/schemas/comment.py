from pydantic import BaseModel, Field, AliasPath
from datetime import datetime
from pydantic.config import ConfigDict

class CommentOut(BaseModel):
  commenter_display_name: str = Field(validation_alias=AliasPath("commenter","display_name"))
  commenter_username: str = Field(validation_alias=AliasPath("commenter","username"))
  post_id: int = Field(validation_alias=AliasPath("post","id"))
  post_title: str = Field(validation_alias=AliasPath("post","title"))
  content: str
  created_at: datetime

class CommentUserCreate(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  content: str

class CommentCreate(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  content: str
  post_id: int
  commenter_id: int

