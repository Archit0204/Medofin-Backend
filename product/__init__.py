from fastapi import APIRouter, FastAPI
import models
from database import engine

app = APIRouter()

models.Base.metadata.create_all(bind=engine)

from .routes.product import product
from .routes.add import add

app.include_router(product)
app.include_router(add)