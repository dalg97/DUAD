def sum_list(my_list):
    cont = 0
    for num in my_list:
        cont += num
    return cont

sum_number = sum_list([74,47,22])
print(sum_number)