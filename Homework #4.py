#1

#my_int = "7020010060810340230200"
#new_my_int = "0"
#result = my_int.count(new_my_int)
#print(result)

#############################

#2

my_int = "7020010060810340230200"
count=0
for e in str(my_int)[::-1]:
    if e=='0':
       count+=1
    else:
           break
print(count)

