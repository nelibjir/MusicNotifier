import abc
from typing import Dict, List, Optional

from src.music_events_notifier.models.error import Error


class AppException(Exception, abc.ABC):
    errors: List[Error]
    headers: Optional[Dict[str, str]]

    def __init__(self, errors: List[Error], headers: Optional[Dict[str, str]] = None):
        self.headers = headers
        self.errors = errors


class UnauthorizedException(AppException):
    @classmethod
    def new(cls, error: str, headers: Optional[Dict[str, str]] = None):
        return cls([Error(error=error)], headers=headers)


class ForbiddenException(AppException):
    pass


class NotFoundException(AppException):
    pass


class ValidationException(AppException):
    pass


class BadRequestException(AppException):
    @classmethod
    def new(cls, error: Optional[str] = None):
        return cls([Error(error=error)])


class InternalException(AppException):
    """
    For application errors, results in 500.
    """

    @classmethod
    def new(cls, error: Optional[str] = None):
        return cls([Error(error=error)])
