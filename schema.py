from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str


class PostUpdate(BaseModel):
    title: str
    content: str
    updated_on: datetime  = None


class PostReturn(BaseModel):
    id: str | int = None
    title: str = None
    content: str = None
    created_on: datetime = None
    updated_on: Optional[datetime] = None
