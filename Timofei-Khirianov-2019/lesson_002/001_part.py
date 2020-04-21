x = 5
# x = int(input('Input X: '))
while x > 0:  # Заголовок цикла
    print(x)
    x -= 1
print()

# Цикл for
# For each next object in cortege print x ** 2
for x in 1, 5, 2, 4, 3:  # Кортеж (Итерируемые объект)
    print(x ** 2)
print()

x = 1
while x < 6:
    print(x)
    x += 1
print()

# Генератор арифметических прогрессий
a = range(1, 11, 1)
print('Напечатать 3-е число из массива')
print('a[2] =', a[2])
print()
for x in a:
    print(x)
print()

for x in range(5):
    print(x)