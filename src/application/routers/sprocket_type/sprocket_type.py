from typing import List
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.routing import APIRouter

from src.application.container import get_dependencies
from src.domain.entities.sprocket import (
    SprocketType,
    CreateSprocketTypeDto,
    UpdateSprocketTypeDto,
)
from src.domain.services import sprocket_service
# from src.domain.services.exceptions import *
from src.infraestructure.database.sqlalchemy import database


repository = get_dependencies().sprocket_repository
router = APIRouter(default_response_class=JSONResponse)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=SprocketType,
    status_code=201,
    responses={201: {"description": "Factory created"}},
)
@database.transaction()
async def create(dto: CreateSprocketTypeDto):
    return await sprocket_service.create(repository, dto)


@router.delete(
    "/{sprocket_type_id}",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "Sprocket Type deleted"},
        404: {"description": "Sprocket Type not found"},
    },
)
@database.transaction()
async def delete(sprocket_type_id: int):
    result = await sprocket_service.delete(repository, sprocket_type_id)
    status_code = 204 if result else 404
    return JSONResponse(status_code=status_code, content="Sprocket Type deleted")


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[SprocketType],
    status_code=200,
    responses={
        200: {"description": "Factories found"},
    },
)
@database.transaction()
async def get_all():
    return list(await sprocket_service.get_all(repository))


@router.get(
    "/{sprocket_type_id}",
    response_class=JSONResponse,
    response_model=SprocketType,
    status_code=200,
    responses={
        200: {"description": "Sprocket Type found"},
        404: {"description": "Sprocket Type not found"},
    },
)
@database.transaction()
async def get(sprocket_type_id: int):
    item = await sprocket_service.get(repository, sprocket_type_id)
    if not item:
        return JSONResponse(status_code=404, content="Sprocket Type retrived")
    return item


@router.put(
    "/{sprocket_type_id}",
    response_class=JSONResponse,
    response_model=SprocketType,
    status_code=200,
    responses={
        200: {"description": "Item replaced"},
        404: {"description": "Item not found"},
    },
)
@database.transaction()
async def update(
    dto: UpdateSprocketTypeDto, sprocket_type_id: int
):
    item = await sprocket_service.update(repository, dto, sprocket_type_id)
    return item if item else JSONResponse(status_code=404, content="Sprocket Type not Found")
