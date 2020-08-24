class SchoolMember:
    """Представляет любого человека в школе."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Create SchoolMember: {})'.format(self.name))

    def tell(self):
        """Вывести информацию."""
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    """Present teacher."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Create Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    """Present student."""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Create Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print()  # Print other string

members = [t, s]
for member in members:
    member.tell()  # работает как для преподавателя, так и для студента