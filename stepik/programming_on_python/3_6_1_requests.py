import requests

r = requests.get('http://example.com')
print(r.text)
print('-------------------')
print()

url = 'http://example.com'
par = {'key1': 'value2', 'key2': 'value2', 'key3': 'value3'}
r = requests.get(url, params=par)
print(r.url)
print('-------------------')

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)
print(r.text)

print(r.cookies['example_cookie_name'])
