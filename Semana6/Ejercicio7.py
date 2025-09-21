def primo_num(num):
    if num <= 1:
        return False
    else:
        for num1 in range(2,num):
            temp_number = num % num1
            if temp_number == 0:
                return False
    return True

def list_numbers(my_list):
    new_list = []
    for number in my_list:
        if primo_num(number):
            new_list.append(number)
    return new_list

final_list = list_numbers([8,3,5,4,1])
print(final_list)