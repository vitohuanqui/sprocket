from fastapi.routing import APIRouter

from . import factory


def _build_router() -> APIRouter:
    rt = APIRouter()
    rt.include_router(factory.router, prefix="/factory", tags=["Factory"])

    return rt


router = _build_router()
