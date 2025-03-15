from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db_settings import db_url

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


engine = create_engine(db_url)

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

new_name = Name(
    first_name="Omar", 
    last_name="Al-Fayez",
    language="Arabic",
    country="Jordan",
    first_name_meaning="Long-lived",
    last_name_meaning="The victorious",
    gender="Male"
    )
session.add(new_name)
session.commit()

print("Created Database")