from fastapi import APIRouter, Depends
import schemas, models
from sqlalchemy.orm import Session
# from methods.getDb import get_db
from database import SessionLocal

add = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getAlternateMeds(filter, countNeeded, db, index):
    
    if (index == 2):
        alternateMeds = db.query(models.Medicine).filter(models.Medicine.salt == filter).limit(countNeeded).all()
    elif (index == 3):
        alternateMeds = db.query(models.Medicine).filter(models.Medicine.symptom == filter).limit(countNeeded).all()

    return alternateMeds

@add.post("/add")
def addMedicine(request: schemas.Medicine, db: Session = Depends(get_db)):
    newMed = models.Medicine(name = request.name, salt = request.salt, symptom = request.symptom)
    db.add(newMed)
    db.commit()
    db.refresh(newMed)
    return newMed