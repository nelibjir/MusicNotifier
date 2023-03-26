import abc


class IEventService(abc.ABC):
    @abc.abstractmethod
    async def save_event_data(
        self,
        interesting_events: set,
        source_data: set,
    ):
        """
        Save the data to SQL and the data from scrapping to NoSql
        """