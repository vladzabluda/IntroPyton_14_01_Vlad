#1

#my_list = ['дом', 'сын', 'дерево', 'жизнь']
#new_my_list = []
#for index, str in enumerate(my_list):
#     if index % 2 == 0 :
#         new_my_list.append(str[::-1])
#     else:
#         new_my_list.append(str)
#print(new_my_list)

##########################################

#2

#my_list = ['дом', 'сын', 'дерево', 'жизнь', 'автобус']
#new_my_list = []
#new_my_list = ( list(filter(lambda x: x.lower().startswith("а"), my_list)) )
#print(new_my_list)

#######################

#3

#my_list = ['дома', 'сын', 'дерево', 'жизнь', 'автобус']
#new_my_list = []
#new_my_list = (list(filter(lambda x: 'а' in x, my_list)))
#print(new_my_list)

########################

#4

#my_list = ['дом', 'сын', 'дерево', 'жизнь', 'автобус', 11, 12, 13,14]
#new_my_list = []
#new_my_list = [value for value in my_list if type(value) == int]
#print(new_my_list)

#######################

#5

#my_str = "Дана строка"
#new_my_str = ''
#for i in range(len(my_str)):
 #   if new_my_str.find(my_str[i]) == -1 and my_str[i] != ' ':
 #       new_my_str += my_str[i]
#print(new_my_str)

###################

#6

#my_str_1 = "Даны две строки "
#my_str_2 = "Создать список"
#my_set_1 = set(my_str_1)
#my_set_2  = set(my_str_2)
#result_set = my_set_1.intersection(my_set_2)
#print(result_set)

############################

#7


str_1 = "Даны две строки "
str_2 = "Создать список"
res = []
for i in str_1 :
    k = str_1.find(i) - str_1.rfind(i)
    if k == 0:
        if i in str_2 and str_2.find(i) - str_2.rfind(i) == 0 :
            print(i)

#############################
