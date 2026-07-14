from fastapi import HTTPException, status
from app.utils.messages.exc_details import http_409_username_conflict
from app.utils.messages.exc_details import http_409_exc_friendship_pending_conflict
from app.utils.messages.exc_details import http_409_exc_friendship_accepted_conflict

def http_409_exc_username_request_conflict() -> Exception:
  return HTTPException(status_code=status.HTTP_409_CONFLICT,
                                      detail=http_409_username_conflict())

def http_409_exc_friendship_request_pending_conflict() -> Exception:
  return HTTPException(status_code=status.HTTP_409_CONFLICT,
                                      detail=http_409_exc_friendship_pending_conflict())

def http_409_exc_friendship_request_accepted_conflict() -> Exception:
  return HTTPException(status_code=status.HTTP_409_CONFLICT,
                                      detail=http_409_exc_friendship_accepted_conflict())