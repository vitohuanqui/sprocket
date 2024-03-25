from typing import Iterable, Optional

from src.domain.entities.sprocket import (CreateSprocketTypeDto, SprocketType,
                                          UpdateSprocketTypeDto)
from src.domain.repositories.sprocket_repository import SprocketTypeRepository


async def create(
    repository: SprocketTypeRepository,
    dto: CreateSprocketTypeDto,
) -> SprocketType:
    return await repository.create(dto)


async def delete(repository: SprocketTypeRepository, id_: int) -> bool:
    return await repository.delete(id_)


async def get(
    repository: SprocketTypeRepository, id_: int
) -> Optional[SprocketType]:
    return await repository.get(id_)


async def get_all(
    repository: SprocketTypeRepository,
) -> Iterable[SprocketType]:
    return await repository.get_all()


async def update(
    repository: SprocketTypeRepository,
    dto: UpdateSprocketTypeDto,
    id_: int,
) -> Optional[SprocketType]:
    return await repository.update(dto, id_)
