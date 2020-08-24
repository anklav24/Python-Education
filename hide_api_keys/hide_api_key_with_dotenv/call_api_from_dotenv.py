import os
from dotenv import load_dotenv  # If you don't have it. Just do this. pip install python-dotenv
load_dotenv()

API_KEY = os.getenv('PROJECT_API_KEY')
YOUR_API_KEY = os.getenv('YOUR_API_KEY')

print(API_KEY)
print(YOUR_API_KEY)
