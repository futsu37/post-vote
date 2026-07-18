from app.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Profile(Base):
  __tablename__ = "profiles"

  id = Column(Integer, index=True, primary_key=True, nullable=False)
  bio = Column(String, nullable=True)
  user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"))

  user = relationship(
    "User",
    foreign_keys=[user_id],
    back_populates="user_profile"
  )