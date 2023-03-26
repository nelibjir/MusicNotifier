import injector
from injector import Module

from src.music_events_notifier.workers.interface import IScrapingWorker
from src.music_events_notifier.workers.scraping_worker import ScrapingWorker


class ScrapingWorkerModule(Module):
    def configure(self, binder: injector.Binder) -> None:
        binder.bind(IScrapingWorker, ScrapingWorker)
