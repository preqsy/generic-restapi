from fastapi import APIRouter, Depends


from data_source import database
from base_database import Database
from schema import PostCreate, PostReturn

router = APIRouter(prefix="/posts")


@router.post("/", response_model=PostReturn)
async def create_post(data_obj: PostCreate, db: Database = Depends(database)):
    data = await db.create(data_obj)

    return data


@router.get("/", response_model=list[PostReturn])
def get_all_data(db: Database = Depends(database)):
    all_data = db.get_all_data()
    print(type(all_data))
    return all_data


