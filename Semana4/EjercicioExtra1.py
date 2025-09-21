#Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. 
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. 
# Si es exactamente igual, muestre “Igual”.

time_in_seconds = int(input("Ingrese el tiempo en segundos: "))
missing_time = 0
time_in_minutes = time_in_seconds / 60
if time_in_minutes < 10:
    missing_time = (10*60) - time_in_seconds
    print(missing_time)
elif time_in_minutes > 10:
    print("Mayor")
else:
    print("Igual")
