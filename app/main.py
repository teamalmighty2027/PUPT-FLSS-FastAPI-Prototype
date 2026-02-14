from fastapi import FastAPI, APIRouter
from .routers import router as api_router

app = FastAPI()
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}