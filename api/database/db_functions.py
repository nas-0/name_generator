from typing import List
from api.database.db_schema import Name
from api.database.db_setup import session
from sqlalchemy import select

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

    print(response)

    if not response:
        return None
    
    names_added = 0
    
    for name_details in response:
        try:
            name = Name(
                first_name=name_details.get("first_name"),
                last_name=name_details.get("last_name"),
                language=name_details.get("language"),
                country=name_details.get("country"),
                first_name_meaning=name_details.get("first_name_meaning"),
                last_name_meaning=name_details.get("last_name_meaning"),
                gender=name_details.get("gender")
                )
            session.add(name)
            session.commit()
            names_added += 1
        except Exception as e:
            print(e)
            print("Could not process name. Moving on...")
            continue
    

    print(f"Added {names_added} names to the database")
    return names_added



