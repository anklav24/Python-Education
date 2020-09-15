from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check the input is a positive integer.
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 0:
        raise ValueError("n must be a positive int")

    # Compute the Nth term.
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 1001):
    print(f"{i}: {fibonacci(i)}")

for i in range(1, 1001):
    print(f"{i}: {fibonacci(i + 1) / fibonacci(i)}")
