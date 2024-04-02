from typing import Union

from fastapi import Depends, Query

from engine import get_databases
from model import MongoModel, PostgresModel
from mongo_db import MongoDB
from postgres_db import PostgresDB

def database(db=Depends(get_databases), db_type: str = Query()) -> Union[PostgresDB, MongoDB]:
    if db_type == "postgres":
        return PostgresDB(db=db, model=PostgresModel)
    elif db_type == "mongo":
        return MongoDB(db=db, model=MongoModel)
    else:
        raise ValueError("Invalid database type")