import uuid
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, TIMESTAMP, Enum as SAEnum, ForeignKey, text

if TYPE_CHECKING:
    from app.models.user import User


class Status(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"


class Friendship(SQLModel, table=True):
    __tablename__ = "friendships"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    sender_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=True,
        ),
    )

    receiver_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=True,
        ),
    )

    requested_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            nullable=False,
            server_default=text("NOW()"),
        )
    )

    status: Status = Field(
        sa_column=Column(
            SAEnum(Status),
            nullable=False,
        )
    )

    sender: Optional[User] = Relationship(
        back_populates="sender_friendship",
        sa_relationship_kwargs={
            "foreign_keys": "Friendship.sender_id"
        },
    )

    receiver: Optional[User] = Relationship(
        back_populates="receiver_friendship",
        sa_relationship_kwargs={
            "foreign_keys": "Friendship.receiver_id"
        },
    )