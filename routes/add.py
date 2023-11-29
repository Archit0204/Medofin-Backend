from fastapi import APIRouter, Depends
import schemas, models
from sqlalchemy.orm import Session
from methods.getDb import get_db

add = APIRouter()

@add.post("/add")
def addMedicine(request: schemas.Medicine, db: Session = Depends(get_db)):
    newMed = models.Medicine(name = request.name, salt = request.salt, symptom = request.symptom)
    db.add(newMed)
    db.commit()
    db.refresh(newMed)
    return newMed