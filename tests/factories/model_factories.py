from functools import partial
from typing import Any, Dict, Iterable, Union

from sqlalchemy.schema import Table

from src.infraestructure.database.models.factory import Factory
from src.infraestructure.database.models.sprocket_type import SprocketType
from src.infraestructure.database.models.sprocket_factory_data import SprocketFactoryData
from src.infraestructure.database.sqlalchemy import metadata


ValuesType = Dict[str, Any]


def insert_model(model: Table, values: Union[ValuesType, Iterable[ValuesType]]) -> None:
    query = model.insert()
    if isinstance(values, Dict):
        with metadata.bind.connect() as conn:
            conn.execute(query, **values)
    else:
        with metadata.bind.connect() as conn:
            conn.execute(query, list(values))


insert_factory_item = partial(insert_model, Factory)
insert_sp_item = partial(insert_model, SprocketType)
insert_sp_data_item = partial(insert_model, SprocketFactoryData)
