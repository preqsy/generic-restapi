from datetime import datetime
from typing import Optional, TypeVar, Type

from .base_database import Database
from sqlalchemy.orm import Session

from .database_connections import Base

ModelType = TypeVar("ModelType", bound=Base)


class PostgresDB(Database):
    def __init__(self, db: Session, model: Type[ModelType]):
        self.db = db
        self.model = model

    async def create(self, data_obj) -> ModelType:
        new_data = self.model(**data_obj.dict())
        self.db.add(new_data)
        self.db.commit()
        self.db.refresh(new_data)
        return new_data

    def get_all_data(self)  -> ModelType:
        all_data = self.db.query(self.model).all()
        if all_data == []:
            return None
        return all_data

    def get_data_by_id(self, id) -> ModelType:
        data_query = self.db.query(self.model).filter(self.model.id == id).first()
        if not data_query:
            return None
        return data_query

    async def update_data(self, id, data_obj: Optional[dict]) -> ModelType:
        data = self.db.query(self.model).filter(self.model.id == id)
        if not data.first():
            return None

        data_dict = data_obj.dict()
        data_dict["updated_on"] = datetime.utcnow()
        data_dict["id"] = data.first().id
        data_dict["created_on"] = data.first().created_on
        data.update(data_dict, synchronize_session=False)
        self.db.commit()

        return data_dict

    async def delete_data(self, id)  -> bool:
        data = self.db.query(self.model).filter(self.model.id == id)
        if not data.first():
            return None
        data.delete(synchronize_session=False)
        self.db.commit()
        return True
