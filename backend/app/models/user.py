from sqlalchemy import DateTime
import uuid
from datetime import datetime
from typing import TYPE_CHECKING
from app.utils.time import get_datetime_utc
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.friendship import Friendship
    from app.models.post import Post
    from app.models.comment import Comment
    from app.models.like import Like


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, nullable=False, max_length=128)
    display_name: str = Field(nullable=False, max_length=128)
    email: str = Field(unique=True, nullable=False, max_length=255)
    hashed_password: str
    created_at: datetime | None = Field(
      default_factory=get_datetime_utc,
      sa_type=DateTime(timezone=True) # type: ignore
    )
    is_active: bool = True
    is_superuser: bool = False

    sender_friendship: list[Friendship] = Relationship(
        back_populates="sender",
        sa_relationship_kwargs={
            "foreign_keys": "Friendship.sender_id"
        },
    )

    receiver_friendship: list[Friendship] = Relationship(
        back_populates="receiver",
        sa_relationship_kwargs={
            "foreign_keys": "Friendship.receiver_id"
        },
    )

    post_author: list[Post] = Relationship(
        back_populates="author",
        sa_relationship_kwargs={
            "foreign_keys": "Post.author_id"
        },
    )

    commenter_user: list[Comment] = Relationship(
        back_populates="commenter",
        sa_relationship_kwargs={
            "foreign_keys": "Comment.commenter_id"
        },
    )

    user_liked: list[Like] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "foreign_keys": "Like.user_id"
        },
    )