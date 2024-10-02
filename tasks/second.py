import asyncio
from typing import Coroutine

from aiohttp import ClientSession
from helpers import fetch_data


async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_data(session, 2, 0)),
            asyncio.create_task(fetch_data(session, "a", 2)),
            asyncio.create_task(fetch_data(session, 3, 1)),
            asyncio.create_task(fetch_data(session, 60, 20)),
            asyncio.create_task(fetch_data(session, 80, 4)),
        ]

        done_tasks = []
        for done_task in asyncio.as_completed(fetchers[:]):
            result = await done_task
            done_tasks.append(result)

            if len(done_tasks) == 2:
                print(done_tasks[-1])

                for task in asyncio.tasks.all_tasks():
                    if task.get_coro() not in to_not_cancel:
                        task.cancel()
                break

    print(f"Количество выполненных задач: {len(done_tasks)}")


to_not_cancel: set[Coroutine] = set()
coro = main()
to_not_cancel.add(coro)

print("# TASK 2")
try:
    asyncio.run(coro)
except asyncio.CancelledError:
    pass
