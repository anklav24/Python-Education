number = 23
running = True

while running:
    guess = int(input('Please enter int count: '))
    if guess == number:
        print('Congratulation! You luck.')
        running = False  # This break loop
    elif guess < number:
        print('No, number some more than it.')
    else:
        print('No, number some less than it.')
else:
    print('loop end')
