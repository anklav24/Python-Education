import os
import requests

path = os.path.join('C:\\', 'Users', 'Admin', 'Downloads', 'dataset_3378_3 (1).txt')
print(f'Path: {path}')

with open(path) as inf:
    url = inf.readline().strip()
    print(f'URL: {url}')
    print()

while True:
    next_file = requests.get(url)
    if next_file.text[:2] == 'We':
        print(next_file.text)
        break
    else:
        print(f'Next_file: {next_file.text}')
        url = f'{url[:-10]}{next_file.text}'
        print(f'URL: {url}')
        print()
