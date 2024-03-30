from pathlib import Path
from pydantic_settings import BaseSettings
from pymongo import MongoClient
import os
from dotenv import find_dotenv, load_dotenv


# cluster = MongoClient(MONGO_URI)


production = cluster.production
collect = production.collect

path = Path.cwd()
env_path = path / ".env"

class Settings(BaseSettings):
    SECRET_KEY: str = "P9Fjdh3b0m21"
    ACCESS_EXPIRY_TIME: int = 30
    REFRESH_EXPIRY_TIME: int = 14
    ALGORITHM: str = "HS256"
    POSTGRES_DATABASE_URL: str = (
        "postgresql://flashfeed_blog_user:Tt94E9MrchtjKun0UhR8XtlK9egwRuY4@dpg-cno7sl21hbls73c62feg-a.oregon-postgres.render.com:5432/flashfeed_blog"
    )
    MONGO_DATABASE_URL: str = "mongodb+srv://Preqsy:0000@cluster0.xvggsoe.mongodb.net/?retryWrites=true&w=majority"
    MONGO_DBNAME: str = ""
    MONGO_COLLECTION_NAME: str = ""

    class Config:
        case_sensitive = True
        env_file = env_path
        env_file_encoding = "utf-8"


settings = Settings()


