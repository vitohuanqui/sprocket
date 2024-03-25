from src.infraestructure.config.enviroment import get_settings

_SETTINGS = get_settings()


class Config:
    CELERY_BROKER_URL: str = _SETTINGS.CELERY_BROKER_URL
    CELERY_RESULT_BACKEND: str = _SETTINGS.CELERY_RESULT_BACKEND
    CELERY_TASK_ROUTES: dict = {
        'tasks.*': {
            'queue': 'high_priority',
        },
        'low_priority_tasks.*': {
            'queue': 'low_priority',
        },
    }

    CELERY_FAST_API_SCHEDULE: dict = {
        "get_sprocket_factory_data": {
            "task": "get_sprocket_factory_data",
            "schedule": 60,
            'options': {'queue': 'periodic'},
        },
    }


settings = Config()
