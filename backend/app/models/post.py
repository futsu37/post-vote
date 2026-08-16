import uuid
from app.utils.time import get_datetime_utc
from datetime import datetime
from typing import TYPE_CHECKING, Optional
from sqlalchemy import DateTime
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, ForeignKey

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.comment import Comment
    from app.models.like import Like


class Post(SQLModel, table=True):
    __tablename__ = "posts"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    author_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=True,
        ),
    )
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)
    created_at: datetime | None = Field(
      default_factory=get_datetime_utc,
      sa_type=DateTime(timezone=True) # type: ignore
    )
    author: Optional[User] = Relationship(
        back_populates="post_author",
        sa_relationship_kwargs={
            "foreign_keys": "Post.author_id"
        },
    )

    comment_post: list[Comment] = Relationship(
        back_populates="post",
        sa_relationship_kwargs={
            "foreign_keys": "Comment.post_id"
        },
    )

    post_liked: list[Like] = Relationship(
        back_populates="post",
        sa_relationship_kwargs={
            "foreign_keys": "Like.post_id"
        },
    )