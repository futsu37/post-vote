from app.db.base import Base
from sqlalchemy import Column, String, Integer, text, TIMESTAMP
from sqlalchemy.orm import relationship 
class User(Base):
  __tablename__ = "users"

  id = Column(Integer,index=True, nullable=False,primary_key=True)
  username = Column(String, unique=True ,nullable=False)
  display_name = Column(String, nullable=False)
  email = Column(String, nullable=False, unique=True)
  password = Column(String, nullable=False)
  created_at = Column(TIMESTAMP,nullable=False,server_default=text("NOW()"))

  sender_friendship = relationship(
    "Friendship",
    foreign_keys="Friendship.sender_id",
    back_populates="sender"
  )
  receiver_friendship = relationship(
    "Friendship",
    foreign_keys="Friendship.receiver_id",
    back_populates="receiver"
  )
  post_author = relationship(
    "Post",
    foreign_keys="Post.author_id",
    back_populates="author"
  )
  commenter_user = relationship(
    "Comment",
    foreign_keys="Comment.commenter_id",
    back_populates="commenter"
  )