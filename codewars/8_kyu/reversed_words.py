def reverseWords(str):
    """Reverses all of the words within the string passed in."""
    lst = str.split()
    lst.reverse()
    return ' '.join(lst)


def reverseWords(str: str) -> str:
    """Reverses all of the words within the string passed in."""
    return ' '.join(str.split()[::-1])


print(reverseWords("The greatest victory is that which requires no battle"))
print(reverseWords("hello world!"))
