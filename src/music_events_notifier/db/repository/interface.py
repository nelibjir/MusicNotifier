import abc
from typing import List

from src.music_events_notifier.db.tables.my_event import MyEvent


class IMyEventsRepository(abc.ABC):
    @abc.abstractmethod
    def save_data(self, my_events: List[MyEvent]):
        """
        Save data to SQL DB
        """