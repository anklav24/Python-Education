zoo = ('Python', 'Elephant', 'Penguin')  # Скобки не обязательны
print('The numbest of animals in a zoo -', len(zoo))

new_zoo = 'Monkey', 'Camel', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('All animals in a new zoo -', new_zoo)
print('Животные привезенные из старого зоопарка -', new_zoo[2])
print('Последнее животное, привезенное из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1 + len(new_zoo[2]))
