# https://www.youtube.com/watch?v=MPjgHxK8k68&list=TLPQMTEwMTIwMjFoJhMKcfqfFw&index=15&ab_channel=CryptoFun%5BIT%5D
import socket
import threading
import time

key = 8194

shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                """
                # Begin
                decrypt = "";
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i) ^ key)
                print(decrypt)
                # End
                """

                time.sleep(0.2)
        except:
            pass


# host = socket.gethostbyname(socket.gethostname())
host = "192.168.88.10"
port = 0

server = ("192.168.88.10", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(False)

alias = input("Name: ")

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

while shutdown == False:
    if join == False:
        s.sendto(("[" + alias + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()
            """
            # Begin
            crypt = ""
            for i in message:
                crypt += chr(ord(i) ^ key)
            message = crypt
            # End
            """
            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + alias + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
