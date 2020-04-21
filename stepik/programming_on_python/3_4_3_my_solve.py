import os

path_to_file = os.path.join('C:\\', 'Users', 'Admin', 'Downloads', 'dataset_3363_3 (6).txt')
cache = {}
max_key, max_value = 0, 0

with open(path_to_file) as inf:
    for line in inf:
        line = line.lower().split()
        for word in set(line):
            print(word)
            cache[word] = line.count(word)
print(cache)

for key, value in cache.items():
    if value > max_value:
        max_value = value
        max_key = key
print(max_key, max_value)

