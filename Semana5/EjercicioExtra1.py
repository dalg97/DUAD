temp_list = list(input("Ingrese la lista de numeros: "))
number_to_search = int(input("Ingrese el numero: "))
numbers_list = [int(x) for x in temp_list]
counter = 0
for num in numbers_list:
    if num == number_to_search:
        counter += 1
print(f"El numero {number_to_search} aparece {counter} veces")