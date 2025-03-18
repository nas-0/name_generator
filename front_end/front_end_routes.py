from litestar import Router, get
from litestar.response import Template

@get("/")
async def index() -> Template:
    return Template(template_name="index.html")

@get("/arabic-name-generator")
async def arabic_names() -> Template:
    return Template(template_name="arabic.html")

    

front_end_router = Router(path="", route_handlers=[index, arabic_names])