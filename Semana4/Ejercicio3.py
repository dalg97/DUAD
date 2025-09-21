import random

verification = True
secret_number = random.randint(1,10)
while(verification): 
    number = int(input("Ingrese un numero: "))  
    if number == secret_number:
        print(f"El numero fue acertado, el numero es {secret_number}")
        verification = False
    else:
        print("Numero incorrecto")

    