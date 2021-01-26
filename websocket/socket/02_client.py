import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8765))
s.sendall(b'Hello, world!')
data = s.recv(1024)
s.close()
print('Received data', repr(data))
