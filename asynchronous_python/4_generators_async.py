# https://www.youtube.com/watch?v=PjZUSSkGLE8&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=4&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2
# run python -i filename  # Передаем все в интерактивный режим
# David Beazley
# It does not work for me.

import socket
from select import select

tasks = []

to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        yield "read", server_socket
        client_socket, addr = server_socket.accept()  # read
        print('Connection from', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield "read", client_socket
        request = client_socket.recv(4096)  # read

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()

            yield "write", client_socket
            client_socket.send(response)  # write

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

    try:
        task = tasks.pop(0)

        reason, sock = next(task)

        if reason == "read":
            to_read[sock] = task
        if reason == "write":
            to_write[sock] = task
    except StopIteration:
        print("Done!")


tasks.append(server())
event_loop()
