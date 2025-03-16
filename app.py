from litestar import Litestar
from api.routes import name_router
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin, RapidocRenderPlugin

config = OpenAPIConfig(
        title="Name Generator API",
        description="API to randomly generate names",
        version="0.0.1",
        render_plugins=[SwaggerRenderPlugin(), RapidocRenderPlugin()]
)

app = Litestar(
    route_handlers=[name_router],
    openapi_config=config
    )