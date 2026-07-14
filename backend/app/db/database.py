from sqlalchemy import create_engine
from app.core.config import settings

SQLALCHEMY_URL = f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"

engine = create_engine(SQLALCHEMY_URL)

