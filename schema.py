from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str
    created_on: datetime = datetime.utcnow()
    updated_on: Optional[datetime] = None


class PostReturn(BaseModel):
    id: str | int = None
    title: str = None
    content: str = None
    created_on: datetime = None
    updated_on: Optional[datetime] = None
