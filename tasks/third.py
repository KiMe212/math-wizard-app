import asyncio
from pprint import PrettyPrinter
from typing import Coroutine

from aiohttp import ClientSession
from helpers import fetch_data

pp = PrettyPrinter()


async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_data(session, 3, 3)),
            asyncio.create_task(fetch_data(session, 3, 3)),
            asyncio.create_task(fetch_data(session, 3, 3)),
            asyncio.create_task(fetch_data(session, 3, 3)),
            asyncio.create_task(fetch_data(session, 3, 3)),
        ]

        done_tasks = []
        for done_task in asyncio.as_completed(fetchers[:]):
            result = await done_task
            done_tasks.append(result)

            if len(done_tasks) == 3:
                if done_tasks[-1]["result"] < 0:
                    print(f"Первые два результата: {done_tasks[0]}, {done_tasks[1]}")

                    for task in asyncio.tasks.all_tasks():
                        if task.get_coro() not in to_not_cancel:
                            task.cancel()
                    break

            if len(done_tasks) == 5:
                print(f"Последние два результата: {done_tasks[-2]}, {done_tasks[-1]}")

    print(f"Количество выполненных задач: {len(done_tasks)}")


to_not_cancel: set[Coroutine] = set()
coro = main()
to_not_cancel.add(coro)

print("# TASK 3")
try:
    asyncio.run(coro)
except asyncio.CancelledError:
    pass
