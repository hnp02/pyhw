import csv

with open("../csv/employees.csv", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)

names = [row[1] + " " + row[2] for row in rows[1:]]
print(names)

names_with_e = [name for name in names if "e" in name]
print(names_with_e)
