print('Простое присваивание:')
shoplist = ['apples', 'mangoes', 'carrots', 'bananas']
mylist = shoplist  # mylist - лишь еще одно имя, указывающее на тот же объект!

del shoplist[0]  # Я сделал первую покупку, поэтому удалю её из списка.

print('shoplist:', shoplist)
print('mylist:', mylist)
print()
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один объект

print('Копирование при помощи полной вырезки:')
mylist = shoplist[:]  # создаем копию путём полной вырезки
del mylist[0]  # удаляем первый элемент

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратиме внимание, что теперь списки разные