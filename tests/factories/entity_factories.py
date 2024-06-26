import factory
from pytest_factoryboy import register

from src.domain.entities.sprocket import (CreateSprocketTypeDto, SprocketType,
                                          UpdateSprocketTypeDto)
from src.domain.entities.sprocket_factory_data import (
    CreateSprocketFactoryDataDto, RetrieveSprocketFactoryDataDto,
    SprocketFactoryData, UpdateSprocketFactoryDataDto)


@register(_name="create_sp_type_dto_factory")
class CreateSprocketTypeDtoFactory(factory.Factory):
    class Meta:
        model = CreateSprocketTypeDto

    teeth = factory.Faker("pyint")
    pitch_diameter = factory.Faker("pyint")
    outside_diameter = factory.Faker("pyint")
    pitch = factory.Faker("pyint")


class UpdateSprocketTypeDtoFactory(factory.Factory):
    class Meta:
        model = UpdateSprocketTypeDto

    teeth = factory.Faker("pyint")
    pitch_diameter = factory.Faker("pyint")
    outside_diameter = factory.Faker("pyint")
    pitch = factory.Faker("pyint")


class SprocketTypeFactory(factory.Factory):
    class Meta:
        model = SprocketType

    id = factory.Faker("pyint", min_value=1)
    teeth = factory.Faker("pyint")
    pitch_diameter = factory.Faker("pyint")
    outside_diameter = factory.Faker("pyint")
    pitch = factory.Faker("pyint")


@register(_name="create_sprocket_data_dto_factory")
class CreateSprocketFactoryDataDtoFactory(factory.Factory):
    class Meta:
        model = CreateSprocketFactoryDataDto

    production = factory.Faker("pyint", min_value=1)
    factory_id = 1
    sprocket_type_id = 1
    time = factory.Faker("date_time")
    goal = factory.Faker("pyint", min_value=1)


class UpdateSprocketFactoryDataDtoFactory(factory.Factory):
    class Meta:
        model = UpdateSprocketFactoryDataDto

    production = factory.Faker("pyint", min_value=1)
    time = factory.Faker("date_time")


class SprocketFactoryDataFactory(factory.Factory):
    class Meta:
        model = SprocketFactoryData

    id = factory.Faker("pyint", min_value=1)
    production = factory.Faker("pyint", min_value=1)
    factory_id = 1
    sprocket_type_id = 1
    time = factory.Faker("date_time")
    goal = factory.Faker("pyint", min_value=1)


class RetrieveSprocketFactoryDataDtoFactory(factory.Factory):
    class Meta:
        model = RetrieveSprocketFactoryDataDto

    production = factory.Faker("pyint", min_value=1)
    time = factory.Faker("date_time")
