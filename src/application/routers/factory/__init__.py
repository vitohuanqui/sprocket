from fastapi.routing import APIRouter

from . import factory


def _build_router() -> APIRouter:
    rt = APIRouter()
    rt.include_router(auth.router, prefix="/oauth2", tags=["Auth"])
    rt.include_router(user.router, prefix="/user", tags=["User"])

    return rt


router = _build_router()
