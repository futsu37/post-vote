from fastapi import FastAPI
from app.api import user, authentication, friendship, post, comment, like, profile
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
      "http://localhost:5173",

      "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(friendship.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(like.router)
app.include_router(profile.router)


@app.get("/")
def root():
  return {"message":"root path"}