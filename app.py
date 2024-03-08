import asyncio
import json

from pyrogram import Client

from src import print_restrictions_table, RestrictionChecker


def get_config(config_file: str) -> dict:
    with open(config_file, "r") as f:
        return json.load(f)


async def main():
    config = get_config("config.json")
    usernames = config["usernames"]

    async with Client(
            name="my_account",
            api_id=config["api"]["id"],
            api_hash=config["api"]["hash"]
    ) as client:
        checker = RestrictionChecker(client)
        username_restrictions = {username: await checker.get_restrictions(username) for username in usernames}

    print_restrictions_table(username_restrictions)


if __name__ == "__main__":
    asyncio.run(main())
