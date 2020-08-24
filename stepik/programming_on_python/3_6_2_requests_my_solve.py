import os
import requests

path = os.path.join('C:\\', 'Users', 'Admin', 'Downloads', 'dataset_3378_2 (5).txt')
print(path)

with open(path) as inf:
    url = inf.readline().strip()
    r = requests.get(url)

for i in r.text.splitlines():
    print(i)

print(len(r.text.splitlines()))
