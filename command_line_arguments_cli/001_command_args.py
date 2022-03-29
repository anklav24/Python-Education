import argparse

parser = argparse.ArgumentParser(description='Demo project')
parser.add_argument('--host', help='Host to listen', default='0.0.0.0')
parser.add_argument('--port', help='Port to accept connections', default='666')
parser.add_argument('--reload', help='reload_true')

args = parser.parse_args()
print(args)

query = 'SELECT * FROM data'

i = 0
# while True:
#     i += 1
#     print(i)
