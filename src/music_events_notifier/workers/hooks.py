from fastapi import FastAPI

from src.injection import get_injector
from src.music_events_notifier.workers.interface import IScrapingWorker


def register_scrapping_hooks(fastapi: FastAPI) -> None:
    scrapping_worker = get_injector().get(IScrapingWorker)

    @fastapi.on_event("startup")
    async def startup():
        scrapping_worker.start_scraping()
