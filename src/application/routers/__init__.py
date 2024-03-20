from fastapi.applications import FastAPI

from src.application.routers import factory, sprocket_type, sprocket_data_factory, root


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(root.router)
    app.include_router(factory.router, prefix="/factory")
    app.include_router(sprocket_type.router, prefix="/sprocket_type")
    app.include_router(sprocket_data_factory.router, prefix="/sprocket_type")
    return app
