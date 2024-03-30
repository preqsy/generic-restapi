from pymongo import MongoClient

from .config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(settings.POSTGRES_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
        
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

cluster = MongoClient(settings.MONGO_DATABASE_URL)
db_name = cluster[settings.MONGO_DBNAME]
collection = db_name[settings.MONGO_COLLECTION_NAME]
    