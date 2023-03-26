import injector
from injector import Module



class MusicEventServiceModule(Module):
    def configure(self, binder: injector.Binder) -> None:
        binder.bind(ILastFmService, LastFmService)
        binder.bind(ITicketPortalService, TicketPortalService)
        binder.bind(IDataCollectorService, DataCollectorService)
