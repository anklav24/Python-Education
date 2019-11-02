number = 23
guess = int(input('Please enter int number: '))

if guess == number:
    print('Поздравляю, вы угадали,')  # Here start new block
    print('(хотя и не выиграли никакого приза!)')
elif guess < number:
    print('Нет, загаданное число немного больше этого.')
else:
    print('Нет, загаданное чило немного меньше этого.')

print('End')

if True:
    print('if really True')
