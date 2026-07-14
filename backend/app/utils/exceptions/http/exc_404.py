from fastapi import HTTPException, status
from app.utils.messages.exc_details import http_404_exc_object_id_not_found, http_404_exc_object_not_found

def http_404_exc_request_object_id_not_found(id: int, object_name: str) -> Exception:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=http_404_exc_object_id_not_found(id,object_name))

def http_404_exc_request_object_not_found(object_name: str) -> Exception:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=http_404_exc_object_not_found(object_name))