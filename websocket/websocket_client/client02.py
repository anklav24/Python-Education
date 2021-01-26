import asyncore
import os
import sys
import websocket

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('usage: %s <message>\n' % os.path.abspath(__file__))
        sys.exit(1)

    ws = websocket.WebSocket('ws://localhost:8888/',
                             onopen=lambda: ws.send(sys.argv[1]),
                             onmessage=lambda m: sys.stdout.write('Echo: %s\n' % m),
                             onclose=lambda: sys.stdout.write('Connection closed.\n'))
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        ws.close()
