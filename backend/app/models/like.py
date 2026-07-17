from app.db.base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship 
class Like(Base):
  __tablename__ = "likes"

  id = Column(Integer,index=True, nullable=False,primary_key=True)
  
  post_id = Column(Integer, ForeignKey("posts.id",ondelete="CASCADE"))
  user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"))

  user = relationship(
    "User",
    foreign_keys=[user_id],
    back_populates="user_liked"
  )
  post = relationship(
    "Post",
    foreign_keys=[post_id],
    back_populates="post_liked" 
  )
