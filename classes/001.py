class Foo:
    def __init__(self):
        self.a = 1
        self.b = 2

    def f(self):
        return self.a + self.b


class Bar(Foo):
    def __init__(self):
        super().__init__()


x = Bar()
print(x.a)
x.a = 50
print(x.f())
