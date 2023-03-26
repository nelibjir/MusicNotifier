from typing import List, Optional

from src.music_events_notifier.common.base_model import ViewModel, Model


class Error(Model):
    error: str
    code: Optional[str]
    loc: Optional[str]


class HTTPError(ViewModel):
    """
    Business models
    """

    detail: List[Error]
