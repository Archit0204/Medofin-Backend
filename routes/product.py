from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from methods.alternative import getAlternateMeds
import models
from methods.getDb import get_db

MAX_LIMIT = 15

product = APIRouter()

@product.get("/fetch/medicine/", status_code = status.HTTP_200_OK)
def fetchMedicine(db: Annotated[Session , Depends(get_db)], value: str | None, index: int = None):

    if value is None:
        raise HTTPException(status_code = 206, detail = "Not a valid value")
    
    if index not in range(1,4):
        index = 1

    if index == 1:
        medicineCount = db.query(models.Medicine).filter(models.Medicine.name == value).count()
        medicine = db.query(models.Medicine).filter(models.Medicine.name == value).limit(MAX_LIMIT).all()
        alternateFilter = medicine[0].salt
        index = 2 # changing the index to search for those particular alternate medicines
    elif index == 2:
        medicineCount = db.query(models.Medicine).filter(models.Medicine.salt == value).count()
        medicine = db.query(models.Medicine).filter(models.Medicine.salt == value).limit(MAX_LIMIT).all()
        alternateFilter = medicine[0].symptom
        index = 3 # changing the index to search for those particular alternate medicines
    elif index == 3:
        medicineCount = db.query(models.Medicine).filter(models.Medicine.symptom == value).count()
        medicine = db.query(models.Medicine).filter(models.Medicine.symptom == value).limit(MAX_LIMIT).all()
        alternateFilter = medicine[0].salt
        index = 2 # changing the index to search for those particular alternate medicines

    if not medicine:
        raise HTTPException(status_code=404, detail="No Medicine found with the given values.")
    
    # print(medicine[0].salt)

    remainingMed = MAX_LIMIT - medicineCount

    alternateMeds = getAlternateMeds(alternateFilter, remainingMed, db, index)

    return {
       'success': True,
        'meta': {
                'status': status.HTTP_302_FOUND,
                'message': "User has searched successfully."
            },
        'data': {
            'count': medicineCount,
            'medicine': medicine,
            'alternatives': alternateMeds
        }
    }
    # return "sucess"