from typing import List
from litestar import get, Router
from api.models.name import nameResponse
from api.database.db_functions import get_ten_names

@get("/ten")
async def get_names() -> List[nameResponse]:

    response = get_ten_names("Arabic")

    name_list = []

    for name_details in response:
        name_list.append(nameResponse.model_validate(name_details))
    
    return name_list

name_router = Router(path="/names", route_handlers=[get_names])