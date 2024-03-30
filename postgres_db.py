from typing import TypeVar, Type
from database import Database
from sqlalchemy.orm import Session

from engine import Base

ModelType = TypeVar("ModelType", bound=Base)

class PostgresDB(Database):
    def __init__(self, db: Session, model:Type[ModelType]):
        self.db = db
        self.model = model


    async def create(self, data):
        new_data = self.model(**data.dict())
        self.db.add(new_data)
        self.db.commit()
        self.db.refresh(new_data)
        return new_data

    async def get_all_data(self):
        all_data = self.db.query(self.model).all()
        if all_data == []:
            return None
        return all_data

    async def get_data_by_id(self, id):
        data_query = self.db.query(self.model).filter(self.model.id == id)
        if not data_query.first():
            return None
        return data_query

    async def update_data(self, id, data_obj):
        data = self.get_data_by_id(id=id)
        if not data:
            return None
        data.update(data_obj, synchronize_session=False)
        self.db.commit()
        self.db.refresh(data)
        return data
    
    async def delete_data(self, id):
        data = self.get_data_by_id(id=id)
        if not data:
            return None
        data.delete(synchronize_session=False)
        self.db.commit()
        return True
