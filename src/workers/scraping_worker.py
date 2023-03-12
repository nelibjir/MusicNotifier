from src.services.last_fm_service import LastFmService
from src.services.ticketportal_service import TicketPortalService


class ScrapingWorker:

    def run(self):
        events = TicketPortalService.get_data_ticketportal()

        print(events)
        lfm = LastFmService()
        result = lfm.request_top_artists("json")
        # we trust LASTFM that the artist name is only once there in top artists
        top_artist_names = [artist.get("name") for artist in result.get("topartists").get("artist")]
        print(top_artist_names)

        my_events = self.filter_users_events(events, top_artist_names)
        print(my_events)

    @staticmethod
    def filter_users_events(events: set, my_artists_list: list) -> set:
        events_interested = set()
        for artist_name in my_artists_list:
            for event_name in events:
                if artist_name in event_name:
                    events_interested.add(event_name)
        return events_interested
