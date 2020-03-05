from stepik.programming_on_python.modules.f_from_x import f

a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}
for i in a:
    print(b[i])