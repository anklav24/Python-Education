# Аннотация типов Type Annotation и docstring
def add(x: "int, > 0", y: int) -> int:
    """ Складывает x и y.
    x - число или строка
    y - число или строка"""
    return x + y


# Функция f
print('add(1, 2) =', add(1, 2))
print(type(add(1, 2)))
print()

