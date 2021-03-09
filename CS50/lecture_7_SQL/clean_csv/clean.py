import csv

title = input("Title: ").strip().lower()

with open("clean.csv", "r") as file:
    reader = csv.DictReader(file)
    counter = 0
    for row in reader:
        if row["title"].strip().lower() == title:
            counter += 1

print(counter)
