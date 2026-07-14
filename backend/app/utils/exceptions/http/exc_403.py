from fastapi import HTTPException, status
from app.utils.messages.exc_details import http_403_forbidden_credentials,http_403_forbidden_befriend_oneself

def http_403_exc_forbidden_request_credentials() -> Exception:
  return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                      detail=http_403_forbidden_credentials())
def http_403_forbidden_befriend_oneself_request() -> Exception:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                      detail=http_403_forbidden_befriend_oneself())