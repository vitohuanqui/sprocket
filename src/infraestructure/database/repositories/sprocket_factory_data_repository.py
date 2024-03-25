import datetime
from typing import Optional, List, Iterable

from sqlalchemy import func, select, extract, text
from sqlalchemy.sql.base import _NoArg

from src.domain.entities.sprocket_factory_data import (
    SprocketFactoryData,
    CreateSprocketFactoryDataDto,
    UpdateSprocketFactoryDataDto,
    RetrieveSprocketFactoryDataDto,
)
from src.domain.entities.sprocket import SprocketType
from src.domain.entities.factory import Factory
from src.infraestructure.database.models.sprocket_factory_data import SprocketFactoryData as Model
from src.infraestructure.database.sqlalchemy import database


async def get_all(query_params: dict=None) -> Iterable[RetrieveSprocketFactoryDataDto]:
    params = [Model.c.is_goal == False]
    MAPPING = {
        'year': ['year'],
        'month': ['year', 'month'],
        'day': ['year', 'month', 'day'],
        'hour': ['year', 'month', 'day', 'hour'],
    }
    if 'end_date' in query_params:
        params.append(Model.c.time <= datetime.datetime.strptime(query_params['end_date'], '%Y-%m-%d'))
    if 'start_date' in query_params:
        params.append(Model.c.time >= datetime.datetime.strptime(query_params['start_date'], '%Y-%m-%d'))
    if 'factory' in query_params:
        params.append(Model.c.factory_id >= int(query_params['factory']))
    if 'sprocket_type' in query_params:
        params.append(Model.c.sprocket_type_id >= int(query_params['sprocket_type']))
    group_by = []
    select_list = [Model.c.production, Model.c.time]
    if 'group_by' in query_params and query_params['group_by'] in MAPPING:
        select_list = [func.sum(Model.c.production).label('production')]
        group_by = [extract(x, Model.c.time) for x in MAPPING[query_params['group_by']]]
        select_list += [extract(x, Model.c.time).label(x) for x in MAPPING[query_params['group_by']]]

    query = select(
        *select_list
    )
    if params:
        query = query.where(*params)
    if group_by:
        query = query.group_by(*group_by).order_by(*group_by)
    result = await database.fetch_all(query)
    response = []
    now = datetime.datetime.now()
    for row in result:
        data = dict(row)
        time = data.get('time')
        if group_by:
            time = datetime.datetime(
                int(data.get('year', now.year)),
                int(data.get('month', now.month)),
                int(data.get('day', now.day)),
                int(data.get('hour', now.hour)))
        response.append(RetrieveSprocketFactoryDataDto.parse_obj({"production": data.get('production', 0), "time": time}))

    return response


async def get_all_by_factory(factory: Factory) -> Iterable[SprocketFactoryData]:
    query = Model.select().where(Model.c.factory_id == factory.id)
    result = await database.fetch_all(query)

    return (SprocketFactoryData.parse_obj(dict(r)) for r in result)


async def get_all_by_sprocket_type(sprocket_type: SprocketType) -> Iterable[SprocketFactoryData]:
    query = Model.select().where(Model.c.sprocket_type_id == sprocket_type.id)
    result = await database.fetch_all(query)
    return (SprocketFactoryData.parse_obj(dict(r)) for r in result)


async def get_all_by_sprocket_type_and_factory(sprocket_type: SprocketType, factory: Factory) -> Iterable[SprocketFactoryData]:
    query = Model.select().where(Model.c.sprocket_type_id == sprocket_type.id, Model.c.factory_id == factory.id)
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


async def save_data(dtos: list[CreateSprocketFactoryDataDto]) -> bool:
    values = [dto.dict() for dto in dtos]
    query = Model.insert().values(values)
    await database.execute(query)
    return True
