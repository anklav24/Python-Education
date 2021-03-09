import csv

with open("machine-readable-business-employment-data-dec-2020-quarter.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip the first row.
    for row in reader:
        print(row)
