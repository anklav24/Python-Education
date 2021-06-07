# https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('DEBUG'))
# true

load_dotenv(override=True)
# override existing variable in the environment
