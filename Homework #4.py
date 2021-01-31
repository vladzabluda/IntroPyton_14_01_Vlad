#1

#my_int = "7020010060810340230200"
#new_my_int = "0"
#result = my_int.count(new_my_int)
#print(result)

#############################

#2

#my_int = "7020010060810340230200"
#count = 0
#for e in str(my_int)[::-1]:
#    if e =='0':
#       count += 1
#    else:
#           break
#print(count)

#################################

#3a

#my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#my_result = my_list_2[::2] + my_list_2[1::2]
#print(my_result)

#####################################

#3б

#my_list_1, my_list_2 = [1, 3, 2, 4,5 ] , [10, 20, 15, 25, 22]
#my_result = [my_list_1[i] for i in range(len(my_list_1)) if my_list_1[i] % 2 == 0] + [my_list_2[i] for i in range(len(my_list_2)) if my_list_2[i] % 2 == 1]
#rint(my_result)

#######################################

#4

#my_list = [1,2,3,4]
#new_list = []
#new_list = my_list[1:]
#value = my_list[0]
#new_list.append(value)
#print(new_list)


#############################

# 5

#my_list = [1,2,3,4]
#my_list += [my_list.pop(0)]
#print(my_list)

#########################

#6

str = '43 34 56'
def to_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default

text_numbers = ['43 34 56']
print(sum(number for word in text_numbers for number in map(to_int, word.split())))


