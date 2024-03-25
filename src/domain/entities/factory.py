from typing import Optional

from pydantic import BaseModel, Field

NameType = Field(..., min_length=3, max_length=100)
URLType = Field(..., min_length=3, max_length=100)


class Factory(BaseModel):
    id: int
    name: str = NameType
    url: Optional[str] = URLType

    class Config:
        allow_mutation = False
        orm_mode = True


class CreateFactoryDto(BaseModel):
    name: str = NameType
    url: str = URLType

    class Config:
        allow_mutation = False


class UpdateFactoryDto(BaseModel):
    name: Optional[str] = NameType
    url: Optional[str] = URLType

    class Config:
        allow_mutation = False
