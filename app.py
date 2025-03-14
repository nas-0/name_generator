from typing import List
from litestar import Litestar, get
from models.name import nameResponse

@get("/names")
async def get_names() -> List[nameResponse]:

    name_1 = nameResponse(name="Nasir", first_name=True, last_name=True, language="Arabic")
    name_2 = nameResponse(name="Ahmed", first_name=True, last_name=True, language="Arabic")
    
    return [name_1, name_2]

app = Litestar([get_names])