import csv


def read_csv(filename):
    with open(filename, 'r') as csv_file:
        data = []
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data

def write_csv(filename, data):
    with open(filename, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

filename = "read_file.csv"
data = read_csv(filename)
print(data)
data.append(["Mary", "USA", 30])
write_csv(filename, data)