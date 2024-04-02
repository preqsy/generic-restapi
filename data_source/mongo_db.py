from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel
from pymongo import ReturnDocument

from .base_database import Database
from typing import TypeVar, Type
from pymongo.database import Database as Mongo

ModelType = TypeVar("ModelType", bound=BaseModel)
DbType = TypeVar("DbType", bound=Mongo)


class MongoDB(Database):
    def __init__(self, db: Type[DbType], model: Type[ModelType]):
        self.db = db
        self.model = model

    async def create(self, data_obj: dict) -> ModelType:
        data_dict = data_obj.dict(exclude_none=True)
        insert_id = self.db.insert_one(data_dict).inserted_id
        return self.model(id=str(insert_id), **data_dict)

    def get_all_data(self) -> ModelType:
        query_result = self.db.find()
        if not query_result:
            return None
        data_dict = []
        for data in query_result:
            data["id"] = str(data["_id"])
            data_dict.append(data)
        return [self.model(**doc) for doc in data_dict]

    def get_data_by_id(self, id: int) -> Optional[dict]:
        query_result = self.db.find_one({"_id": ObjectId(id)})
        if not query_result:
            return None
        query_result["id"] = str(query_result["_id"])
        return self.model(**query_result)

    async def update_data(self, id: int, data_obj) -> Optional[dict | ModelType]:
        update_data_dict = data_obj.dict()
        update_data_dict["updated_on"] = datetime.utcnow()
        update_data_dict["id"] = id
        data = self.db.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": update_data_dict},
            return_document=ReturnDocument.AFTER,
        )
        return self.model(**update_data_dict)

    async def delete_data(self, id: int) -> bool:
        query_result = self.db.delete_one({"_id": ObjectId(id)})
        if query_result.deleted_count > 0:
            return True
        return False
        
