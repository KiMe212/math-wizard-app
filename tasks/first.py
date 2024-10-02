import asyncio
from pprint import PrettyPrinter

from aiohttp import ClientSession
from helpers import fetch_data

pp = PrettyPrinter()


async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_data(session, 2, 0)),
            asyncio.create_task(fetch_data(session, "a", 2)),
            asyncio.create_task(fetch_data(session, 3, "b")),
            asyncio.create_task(fetch_data(session, 40.0, 10.0)),
            asyncio.create_task(fetch_data(session, 5, 40)),
        ]

        results = await asyncio.gather(*fetchers, return_exceptions=True)
        pp.pprint(results)


print("# TASK 1")
asyncio.run(main())
