"""Обрабатываем JSON так, чтобы не возникало исключений если ключа нет в сообщении"""
import json
from collections import defaultdict

"""
Отличие defaultdict в том что он изменяет сам словарь,
а метод словаря .get просто возвращает значение
"""

message = '{"user":"user_name", "token": "user_token"}'

message = json.loads(message)
message = defaultdict(lambda x=None: None, message)  # If the value doesn't exist equate it to None

user_name = message["user"]
user_token = message["token"]
does_not_exist = message["does_not_exist"]

print(f'{message=}', user_name, user_token, does_not_exist, sep="\n")
