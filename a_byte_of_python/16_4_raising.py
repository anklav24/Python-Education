class ShortInputException(Exception):
    """Пользовательский класс исключения."""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Input something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Здесь может происходить обычная работа.
except EOFError:
    print('Why are you do EOF?')
except ShortInputException as ex:
    print('ShortInputException: Length entered string -- {}; \
ожидалось, как минимум, {}'.format(ex.length, ex.atleast))
else:
    print('There were no exceptions.')
