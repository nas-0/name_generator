from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin, RapidocRenderPlugin
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig

from pathlib import Path

from api.routes import name_router
from front_end.front_end_routes import front_end_router

config = OpenAPIConfig(
        title="Name Generator API",
        description="API to randomly generate names",
        version="0.0.1",
        render_plugins=[SwaggerRenderPlugin(), RapidocRenderPlugin()]
)

jinja_config = TemplateConfig(
        directory=Path("front_end/templates"),
        engine=JinjaTemplateEngine,
    )

app = Litestar(
    route_handlers=[name_router, front_end_router],
    openapi_config=config,
    template_config=jinja_config
    )