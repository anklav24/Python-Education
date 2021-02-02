# Вытащи куда нибудь в отдельную папку и заработает

import asyncio
import logging

from tornado.websocket import websocket_connect

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")


async def read_message(client):
    while True:
        message = await client.read_message()
        logging.info(f"{message}")


async def write_message(client):
    tasks = ('{"task": "check_game_queue"}',
             '{"task": "check_spectator_queue"}',
             '{"task": "get_in_game_queue"}',
             )
    for task in tasks:
        await client.write_message(task)
        logging.info(f"{task}")


async def main():
    url = "ws://app.testdlab.com:8888/websocket"
    client = await websocket_connect(url)
    task1 = asyncio.create_task(read_message(client))
    task2 = asyncio.create_task(write_message(client))
    tasks = [task1, task2]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
