def simple_multiplication(number: int) -> int:
    """Multiplying a given number by eight if it is an even number and by nine otherwise."""
    return number * (8 if number % 2 == 0 else 9)


def simple_multiplication(number: int) -> int:
    """Multiplying a given number by eight if it is an even number and by nine otherwise."""
    return number * (8 + number % 2)


def simple_multiplication(number: int) -> int:
    """Multiplying a given number by eight if it is an even number and by nine otherwise."""
    return number * 9 if number % 2 else number * 8


print(simple_multiplication(1))
print(simple_multiplication(2))
