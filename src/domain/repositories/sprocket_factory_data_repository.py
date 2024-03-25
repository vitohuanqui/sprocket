from typing import Iterable, Optional, Protocol

from src.domain.entities.factory import Factory
from src.domain.entities.sprocket import SprocketType
from src.domain.entities.sprocket_factory_data import (
    CreateSprocketFactoryDataDto, RetrieveSprocketFactoryDataDto,
    SprocketFactoryData, UpdateSprocketFactoryDataDto, ResponseFactoryDataDto)


class SprocketFactoryDataRepository(Protocol):
    async def delete(self, id_: int) -> bool: ...

    async def get(self, id_: int) -> Optional[SprocketFactoryData]: ...

    async def create(
        self, dto: CreateSprocketFactoryDataDto
    ) -> SprocketFactoryData: ...

    async def update(
        self,
        dto: UpdateSprocketFactoryDataDto,
        id_: int,
    ) -> Optional[SprocketFactoryData]: ...

    async def get_all(
        self, query_params: dict = None
    ) -> ResponseFactoryDataDto: ...

    async def get_all_by_factory(
        self, factory: Factory
    ) -> Iterable[SprocketFactoryData]: ...

    async def get_all_by_sprocket_type(
        self, sprocket_type: SprocketType
    ) -> Iterable[SprocketFactoryData]: ...

    async def get_all_by_sprocket_type_and_factory(
        self, sprocket_type: SprocketType, factory: Factory
    ) -> Iterable[SprocketFactoryData]: ...

    async def save_data(
        self, data: list[CreateSprocketFactoryDataDto]
    ) -> Iterable[SprocketFactoryData]: ...
