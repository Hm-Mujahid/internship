import csv

# Writing CSV
with open("example.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "London"])
    writer.writerow(["Charlie", 22, "Bangalore"])

# Reading CSV
with open("example.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
