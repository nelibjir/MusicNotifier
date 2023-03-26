import asyncio

import logging
from dataclasses import dataclass

from injector import Inject, inject

from src.music_events_notifier.db.repository.interface import IMyEventsRepository
from src.music_events_notifier.services.interface import IEventService

log = logging.getLogger(__name__)


@inject
@dataclass
class EventServiceDependencies:
    repository: IMyEventsRepository


class EventService(IEventService):
    def __init__(
        self,
        deps: Inject[EventServiceDependencies],
    ):
        self.deps = deps

    async def save_event_data(self, interesting_events: set, source_data: set):
        # TODO save here also to Mongo
        await self.deps.repository.save_data()