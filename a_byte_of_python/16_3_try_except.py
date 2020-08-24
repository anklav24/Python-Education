while True:
    try:
        text = input('Input something --> ')
    except EOFError:
        print('Why are you do EOF?')
        break
    except KeyboardInterrupt:
        print('You canceled operation.')
    else:
        print('You entered: {}'.format(text))
