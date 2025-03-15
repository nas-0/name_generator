from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Name(Base):
    __tablename__ = "names"
    
    first_name = Column(String(50), nullable=False, primary_key=True)
    last_name = Column(String(50), nullable=False, primary_key=True)
    language = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    first_name_meaning = Column(String(200))
    last_name_meaning = Column(String(200))
    gender = Column(String(10), nullable=False)