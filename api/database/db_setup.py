from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from api.settings import db_url

engine = create_engine(db_url)
session = Session(engine)