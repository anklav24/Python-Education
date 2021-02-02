# Вытащи куда нибудь в отдельную папку и заработает

import logging

from tornado.ioloop import IOLoop
from tornado.websocket import websocket_connect

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:   %(message)s")


async def main():
    url = "ws://app.testdlab.com:8888/websocket"
    client = await websocket_connect(url)

    tasks = ('{"task": "check_game_queue"}',
             '{"task": "check_spectator_queue"}',
             '{"task": "get_in_game_queue"}',
             )
    for task in tasks:
        await client.write_message(task)

    while True:
        message = await client.read_message()
        logging.info(f"{message}")


if __name__ == '__main__':
    IOLoop.current().run_sync(main)
