from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SprocketFactoryData(BaseModel):
    id: int
    is_goal: bool
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
    is_goal: Optional[bool] = False

    class Config:
        allow_mutation = False


class UpdateSprocketFactoryDataDto(BaseModel):
    production: Optional[int]
    time: Optional[datetime]

    class Config:
        allow_mutation = False


class RetrieveSprocketFactoryDataDto(BaseModel):
    production: int
    time: datetime

    class Config:
        allow_mutation = False
