def digitize(n):
    n = list(str(n))[::-1]
    count = 0
    for i in n:
        n[count] = int(i)
        count += 1
    return n

print(digitize(35231))

def digitize_community(n):
    return map(int, str(n)[::-1])

print(digitize_community(35231))

def digitize_community_1(n):
    return [int(x) for x in reversed(str(n))]

print(digitize_community_1(35321))
