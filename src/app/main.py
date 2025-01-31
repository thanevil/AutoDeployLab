import logging
from fastapi import FastAPI
from pydantic_settings import BaseSettings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    app_name: str = "AutoDeployLab"
    debug: bool = False

    class Config:
        env_file = ".env"  # Load values from .env file if available

settings = Settings()

app = FastAPI(title=settings.app_name)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": f"Welcome to {settings.app_name}!"}

@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "healthy"}
