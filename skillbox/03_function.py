# импорт функции определленой
# from helper_03_function import check_symbols
# Импортировать целиком модуль
import helper_03_function
import os

username = 'asdfjk324#'
email = 'qwe@q#we.ru'
# Обращение через функцию
# if check_symbols(['#', '$#', '@'], username):
#     print('Wrong username')
# if check_symbols(restricted_symbols=['#', '$#', '%'], s=email):
#     print('Wrong password')

# Обращение через модуль в функции
if helper_03_function.check_symbols(['#', '$#', '@'], username):
    print('Wrong username')
if helper_03_function.check_symbols(restricted_symbols=['#', '$#', '%'], s=email):
    print('Wrong password')

print(os.name)