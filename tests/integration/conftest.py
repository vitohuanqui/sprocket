import pytest

from fastapi.testclient import TestClient
from pytest_factoryboy import register

from src.application.app import init_app
from src.infraestructure.config.enviroment import get_settings
from tests.factories.entity_factories import CreateSprocketTypeDtoFactory, \
    CreateSprocketFactoryDataDtoFactory, SprocketFactoryDataFactory
from tests.utils.utils import clear_database


@pytest.fixture(name="env_settings")
def env_settings():
    return get_settings()


@pytest.fixture(name="web_app")
def web_app_fixture(env_settings):
    return init_app(env_settings)


@pytest.fixture(name="test_client")
def test_client_fixture(web_app):
    with clear_database():
        yield TestClient(web_app)


register(CreateSprocketTypeDtoFactory)
register(SprocketFactoryDataFactory, _name="factory_sp_data")
