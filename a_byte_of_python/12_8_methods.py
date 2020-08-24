name = 'Swaroop'  # This an object of a string
print('String:', name)

if name.startswith('Swa'):
    print('Yes, string start on “Swa”')

if 'a' in name:
    print('Yes, it contains a string “a”')

if name.find('war') != -1:
    print('Yes, it contains a string “war”')
print()

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
