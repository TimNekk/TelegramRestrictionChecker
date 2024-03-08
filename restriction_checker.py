from pyrogram import Client
from pyrogram.types import Restriction


class RestrictionChecker:
    def __init__(self, client: Client):
        self.__client = client

    async def get_restrictions(self, username: str) -> list[Restriction]:
        return (await self.__client.get_chat(username)).restrictions

    async def is_restricted(self, username: str) -> bool:
        return bool(await self.get_restrictions(username))
