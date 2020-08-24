def sum_numbers(text: str) -> int:
    """In a given text sum the numbers."""
    text = text.split()
    summ = []
    for i in text:
        if i.isdigit():
            summ.append(int(i))
    return sum(summ)


def sum_numbers(text: str) -> int:
    """In a given text sum the numbers."""
    return sum(int(word) for word in text.split() if word.isdigit())

sum_numbers('hi')  #0
sum_numbers('who is 1st here') #0
sum_numbers('my numbers is 2') #2
sum_numbers('5 plus 6 is') #11
sum_numbers('') #0

