from functools import partial
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from tests.utils.utils import assert_validation_error
from src.domain.entities.sprocket import CreateSprocketTypeDto


DataType = Dict[str, Any]


@pytest.fixture(name="valid_data")
def valid_data_fixture() -> DataType:
    return {
      "teeth": 5,
      "pitch_diameter": 5,
      "outside_diameter": 6,
      "pitch": 1
    }


@pytest.fixture(name="invalid_data")
def invalid_data_fixture() -> DataType:
    return {
      "teeth": "teeth",
      "pitch_diameter": 5,
      "outside_diameter": 6,
      "pitch": 1
    }


@pytest.mark.unit
class TestCreateSprocketTypeDto:
    class TestModel:
        def test_validation(self, valid_data):
            assert CreateSprocketTypeDto(**valid_data)

        def test_invalidation(self, invalid_data):
            with pytest.raises(ValidationError):
                CreateSprocketTypeDto(**invalid_data)

    class TestTeeth:
        assert_validation_error = partial(assert_validation_error, 1, "teeth")

        def test_must_be_int(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"teeth": "1et"})
                CreateSprocketTypeDto(**valid_data)

            self.assert_validation_error("int_parsing", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("teeth")
                CreateSprocketTypeDto(**valid_data)

            self.assert_validation_error("missing", excinfo)
