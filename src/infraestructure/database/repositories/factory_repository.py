from typing import Optional

from src.domain.entities.factory import Factory
from src.infraestructure.database.models.factory import Factory as Model
from src.infraestructure.database.sqlalchemy import database


async def get(id_: int) -> Optional[Factory]:
    query = Model.select().where(Model.c.id == id_)
    result = await database.fetch_one(query)

    return Factory.parse_obj(dict(result)) if result else None


async def persist(name: str) -> Factory:
    values = {
        "name": name,
    }
    query = Model.insert().values(**values)

    last_record_id = await database.execute(query)
    return Factory.parse_obj({**values, "id": last_record_id})
