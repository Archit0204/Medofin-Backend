from fastapi import FastAPI

from . import app as run

app = FastAPI()

app.include_router(run)