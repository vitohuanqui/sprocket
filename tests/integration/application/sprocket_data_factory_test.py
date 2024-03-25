import pytest


@pytest.mark.integration
class TestHandleCreateOne:
    def test_success(self, test_client, create_sprocket_type_dto):
        with test_client:
            response = test_client.post(
                "/sprocket-type/",
                json=create_sprocket_type_dto.dict(),
            )
            data, status_code = response.json(), response.status_code
            assert status_code == 201
            data.pop('id')
            assert data == {
                "teeth": create_sprocket_type_dto.teeth,
                "pitch_diameter": create_sprocket_type_dto.pitch_diameter,
                "outside_diameter": create_sprocket_type_dto.outside_diameter,
                "pitch": create_sprocket_type_dto.pitch,
            }

    def test_validation_error(self, test_client):
        with test_client:
            response = test_client.post(
                "/sprocket-data-factory/",
                json={},
            )
            data, status_code = response.json(), response.status_code
            assert status_code == 422


@pytest.mark.integration
class TestHandleGetAll:
    def test_success(self, test_client, factory_sp_data):
        with test_client:

            # insert_sp_data_item(factory_sp_data.dict())

            response = test_client.get("/sprocket-data-factory/")
            data, status_code = response.json(), response.status_code
            assert status_code == 200
