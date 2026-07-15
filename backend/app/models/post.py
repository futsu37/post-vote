from app.db.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship

class Post(Base):
  __tablename__ = "posts"

  id = Column(Integer, index=True, primary_key=True, nullable=False)
  author_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"))
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  created_at = Column(TIMESTAMP,nullable=False,server_default=text("NOW()"))

  author = relationship(
    "User",
    foreign_keys=[author_id],
    back_populates="post_author"
  )