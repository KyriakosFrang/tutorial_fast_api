from fastapi import FastAPI
from config import config  # type: ignore
from routes.core import core_router  # type:ignore
from routes.item import item_router

api_path = f"/api/{config.API_VERSION}"

app = FastAPI(title="MyApp", version="0.1")

app.include_router(
    core_router, tags=["core"], responses={404: {"description": "Not Found"}}
)


app.include_router(
    item_router,
    prefix=f"{api_path}/gaming",
    tags=["gaming"],
    responses={404: {"description": "Not found"}},
)


@app.on_event("startup")
async def app_startup():
    config.load_config()


@app.on_event("shutdown")
async def app_shutdown():
    config.close_db_client()
