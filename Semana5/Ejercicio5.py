new_list = []
highest_number = 0
for counter in range(10):
    num = int(input(f"Ingrese el numero{counter+1}: "))
    new_list.append(num)
    if num > highest_number:
        highest_number = num
print(f"{new_list}. El mas alto fue {highest_number}")