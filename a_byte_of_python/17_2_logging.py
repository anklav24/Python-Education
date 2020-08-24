import logging
import os
import platform

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
                                os.getenv('HOMEPATH'), \
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Save log into', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug('Start program')
logging.info('Some action')
logging.warning('Program dying')
