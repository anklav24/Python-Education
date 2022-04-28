from jinja2 import Template


# https://www.youtube.com/watch?v=cFJqMXxVNsI&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&ab_channel=selfedu


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('alex', 20)

template = Template("Hello, {{ person.name.title() }}! Your age is {{ person.age }}.")
msg = template.render(person=person)

print(msg)
