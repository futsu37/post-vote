
from jose import jwt, JWTError
from app.core.config import settings
from datetime import datetime, timezone, timedelta


from app.utils.exceptions.http.exc_403 import http_403_exc_forbidden_request_credentials

from app.schemas.token import TokenData

def create_access_token(data: dict) -> str:
  to_encode = data.copy()
  expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.token_expire_minutes)
  
  to_encode.update({"exp":expires_at })
  access_token = jwt.encode(to_encode,settings.secret_key,settings.algorithm)
  return access_token

def verify_access_token(token: str) -> TokenData:
  
  try:
    payload = jwt.decode(token,settings.secret_key,[settings.algorithm,])
    user_id = payload.get("user_id")
    if not user_id:
      raise http_403_exc_forbidden_request_credentials()
    token_data = TokenData(id=str(user_id))
    return token_data
  except JWTError:
    raise http_403_exc_forbidden_request_credentials()

  