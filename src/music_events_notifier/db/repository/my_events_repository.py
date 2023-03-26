from dataclasses import dataclass
from typing import List

from databases import Database
from injector import inject, Inject

from src.music_events_notifier.db.repository.interface import IMyEventsRepository
from src.music_events_notifier.db.tables.my_event import MyEvent


@inject
@dataclass
class MyEventsRepositoryDependencies:
    db: Database


class MyEventsRepository(IMyEventsRepository):
    def __init__(
        self,
        deps: Inject[MyEventsRepositoryDependencies],
    ):
        self.deps = deps

    def save_data(self, my_events: List[MyEvent]):
        await self.deps.db.execute_many(MyEvent.insert(), my_events)
