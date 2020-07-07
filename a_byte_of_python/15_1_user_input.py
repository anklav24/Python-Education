def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


# Составил список заменяемых символов
replace_symbols = ("'", " ", ",", ".", "!")

while True:
    something = input('Input text: ')
    # Удаляем из строки все запрещенные символы находящиеся в кортеже.
    for symbol in replace_symbols:
        something = something.replace(symbol, '')

    # Меняем регистр всех букв чтобы строка прошла проверку.
    something = something.lower()
    print(something)

    if is_palindrome(something):
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not palindrome.")
    print()
