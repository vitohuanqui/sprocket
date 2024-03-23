import datetime
from typing import Optional, List, Iterable

from src.domain.entities.sprocket_factory_data import (
    SprocketFactoryData,
    CreateSprocketFactoryDataDto,
    UpdateSprocketFactoryDataDto,
)
from src.domain.entities.sprocket import SprocketType
from src.domain.entities.factory import Factory
from src.infraestructure.database.models.sprocket_factory_data import SprocketFactoryData as Model
from src.infraestructure.database.sqlalchemy import database


async def get_all() -> Iterable[SprocketFactoryData]:
    query = Model.select()
    result = await database.fetch_all(query)

    return (SprocketFactoryData.parse_obj(dict(r)) for r in result)


async def get_all_by_factory(factory: Factory) -> Iterable[SprocketFactoryData]:
    query = Model.select().where(Model.c.factory_id == factory.id)
    result = await database.fetch_all(query)

    return (SprocketFactoryData.parse_obj(dict(r)) for r in result)


async def get_all_by_sprocket_type(sprocket_type: SprocketType) -> Iterable[SprocketFactoryData]:
    query = Model.select().where(Model.c.sprocket_type_id == sprocket_type.id)
    result = await database.fetch_all(query)
    return (SprocketFactoryData.parse_obj(dict(r)) for r in result)


async def get_all_by_sprocket_type_and_factory(sprocket_type: SprocketType, factory: Factory) -> Iterable[SprocketFactoryData]:
    query = Model.select().where(Model.c.sprocket_type_id == sprocket_type.id).where(Model.c.factory_id == factory.id)
    result = await database.fetch_all(query)

    return (SprocketFactoryData.parse_obj(dict(r)) for r in result)


async def get(id_: int) -> Optional[SprocketFactoryData]:
    query = Model.select().where(Model.c.id == id_)
    result = await database.fetch_one(query)

    return SprocketFactoryData.parse_obj(dict(result)) if result else None


async def create(dto: CreateSprocketFactoryDataDto, is_goal: bool=False) -> SprocketFactoryData:
    #TODO: check if we using a datetime now.
    values = {**dto.dict(), "is_goal": is_goal, "time": datetime.datetime.now()}
    query = Model.insert().values(**values)
    last_record_id = await database.execute(query)
    return SprocketFactoryData.parse_obj({**values, "id": last_record_id})


async def update(dto: UpdateSprocketFactoryDataDto, id_: int) -> Optional[SprocketFactoryData]:
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
