from abc import ABC, abstractmethod
from typing import Any


class ApiThirdDataRepository(ABC):
    @abstractmethod
    def fetch_data(self) -> Any:
        pass
