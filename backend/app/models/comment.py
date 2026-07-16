from app.db.base import Base
from sqlalchemy import Column, String, Integer, text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship 
class Comment(Base):
  __tablename__ = "comments"

  id = Column(Integer,index=True, nullable=False,primary_key=True)

  content = Column(String, nullable=False)

  commenter_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"))
  post_id = Column(Integer, ForeignKey("posts.id",ondelete="CASCADE"))

  created_at = Column(TIMESTAMP,nullable=False,server_default=text("NOW()"))

  commenter = relationship(
    "User",
    foreign_keys=[commenter_id],
    back_populates="commenter_user"
  )
  post = relationship(
    "Post",
    foreign_keys=[post_id],
    back_populates="comment_post"
  )