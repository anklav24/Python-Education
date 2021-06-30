"""Обрабатываем JSON так, чтобы не возникало исключений если ключа нет в сообщении"""
import json

message = '{"user":"user_name", "token": "user_token"}'

message = json.loads(message)

# user_name = message["user"]
# user_token = message["token"]
# does_not_exist = message["does_not_exist"]

user_name = message.get("user")
user_token = message.get("token")
does_not_exist = message.get("does_not_exist")
"""
It's like
does_not_exist = message.get("does_not_exist", default_value=None)

So
does_not_exist = message.get("does_not_exist", "qwerty")
printed > qwerty
"""
print(f'{message=}', f'{type(message)=}', user_name, user_token, does_not_exist, sep="\n")