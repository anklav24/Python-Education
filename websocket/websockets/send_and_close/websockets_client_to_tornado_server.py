import asyncio
import websockets
import time


async def connect_to_server(url, header):
    async with websockets.connect(url) as websocket:
        await websocket.send(header)
        print(f"> {header}")

        response = await websocket.recv()
        print(f"< {response}")

# async def connect_to_server(url, header):
#     async with websockets.connect(url) as websocket:
#         await websocket.send(header)
#         response = await websocket.recv()
#         print(response)

# def main():
#     for action in actions:
#         header = '{"task":"' + action + '", "token":"' + token + '"}'
#         asyncio.get_event_loop().run_until_complete(connect_to_server(url, header))
#         print()
#         time.sleep(3)


def main():
    asyncio.get_event_loop().run_until_complete(connect_to_server(url, header))
    asyncio.get_event_loop().run_forever()


actions = ["join", "queue", "search", "echo", "decline"]
token = "Mr.Hidden1"
url = "ws://localhost:8888/chatsocket"
header = '{"task":"join", "token":"' + token + '"}'

if __name__ == "__main__":
    main()
