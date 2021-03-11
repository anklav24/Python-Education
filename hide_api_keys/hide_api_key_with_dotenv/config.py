import os
import dotenv

dotenv.load_dotenv("production.env")

API_KEY = os.getenv('IMPORTANT_API_KEY_IN_ENV_FILE')
