from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel
from pymongo import ReturnDocument

from database import Database
from typing import TypeVar, Type
from pymongo.database import Database as Mongo

ModelType = TypeVar("ModelType", bound=BaseModel)
DbType = TypeVar("DbType", bound=Mongo)


class MongoDB(Database):
    def __init__(self, db: Type[DbType], model: Type[ModelType]):
        self.db = db
        self.model = model

    def create(self, data_obj: dict) -> Optional[dict]:
        data_dict = data_obj.dict(exclude_none=True)
        insert_id = self.db.insert_one(data_dict).inserted_id

        return self.model(id=insert_id, **data_dict)

    def get_all_data(self) -> Optional[dict]:
        query_result = self.db.find()
        if not query_result:
            return None
        return self.model(**query_result)

    def get_data_by_id(self, id: int) -> Optional[dict]:
        query_result = self.db.find_one({"_id": ObjectId(id)})
        if not query_result:
            return None
        return self.model(**query_result)

    def update_data(self, id: int, data_obj) -> Optional[dict]:
        update_data = data_obj.dict()
        update_data["update_on"] = datetime.utcnow()
        data = self.db.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER,
        )

        return self.model(**update_data)

    def delete_data(self, id: int) -> bool:
        query_result = self.db.delete_one({"_id": ObjectId(id)})
        if query_result.deleted_count > 0:
            return True
        return False
        
