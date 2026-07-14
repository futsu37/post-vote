from app.db.base import Base
from sqlalchemy import Column, Integer, text, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
class Status(enum.Enum):
  PENDING = "PENDING"
  ACCEPTED = "ACCEPTED"

class Friendship(Base):
  __tablename__ = "friendships"

  id = Column(Integer,index=True, nullable=False,primary_key=True)
  sender_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"))
  receiver_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"))
  requested_at = Column(TIMESTAMP,nullable=False,server_default=text("NOW()"))
  status = Column(Enum(Status), nullable=False)

  sender = relationship(
    "User",
    foreign_keys=[sender_id],
    back_populates="sender_friendship"
  )
  receiver = relationship(
    "User",
    foreign_keys=[receiver_id],
    back_populates="receiver_friendship"
  )