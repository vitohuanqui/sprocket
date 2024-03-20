from typing import Optional

from src.domain.entities.sprocket import SprocketType
from src.infraestructure.database.models.sprocket_type import SprocketType as Model
from src.infraestructure.database.sqlalchemy import database


async def get(id_: int) -> Optional[SprocketType]:
    query = Model.select().where(Model.c.id == id_)
    result = await database.fetch_one(query)

    return SprocketType.parse_obj(dict(result)) if result else None


async def persist(teeth: int, pitch_diameter: int, outside_diameter: int, pitch: int) -> SprocketType:
    values = {
        "teeth": teeth,
        "pitch_diameter": pitch_diameter,
        "outside_diameter": outside_diameter,
        "pitch": pitch,
    }
    query = Model.insert().values(**values)

    last_record_id = await database.execute(query)
    return SprocketType.parse_obj({**values, "id": last_record_id})
