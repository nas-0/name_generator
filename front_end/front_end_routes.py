from typing import List
from litestar import Router, get, post
from api.models.name import nameResponse, nameRequest
from api.database import db_functions
from litestar.response import Template

@get("/")
async def index() -> Template:
    return Template(template_name="index.html")
    

front_end_router = Router(path="", route_handlers=[index])