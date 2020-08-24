def power_sum(power, *args):
    """Возвращает сумму аргументов, возведённых в указанную степень."""
    total = 0
    for i in args:
        print(args)
        total += pow(i, power)
        return total


# Код не работает как должен, возводит в степень только первый аргумент из кортежа.
print(power_sum(2, 2, 4))
print()
print(power_sum(2, 2, 4, 8))
print()
print(power_sum(2, 10))
print()
print(power_sum(2, 10, 100))
