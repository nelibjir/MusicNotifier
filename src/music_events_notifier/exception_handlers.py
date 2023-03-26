import logging

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .exceptions import (
    AppException,
    BadRequestException,
    Error,
    ForbiddenException,
    InternalException,
    NotFoundException,
    UnauthorizedException,
    ValidationException,
)
from .models.error import HTTPError

logger = logging.getLogger(__name__)


def create_response(status_code: int, exception: AppException):
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(HTTPError(detail=exception.errors)),
        headers=exception.headers,
    )


def register_handlers(
    app: FastAPI,
) -> None:
    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(
        _: Request, exc: RequestValidationError
    ):
        errors = []
        for e in exc.errors():
            errors.append(
                Error(
                    error=e["msg"],
                )
            )
        return create_response(
            status.HTTP_422_UNPROCESSABLE_ENTITY, ValidationException(errors=errors)
        )

    @app.exception_handler(UnauthorizedException)
    async def unauthorized_exception_handler(_: Request, exc: UnauthorizedException):
        return create_response(status.HTTP_401_UNAUTHORIZED, exc)

    @app.exception_handler(ForbiddenException)
    async def forbidden_exception_handler(_: Request, exc: ForbiddenException):
        return create_response(status.HTTP_403_FORBIDDEN, exc)

    @app.exception_handler(NotFoundException)
    async def notfound_exception_handler(_: Request, exc: NotFoundException):
        return create_response(status.HTTP_404_NOT_FOUND, exc)

    @app.exception_handler(ValidationException)
    async def validation_exception_handler(_: Request, exc: ValidationException):
        return create_response(status.HTTP_422_UNPROCESSABLE_ENTITY, exc)

    @app.exception_handler(InternalException)
    async def internal_exception_handler(_: Request, exc: InternalException):
        logger.error(str(exc), extra={"exception": exc})
        return create_response(status.HTTP_500_INTERNAL_SERVER_ERROR, exc)

    @app.exception_handler(Exception)
    async def general_exception_handler(_: Request, exc: Exception):
        logger.error(str(exc), extra={"exception": exc})
        return create_response(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            InternalException([Error(error="SERVER_ERROR")]),
        )

    @app.exception_handler(BadRequestException)
    async def bad_request_exception_handler(_: Request, exc: BadRequestException):
        return create_response(status.HTTP_400_BAD_REQUEST, exc)
