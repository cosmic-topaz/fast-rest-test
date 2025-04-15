# backend/app/config.py

from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings  
from pydantic import Field

# .env 로드
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    MYSQL_HOST: str = Field(...)
    MYSQL_PORT: int = Field(...)
    MYSQL_USER: str = Field(...)
    MYSQL_PASSWORD: str = Field(...)
    MYSQL_DB: str = Field(...)

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return (
            f"mysql+mysqlconnector://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )

settings = Settings()