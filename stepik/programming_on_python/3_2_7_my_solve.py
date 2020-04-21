# from stepik.programming_on_python.modules.f_from_x import f
from stepik.programming_on_python.modules.f_from_x import f

n = int(input())
cache = {}
for i in range(n):
    x = int(input())
    if x in cache:
        print(cache[x])
    else:
        print(f(x))
        cache[x] = f(x)

# TODO: Do something useful.
# TODO: Test live template. Just let's start type "todo" and press "Tab" button. (Of course without quotes)
