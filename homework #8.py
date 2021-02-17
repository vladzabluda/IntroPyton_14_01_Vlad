import random
names = ["Zabluda", "Petrov", "Ivanov"]
domains = ["net", "com", "ua"]
################################################

#Генерируем случайную фамилию из списка.

import_names = random.choice(names)
print(import_names)

######################

#Генерируем число от 100-999.

i=0
while i<1:
    number = random.randint(100,999)
    print(number)
    i = i+1


######################

#Генерируем ameil длиной от 5 до 7 символов.

import random
import string
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(random.randint(5, 7)))

    print(rand_string)
    return rand_string
new_rand_string = generate_random_string(7)

##############################

#Генерируем домен из списка. Добавляем (.) и (@)


import_domains = random.choice(domains)
print(import_domains)

print(str(import_names)+"."+str(number)+"@"+str(new_rand_string)+"."+str(import_domains))

###############################
##Генерирум строку, длиной от 5 до 10 слов.
#Генерирум строку, длина слов от 1 до 10 символов.
#Каждое слово начинается с символа вверхнем регистре.

import string
import random


def create_random_str():
     rand_string = new_rand_string
     count = random.randint(5,10)
     return rand_string * count


def create_spaces(new_rand_string):
    index = 0
    rand_str_to_list = list(new_rand_string)
    condition = True
    while condition:
        step = random.randint(1, 10)
        index += step
        if index < len(new_rand_string):
            rand_str_to_list[index] = " "
        else:
            condition = False
    new_rand_string = "".join(rand_str_to_list)
    return new_rand_string


def modify_word(word):
    return word.capitalize()

def modify_str(new_rand_string):
    new_rand_string_split = new_rand_string.split()
    result = []
    for word in new_rand_string_split:

        word = modify_word(word)
        result.append(word)
    return " ".join(result)


new_rand_string = create_random_str()
new_rand_string = create_spaces(new_rand_string)
new_rand_string = modify_str(new_rand_string)
print(new_rand_string)

##############

# Добавляем знаки припенания(,).

print(new_rand_string.replace(" ", ", "))

