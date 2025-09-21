#4. **Tabla de multiplicar personalizada**
#    - Pida al usuario un número del 1 al 10
#    - Muestre su tabla de multiplicar del 1 al 12

num = int(input("Ingrese un numero del 1 al 10: "))
counter = 1
result = 0
while counter <= 12:
    result = num*counter
    print(f"{num} x {counter} = {result}")
    counter = counter + 1