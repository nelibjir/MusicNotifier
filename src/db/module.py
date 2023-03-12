import databases
from injector import Module, provider, singleton

from src.data_evaluation import settings


class DbModule(Module):
    @singleton
    @provider
    def provide_database(self) -> databases.Database:
        return databases.Database(settings.DATABASE_URL)
