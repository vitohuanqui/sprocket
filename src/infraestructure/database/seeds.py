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
    values_sprocket_type = [
    ]
    values_factory = []
    await _populate_table(db, Factory, values_factory)
    await _populate_table(db, SprocketType, values_sprocket_type)
    for idx_factory, _ in enumerate(values_factory):
        for idx_spr_type, _ in enumerate(values_sprocket_type):
            await _populate_sprocket_factory_data(db, idx_factory, idx_spr_type)


async def _populate_sprocket_factory_data(db: Database, factory_id: int, sprocket_type_id: int) -> None:
    values = [
        {"msg": "Program new awesome web app", "is_done": True, "user_id": factory_id},
        {"msg": "Play videogames", "is_done": True, "user_id": factory_id},
        {"msg": "Wash dishes", "is_done": False, "user_id": factory_id},
        {"msg": "Write blog post", "is_done": False, "user_id": factory_id},
    ]
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
