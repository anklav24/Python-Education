import os

dataset_path, dataset = os.path.join('C:\\', 'Users', 'Admin', 'Downloads', 'dataset_3380_5 (2).txt'), []

with open(dataset_path) as inf:
    dataset += [line.strip().split('\t') for line in inf]

for class_number in range(1, 12):
    height, children = 0, 0
    for row in dataset:
        if int(row[0]) == class_number:
            height += int(row[2])
            children += 1
    if children > 0:
        print(class_number, height / children)
    else:
        print(class_number, '-')
