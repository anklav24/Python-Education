import requests
url, name, count = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt', 0
while name[:2] != 'We':
    name = requests.get(url + name).text
    count += 1
    print(count)
print(name)