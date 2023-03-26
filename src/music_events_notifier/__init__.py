from typing import Final

from fastapi import APIRouter, FastAPI
from starlette import status

from .exception_handlers import register_handlers
from .models.error import HTTPError
from .settings import settings

PREFIX: Final[str] = "/api"


def create_root_router():
    # later here the endpoint for communication

    root_router = APIRouter(prefix=PREFIX)

    return root_router


def create_app() -> FastAPI:
    fastapi = FastAPI(
        title="Music Notifier API",
        responses={
            status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": HTTPError},
        },
        openapi_url="/openapi.json" if settings.ENVIRONMENT == "develop" else "",
    )
    fastapi.include_router(create_root_router())
    register_handlers(fastapi)

    return fastapi
