def expression_matter(a: int, b: int, c: int) -> int:
    """+ * ()"""
    """
    Given that a, b, c >= 1,
    (a+b)c = ac + bc >= a + bc
    a*(b+c) = ab + ac >= a*b + c
    """
    arr = []
    arr.append(a + b + c)
    arr.append(a * b * c)
    arr.append((a + b) * c)
    arr.append(a * (b + c))
    return max(arr)


def expression_matter_community(a, b, c):
    return max(a + b + c, a * b * c, (a + b) * c, a * (b + c))


print(expression_matter(1, 2, 3))
print(expression_matter_community(1, 2, 3))

