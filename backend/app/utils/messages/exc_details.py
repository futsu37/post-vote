def http_409_username_conflict() -> str:
  return "User with this username already exist!"

def http_409_exc_friendship_pending_conflict() -> str:
  return "You already sended friend request to that user!"

def http_409_exc_friendship_accepted_conflict() -> str:
  return "You already friends with this user!"

def http_404_exc_object_id_not_found(id: int, object_name: str) -> str:
  return f"The {object_name} with id {id} doesn't exist"

def http_404_exc_object_not_found(object_name: str) -> str:
  return f"The {object_name} doesn't exist"

def http_403_forbidden_credentials() -> str:
  return "Could not validate credentials"

def http_403_forbidden_befriend_oneself() -> str:
  return "You can't request friend operations with yourself!"

def http_403_forbidden_post_update() -> str:
  return "You can only edit your own posts!"

def http_403_forbidden_post_delete() -> str:
  return "You can only delete your own posts!"

def http_403_forbidden_comment_update() -> str:
  return "You can only edit your own comments!"

def http_403_forbidden_comment_delete() -> str:
  return "You can only delete your own comments!"


def http_401_unauthorized_login() -> str:
  return "Could not complete authenticaion. Wrong password or username"