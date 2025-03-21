from typing import List
from litestar import Router, get, post
from api.models.name import nameResponse, nameRequest
from api.database import db_functions

@get("/ten")
async def get_names() -> List[nameResponse]:

    response = db_functions.get_ten_names("Arabic")

    name_list = []

    for name_details in response:
        name_list.append(nameResponse.model_validate(name_details))
    
    return name_list

@post("/")
async def add_names(data: nameRequest) -> dict:
    response = db_functions.add_names(data.amount, data.language)

    return {
        "names_added": response
    }

name_router = Router(path="/names", route_handlers=[get_names, add_names])