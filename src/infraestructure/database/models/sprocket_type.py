from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer

from src.infraestructure.database.sqlalchemy import metadata

SprocketType = Table(
    "sprocket_type",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("teeth", Integer),
    Column("pitch_diameter", Integer),
    Column("outside_diameter", Integer),
    Column("pitch", Integer),
)
