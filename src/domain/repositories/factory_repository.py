from typing import Iterable, Optional, Protocol

from src.domain.entities.factory import (
    Factory,
    UpdateFactoryDto,
    CreateFactoryDto,
)


class FactoryRepository(Protocol):
    async def delete(self, id_: int) -> bool:
        ...

    async def get(self, id_: int) -> Optional[Factory]:
        ...

    async def create(self, dto: CreateFactoryDto) -> Factory:
        ...

    async def update(
        self, dto: UpdateFactoryDto, id_: int,
    ) -> Optional[Factory]:
        ...

    async def get_all(self) -> Iterable[Factory]:
        ...
