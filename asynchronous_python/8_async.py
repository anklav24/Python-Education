# Download jpg jpeg from website
# https://www.youtube.com/watch?v=LO61F07s7gw&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=7&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2
# Просто не асинхронная программа
import requests
from time import time


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = response.url.split("/")[-1]
    with open(filename, "wb") as file:
        file.write(response.content)


def main():
    t0 = time()
    url = "https://loremflickr.com/320/240"

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)


if __name__ == '__main__':
    main()