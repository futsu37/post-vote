from pydantic import BaseModel, Field, AliasPath
from typing import Optional
from datetime import datetime
from pydantic.config import ConfigDict
from app.models.friendship import Status

class FriendshipOut(BaseModel):
  sender_username: str = Field(validation_alias=AliasPath("sender","username"))
  receiver_username: str = Field(validation_alias=AliasPath("receiver","username"))
  requested_at: datetime
  status: Status

class FriendshipCreate(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  sender_id: int
  receiver_id: int
  status: Status
