from litestar import Litestar
from api.routes import name_router


app = Litestar(route_handlers=[name_router])