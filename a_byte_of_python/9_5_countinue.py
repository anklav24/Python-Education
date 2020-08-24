while True:
    print('Hello world')
    s = input('Enter anything: ')
    if s == 'exit':
        print('See you!')
        break
    if len(s) < 3:
        print('So less!')
        continue
    print('This string correct length')
