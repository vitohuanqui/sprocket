import asyncio

from celery import Celery

from src.infraestructure.cellery.config import settings as celery_settings
from src.infraestructure.database.sqlalchemy import connect_database
from src.infraestructure.database.sqlalchemy import \
    init_database as init_pgsql_db


async def start_db():
    init_pgsql_db()
    await connect_database()


celery = Celery('Celery App')
celery.config_from_object(celery_settings, namespace='CELERY')
loop = asyncio.get_event_loop()
factories = loop.run_until_complete(start_db())
celery.autodiscover_tasks(['src.application.celery_tasks'])
celery.conf.beat_schedule = {
    'get_sprocket_factory_data': {
        'task': 'get_sprocket_factory_data',
        "schedule": 60,
    },
}
# from celery import current_app as current_celery_app
#
# from src.infraestructure.cellery.config import settings as celery_settings
#
#
# def create_celery():
#     celery_app = current_celery_app
#     celery_app.config_from_object(celery_settings, namespace='CELERY')
#     celery_app.autodiscover_tasks(['src.application.celery_tasks'])
#     celery_app.conf.beat_schedule = {
#         'get_sprocket_factory_data': {
#             'task': 'get_sprocket_factory_data',
#             "schedule": 60,
#         },
#     }
#
#     return celery_app
