from fastapi import APIRouter, Depends, Response, status


from databases.database_router import database
from databases.base_database import Database
from exception import InvalidRequest
from schema import PostCreate, PostReturn, PostUpdate

router = APIRouter(prefix="/posts")


@router.post("/", response_model=PostReturn)
async def create_post(data_obj: PostCreate, db: Database = Depends(database)):
    created_data = await db.create(data_obj)
    return created_data


@router.get("/", response_model=list[PostReturn])
def get_all_data(db: Database = Depends(database)):
    all_data = db.get_all_data()
    if not all_data:
        raise InvalidRequest(detail="No Post")
    return all_data
    
    
@router.get("/{id}", response_model=PostReturn)
def get_single_item(id: str | int, db: Database = Depends(database)):
    single_data = db.get_data_by_id(id=id)
    if not single_data:
        raise InvalidRequest(detail=f"Post with ID:{id} doesn't exist")
    return single_data

@router.put("/{id}", response_model=PostReturn)
async def update_item(id: str | int, data_obj: PostUpdate,db: Database = Depends(database)):
    item_query = db.get_data_by_id(id=id)
    if not item_query:
        raise InvalidRequest(detail=f"Post with ID:{id} doesn't exist")
    data = await db.update_data(id=id, data_obj=data_obj)
    
    return data

@router.delete("/{id}")
async def delete_item(id: str|int, db: Database = Depends(database)):
    item_query = db.get_data_by_id(id=id)
    if not item_query:
        raise InvalidRequest(detail=f"Post with ID:{id} doesn't exist")
    await db.delete_data(id=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
