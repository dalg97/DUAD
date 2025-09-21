counter = 1
temp_number = 0
while counter <= 3:
    number = int(input(f"Ingrese el numero{counter}: "))
    if number > temp_number:
        temp_number = number
    counter = counter + 1
print(f"El numero mayor es: {temp_number} ")


