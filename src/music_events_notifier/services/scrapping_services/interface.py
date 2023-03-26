import abc


class ITicketPortalService(abc.ABC):
    @abc.abstractmethod
    async def get_event_data(self):
        """
        Get the data from TicketPortal site
        """


class ILastFmService(abc.ABC):
    @abc.abstractmethod
    def request_top_artists(self, output_format):
        """
        Get the top artists from LastFM page
        """