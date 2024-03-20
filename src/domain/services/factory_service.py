from typing import Iterable, Optional

from src.domain.entities.factory import (
    Factory,
    CreateFactoryDto,
    UpdateFactoryDto,
)
from src.domain.repositories.factory_repository import FactoryRepository


async def create(
    repository: FactoryRepository, dto: CreateFactoryDto,
) -> Factory:
    return await repository.create(dto)


async def delete(repository: FactoryRepository, id_: int) -> bool:
    return await repository.delete(id_)


async def get(repository: FactoryRepository, id_: int) -> Optional[Factory]:
    return await repository.get(id_)


async def get_all(repository: FactoryRepository) -> Iterable[Factory]:
    return await repository.get_all()


async def update(
    repository: FactoryRepository,
    dto: UpdateFactoryDto,
    id_: int,
) -> Optional[Factory]:
    return await repository.update(dto, id_)
