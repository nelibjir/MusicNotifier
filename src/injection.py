from typing import Optional

import injector

from src.music_events_notifier.services.module import MusicEventServiceModule


def configure_injector() -> injector.Injector:

    from src.music_events_notifier.db.module import DbModule
    from src.music_events_notifier.workers.module import ScrapingWorkerModule

    i = injector.Injector(
        modules=[
            DbModule,
            ScrapingWorkerModule,
            MusicEventServiceModule,
        ],
        auto_bind=True,
    )
    return i


_inj: Optional[injector.Injector] = None


def get_injector():
    global _inj
    assert _inj is not None, "Injector not initialized"
    return _inj


def init_injector():
    global _inj
    if _inj is None:
        _inj = configure_injector()


def clear_injector():
    global _inj
    del _inj
    _inj = None  # noqa: F841
