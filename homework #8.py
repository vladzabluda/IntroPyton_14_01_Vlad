import random
names = ["Zabluda", "Petrov", "Ivanov"]
domains = ["net", "com", "ua"]
#

import_names = random.choice(names)
print(import_names)
#
i=0
while i<3:
    number = random.randint(100,999)
    print(number)
    i = i+1

#
import random
import string
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))

    print(rand_string)
    return rand_string
new_rand_string = generate_random_string(7)




#
import_domains = random.choice(domains)
print(import_domains)

print(str(import_names)+"."+str(number)+"@"+str(new_rand_string)+"."+str(import_domains))

