def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


while True:
    something = input('Input text: ')
    if is_palindrome(something):
        print("Yes, it is a palindrome.")
    else:
        print("No, it's not palindrome.")
    print()
