import csv

with open('read_file.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)

with open('write_file.csv', 'w', newline="") as csvfile:
    fieldnames = ['Name', 'The country', 'Age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Age': 22, 'The country': 'Poland', 'Name': 'Ivan'})
    writer.writerow({'Age': 56, 'The country': 'USA', 'Name': 'Bob'})