from fastapi import APIRouter
from app.api.routes import authentication, comment, friendship, like, post, profile, user
api_router = APIRouter()

api_router.include_router(authentication.router)
api_router.include_router(comment.router)
api_router.include_router(friendship.router)
api_router.include_router(like.router)
api_router.include_router(post.router)
api_router.include_router(profile.router)
api_router.include_router(user.router)