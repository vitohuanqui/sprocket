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


async def fetch_all_by_sprocket_type(sprocket_type_id: SprocketType) -> Iterable[SprocketFactoryData]:
    query = Model.select().where(Model.c.sprocket_type_id == sprocket_type_id.id)

    results = await database.fetch_all(query)
    return (SprocketFactoryData.parse_obj(dict(r)) for r in results)
