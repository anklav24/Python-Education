def f(v):
    if v <= -2:
        return 1 - (v + 2)**2
    elif -2 < v <= 2:
        return -(v/2)
    elif 2 < v:
        return (v - 2)**2 + 1
    else:
        pass

n = int(input())
cache = {}
for i in range(n):
    x = int(input())
    if x in cache:
        print(cache[x])
    else:
        print(f(x))
        cache[x] = f(x)
