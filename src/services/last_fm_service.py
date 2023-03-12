import logging
import time

import requests

from src.settings import settings

log = logging.getLogger(__name__)


class LastFmService:
    HEADERS = {
        "User-Agent": f"Event notifier, user: Nelibjir",
    }

    def request_top_artists(self, output_format):
        if output_format not in ["json", "xml"]:
            log.error(f"Not supported format: {output_format}")
            return
        # TODO: user.gettopartists can be as parameter and format also
        #       number constants should be put also away
        request_url = settings.LAST_FM_BASE_URL + \
                      f"?method=user.gettopartists" \
                      f"&user={settings.LAST_FM_USERNAME}" \
                      f"&api_key={settings.LAST_FM_API_KEY}" \
                      f"&period={settings.LAST_FM_HISTORY}" \
                      f"&limit={settings.LAST_FM_LIMIT}" \
                      f"&format={output_format}"
        response = requests.get(request_url, headers=self.HEADERS)
        for retry_nb in range(settings.REQUEST_NB_ATTEMPTS):
            if response.status_code == 200:
                break
            else:
                log.info(
                    f"Re-attempting to load LAST FM Data on url: {request_url}. "
                    f"Re-attempt no.: {retry_nb + 1}."
                )
                time.sleep(10 ** retry_nb)
                response = requests.get(request_url, headers=HEADERS)
        else:
            log.error(
                "Request for top artists from LAST FM failed with status code "
                + str(response.status_code)
                + "after "
                + str(settings.REQUEST_NB_ATTEMPTS + 1)
                + " re-attempts. Request URL:"
                + request_url
            )
            raise ConnectionError
        log.info("Successfully loaded top artists from LAST FM.")
        return response.json()
