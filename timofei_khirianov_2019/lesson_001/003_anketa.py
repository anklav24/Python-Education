name = input('Hello! What is your name? : ')
print('Nice to meet you,', name + '!')
print()

age = int(input('How old are you ' + name + '? : '))
print()

x = age + 1

print('А я думал тебе', x, end=' ')
if x >= 11 and x <= 19:
    print('лет', end='')
elif x % 10 == 1:
    print('год', end='')
elif x % 10 >= 2 and x % 10 <= 4:
    print('года', end='')
else:
    print('лет', end='')
print('!')
