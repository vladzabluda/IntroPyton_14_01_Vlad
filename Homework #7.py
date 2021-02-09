

# 1

list = []
from random import randint
random = randint(1, 100)
for i in range(20):
    list.append(randint(1, 100))
print(list)

#######################

#2

import random as rnd
triangle = {"A": {(rnd.randint(-10, 10),
               rnd.randint(-10, 10),
               rnd.randint(-10, 10))},
         "B": {(rnd.randint(-10, 10),
               rnd.randint(-10, 10),
               rnd.randint(-10, 10))},
         "C": {(rnd.randint(-10, 10),
               rnd.randint(-10, 10),
               rnd.randint(-10, 10))}}
print(triangle)

############################

#4

persons = [
   { "name": 'Вова', "age": 15 },
   { "name": 'Оля', "age": 25 },
   { "name": 'Олег', "age": 18 },
   { "name": 'Артем', "age": 33 },
   { "name": 'Саша', "age": 47 },
]
min_age = float('inf')
max_len = float('-inf')

for person in persons:
    if person['age'] < min_age:
        min_age = person['age']
    if len(person['name']) > max_len:
        max_len = len(person['name'])
names_min_age = [p['name'] for p in persons if p['age'] == min_age]
names_max_len = [p['name'] for p in persons if len(p['name']) == max_len]

print(names_min_age, names_max_len)
from statistics import mean
persons = {
        'Вова': 15,
        'Оля': 25,
        'Олег': 18,
        'Артем': 33,
        'Саша': 47
}
persons_values = list(persons.values())
mean = sum(persons_values)/float(len(persons_values))
print(mean)


#5

my_dict_1 = {"a":1,
             "b":2,
             "c":3}
my_dict_2 = {"c":3,
             "d":4,
             "e":5,
             "f":6}
my_result_1 = []
my_result_2 = []
my_result_3 = {}
my_list_1 = {key: my_dict_2[key] for key in my_dict_1
     if my_dict_1[key] == my_dict_2.get(key)}
for key in sorted(my_list_1.keys()):
  my_result_1.append(key)
print(my_result_1)

my_list_2 = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
for key in sorted(my_list_2.keys()):
 my_result_2.append(key)
print(my_result_2)

my_result_3 = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
print(my_result_3)
