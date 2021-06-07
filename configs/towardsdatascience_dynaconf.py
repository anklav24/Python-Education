# https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

# .env
# ROOT_PATH_FOR_DYNACONF = "configs/"
# SETTINGS_FILE_FOR_DYNACONF="['settings.ini', 'settings2.ini']"

from dynaconf import settings

print(settings["DB"])
# xiaoxu_database
