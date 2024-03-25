import json
import logging
from typing import Any, Dict, Iterable

from databases import Database
from sqlalchemy.schema import Table

from src.infraestructure.database.models.factory import Factory
from src.infraestructure.database.models.sprocket_type import SprocketType
from src.infraestructure.database.models.sprocket_factory_data import SprocketFactoryData
from src.infraestructure.database.sqlalchemy import (
    database_context,
    init_database,
    truncate_database,
)

logger = logging.getLogger(__name__)


async def _populate_table(
    db: Database, table: Table, values: Iterable[Dict[str, Any]],
):
    name: str = table.name
    query = table.insert()

    logger.info(f"Seeding table {name}")
    await db.execute_many(query, list(values))
    logger.info(f"Seeded table {name} successfully")


async def _populate_data(db: Database) -> None:
    f = open('seed_sprocket_types.json')
    values_sprocket_type = json.load(f)['sprockets']
    f.close()
    values_factory = [{
        'name': 'Factory #1',
        'url': 'third-app:8000/data'
    },{
        'name': 'Factory #2',
        'url': 'third-app:8000/data'
    }]
    await _populate_table(db, Factory, values_factory)
    await _populate_table(db, SprocketType, values_sprocket_type)
    for idx_factory, _ in enumerate(values_factory):
        for idx_spr_type, _ in enumerate(values_sprocket_type):
            await _populate_sprocket_factory_data(db, idx_factory, idx_spr_type)


async def _populate_sprocket_factory_data(db: Database, factory_id: int, sprocket_type_id: int) -> None:
    f = open('seed_factory_data.json')
    values = []
    json_values = json.load(f)['factories']
    for factory in json_values:
        for idx, val in enumerate(factory['factory']['chart_data']['sprocket_production_actual']):
            values.append({
                'production': val,
                'time': factory['factory']['chart_data']['time'][idx],
                'is_goal': False,
                'factory_id': factory_id,
                'sprocket_type_id': sprocket_type_id
            })
            values.append({
                'production': factory['factory']['chart_data']['sprocket_production_goal'][idx],
                'time': factory['factory']['chart_data']['time'][idx],
                'is_goal': True,
                'factory_id': factory_id,
                'sprocket_type_id': sprocket_type_id
            })
    f.close()
    await _populate_table(db, SprocketFactoryData, values)


async def run() -> None:
    logger.info("Initializing databases")
    init_database()
    async with database_context() as database:
        logger.info("Truncating database")
        await truncate_database()
        logger.info("Populating database")
        await _populate_data(database)
        logger.info("Finished populating PostgreSQL database")
