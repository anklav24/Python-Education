import csv

with open("phonebook.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skips a header.
    for row in reader:
        print(row)

# It's the same.
with open("phonebook.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skips a header.
    for row in reader:
        print(row)

import os
os.system("more phonebook.csv")

