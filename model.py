from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel
from engine import Base
from sqlalchemy import TIMESTAMP, Column, DateTime, Integer, String
from sqlalchemy.sql.expression import text

class PostgresModel(Base):
    __tablename__ = "post"
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_on = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_on = Column(DateTime, nullable=True)
    

# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v: str):
#         try:
#             return cls(v)
#         except Exception:
#             raise ValueError(f"{v} is not a valid ObjectId")
        
class MongoModel(BaseModel):
    id: Optional[str] = None
    title: str
    content: str
    created_on: datetime = datetime.utcnow()
    updated_on: datetime = None
    