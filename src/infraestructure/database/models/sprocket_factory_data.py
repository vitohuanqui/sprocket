from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer, Text, Boolean, DateTime

from src.infraestructure.database.sqlalchemy import metadata

SprocketFactoryData = Table(
    "sprocket_factory_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("sprocket_type_id", Integer),
    Column("factory_id", Integer),
    Column("production", Integer),
    Column("is_goal", Boolean),
    Column("time", DateTime(timezone=True)),
)
