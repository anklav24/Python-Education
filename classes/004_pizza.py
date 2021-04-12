import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    def area(self):
        return self.circle_area(self.radius)

    # @classmethod
    # def margherita(cls):
    #     return cls(['mozzarella', 'tomatoes'])
    #
    # @classmethod
    # def prosciutto(cls):
    #     return cls(['mozzarella', 'tomatoes', 'ham'])

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(10, ['cheeze', 'tomatoes'])
print(p)
print(p.area())
# print(Pizza.margherita())
# print(Pizza.prosciutto())
print()
