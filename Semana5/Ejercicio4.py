the_list = [4,8,2,3,4,6]
#the_list = [4,8,2,3,4,6,11,11,11,11,11,11,11,11,11,11,11,11]
new_list = []
for index,num in enumerate(the_list):
    if (the_list[index] % 2) == 0:
        new_list.append(num)
print(new_list)