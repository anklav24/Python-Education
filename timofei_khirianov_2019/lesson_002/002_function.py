# def сокращение от слова define - определять
def f(x, y):
    return x + y


def p3(x):
    print(x)
    print(x)
    print(x)


# Функция f
print('f(1, 2) =', f(1, 2))
print(type(f(1, 2)))
print()

# Функция p3
x = p3('Hello')
print(type(x))