from typing import Optional

from pydantic import BaseModel, EmailStr


class SprocketType(BaseModel):
    id: int
    teeth: int
    pitch_diameter: int
    outside_diameter: int
    pitch: int

    class Config:
        allow_mutation = False
        orm_mode = True


class CreateSprocketTypeDto(BaseModel):
    teeth: int
    pitch_diameter: int
    outside_diameter: int
    pitch: int

    class Config:
        allow_mutation = False


class UpdateSprocketTypeDto(BaseModel):
    teeth: Optional[int]
    pitch_diameter: Optional[int]
    outside_diameter: Optional[int]
    pitch: Optional[int]

    class Config:
        allow_mutation = False
