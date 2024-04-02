from datetime import datetime
from typing import Optional


from pydantic import BaseModel
from databases.database_connections import Base
from sqlalchemy import TIMESTAMP, Column, DateTime, Integer, String
from sqlalchemy.sql.expression import text


class PostgresModel(Base):
    __tablename__ = "post"
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_on = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_on = Column(DateTime, nullable=True)


class MongoModel(BaseModel):
    id: Optional[str] = None
    title: str
    content: str
    created_on: datetime = datetime.utcnow()
    updated_on: Optional[datetime] = None
