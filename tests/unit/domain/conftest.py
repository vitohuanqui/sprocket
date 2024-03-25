import pytest
from pytest_factoryboy import register

from tests.factories.entity_factories import *

FACTORIES = [
    UpdateSprocketTypeDtoFactory,
    SprocketTypeFactory,
]

for factory in FACTORIES:
    register(factory)


@pytest.fixture()
def mock_function(mocker):
    return lambda name, return_value: mocker.MagicMock(
        name=name, return_value=return_value
    )


@pytest.fixture()
def mock_module(mocker):
    return lambda name, spec: mocker.Mock(name=name, spec=spec)
