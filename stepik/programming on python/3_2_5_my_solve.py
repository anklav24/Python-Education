def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key not in d:
        d[2 * key] = [value]
    elif 2 * key not in d:
        d[2 * key].append(value)


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
