import os


path = 'C:\\Users\\admin\\PycharmProjects\\IntroPyton_14_01_Vlad'
files = os.listdir(path)
for file in sorted(files)[:1]:

   # print(files)
    file_path = os.path.join(path, file)


    with open("names.txt", "r") as txt_file:
        data = []
        for line in txt_file.readlines():
            data.append(line.strip())
        data = [x.replace('\t', ' ') for x in data]

    #print(data)
for i in data:
    lst = i.split()
    print(lst[1])


#################

import json
data = {"test_list": [data]}
filename = "test_json_write.json"
with open(filename, "w") as js_file:
    json.dump(data, js_file)

####################

#import pprint
import random
import string


def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


def random_value():
    return random.choice([
        lambda: random.randint(-100, 100),
        lambda: random.uniform(0, 1),
        lambda: random.choice([False, True])
    ])();

def random_dict():
    return {random_key(): random_value() for _ in range(random.randint(5, 20))}

print(random_dict())

####################

import json
data = {"generate_and_write_json": [random_dict()]}
filename = "generate_and_write_json.json"
with open(filename, "w") as js_file:
    json.dump(data, js_file)
