import injector
from injector import Module

from src.music_events_notifier.services.events_service import EventService
from src.music_events_notifier.services.interface import IEventService
from src.music_events_notifier.services.scrapping_services.interface import ILastFmService, ITicketPortalService
from src.music_events_notifier.services.scrapping_services.last_fm_service import LastFmService
from src.music_events_notifier.services.scrapping_services.ticketportal_service import TicketPortalService


class MusicEventServiceModule(Module):
    def configure(self, binder: injector.Binder) -> None:
        binder.bind(ILastFmService, LastFmService)
        binder.bind(ITicketPortalService, TicketPortalService)
        binder.bind(IEventService, EventService)
