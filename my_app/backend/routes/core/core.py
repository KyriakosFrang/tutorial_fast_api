from fastapi import APIRouter

__all__ = ["core_router"]

core_router = APIRouter()


@core_router.get("/", status_code=200)
def healthcheck():
    return {"healthcheck": "OK"}

