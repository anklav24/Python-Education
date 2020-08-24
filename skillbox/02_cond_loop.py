if 8 / 3 == 2:
    print('Ok 1')
elif 8 / 3 == 2.66666666666666666666666666666:
    print('Ok 2')
elif 8 / 3 == 2.66666666666666666666666666666:
    print('Ok 2')
elif 8 / 3 == 2.66666666666666666666666666666:
    print('Ok 2')
else:
    print('Not ok')

password = '' # not known

if not password:
    true_password = '12345'
else:
    true_password = password

# то же самое только в одну строку
true_password = password if password else '12345'
print(true_password)

for i in [1, 2, 3, 4, 5, 6]:
    print(i * i)

print()

for i in range(1, 11):
    # Только четные числа
    if i % 2 == 0:
        print(i)

# то же самое только в одну строку
print()
print('List')
lc = [i * i for i in range(1, 11)]
print(lc)
print()

i = 0
while len(str(i)) < 3:
    print(i)
    i += 1 # i = i + 1