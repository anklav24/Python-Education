# from stepik.programming_on_python.modules.f_from_x import f
from .modules.f_from_x import f

n = int(input())
cache = {}
for i in range(n):
    x = int(input())
    if x in cache:
        print(cache[x])
    else:
        print(f(x))
        cache[x] = f(x)
