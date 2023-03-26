import databases
from injector import Module, provider, singleton

from src.music_events_notifier import settings


class DbModule(Module):
    @singleton
    @provider
    def provide_database(self) -> databases.Database:
        return databases.Database(settings.DATABASE_URL)
