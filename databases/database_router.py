from typing import Union

from fastapi import Depends, Query

from .database_connections import get_databases
from model import MongoModel, PostgresModel
from .mongo_db import MongoDB
from .postgres_db import PostgresDB

def database(db=Depends(get_databases), db_type: str = Query()) -> Union[PostgresDB, MongoDB]:
    """Returns the appropriate database connection based on the provided db_type."""
    if db_type == "postgres":
        return PostgresDB(db=db, model=PostgresModel)
    elif db_type == "mongo":
        return MongoDB(db=db, model=MongoModel)
    else:
        raise ValueError("Invalid database type")