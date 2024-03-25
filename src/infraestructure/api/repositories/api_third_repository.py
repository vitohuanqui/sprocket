from typing import Any

import requests


def fetch_data(url) -> Any:
    response = requests.get(url or 'http://third-container:8000/data')
    data = response.json()
    return data
