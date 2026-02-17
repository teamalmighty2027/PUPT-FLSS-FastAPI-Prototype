from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import router as api_router
from .db.base import get_db
from .config import Settings

app = FastAPI()
app.include_router(api_router)

# CORS configuration for development
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@lru_cache
def get_settings():
    return Settings()

@app.get("/")
async def root():
    get_db()
    return {"message": "Hello World"}