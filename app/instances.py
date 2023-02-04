from app.api import router
from app.setup import App


tags_metadata = [
    {"name": "category", "description": "Эндпоинт который вернёт блюда по категориям"},

]

app = App(
    title="menu",
    version="0.0.1",
    description="Backend services for menu services",
    docs_url="/api/menu/docs",
    openapi_url="/api/ment/openapi.json",
    redoc_url=None,
    openapi_tags=tags_metadata,
    router=router,
)
