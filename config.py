from pathlib import Path
from pydantic_settings import BaseSettings



path = Path.cwd()
env_path = path / ".env"

class Settings(BaseSettings):

    POSTGRES_DATABASE_URL: str = ""
    
    MONGO_DATABASE_URL: str = ""
    MONGO_DBNAME: str = ""
    MONGO_COLLECTION_NAME: str = ""

    class Config:
        case_sensitive = True
        env_file = env_path
        env_file_encoding = "utf-8"


settings = Settings()


