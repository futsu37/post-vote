def http_409_username_conflict() -> str:
  return "User with this username already exist!"

def http_409_friendship_pending_conflict() -> str:
  return "This friend request is already in pending state!"

def http_409_friendship_accepted_conflict() -> str:
  return "You're already friends with this user!"

def http_409_like_post_conflict() -> str:
  return "You can't like the same post twice!"

def http_409_profile_create_conflict() -> str:
  return "The user can have only one profile at a time!"

def http_404_object_id_not_found(id: int, object_name: str) -> str:
  return f"The {object_name} with id {id} doesn't exist"

def http_404_object_not_found(object_name: str) -> str:
  return f"The {object_name} doesn't exist"

def http_403_forbidden_credentials() -> str:
  return "Could not validate credentials"

def http_403_forbidden_befriend_oneself() -> str:
  return "You can't request friend operations with yourself!"

def http_403_forbidden_friend_sender_operation() -> str:
  return "Only receiver can accept/reject friend request!"

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