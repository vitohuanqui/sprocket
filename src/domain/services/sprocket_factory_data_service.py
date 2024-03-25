from typing import Iterable, Optional

from src.domain.entities.factory import Factory
from src.domain.entities.sprocket import SprocketType
from src.domain.entities.sprocket_factory_data import (
    CreateSprocketFactoryDataDto, RetrieveSprocketFactoryDataDto,
    SprocketFactoryData, UpdateSprocketFactoryDataDto)
from src.domain.repositories.sprocket_factory_data_repository import \
    SprocketFactoryDataRepository


async def create(
    repository: SprocketFactoryDataRepository,
    dto: CreateSprocketFactoryDataDto,
) -> SprocketFactoryData:
    return await repository.create(dto)


async def delete(repository: SprocketFactoryDataRepository, id_: int) -> bool:
    return await repository.delete(id_)


async def get(
    repository: SprocketFactoryDataRepository, id_: int
) -> Optional[SprocketFactoryData]:
    return await repository.get(id_)


async def get_all(
    repository: SprocketFactoryDataRepository, query_params: dict = None
) -> Iterable[RetrieveSprocketFactoryDataDto]:
    return await repository.get_all(query_params)


async def get_all_by_factory(
    repository: SprocketFactoryDataRepository, factory: Factory
) -> Iterable[SprocketFactoryData]:
    return await repository.get_all_by_factory(factory)


async def get_all_by_sprocket_type(
    repository: SprocketFactoryDataRepository, sprocket_type: SprocketType
) -> Iterable[SprocketFactoryData]:
    return await repository.get_all_by_sprocket_type(sprocket_type)


async def get_all_by_sprocket_type_and_factory(
    repository: SprocketFactoryDataRepository,
    sprocket_type: SprocketType,
    factory: Factory,
) -> Iterable[SprocketFactoryData]:
    return await repository.get_all_by_sprocket_type_and_factory(
        sprocket_type, factory
    )


async def update(
    repository: SprocketFactoryDataRepository,
    dto: UpdateSprocketFactoryDataDto,
    id_: int,
) -> Optional[SprocketFactoryData]:
    return await repository.update(dto, id_)
