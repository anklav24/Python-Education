import csv

title_2_set = set()
titles = {}

with open("machine-readable-business-employment-data-dec-2020-quarter.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        title = row["Series_reference"].strip().lower()
        title_2_set.add(title)

        if title not in titles:
            titles[title] = 0
        titles[title] += 1

for i in sorted(title_2_set):
    print(i)


def f(title):
    return titles[title]


for title in sorted(titles, key=f, reverse=True):
    print(title, titles[title])

# or just use lamda fuction
for title in sorted(titles, key=lambda x: titles[x], reverse=True):
    print(title, titles[title])
