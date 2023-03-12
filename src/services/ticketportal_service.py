from requests_html import HTMLSession

from src.settings import settings


class TicketPortalService:

    @staticmethod
    def get_data_ticketportal() -> set:
        session = HTMLSession()
        r = session.get(settings.TICKETPORTAL_URL)
        r.html.render()
        # page = requests.get(URL)

        number = 0
        events = set()
        while True:
            # try what willl happen if it will no
            element = r.html.find(f"#timeline_row_{str(number)}")
            number += 1
            if element is None or len(element) == 0:
                break

            for event_name in element[0].find("h3"):
                events.add(event_name.text)

        return events
