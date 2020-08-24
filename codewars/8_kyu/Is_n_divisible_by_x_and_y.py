def is_divisible_comminity(n, x, y):
    return n % x == 0 and n % y == 0


def is_divisible_my_solution(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


print(is_divisible_comminity(12, 4, 4))
print(is_divisible_comminity(3, 4, 4))
print()

print(is_divisible_my_solution(12, 4, 4))
print(is_divisible_my_solution(2, 4, 4))
