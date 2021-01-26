# #!/usr/bin/python

from websocket import create_connection

ws = create_connection("ws://localhost:8888/chatsocket")
ws.send('{"task":"join", "token":"Mr.Hidden"}')
result = ws.recv()
print(f"Received {result}")
ws.close()
