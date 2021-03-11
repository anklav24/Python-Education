import os
import dotenv

"""
По умолчанию ищет .env файл
Но можно натравить на свой
"""
dotenv.load_dotenv("production.env")

API_KEY = os.getenv('IMPORTANT_API_KEY_IN_ENV_FILE')
