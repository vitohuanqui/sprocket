from fastapi.applications import FastAPI

from src.application.routers import (factory, root, sprocket_data_factory,
                                     sprocket_type)


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(root.router)
    app.include_router(factory.router)
    app.include_router(sprocket_type.router)
    app.include_router(sprocket_data_factory.router)
    return app
