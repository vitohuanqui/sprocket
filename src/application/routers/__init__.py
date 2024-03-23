from fastapi.applications import FastAPI

from src.application.routers import factory, sprocket_type, sprocket_data_factory, root


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(root.router)
    app.include_router(factory.router)
    app.include_router(sprocket_type.router)
    app.include_router(sprocket_data_factory.router)
    return app
