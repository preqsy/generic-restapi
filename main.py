from fastapi import FastAPI

import model
from engine import engine
import endpoint

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(endpoint.router)
