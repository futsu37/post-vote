from fastapi import HTTPException, status
from app.utils.messages.exc_details import http_401_unauthorized_login

def http_401_exc_unauthorized_request() -> Exception:
  return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                      detail=http_401_unauthorized_login())