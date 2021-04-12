class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'


# Теперь давайте посмотрим, что произойдет,
# если мы попытаемся вызвать эти методы в самом классе, т. е.,
# без предварительного создания экземпляра объекта:

print(MyClass.class_method())
print(MyClass.static_method())
print(MyClass.method())
