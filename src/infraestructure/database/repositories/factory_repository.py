from typing import Optional, Iterable

from src.domain.entities.factory import Factory, CreateFactoryDto, UpdateFactoryDto
from src.infraestructure.database.models.factory import Factory as Model
from src.infraestructure.database.sqlalchemy import database


async def get(id_: int) -> Optional[Factory]:
    query = Model.select().where(Model.c.id == id_)
    result = await database.fetch_one(query)

    return Factory.parse_obj(dict(result)) if result else None


async def get_all() -> Iterable[Factory]:
    query = Model.select()
    result = await database.fetch_all(query)

    return (Factory.parse_obj(dict(r)) for r in result)


async def create(dto: CreateFactoryDto) -> Factory:
    values = dto.dict()
    query = Model.insert().values(**values)

    last_record_id = await database.execute(query)
    return Factory.parse_obj({**values, "id": last_record_id})


async def update(dto: UpdateFactoryDto, id_: int) -> Optional[Factory]:
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
