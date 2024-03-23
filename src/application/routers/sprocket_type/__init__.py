from fastapi.routing import APIRouter

from . import sprocket_type


def _build_router() -> APIRouter:
    rt = APIRouter()
    rt.include_router(sprocket_type.router, prefix="/sprocket-type", tags=["Sprocket Type"])

    return rt


router = _build_router()
