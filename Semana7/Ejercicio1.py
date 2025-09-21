import os
def menu():
    number = 0
    while True:
        print(number)
        try:
            option = int(input("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Borrar Resultado\n6.Salir\n"))
        except ValueError:
            print("Error: Opcion Invalida")
            exit()

        if option < 1 or option > 6:
            raise ValueError("Error: Ingrese un numero valido")
        elif option == 1:
            number = sum(number)
        elif option == 2:
            number = rest(number)
        elif option == 3:
            number = multi(number)
        elif option == 4:
            number = division(number)
        elif option == 5:
            number = 0
            clean()
        elif option == 6:
            exit()

    
def sum(number):
    try:
        num = int(input())
        number += num
        clean()
        return number
    except ValueError:
        print("Numero invalido")
        exit()


def rest(number):
    try:
        num = int(input())
        number -= num
        clean()
        return number
    except ValueError:
        print("Numero invalido")
        exit()

def multi(number):
    try:
        num = int(input())
        number = number * num
        clean()
        return number
    except ValueError:
        print("Numero invalido")
        exit()

def division(number):
    try:
        num = int(input())
        number = number / num
        clean()
        return number
    except ValueError:
        print("Numero invalido")
        exit()
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        exit()

def clean():
    os.system('cls')

def main():
    try:
        menu()
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()