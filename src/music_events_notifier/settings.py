from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    LAST_FM_API_KEY: str = Field(..., env="LAST_FM_API_KEY")
    LAST_FM_REQUEST_USERNAME: str = Field(..., env="LAST_FM_REQUEST_USERNAME")
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    SENTRY_DNS: str = Field(..., env="SENTRY_DNS")
    ENVIRONMENT: str = Field(..., env="ENVIRONMENT")

    LAST_FM_BASE_URL = "http://ws.audioscrobbler.com/2.0/"
    # overall | 7day | 1month | 3month | 6month | 12month
    LAST_FM_HISTORY = "12month"
    LAST_FM_LIMIT = 100

    TICKETPORTAL_URL = "https://www.ticketportal.cz/hudba"

    REQUEST_NB_ATTEMPTS = 5

    class Config:
        env_file = "../../.env"


settings = Settings()
