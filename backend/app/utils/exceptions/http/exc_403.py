from fastapi import HTTPException, status
from app.utils.messages.exc_details import (http_403_forbidden_credentials,
                                            http_403_forbidden_befriend_oneself,
                                            http_403_forbidden_post_update,
                                            http_403_forbidden_post_delete,
                                            http_403_forbidden_comment_update,
                                            http_403_forbidden_comment_delete,
                                            http_403_forbidden_friend_sender_operation)

def http_403_exc_forbidden_request_credentials() -> Exception:
  return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                      detail=http_403_forbidden_credentials())

def http_403_exc_forbidden_befriend_oneself_request() -> Exception:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                      detail=http_403_forbidden_befriend_oneself())
def http_403_exc_forbidden_friend_sender_operation_request() -> Exception:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                      detail=http_403_forbidden_friend_sender_operation())
                                      
def http_403_exc_forbidden_post_update_request() -> Exception:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                  detail=http_403_forbidden_post_update())
def http_403_exc_forbidden_post_delete_request() -> Exception:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                  detail=http_403_forbidden_post_delete())
def http_403_exc_forbidden_comment_update_request() -> Exception:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                  detail=http_403_forbidden_comment_update())
def http_403_exc_forbidden_comment_delete_request() -> Exception:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                  detail=http_403_forbidden_comment_delete())