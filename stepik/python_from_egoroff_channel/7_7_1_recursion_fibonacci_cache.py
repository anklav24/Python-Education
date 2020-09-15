fibonacci_cache = {}


def fibonacci(n):
    # If we have cached the value, then return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the nth term.
    if n == 0: value = 0
    elif n == 1 or n == 2: value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the value and return it.
    fibonacci_cache[n] = value
    return value


for n in range(0, 1001, 100):
    print(f"{n}: {fibonacci(n)}")
