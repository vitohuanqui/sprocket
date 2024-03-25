from fastapi.routing import APIRouter

from . import sprocket_data_factory


def _build_router() -> APIRouter:
    rt = APIRouter()
    rt.include_router(
        sprocket_data_factory.router,
        prefix="/sprocket-data-factory",
        tags=["Sprocket Factory Data"],
    )

    return rt


router = _build_router()
