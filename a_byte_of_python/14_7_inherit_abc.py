from abc import *


class SchoolMember:
    """представляет любого человека в школе."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(create SchoolMember: {})'.format(self.name))

    @abstractmethod
    def tell(self):
        """Вывести информацию."""
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    """present teacher."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(create Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    """present student."""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(create Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print()  # print other string

members = [t, s]
for member in members:
    member.tell()  # работает как для преподавателя, так и для студента