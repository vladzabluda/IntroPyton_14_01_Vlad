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

my_list = ['дом', 'сын', 'дерево', 'жизнь', 'автобус']
new_my_list = ( list(filter(lambda x: x.lower().startswith("а"), my_list)) )
print(new_my_list)

#######################

