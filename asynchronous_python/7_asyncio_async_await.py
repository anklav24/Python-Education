# https://www.youtube.com/watch?v=LO61F07s7gw&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=7&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2
# pip (pip3) install aiohttp
import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(f"print_nums: {num}")
        num += 1
        await asyncio.sleep(0.5)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"print_time: {count} seconds have passed.")
        count += 1
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
