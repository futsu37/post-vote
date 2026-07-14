from fastapi import FastAPI
from app.api import user, authentication, friendship
app = FastAPI()

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(friendship.router)

@app.get("/")
def root():
  return {"message":"root path"}