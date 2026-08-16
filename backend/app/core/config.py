from pydantic import computed_field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
  model_config = SettingsConfigDict(
    env_file="../.env",
    env_ignore_empty=True,
    extra="ignore"
  )

  secret_key: str
  token_expire_minutes: int = 30
  
  db_username: str
  db_password: str
  db_hostname: str
  db_port: int
  db_name: str
  
  algorithm: str

  api_v1_str: str = "/api/v1"

  @computed_field
  @property
  def sqlalchemy_database_uri(self) -> PostgresDsn:
    return PostgresDsn.build(
      scheme="postgresql+psycopg",
      username=self.db_username,
      password=self.db_password,
      host=self.db_hostname,
      port=self.db_port,
      path=self.db_name
    )


settings = Setting()