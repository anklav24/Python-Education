import sys
import os

print('command line arguments:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
print()
print(os.getcwd())
