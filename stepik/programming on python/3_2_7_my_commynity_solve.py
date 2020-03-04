def f(v):
    if v <= -2:
        return 1 - (v + 2)**2
    elif -2 < v <= 2:
        return -(v/2)
    elif 2 < v:
        return (v - 2)**2 + 1
    else:
        pass

a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}
for i in a:
    print(b[i])