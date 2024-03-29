import asyncio
import logging
from dataclasses import dataclass
from typing import Set

from injector import inject, Inject

import nest_asyncio

from src.music_events_notifier.db.tables.my_event import MyEvent
from src.music_events_notifier.services.scrapping_services.interface import ITicketPortalService, ILastFmService
from src.music_events_notifier.workers.interface import IScrapingWorker

nest_asyncio.apply()

log = logging.getLogger(__name__)


@inject
@dataclass
class ScrapingWorkerDependencies:
    ticket_portal_service: ITicketPortalService
    lastfm_service: ILastFmService


class ScrapingWorker(IScrapingWorker):
    def __init__(
        self,
        deps: Inject[ScrapingWorkerDependencies],
    ):
        self.deps = deps

    def start_scraping(self):
        events = asyncio.run(self.deps.ticket_portal_service.get_event_data())
        log.info(events)

        result = self.deps.lastfm_service.request_top_artists("json")
        # we trust LASTFM that the artist name is only once there in top artists
        top_artist_names = {artist.get("name") for artist in result.get("topartists").get("artist")}
        log.info(top_artist_names)

        my_events = self.filter_users_events(events, top_artist_names)
        log.info(my_events)

    @staticmethod
    def filter_users_events(events: Set[MyEvent], my_artists: set) -> set:
        events_interested = set()
        for artist_name in my_artists:
            for event in events:
                if artist_name in event.name:
                    events_interested.add(artist_name)
        return events_interested
