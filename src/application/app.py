from fastapi.applications import FastAPI
from toolz import pipe

from src.application.routers import register_routers as register_routers
from src.infraestructure.config.enviroment import Settings
from src.infraestructure.database.sqlalchemy import (connect_database,
                                                     disconnect_database)
from src.infraestructure.database.sqlalchemy import \
    init_database as init_pgsql_db


def create_instance(settings: Settings) -> FastAPI:
    return FastAPI(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
    )


def init_databases(app: FastAPI) -> FastAPI:
    init_pgsql_db()
    return app


def register_events(app: FastAPI) -> FastAPI:
    app.on_event("startup")(connect_database)
    app.on_event("shutdown")(disconnect_database)

    return app


def register_middlewares(app: FastAPI) -> FastAPI:
    return app


def init_app(settings: Settings) -> FastAPI:
    app: FastAPI = pipe(
        settings,
        create_instance,
        init_databases,
        register_events,
        register_middlewares,
        register_routers,
    )
    return app
