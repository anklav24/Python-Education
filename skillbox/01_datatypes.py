a = 1 / 3
b = a + 2

print(a)

print(type(a))

print(a + a + a)
s = '1234567890'
print(type(s))

# выкинуть один символ с конца

print(s[0:-1])

list_of_something = [1, 2, 3, 4, 'abc', ['1', True]]
print(list_of_something)
print(list_of_something[0])
print(list_of_something[5][0])
print(list_of_something[3:4])
print(list_of_something[3:-1])

dictionary = {
    'key': 'value',
    'Moscow': 'Москва',
    'l': list_of_something
}

print(dictionary)
print(dictionary['Moscow'])
print(dictionary['l'])

