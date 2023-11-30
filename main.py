from fastapi import FastAPI

from product import app as run

app = FastAPI()

app.include_router(run)