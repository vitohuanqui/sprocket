from typing import Iterable, Optional, Protocol

from src.domain.entities.sprocket import (
    SprocketType,
    UpdateSprocketTypeDto,
    CreateSprocketTypeDto,
)


class SprocketTypeRepository(Protocol):
    async def delete(self, id_: int) -> bool:
        ...

    async def get(self, id_: int) -> Optional[SprocketType]:
        ...

    async def create(self, dto: CreateSprocketTypeDto) -> SprocketType:
        ...

    async def update(
        self, dto: UpdateSprocketTypeDto, id_: int,
    ) -> Optional[SprocketType]:
        ...

    async def get_all(self) -> Iterable[SprocketType]:
        ...
