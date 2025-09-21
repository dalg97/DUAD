the_list = [5,9,4,11,7,5,10]
lowest_number = the_list[0]
for num in the_list:
    if num < lowest_number:
        lowest_number = num
print(f"El valor mas pequeno fue: {lowest_number}")