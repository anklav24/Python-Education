import logging
import requests


logging.basicConfig(level='DEBUG', filename='001_mylog.log')
logger = logging.getLogger()
print(logger)

for key in logging.Logger.manager.loggerDict:
    print(key)

logging.getLogger('urllib3').setLevel('CRITICAL')

def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')

    print(dir(logger))
    print()

    print(logger, logger.level)
    print()

    logger.setLevel('DEBUG')  # logging.DEBUG
    print(logger.level)
    print()

    print(logger.handlers)

    r = requests.get('https://www.google.ru')

if __name__ == '__main__':
    main('oleg')
