from typing import Union
from fastapi import Depends, FastAPI

from database import Database
from engine import get_db, get_mongo_db
from model import Post, PostM
from mongo_db import MongoDB
from postgres_db import PostgresDB
from schema import PostCreate
import model
from engine import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_databases(db= Depends(get_db), db_type="postgres") -> Union[PostgresDB, MongoDB]:
    if db_type == "postgres":
        # db = Depends(get_db)
        return PostgresDB(db=db, model=Post)
    elif db_type == "mongo":
        # db=Depends(get_mongo_db)
        return MongoDB(db=db, model=PostM)
    
    raise ValueError
    

@app.post("/post")
def create_post(data_obj: PostCreate, db:Database=Depends(get_databases)):
    data = db.create(data_obj)
    return data
    
