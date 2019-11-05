shoplist = ['Apples', 'Mangoes', 'Carrots', 'Bananas']
name = 'swaroop'

# Операция индексирования
print('Element 0 -', shoplist[0])
print('Element 1 -', shoplist[1])
print('Element 2 -', shoplist[2])
print('Element 3 -', shoplist[3])
print('Element -1 -', shoplist[-1])
print('Element -2 -', shoplist[-2])
print('Element 0 -', shoplist[0])
print()

# Вырезка из списка
print('Elements from 1 until 3:', shoplist[1:3])
print('Elements from 2 until end:', shoplist[2:])
print('Elements from 1 until -1:', shoplist[1:-1])
print('Elements from start until end:', shoplist[:])
print()

# Вырезка из строки
print('Symbols from 1 until 3:', name[1:3])
print('Symbols from 2 until end:', name[2:])
print('Symbols from 1 until -1:', name[1:-1])
print('Symbols from start until end:', name[:])
print()

# 3-й аргумент шаг вырезки
print(shoplist)
print()
print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::4])
print(shoplist[::5])
print(shoplist[::-1])
print(shoplist[::-2])
print(shoplist[::-3])
