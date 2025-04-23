
# backend/app/config.py

from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path

class Settings(BaseSettings):
    MYSQL_USER: str = Field(..., env="MYSQL_USER")
    MYSQL_PASSWORD: str = Field(..., env="MYSQL_PASSWORD")
    MYSQL_HOST: str = Field(..., env="MYSQL_HOST")
    MYSQL_PORT: int = Field(..., env="MYSQL_PORT")
    MYSQL_DB: str = Field(..., env="MYSQL_DB")
    JWT_SECRET_KEY: str = Field(..., env="JWT_SECRET_KEY")  # ← 이거 빠졌는지 확인

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return (
            f"mysql+mysqlconnector://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )

    class Config:
        env_file = Path(__file__).resolve().parent.parent.parent / ".env"

def get_settings() -> Settings:
    return Settings()

settings = get_settings()