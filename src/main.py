import logging

import sentry_sdk
import uvicorn
from sentry_sdk import set_level
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from src.settings import settings

log = logging.getLogger(__name__)

sentry_sdk.init(
    settings.SENTRY_DNS,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=0.0,
    environment=settings.ENVIRONMENT,
)

set_level("warning")

logging.basicConfig(level=logging.INFO)

# TODO https://goout.net/
# TODO ticketstream
init_injector()
app = create_app()
register_user_db_hooks(app)
register_evaluation_hooks(app)

try:
    app.add_middleware(SentryAsgiMiddleware)
except Exception:
    log.warning("SentryAsgiMiddleware integration failed")
    # pass silently if the Sentry integration failed
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
