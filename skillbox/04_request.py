import requests

r = requests.get('https://google.com')
print(r.text)

# 1
i = 0
while i < 1000:
    r = requests.get('https://4ДУШИ.РФ')
    print(r.text)
    i += 1

print()
# 1
for i in range(1000):
    r = requests.get('https://4ДУШИ.РФ')
    print(r.text)
    i += 1

