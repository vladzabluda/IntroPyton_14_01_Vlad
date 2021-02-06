#2

#my_list = ["абракадабра", "мемчик", "абзац", "море", "бровь"]
#newlist = [newlist for newlist in my_list if "а" in newlist]
#print(newlist)

#str = '43 34 56'
#new_str = ['43 34 56']
#result = [sum(map(int, s.split())) for s in new_str]
#print(result)

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