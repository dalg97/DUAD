#Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. 
# Luego muestre el resultado de la suma.
num = int(input("Ingrese un numero: "))
result = 0
counter = 1
while counter <= num:
    result = result + counter
    counter = counter + 1
print(f"La suma es: {result}")