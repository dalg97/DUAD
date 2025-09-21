the_list = [5,8,7,4,9,4,1,8,7]
temp_num_1 = the_list[0]
for index in range(len(the_list)):
    if index == len(the_list)-1:
        the_list[0] = the_list[index]
        the_list[index] = temp_num_1
print(the_list)
