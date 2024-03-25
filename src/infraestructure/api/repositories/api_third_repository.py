from typing import Any
from slack_sdk import WebClient
import requests

from src.infraestructure.config.enviroment import get_settings
_SETTINGS = get_settings()


def notify_error_connection(msg):
    client = WebClient(token=_SETTINGS.SLACK_API_TOKEN)
    response = client.chat_postMessage(
        channel=_SETTINGS.SLACK_CHANNEL, text=msg)
    assert response["ok"]


def fetch_data(url) -> Any:
    data = {}
    try:
        response = requests.get(url or 'http://third-container:8000/data')
        data = response.json()
    except Exception as e:
        msg = f"Error with connection: {str(e)}"
        notify_error_connection(msg)
    finally:
        return data

