from typing import Any

from aiohttp import ClientSession


async def fetch_data(session: ClientSession, x: Any, y: Any):
    async with session.get(
        "http://localhost:8008/chaos_div",
        params={"x": x, "y": y},
    ) as response:
        return await response.json()
