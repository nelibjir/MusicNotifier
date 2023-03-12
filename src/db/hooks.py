from databases import Database
from fastapi import FastAPI

from src.injection import get_injector


def register_user_db_hooks(fastapi: FastAPI) -> None:
    database = get_injector().get(Database)

    @fastapi.on_event("startup")
    async def startup():
        await database.connect()

    @fastapi.on_event("shutdown")
    async def shutdown():
        await database.disconnect()
