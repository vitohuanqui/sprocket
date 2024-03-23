from typing import Optional, Iterable

from src.domain.entities.sprocket import SprocketType, CreateSprocketTypeDto, UpdateSprocketTypeDto
from src.infraestructure.database.models.sprocket_type import SprocketType as Model
from src.infraestructure.database.sqlalchemy import database


async def get(id_: int) -> Optional[SprocketType]:
    query = Model.select().where(Model.c.id == id_)
    result = await database.fetch_one(query)

    return SprocketType.parse_obj(dict(result)) if result else None


async def create(dto: CreateSprocketTypeDto) -> SprocketType:
    values = dto.dict()
    query = Model.insert().values(**values)

    last_record_id = await database.execute(query)
    return SprocketType.parse_obj({**values, "id": last_record_id})


async def get_all() -> Iterable[SprocketType]:
    query = Model.select()
    result = await database.fetch_all(query)

    return (SprocketType.parse_obj(dict(r)) for r in result)


async def update(dto: UpdateSprocketTypeDto, id_: int) -> Optional[SprocketType]:
    if not await get(id_):
        return None
    values = dto.dict(exclude_unset=True)
    query = (
        Model.update()
        .where(Model.c.id == id_)
        .values(**values)
    )
    await database.execute(query)

    return await get(id_)


async def delete(id_: int) -> bool:
    if not await get(id_):
        return False

    query = (
        Model.delete()
        .where(Model.c.id == id_)
    )
    await database.execute(query)
    return True
