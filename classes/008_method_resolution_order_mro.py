# Python: Быстрый старт, ООП2
# https://www.youtube.com/watch?v=cXjUIJAZcfs&list=WL&index=13

class A:
    VAR = 'A'

    def method(self):
        pass


class B:
    VAR = 'B'

    def method(self):
        pass


class C(A, B):  # Порядок наследования имеет значение!
    def method(self):
        print(self.VAR)


class D(C):
    pass


d = D()

print(d.method)
d.method()
print(D.__mro__)  # Показывает где класс будет искать атрибуты.
print(D.mro())  # Показывает где класс будет искать атрибуты.
