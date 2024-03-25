import pytest

from src.domain.repositories.sprocket_repository import SprocketTypeRepository
from src.domain.services import sprocket_service


@pytest.fixture()
def repository(mock_module):
    return mock_module("sprocket_repository", SprocketTypeRepository)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_create(repository, create_sprocket_type_dto_factory, sprocket_type_factory):
    repository.create.return_value = sprocket_type_factory
    result = await sprocket_service.create(repository, create_sprocket_type_dto_factory)
    repository.create.assert_called_once_with(create_sprocket_type_dto_factory)
    assert result == sprocket_type_factory


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete(repository):
    id_ = 1
    repository.delete.return_value = True
    result = await sprocket_service.delete(repository, id_)
    repository.delete.assert_called_once_with(id_)
    assert result is True


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get(repository, sprocket_type_factory):
    id_ = sprocket_type_factory.id
    repository.get.return_value = sprocket_type_factory
    result = await sprocket_service.get(repository, id_)
    repository.get.assert_called_once_with(id_)
    assert result == sprocket_type_factory


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update(repository, update_sprocket_type_dto_factory, sprocket_type_factory):
    id_ = 1
    repository.update.return_value = sprocket_type_factory
    result = await sprocket_service.update(
        repository, update_sprocket_type_dto_factory, id_
    )
    repository.update.assert_called_once_with(update_sprocket_type_dto_factory, id_)
    assert result == sprocket_type_factory
