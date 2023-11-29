from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Medicine(Base):
    __tablename__ = "medicine"

    name = Column(String, unique=True, index=True, primary_key=True)
    salt = Column(String, unique=False, index=True, primary_key=True)
    symptom = Column(String, unique=False, index=True) 