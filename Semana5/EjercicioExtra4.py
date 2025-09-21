the_list = [56,87,1,25,45,30]
new_list = []
average = 0
total_sum = 0
for num in the_list:
    total_sum = total_sum + num
average = total_sum / len(the_list)
for num in the_list:
    if num > average:
        new_list.append(num)

print(f"Promedio: {average}\nNueva Lista: {new_list}")
