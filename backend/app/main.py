from fastapi import FastAPI
from app.api.main import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
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

app.include_router(api_router,prefix=settings.api_v1_str)

@app.get("/")
def root():
  return {"message":"root path"}