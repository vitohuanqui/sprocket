from typing import List
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.routing import APIRouter

from src.application.container import get_dependencies
from src.domain.entities.factory import (
    Factory,
    CreateFactoryDto,
    UpdateFactoryDto,
)
from src.domain.services import factory_service
# from src.domain.services.exceptions import *
from src.infraestructure.database.sqlalchemy import database


repository = get_dependencies().factory_repository
router = APIRouter(default_response_class=JSONResponse)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=Factory,
    status_code=201,
    responses={201: {"description": "Factory created"}},
)
@database.transaction()
async def create(dto: CreateFactoryDto):
    return await factory_service.create(repository, dto)


@router.delete(
    "/{factory_id}",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "Factory deleted"},
        404: {"description": "Factory not found"},
    },
)
@database.transaction()
async def delete(factory_id: int):
    result = await factory_service.delete(repository, factory_id)
    status_code = 204 if result else 404
    return JSONResponse(status_code=status_code)


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[Factory],
    status_code=200,
    responses={
        200: {"description": "Factories found"},
    },
)
@database.transaction()
async def get_all():
    return list(await factory_service.get_all(repository))


@router.get(
    "/{factory_id}",
    response_class=JSONResponse,
    response_model=Factory,
    status_code=200,
    responses={
        200: {"description": "Factory found"},
        404: {"description": "Factory not found"},
    },
)
@database.transaction()
async def get(factory_id: int):
    item = await factory_service.get(repository, factory_id)
    if not item:
        return JSONResponse(status_code=404)
    return item


@router.put(
    "/{factory_id}",
    response_class=JSONResponse,
    response_model=Factory,
    status_code=200,
    responses={
        200: {"description": "Item replaced"},
        404: {"description": "Item not found"},
    },
)
@database.transaction()
async def update(
    dto: UpdateFactoryDto, factory_id: int
):
    item = await factory_service.update(repository, dto, factory_id)
    return item if item else JSONResponse(status_code=404)
