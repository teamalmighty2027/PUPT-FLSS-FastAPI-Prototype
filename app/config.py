from pydantic_settings import BaseSettings, SettingsConfigDict
import logging 

class Settings(BaseSettings):
    PROJECT_NAME: str = "FLSS FastAPI Prototype"
    DATABASE_URL: str 
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
logger = logging.getLogger('uvicorn.error')