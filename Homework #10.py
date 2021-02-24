
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

#####################
path = 'C:\\Users\\admin\\PycharmProjects\\IntroPyton_14_01_Vlad\\read_file.txt'
read_file = open(path,'r')
read = read_file.read()
print(read)

with open('write_file.txt', 'w') as opened_file:
    opened_file.write('qwertyu')
    file = open('write_file', 'w')
    try:
        file.write('qwertyu!')
    finally:
        file.close()

#################
import json

with open('read_file.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    print(text)

import json
data = {"write_file": [text]}
filename = "write_file.json"
with open(filename, "w") as js_file:
    json.dump(data, js_file)