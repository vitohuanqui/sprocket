from typing import List

from fastapi.requests import Request
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.routing import APIRouter

from src.application.container import get_dependencies
from src.domain.entities.sprocket_factory_data import (
    CreateSprocketFactoryDataDto, RetrieveSprocketFactoryDataDto,
    SprocketFactoryData, UpdateSprocketFactoryDataDto, ResponseFactoryDataDto)
from src.domain.services import (factory_service,
                                 sprocket_factory_data_service,
                                 sprocket_service)
# from src.domain.services.exceptions import *
from src.infraestructure.database.sqlalchemy import database

repository = get_dependencies().sprocket_factory_data_repository
sprocket_type_repository = get_dependencies().sprocket_repository
factory_repository = get_dependencies().factory_repository
router = APIRouter(default_response_class=JSONResponse)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=SprocketFactoryData,
    status_code=201,
    responses={201: {"description": "Factory created"}},
)
@database.transaction()
async def create(dto: CreateSprocketFactoryDataDto):
    return await sprocket_factory_data_service.create(repository, dto)


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
    result = await sprocket_factory_data_service.delete(
        repository, sprocket_type_id
    )
    status_code = 204 if result else 404
    return JSONResponse(
        status_code=status_code, content="Sprocket Type deleted"
    )


@router.get(
    "",
    response_class=JSONResponse,
    response_model=ResponseFactoryDataDto,
    status_code=200,
    responses={
        200: {"description": "Factories found"},
    },
)
@database.transaction()
async def get_all(request: Request):
    params = dict(request.query_params)
    return await sprocket_factory_data_service.get_all(repository, params)


@router.get(
    "/{factory_id}",
    response_class=JSONResponse,
    response_model=List[SprocketFactoryData],
    status_code=200,
    responses={
        200: {"description": "Factories found"},
    },
)
@database.transaction()
async def get_all_by_factory(factory_id: int):
    factory = await factory_service.get(factory_repository, factory_id)
    return list(
        await sprocket_factory_data_service.get_all_by_factory(
            repository, factory
        )
    )


@router.get(
    "/{sprocket_type_id}",
    response_class=JSONResponse,
    response_model=List[SprocketFactoryData],
    status_code=200,
    responses={
        200: {"description": "Factories found"},
    },
)
@database.transaction()
async def get_all_by_sprocket_type(sprocket_type_id: int):
    sprocket_type = await sprocket_service.get(
        sprocket_type_repository, sprocket_type_id
    )
    return list(
        await sprocket_factory_data_service.get_all_by_sprocket_type(
            repository, sprocket_type
        )
    )


@router.get(
    "/{factory_id}/{sprocket_type_id}",
    response_class=JSONResponse,
    response_model=List[SprocketFactoryData],
    status_code=200,
    responses={
        200: {"description": "Factories found"},
    },
)
@database.transaction()
async def get_all_by_factory(factory_id: int, sprocket_type_id: int):
    factory = await factory_service.get(factory_repository, factory_id)
    sprocket_type = await sprocket_service.get(
        sprocket_type_repository, sprocket_type_id
    )
    return list(
        await sprocket_factory_data_service.get_all_by_sprocket_type_and_factory(
            repository, sprocket_type, factory
        )
    )


@router.get(
    "/{sprocket_type_id}",
    response_class=JSONResponse,
    response_model=SprocketFactoryData,
    status_code=200,
    responses={
        200: {"description": "Sprocket Type found"},
        404: {"description": "Sprocket Type not found"},
    },
)
@database.transaction()
async def get(sprocket_type_id: int):
    item = await sprocket_factory_data_service.get(
        repository, sprocket_type_id
    )
    if not item:
        return JSONResponse(status_code=404, content="Sprocket Type retrived")
    return item


@router.put(
    "/{sprocket_type_id}",
    response_class=JSONResponse,
    response_model=SprocketFactoryData,
    status_code=200,
    responses={
        200: {"description": "Item replaced"},
        404: {"description": "Item not found"},
    },
)
@database.transaction()
async def update(dto: UpdateSprocketFactoryDataDto, sprocket_type_id: int):
    item = await sprocket_factory_data_service.update(
        repository, dto, sprocket_type_id
    )
    return (
        item
        if item
        else JSONResponse(status_code=404, content="Sprocket Type not Found")
    )
