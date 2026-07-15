from pydantic.config import ConfigDict
from pydantic import BaseModel, AliasPath, Field
from datetime import datetime

class PostUserCreate(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  title: str
  content: str

class PostUpdate(PostUserCreate):
  model_config = ConfigDict(from_attributes=True)
  
  title: str | None = None
  content: str | None = None

class PostCreate(PostUserCreate):
  author_id: int


  
class PostOut(BaseModel):
  id: int
  author_id: int
  author_display_name: str = Field(validation_alias=AliasPath("author","display_name"))
  title: str
  content: str
  created_at: datetime
