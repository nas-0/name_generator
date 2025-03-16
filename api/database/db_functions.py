from typing import List
from api.database.db_schema import Name
from api.database.db_setup import session
from sqlalchemy import select, insert

from api.ai_scripts.name_generation import generate_names

def get_ten_names(language: str) -> List[dict]: 

    names = []

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

def add_names(amount: str, language: str, country: str = None) -> str:
    response = generate_names(amount, language).get("names", "")

    if not response:
        return None
    
    for name in response:
        names_added = 0
        try:
            statement = insert(Name).values(
                first_name=name.get("first_name"),
                last_name=name.get("last_name"),
                language=name.get("language"),
                country=name.get("country"),
                first_name_meaning=name.get("first_name_meaning"),
                last_name_meaning=name.get("last_name_meaning"),
                gender=name.get("gender")
                )
            names_added += 1
        except:
            print("Could not process name. Moving on...")
            continue
    
        print(f"Added {names_added} names to the database")



