

from datetime import datetime
from pydantic import BaseModel


class PostCreate(BaseModel):
    # id: int = None
    title: str
    content: str
    created_on: datetime = datetime.utcnow()
    updated_on: datetime = None