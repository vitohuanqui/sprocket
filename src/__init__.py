import uvicorn

from src.infraestructure.config.enviroment import get_settings
from src.application.app import init_app


_SETTINGS = get_settings()


web_app = init_app(_SETTINGS)


def start_web_server() -> None:
    settings = get_settings()
    uvicorn.run(
        "src:web_app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        log_level=settings.LOG_LEVEL,
    )
