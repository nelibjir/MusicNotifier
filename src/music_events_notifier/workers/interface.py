import abc


class IScrapingWorker(abc.ABC):
    @abc.abstractmethod
    async def start_scraping(
        self,
    ):
        """
        Start the scraping process
        """
