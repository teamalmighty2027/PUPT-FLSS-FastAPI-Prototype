from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from .routers import router as api_router
from .config import logger
from .db.base import get_db

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

@app.get("/health/db")
async def health_check_db():
    try:
        async for session in get_db():
            await session.execute(text('SELECT 1;'))
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        return {"status": "error"}

@app.get("/")
async def root():
    return {"message": "Hello World"}