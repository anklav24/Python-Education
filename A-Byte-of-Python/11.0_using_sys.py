import os
import sys

print('command line arguments:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
print()
print(os.getcwd())
