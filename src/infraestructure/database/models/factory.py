from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer, Text

from src.infraestructure.database.sqlalchemy import metadata

Factory = Table(
    "factory",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text()),
    Column("url", Text()),
)
