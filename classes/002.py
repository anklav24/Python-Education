class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'


obj = MyClass()
print(obj.method())
# It's the same.
print(MyClass.method(obj))

print(obj.class_method())


class MyClass:
    def method(monkey):
        return 'instance method called', monkey

    @classmethod
    def class_method(elephant):
        return 'class method called', elephant

    @staticmethod
    def static_method():
        return 'static method called'


obj = MyClass()
print(obj.method())

print(obj.static_method())
