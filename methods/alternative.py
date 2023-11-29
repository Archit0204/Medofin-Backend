import models

def getAlternateMeds(filter, countNeeded, db, index):
    
    if (index == 2):
        alternateMeds = db.query(models.Medicine).filter(models.Medicine.salt == filter).limit(countNeeded).all()
    elif (index == 3):
        alternateMeds = db.query(models.Medicine).filter(models.Medicine.symptom == filter).limit(countNeeded).all()

    return alternateMeds