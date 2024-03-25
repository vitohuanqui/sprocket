from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SprocketFactoryData(BaseModel):
    id: int
    goal: int
    production: int
    factory_id: int
    time: datetime
    sprocket_type_id: int

    class Config:
        allow_mutation = False
        orm_mode = True


class CreateSprocketFactoryDataDto(BaseModel):
    production: int
    factory_id: int
    sprocket_type_id: int
    time: Optional[datetime] = datetime.now
    goal: int

    class Config:
        allow_mutation = False


class UpdateSprocketFactoryDataDto(BaseModel):
    production: Optional[int]
    goal: Optional[int]
    time: Optional[datetime]

    class Config:
        allow_mutation = False


class RetrieveSprocketFactoryDataDto(BaseModel):
    production: int
    time: datetime
    goal: int

    class Config:
        allow_mutation = False


class ResponseFactoryDataDto(BaseModel):
    production: list[int]
    goal: list[int]
    times: list[int]

    class Config:
        allow_mutation = False
