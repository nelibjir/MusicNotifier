import logging
import requests
from requests_html import AsyncHTMLSession

from src.music_events_notifier.db.tables.my_event import MyEvent
from src.music_events_notifier.services.scrapping_services.interface import ITicketPortalService
from src.music_events_notifier.settings import settings

log = logging.getLogger(__name__)


class TicketPortalService(ITicketPortalService):
    def __init__(self):
        self._asession = AsyncHTMLSession()

    async def get_event_data(self) -> set:
        row_number = 0
        events = set()

        try:
            r = (await self._asession.get(settings.TICKETPORTAL_URL))
            await r.html.arender()

            while True:
                # try what will happen if it will no
                element = r.html.find(f"#timeline_row_{str(row_number)}")
                row_number += 1
                if element is None or len(element) == 0:
                    break

                for caption in element[0].find(".caption"):
                    city = caption.find(".place")[0].text
                    event_name = caption.find("h3")[0].text
                    date = caption.find(".date")[0].text
                    event = MyEvent(date=date, location=city, name=event_name)
                    events.add(event)

                #for event_name in element[0].find("h3"):
                #    event_names.add(event_name.text)
        except requests.exceptions.RequestException as e:
            log.error(f"Error while requesting Ticket Portal: {e}")

        return events
