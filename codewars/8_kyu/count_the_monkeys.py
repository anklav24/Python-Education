def monkey_count(n):
    """Count monkeys from first to last."""
    monkeys = []
    for i in range(1, n + 1):
        monkeys.append(i)
    return monkeys


def monkey_count_community(n):
    return range(1, n + 1)


print(monkey_count(5))
print(monkey_count_community(5))
