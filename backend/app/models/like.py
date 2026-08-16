import uuid
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, ForeignKey

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.post import Post


class Like(SQLModel, table=True):
    __tablename__ = "likes"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    post_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            ForeignKey("posts.id", ondelete="CASCADE"),
            nullable=True,
        ),
    )

    user_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=True,
        ),
    )

    user: Optional[User] = Relationship(
        back_populates="user_liked",
        sa_relationship_kwargs={
            "foreign_keys": "Like.user_id"
        },
    )

    post: Optional[Post] = Relationship(
        back_populates="post_liked",
        sa_relationship_kwargs={
            "foreign_keys": "Like.post_id"
        },
    )