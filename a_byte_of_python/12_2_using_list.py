# This is my shopping list.
shoplist = ['Apples', 'Mangoes', 'Carrots', 'Bananas']

print('I should do', len(shoplist), 'purchase.')
print('Purchase:', end=' ')
for item in shoplist:
    print(item, end=' ')
print()
print()

print('Also, need buy some rice.')
shoplist.append('Rice')
print('Now my shopping list such is:', shoplist)
print()
print('I\'ll sort my shopping list')
shoplist.sort()
print('The sorted list looks like that:', shoplist)
print()

print('The first thing I need to buy is:', shoplist[0])
olditem = shoplist[0]
del shoplist[0]

print()
print('I buy', olditem)
print('Now my shoplist list such is')
