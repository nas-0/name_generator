from typing import List
from api.database.db_setup import Name
from api.database.db_settings import engine
from sqlalchemy import select
from sqlalchemy.orm import Session

def get_ten_names(language: str) -> List[dict]: 

    names = []

    session = Session(engine)
    statement = select(Name).where(Name.language == language)

    for user in session.scalars(statement):
        name_dict = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "language": user.language,
            "country": user.country,
            "first_name_meaning": user.first_name_meaning,
            "last_name_meaning": user.last_name_meaning,
            "gender": user.gender

        }
        names.append(name_dict)

    return names
