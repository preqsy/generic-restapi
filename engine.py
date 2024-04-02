from fastapi import Query
from pymongo import MongoClient


from fastapi import Query

from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(settings.POSTGRES_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_postgres_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


def get_mongo_db():
    cluster = MongoClient(settings.MONGO_DATABASE_URL)
    db_name = cluster[settings.MONGO_DBNAME]
    collection = db_name[settings.MONGO_COLLECTION_NAME]
    return collection


def get_databases(db_type: str = Query()):
    if db_type == "postgres":
        return get_postgres_db()
    elif db_type == "mongo":
        return get_mongo_db()


