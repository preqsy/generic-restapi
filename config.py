from pathlib import Path
from pydantic_settings import BaseSettings
from pymongo import MongoClient
import os
from dotenv import find_dotenv, load_dotenv


# cluster = MongoClient(MONGO_URI)


# production = cluster.production
# collect = production.collect

path = Path.cwd()
env_path = path / ".env"

class Settings(BaseSettings):
    SECRET_KEY: str = "P9Fjdh3b0m21"
    ACCESS_EXPIRY_TIME: int = 30
    REFRESH_EXPIRY_TIME: int = 14
    ALGORITHM: str = "HS256"
    POSTGRES_DATABASE_URL: str = (
        "postgresql://postgres:50610903@localhost:5432/test_api"
    )
    MONGO_DATABASE_URL: str = "mongodb+srv://Preqsy:0000@cluster0.xvggsoe.mongodb.net/?retryWrites=true&w=majority"
    MONGO_DBNAME: str = "production"
    MONGO_COLLECTION_NAME: str = "collect"

    class Config:
        case_sensitive = True
        env_file = env_path
        env_file_encoding = "utf-8"


settings = Settings()


