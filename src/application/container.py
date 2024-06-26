from dataclasses import dataclass
from typing import Callable, cast

from src.domain.repositories.api import ApiThirdDataRepository
from src.domain.repositories.factory_repository import FactoryRepository
from src.domain.repositories.sprocket_factory_data_repository import \
    SprocketFactoryDataRepository
from src.domain.repositories.sprocket_repository import SprocketTypeRepository
from src.infraestructure.api.repositories import api_third_repository
from src.infraestructure.database.repositories import (
    factory_repository, sprocket_factory_data_repository,
    sprocket_type_repository)


@dataclass(frozen=True)
class Dependencies:
    factory_repository: FactoryRepository
    sprocket_repository: SprocketTypeRepository
    sprocket_factory_data_repository: SprocketFactoryDataRepository
    api_third_repository: ApiThirdDataRepository


def _build_dependencies() -> Callable[[], Dependencies]:
    deps = Dependencies(
        factory_repository=cast(FactoryRepository, factory_repository),
        sprocket_repository=cast(
            SprocketTypeRepository, sprocket_type_repository
        ),
        sprocket_factory_data_repository=cast(
            SprocketFactoryDataRepository, sprocket_factory_data_repository
        ),
        api_third_repository=cast(
            ApiThirdDataRepository, api_third_repository
        ),
    )

    def fn() -> Dependencies:
        return deps

    return fn


get_dependencies = _build_dependencies()
