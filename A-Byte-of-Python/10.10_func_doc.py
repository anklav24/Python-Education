def printMax(x, y):
    """Выводит максимальное из двух чисел.

       Оба должны быть целыми числами."""
    x = int(x)  # конвертирует в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'max number')
    else:
        print(y, 'max number')


printMax(3, 5)
print(printMax.__doc__)
