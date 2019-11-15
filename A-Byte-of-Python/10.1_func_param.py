def print_max(a, b):
    if a > b:
        print(a, 'max')
    elif a == b:
        print(a, 'equally', b)
    else:
        print(b, 'max')


print_max(1, 4)  # straight forward value Прямая передача значений

x = 5
y = 6
print_max(x, y)  # передача переменных в качестве аргументов
