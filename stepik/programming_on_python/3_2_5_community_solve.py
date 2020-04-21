def update_dictionary(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)  # {2: [-1]}
print()

update_dictionary(d, 2, -2)
print(d)  # {2: [-1, -2]}
print()

update_dictionary(d, 1, -3)
print(d)  # {2: [-1, -2, -3]}
print()

update_dictionary(d, 3, -3)
print(d)
print()
