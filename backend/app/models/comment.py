import uuid
from app.utils.time import get_datetime_utc
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, DateTime, ForeignKey

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.post import Post


class Comment(SQLModel, table=True):
    __tablename__ = "comments"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    content: str = Field(
        nullable=False,
    )

    commenter_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=True,
        ),
    )

    post_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            ForeignKey("posts.id", ondelete="CASCADE"),
            nullable=True,
        ),
    )

    created_at: datetime | None = Field(
      default_factory=get_datetime_utc,
      sa_type=DateTime(timezone=True) # type: ignore
    )

    commenter: Optional[User] = Relationship(
        back_populates="commenter_user",
        sa_relationship_kwargs={
            "foreign_keys": "Comment.commenter_id"
        },
    )

    post: Optional[Post] = Relationship(
        back_populates="comment_post",
        sa_relationship_kwargs={
            "foreign_keys": "Comment.post_id"
        },
    )