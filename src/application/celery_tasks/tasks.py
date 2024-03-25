import asyncio
import datetime

from celery import shared_task

from src.application.container import get_dependencies
from src.domain.entities.sprocket_factory_data import \
    CreateSprocketFactoryDataDto
from src.domain.services import factory_service, sprocket_service

repository = get_dependencies().api_third_repository
factory_repository = get_dependencies().factory_repository
sp_factory_data_repository = (
    get_dependencies().sprocket_factory_data_repository
)
sprocket_type_repository = get_dependencies().sprocket_repository


@shared_task(name="get_sprocket_factory_data")
def _get_sprocket_factory_data():
    time = datetime.datetime.now().timestamp()
    data = []
    loop = asyncio.get_event_loop()
    factories = loop.run_until_complete(
        factory_service.get_all(factory_repository)
    )
    sp_types = loop.run_until_complete(
        sprocket_service.get_all(sprocket_type_repository)
    )
    for factory in factories:
        response_data = repository.fetch_data(factory.url)
        for sp_type in sp_types:
            data.append(
                CreateSprocketFactoryDataDto(
                    **{
                        "production": response_data['production'],
                        "time": time,
                        "factory_id": factory.id,
                        "sprocket_type_id": sp_type.id,
                        "is_goal": False,
                    }
                )
            )
            data.append(
                CreateSprocketFactoryDataDto(
                    **{
                        "production": response_data['goal'],
                        "time": time,
                        "factory_id": factory.id,
                        "sprocket_type_id": sp_type.id,
                        "is_goal": True,
                    }
                )
            )
    loop.run_until_complete(sp_factory_data_repository.save_data(data))
