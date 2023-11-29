from pydantic import BaseModel

class Medicine(BaseModel):
    name: str
    salt: str
    symptom: str

    class Config:
        from_attributes = True

class Meta(BaseModel):
    status: int
    message: str

class StandardResponse(BaseModel):
    success: bool
    meta: Meta
    data: dict | None
    